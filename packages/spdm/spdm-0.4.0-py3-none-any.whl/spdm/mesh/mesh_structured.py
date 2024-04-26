import typing

import numpy as np

from ..utils.typing import ArrayLike, ArrayType, as_array
from .Mesh import Mesh


class StructuredMesh(Mesh):
    """ StructureMesh
      
    结构化网格上的点可以表示为长度为n=rank的归一化ntuple，记作 uv，uv_r \in [0,1]

    """

    def __init__(self, shape: ArrayLike, *args, cycles=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._shape = as_array(shape)
        self._cycles = cycles
        # shape = tuple(shape)
        # if cycles is None:
        #     cycles = [False] * ndims
        # if not isinstance(cycles, collections.abc.Sequence):
        #     cycles = [cycles]
        # if len(cycles) == 1:
        #     cycles = cycles * ndims

        # self._cycles: typing.Tuple[int] = self._metadata.get("cycles", None)

        # if self._cycles is None:
        #     self._cycles = ([False]*self.geometry.rank)
        # # logger.debug(f"Create {self.__class__.__name__} rank={self.rank} shape={self.shape} ndims={self.ndims}")
        # bbox = self.geometry.bbox
        # shape = self.shape
        # if not isinstance(shape, np.ndarray):
        #     raise TypeError(f"shape is not np.ndarray")
        # self._dx = (bbox[1]-bbox[0])/shape
        # self._origin = bbox[0]

    @property
    def cycles(self) -> typing.List[float]: return self._cycles
    """ Periodic boundary condition   周期性边界条件,  标识每个维度是否是周期性边界 """

    @property
    def origin(self) -> ArrayType: return self._origin

    @property
    def dx(self) -> ArrayType: return self._dx

    def coordinates(self, *uvw) -> ArrayType:
        if len(uvw) == 1:
            uvw = uvw[0]
        return np.stack([((uvw[i])*self.dx[i]+self.origin[i]) for i in range(self.rank)])

    def parametric_coordinates(self, *xyz) -> ArrayType:
        if len(uvw) == 1:
            uvw = uvw[0]
        return np.stack([((xyz[i]-self.origin[i])/self.dx[i]) for i in range(self.rank)])

    def interpolator(self, *args, **kwargs) -> typing.Callable:
        """ Interpolator of the Mesh
            网格的插值器, 用于网格上的插值
            返回一个函数，该函数的输入是一个坐标，输出是一个值
            输入坐标若为标量，则返回标量值
            输入坐标若为数组，则返回数组
        """
        raise NotImplementedError(f"{args} {kwargs}")
