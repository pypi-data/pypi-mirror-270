from __future__ import annotations
import tempfile
import shutil
import pathlib
import os
import typing
import uuid
import contextlib
from ..utils.logger import logger
from ..utils.envs import SP_DEBUG, SP_LABEL
from ..utils.plugin import Pluggable
from ..view import View as sp_view

from .HTree import HTreeNode
from .TimeSeries import TimeSeriesAoS, TimeSlice
from .Edge import InPorts, OutPorts
from .sp_property import SpTree, sp_tree


@sp_tree
class Actor(Pluggable):

    def __init__(self, *args, **kwargs) -> None:
        if self.__class__ is Actor and self.__class__.__dispatch_init__(None, self, *args, **kwargs) is not False:
            return
        SpTree.__init__(self, *args, **kwargs)
        self._uid = uuid.uuid3(uuid.uuid1(clock_seq=0), self.__class__.__name__)

    def _repr_svg_(self):
        return sp_view.display(self.__geometry__(), output="svg")

    def __geometry__(self):
        return None

    @property
    def tag(self) -> str:
        return f"{self._plugin_prefix}{self.__class__.__name__.lower()}"

    @property
    def uid(self) -> uuid.UUID:
        return self._uid

    @contextlib.contextmanager
    def working_dir(self, suffix: str = "", prefix="") -> typing.Generator[pathlib.Path, None, None]:
        pwd = pathlib.Path.cwd()

        working_dir = f"{self.output_dir}/{prefix}{self.tag}{suffix}"

        temp_dir = None

        if SP_DEBUG:
            current_dir = pathlib.Path(working_dir)
            current_dir.mkdir(parents=True, exist_ok=True)
        else:
            temp_dir = tempfile.TemporaryDirectory(prefix=self.tag)
            current_dir = pathlib.Path(temp_dir.name)

        os.chdir(current_dir)

        logger.info(f"Enter directory {current_dir}")

        try:
            yield current_dir
        except Exception as error:
            if temp_dir is not None:
                shutil.copytree(temp_dir.name, working_dir, dirs_exist_ok=True)
            os.chdir(pwd)
            logger.info(f"Enter directory {pwd}")
            logger.exception(f"Failed to execute actor {self.tag}! \n See log in {working_dir} ")
        else:
            if temp_dir is not None:
                temp_dir.cleanup()

            os.chdir(pwd)
            logger.info(f"Enter directory {pwd}")

    @property
    def output_dir(self) -> str:
        return (
            self.get_cache("output_dir", None)
            or os.getenv("SP_OUTPUT_DIR", None)
            or f"{os.getcwd()}/{SP_LABEL.lower()}_output"
        )

    time_slice: TimeSeriesAoS[TimeSlice]
    """ 时间片序列，保存 Actor 历史状态。
        @note: TimeSeriesAoS 长度为 n(=3) 循环队列。当压入序列的 TimeSlice 数量超出 n 时，会调用 TimeSeriesAoS.__full__(first_slice)  
    """

    inports: InPorts
    """ 输入的 Edge，记录对其他 Actor 的依赖。 """

    outports: OutPorts
    """ 输出的 Edge，可视为对于引用（reference）的记录"""

    @property
    def current(self) -> typing.Type[TimeSlice]:
        """当前时间片，指向 Actor 所在时间点的状态。"""
        return self.time_slice.current

    @property
    def previous(self) -> typing.Generator[typing.Type[TimeSlice], None, None]:
        """倒序返回前面的时间片，"""
        yield from self.time_slice.previous

    @property
    def time(self) -> float:
        """当前时间，"""
        return self.time_slice.current.time

    @property
    def iteration(self) -> int:
        """当前时间片执行 refresh 的次数。对于新创建的 TimeSlice，iteration=0"""
        return self.time_slice.current.iteration

    def initialize(self, *args, **kwargs) -> None:
        """初始化 Actor 。"""
        if self.time_slice.is_initializied:
            return

        self.time_slice.initialize(*args, **kwargs)

        tp_hints = typing.get_type_hints(self.__class__.refresh)

        for name, tp in tp_hints.items():
            if name == "return":
                continue
            elif getattr(tp, "_name", None) == "Optional":  # check typing.Optional
                t_args = typing.get_args(tp)
                if len(t_args) == 2 and t_args[1] is type(None):
                    tp = t_args[0]

            self.inports[name].link(type_hint=tp)

        # 查找父节点的输入 ，更新链接 Edge
        self.inports.refresh()
        self.outports.refresh()

    def preprocess(self, *args, **kwargs) -> typing.Type[TimeSlice]:
        """Actor 的预处理，若需要，可以在此处更新 Actor 的状态树。"""

        for k in [*kwargs.keys()]:
            if isinstance(kwargs[k], HTreeNode):
                self.inports[k] = kwargs.pop(k)
        # inputs = {k: kwargs.pop(k) for k in [*kwargs.keys()] if isinstance(kwargs[k], HTreeNode)}

        # self.inports.update(inputs)

        current = self.time_slice.current

        current.refresh(*args, **kwargs)

        return current

    def execute(self, current: typing.Type[TimeSlice], *args) -> typing.Type[TimeSlice]:
        """根据 inports 和 前序 time slice 更新当前time slice"""
        return current

    def postprocess(self, current: typing.Type[TimeSlice]) -> typing.Type[TimeSlice]:
        """Actor 的后处理，若需要，可以在此处更新 Actor 的状态树。
        @param current: 当前时间片
        @param working_dir: 工作目录
        """
        return current

    def refresh(self, *args, **kwargs) -> typing.Type[TimeSlice]:
        """更新当前 Actor 的状态。
        更新当前状态树 （time_slice），并执行 self.iteration+=1

        """

        current = self.preprocess(*args, **kwargs)

        current = self.execute(current, self.time_slice.previous)

        current = self.postprocess(current)

        return current

    def flush(self) -> None:
        """保存当前时间片的状态。
        根据当前 inports 的状态，更新状态并写入 time_slice，
        默认 do nothing， 返回当前时间片
        """
        return self.time_slice.flush()

    def finalize(self) -> None:
        """完成。"""

        self.flush()
        self.time_slice.finalize()

    def fetch(self, *args, **kwargs) -> typing.Type[TimeSlice]:
        return HTreeNode._do_fetch(self.time_slice.current, *args, **kwargs)

