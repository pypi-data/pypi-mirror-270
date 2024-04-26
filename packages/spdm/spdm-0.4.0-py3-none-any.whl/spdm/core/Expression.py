from __future__ import annotations
import warnings
import typing
from copy import copy, deepcopy
import functools
import collections.abc
import numpy as np

from ..utils.typing import ArrayType
from ..utils.tags import _not_found_
from ..utils.typing import ArrayType, NumericType, array_type, as_array, is_scalar, is_array, numeric_type
from ..utils.logger import logger
from ..utils.misc import group_dict_by_prefix
from ..numlib.interpolate import interpolate

from .Functor import Functor
from .Entry import Entry
from .HTree import HTreeNode, HTree, HTreeNode, List
from .Domain import DomainBase
from .Path import update_tree, Path
from .Functor import Functor, DerivativeOp


_T = typing.TypeVar("_T", float, bool, array_type, HTreeNode)


class Expression(HTreeNode):
    """Expression

    表达式是由多个操作数和运算符按照约定的规则构成的一个序列。
    其中运算符表示对操作数进行何种操作，而操作数可以是变量、常量、数组或者表达式。
    表达式可以理解为树状结构，每个节点都是一个操作数或运算符，每个节点都可以有多个子节点。
    表达式的值可以通过对树状结构进行遍历计算得到。
    没有子节点的节点称为叶子节点，叶子节点可以是常量、数组，也可以是变量和函数。

    变量是一种特殊的函数，它的值由上下文决定。

    例如：
        >>> import spdm
        >>> x = spdm.core.Expression(op=np.sin)
        >>> y = spdm.core.Expression(op=np.cos)
        >>> z = x + y
        >>> z
        <Expression   op="add" />
        >>> z(0.0)
        3.0


    """

    Domain = DomainBase

    @staticmethod
    def guess_dims(holder, prefix="coordinate", **kwargs):
        if holder is None or holder is _not_found_:
            return _not_found_
        elif isinstance(holder, List):
            return Expression.guess_dims(holder._parent, prefix=prefix, **kwargs)

        coords = []

        metadata = getattr(holder, "_metadata", {})

        dims_s, *_ = group_dict_by_prefix(metadata, prefix, sep=None)

        if dims_s is not None and len(dims_s) > 0:
            dims_s = {int(k): v for k, v in dims_s.items() if k.isdigit()}
            dims_s = dict(sorted(dims_s.items(), key=lambda x: x[0]))

            for c in dims_s.values():
                if not isinstance(c, str):
                    d = as_array(c)
                elif c == "1...N":
                    d = None
                # elif isinstance(holder, HTree):
                #     d = holder.get(c, _not_found_)
                else:
                    d = Path(c).get(holder, _not_found_)

                if d is _not_found_ or d is None:
                    # logger.warning(f"Can not get coordinates {c} from {holder}")
                    coords = []
                    break
                coords.append(as_array(d))

                # elif c.startswith("../"):
                #     d = as_array(holder._parent.get(c[3:], _not_found_))
                # elif c.startswith(".../"):
                #     d = as_array(holder._parent.get(c, _not_found_))
                # elif hasattr(holder.__class__, "get"):
                #     d = as_array(holder.get(c, _not_found_))
                # else:
                #     d = _not_found_
                # elif c.startswith("*/"):
                #     raise NotImplementedError(f"TODO:{self.__class__}.dims:*/")
                # else:
                #     d = as_array(holder.get(c, _not_found_))

        if len(coords) == 0:
            return Expression.guess_dims(getattr(holder, "_parent", None), prefix=prefix, **kwargs)
        else:
            return tuple(coords)

    @staticmethod
    def guess_domain(obj, **kwargs):
        holder = obj
        domain = None
        while holder is not _not_found_ and holder is not None:
            domain_pth = getattr(holder, "_metadata", {}).get("domain", None)
            if domain_pth is not None:
                domain = Path(domain_pth).get(holder, _not_found_)
                if domain is not _not_found_:
                    break
            holder = getattr(holder, "_parent", None)

        if isinstance(domain, array_type) and domain.ndim == 1:
            domain = [domain]

        if domain is None or domain is _not_found_:
            domain = Expression.guess_dims(obj, **kwargs)

        return domain

    def __init__(self, op, *args, domain=_not_found_, **kwargs) -> None:
        """
        Parameters


        op : typing.Callable  | ExprOp
            运算符，可以是函数，也可以是类的成员函数
        args : typing.Any
            操作数
        kwargs : typing.Any
            命名参数， 用于传递给运算符的参数

        """

        if self.__class__ is not Expression:
            super().__init__(**kwargs)
            self._op = op
            self._children = args
            self._domain = domain

        elif is_scalar(op):  # 常量/标量表达式
            match op:
                case 0:
                    TP = ConstantZero
                case 1:
                    TP = ConstantOne
                case _:
                    TP = Scalar

            self.__class__ = TP
            TP.__init__(self, op, *args, domain=domain, **kwargs)

        elif isinstance(op, array_type):  # 构建插值函数
            from .Function import Function

            TP = Function

            self.__class__ = TP
            TP.__init__(self, op, *args, domain=domain, **kwargs)

        else:  # 一般表达式
            super().__init__(**kwargs)
            self._op = op
            self._children = args
            self._domain = domain

    def __copy__(self) -> Expression:
        """复制一个新的 Expression 对象"""
        other: Expression = super().__copy__()
        other._op = copy(self._op)
        other._domain = self._domain
        other._children = copy(self._children)
        return other

    def __serialize__(self, dumper=None):
        logger.debug(f"TODO: __serialize__ {self}")
        return None

    @property
    def domain(self) -> DomainBase:
        """返回表达式的定义域"""

        if self._domain is None or self._domain is _not_found_:
            self._domain = Expression.guess_domain(self)

        if self._domain is None or self._domain is _not_found_:
            for child in self._children:
                domain = getattr(child, "domain", _not_found_)
                if domain is not _not_found_:
                    break
                elif isinstance(domain, DomainBase) and not domain.is_full:
                    break
            else:
                domain = _not_found_

            self._domain = domain

        if self._domain is _not_found_:
            raise RuntimeError(f"Can not get domain!")

        elif not isinstance(self._domain, DomainBase):
            self._domain = self.__class__.Domain(self._domain)

        return self._domain

    @property
    def has_children(self) -> bool:
        """判断是否有子节点"""
        return len(self._children) > 0

    @property
    def empty(self) -> bool:
        return not self.has_children and self._op is None

    def __repr__(self) -> str:
        return self._render_latex_()

    def __str__(self) -> str:
        return self._render_latex_()

    def _render_latex_(self) -> str:
        vargs = []
        for expr in self._children:
            if isinstance(expr, (bool, int, float, complex)):
                res = str(expr)
            elif expr is None:
                res = "n.a"
            elif isinstance(expr, np.ndarray):
                if len(expr.shape) == 0:
                    res = f"{expr.item()}"
                else:
                    res = f"{expr.dtype}[{expr.shape}]"
            elif isinstance(expr, Variable):
                res = f"{expr.__label__}"
            elif isinstance(expr, Expression):
                res = expr._render_latex_()
            elif isinstance(expr, np.ufunc):
                res = expr.__name__
            else:
                res = expr.__class__.__name__
            vargs.append(res)

        if isinstance(self._op, np.ufunc):
            op_tag = EXPR_OP_TAG.get(self._op.__name__, self._op.__name__)

            if self._op.nin == 1:
                res = rf"{op_tag}{{{vargs[0]}}}"

            elif self._op.nin == 2:
                if op_tag == "/":
                    res = f"\\frac{{{vargs[0]}}}{{{vargs[1]}}}"
                else:
                    res = rf"{{{vargs[0]}}} {op_tag} {{{vargs[1]}}}"
            else:
                raise RuntimeError(f"Tri-op is not defined!")

        elif (op_tag := self._metadata.get("label", None) or self._metadata.get("name", None)) is not None:
            if len(vargs) == 0:
                res = op_tag
            else:
                res: str = rf"{op_tag}\left({','.join(vargs)}\right)"

        else:
            if isinstance(self._op, Expression):
                op_tag = self._op.__label__
            else:
                op_tag = self._op.__class__.__name__

            res: str = rf"{op_tag}\left({','.join(vargs)}\right)"

        return res

    def _repr_latex_(self) -> str:
        """for jupyter notebook display"""
        return f"$${self._render_latex_()}$$"

    @property
    def dtype(self):
        return float

    def __array_ufunc__(self, ufunc, method, *args, **kwargs) -> Expression:
        """
        重载 numpy 的 ufunc 运算符, 用于在表达式中使用 numpy 的 ufunc 函数构建新的表达式。
        例如：
            >>> import numpy as np
            >>> import spdm
            >>> x = spdm.core.Expression(np.sin)
            >>> y = spdm.core.Expression(np.cos)
            >>> z = x + y
            >>> z
            <Expression   op="add" />
            >>> z(0.0)
            1.0
        """
        if method != "__call__" or len(kwargs) > 0:
            return Expression(Functor(ufunc, method=method, **kwargs), *args)
        else:
            return Expression(ufunc, *args)

    def __array__(self, dtype=None) -> array_type:
        """在定义域上计算表达式，返回数组。"""

        if self._cache is None or self._cache is _not_found_:
            if self.domain is None or self.domain is _not_found_:
                raise RuntimeError(f"Domain is not defined")

            x = self.domain.points

            if len(x) == 0:
                raise RuntimeError(f"Empty domain, __array__ fail!")

            self._cache = self.__call__(*x)

        return self._cache

    def __ppoly__(self):
        """表达式的多项式近似

        Raises:
            RuntimeError: 当 domain 为空时报错

        Returns:
            多项式: 多项式
        """
        if getattr(self, "_ppoly", _not_found_) is _not_found_:
            self._ppoly = self.domain.interpolate(self.__array__())

        return self._ppoly

    def _eval_children(self, *args, **kwargs):
        if len(self._children) == 0:
            return args
        else:
            new_children = []
            for child in self._children:
                try:
                    if callable(child) and len(args) + len(kwargs) > 0:
                        value = child(*args, **kwargs)
                    else:
                        value = np.asarray(child)

                except Exception as error:
                    raise RuntimeError(f"Failure to calculate  child {child} !") from error
                else:
                    new_children.append(value)
            return new_children

    def __eval__(self, *args, **kwargs):
        if not callable(self._op):
            raise RuntimeError(f"Unknown functor {self._op} {type( self._op)}")

        new_children = self._eval_children(*args, **kwargs)

        # 执行当前节点算符
        res = self._op(*new_children)

        # with warnings.catch_warnings():
        #     warnings.filterwarnings("error", category=RuntimeWarning)
        #     try:
        #         # 执行当前节点算符
        #         res = self._op(*new_children)
        #     except RuntimeWarning:
        #         logger.exception(f"{self._render_latex_()} {self._op} {new_children}")
        #         # raise RuntimeError((res, args))
        #         # res=np.nan_to_num(res,nan=1.0e-33)
        #         res = np.nan

        return res

    def __call__(self, *args, **kwargs) -> Expression | array_type:
        """
        重载函数调用运算符，用于计算表达式的值

        TODO:
        - support JIT compilation
        - support broadcasting?
        - support multiple meshes?

        Parameters

        xargs : NumericType
            自变量/坐标，可以是标量，也可以是数组
        kwargs : typing.Any
            命名参数，用于传递给运算符的参数
        """
        if len(args) + len(kwargs) == 0:  # 空调用，返回自身
            return self

        elif any([isinstance(a, Expression) for a in args]):  #  创建复合函数
            return Expression(self, *args, **kwargs)

        else:  # 执行计算
            return self.__eval__(*args, **kwargs)

    def derivative(self, order: int, *args, **kwargs) -> Derivative:
        return Derivative(self, *args, order=order, **kwargs)

    def antiderivative(self, order: int, *args, **kwargs) -> Antiderivative:
        return Antiderivative(self, *args, order=order, **kwargs)

    def partial_derivative(self, order: typing.Tuple[int, ...], *args, **kwargs) -> PartialDerivative:
        return PartialDerivative(self, *args, order=order, **kwargs)

    def pd(self, *order, **kwargs) -> PartialDerivative:
        return self.partial_derivative(order, **kwargs)

    def integral(self, *args, **kwargs) -> float:
        raise NotImplementedError(f"")

    @property
    def d(self) -> Expression:
        """1st derivative 一阶导数"""
        return self.derivative(1)

    @property
    def d2(self) -> Expression:
        """2nd derivative 二阶导数"""
        return self.derivative(2)

    @property
    def I(self) -> Expression:
        """antiderivative 原函数"""
        return self.antiderivative(1)

    @property
    def dln(self) -> Expression:
        """logarithmic derivative 对数求导"""
        return self.derivative(1) / self

    def find_roots(self, *args, **kwargs) -> typing.Generator[float, None, None]:
        raise NotImplementedError(f"TODO: find_roots")

    def fetch(self, *args, _parent=None, **kwargs):
        if len(args) + len(kwargs) == 0:
            if self._cache is not None:
                return self._cache
            else:
                return self.__array__()
        else:
            res = self.__call__(*args, **kwargs)

            if res is self:
                res = self.__copy__()

            if isinstance(res, HTreeNode):
                res._parent = _parent

        return res

    # fmt: off
    def __neg__      (self                             ) : return Expression(np.negative     ,  self     )
    def __add__      (self, o: NumericType | Expression) : return Expression(np.add          ,  self, o  ) if not ((is_scalar(o) and o == 0 ) or isinstance(o, ConstantZero) or o is _not_found_ and o is None) else self
    def __sub__      (self, o: NumericType | Expression) : return Expression(np.subtract     ,  self, o  ) if not ((is_scalar(o) and o == 0 ) or isinstance(o, ConstantZero) or o is _not_found_ and o is None) else self
    def __mul__      (self, o: NumericType | Expression) : return Expression(np.multiply     ,  self, o  ) if not (is_scalar(o) and (o ==0 or o==1)) else (ConstantZero() if o==0 else self)
    def __matmul__   (self, o: NumericType | Expression) : return Expression(np.matmul       ,  self, o  ) if not (is_scalar(o) and (o ==0 or o==1)) else (ConstantZero() if o==0 else self)
    def __truediv__  (self, o: NumericType | Expression) : return Expression(np.true_divide  ,  self, o  ) if not (is_scalar(o) and (o ==0 or o==1)) else (Scalar(np.nan) if o==0 else self)
    def __pow__      (self, o: NumericType | Expression) : return Expression(np.power        ,  self, o  ) if not (is_scalar(o) and (o ==0 or o==1)) else (ConstantOne() if o==0 else self)
    def __eq__       (self, o: NumericType | Expression) : return Expression(np.equal        ,  self, o  )
    def __ne__       (self, o: NumericType | Expression) : return Expression(np.not_equal    ,  self, o  )
    def __lt__       (self, o: NumericType | Expression) : return Expression(np.less         ,  self, o  )
    def __le__       (self, o: NumericType | Expression) : return Expression(np.less_equal   ,  self, o  )
    def __gt__       (self, o: NumericType | Expression) : return Expression(np.greater      ,  self, o  )
    def __ge__       (self, o: NumericType | Expression) : return Expression(np.greater_equal,  self, o  )
    def __radd__     (self, o: NumericType | Expression) : return Expression(np.add          ,  o, self  ) if not ((is_scalar(o) and o == 0 ) or isinstance(o, ConstantZero) or o is _not_found_ and o is None) else self
    def __rsub__     (self, o: NumericType | Expression) : return Expression(np.subtract     ,  o, self  ) if not ((is_scalar(o) and o == 0 ) or isinstance(o, ConstantZero) or o is _not_found_ and o is None) else self.__neg__()
    def __rmul__     (self, o: NumericType | Expression) : return Expression(np.multiply     ,  o, self  ) if not (is_scalar(o) and (o ==0 or o==1)) else (ConstantZero() if o==0 else self)
    def __rmatmul__  (self, o: NumericType | Expression) : return Expression(np.matmul       ,  o, self  ) if not (is_scalar(o) and (o ==0 or o==1)) else (ConstantZero() if o==0 else self)
    def __rtruediv__ (self, o: NumericType | Expression) : return Expression(np.divide       ,  o, self  )
    def __rpow__     (self, o: NumericType | Expression) : return Expression(np.power        ,  o, self  ) if not (is_scalar(o) and o ==1)  else ConstantOne()
    def __abs__      (self                             ) : return Expression(np.abs          ,  self     )
    def __pos__      (self                             ) : return Expression(np.positive     ,  self     )
    def __invert__   (self                             ) : return Expression(np.invert       ,  self     )
    def __and__      (self, o: NumericType | Expression) : return Expression(np.bitwise_and  ,  self, o  ) if not isinstance(o,bool) else ( self if o ==True else False)
    def __or__       (self, o: NumericType | Expression) : return Expression(np.bitwise_or   ,  self, o  ) if not isinstance(o,bool) else ( True if o ==True else self)
    def __xor__      (self, o: NumericType | Expression) : return Expression(np.bitwise_xor  ,  self, o  )
    def __rand__     (self, o: NumericType | Expression) : return Expression(np.bitwise_and  ,  o, self  ) if not isinstance(o,bool) else ( self if o ==True else False)
    def __ror__      (self, o: NumericType | Expression) : return Expression(np.bitwise_or   ,  o, self  ) if not isinstance(o,bool) else ( True if o ==True else self)
    def __rxor__     (self, o: NumericType | Expression) : return Expression(np.bitwise_xor  ,  o, self  )
    def __rshift__   (self, o: NumericType | Expression) : return Expression(np.right_shift  ,  self, o  )
    def __lshift__   (self, o: NumericType | Expression) : return Expression(np.left_shift   ,  self, o  )
    def __rrshift__  (self, o: NumericType | Expression) : return Expression(np.right_shift  ,  o, self  )
    def __rlshift__  (self, o: NumericType | Expression) : return Expression(np.left_shift   ,  o, self  )
    def __mod__      (self, o: NumericType | Expression) : return Expression(np.mod          ,  self, o  )
    def __rmod__     (self, o: NumericType | Expression) : return Expression(np.mod          ,  o, self  )
    def __floordiv__ (self, o: NumericType | Expression) : return Expression(np.floor_divide ,  self, o  )
    def __rfloordiv__(self, o: NumericType | Expression) : return Expression(np.floor_divide ,  o, self  )
    def __trunc__    (self                             ) : return Expression(np.trunc        ,  self     )
    def __round__    (self, n=None                     ) : return Expression(np.round        ,  self, n  )
    def __floor__    (self                             ) : return Expression(np.floor        ,  self     )
    def __ceil__     (self                             ) : return Expression(np.ceil         ,  self     )
    # fmt: on


EXPR_OP_TAG = {
    "negative": "-",
    "add": "+",
    "subtract": "-",
    "multiply": r"\cdot",
    "matmul": r"\cdot",
    "true_divide": "/",
    "power": "^",
    "equal": "==",
    "not_equal": "!",
    "less": "<",
    "less_equal": "<=",
    "greater": ">",
    "greater_equal": ">=",
    "add": "+",
    "subtract": "-",
    "multiply": r"\cdot",
    "matmul": r"\cdot",
    "divide": "/",
    "power": "^",
    # "abs": "",
    "positive": "+",
    # "invert": "",
    "bitwise_and": "&",
    "bitwise_or": "|",
    # "bitwise_xor": "",
    # "right_shift": "",
    # "left_shift": "",
    # "right_shift": "",
    # "left_shift": "",
    "mod": "%",
    # "floor_divide": "",
    # "floor_divide": "",
    # "trunc": "",
    # "round": "",
    # "floor": "",
    # "ceil": "",
    "sqrt": r"\sqrt",
}


class Variable(Expression):
    """Variable

    变量是一种特殊的函数，它的值由上下文决定。
    例如：
    >>> import spdm
    >>> x = spdm.core.Variable(0,"x")
    >>> y = spdm.core.Variable(1,"y")
    >>> z = x + y
    >>> z
    <Expression   op="add" />
    >>> z(0.0, 1.0)
    1.0

    """

    def __init__(self, idx: int | str, name: str = None, domain=None, **kwargs) -> None:
        if name is None:
            name = idx if isinstance(idx, str) else f"_{idx}"
        super().__init__(None, name=name, domain=domain, **kwargs)
        self._idx = idx

    def __copy__(self) -> Scalar:
        res = super().__copy__()
        res._idx = self._idx
        return res

    @property
    def _type_hint(self) -> typing.Type:
        """获取函数的类型"""
        orig_class = getattr(self, "__orig_class__", None)
        if orig_class is not None:
            return typing.get_args(orig_class)[0]
        else:
            return float

    @property
    def index(self):
        return self._idx

    def __call__(self, *args, **kwargs):
        if all([isinstance(a, Variable) for a in args]):
            res = self
        elif len(args) == 1 and isinstance(args[0], HTree):
            pth = Path(self.__name__)
            res = pth.get(args[0], _not_found_)
            if res is _not_found_:
                res = pth.get(kwargs, _not_found_)
            if res is _not_found_:
                raise RuntimeError(f"Can not get variable {self.__name__}")
        elif self._idx < len(args):
            res = args[self._idx]
        elif self.__name__.isidentifier():
            res = kwargs.get(self.__name__)
        else:
            raise RuntimeError(
                f"Variable {self.__label__} require {self._idx+1} args, or {self.__name__} in kwargs but only {args} provided!"
            )

        return res

    def __repr__(self) -> str:
        return self.__label__


class Scalar(Expression):
    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 0 or not isinstance(args[0], (float, int, bool)):
            raise ValueError(f"args should be float|int|bool")
        super().__init__(None, *args, **kwargs)

    @property
    def __label__(self):
        return self._children[0]

    def __array__(self) -> ArrayType:
        return np.array(self._children[0])

    def __str__(self):
        return str(self._children[0])

    def __repr__(self) -> str:
        return str(self._children[0])

    def __equal__(self, other) -> bool:
        return self._children[0] == other

    def __call__(self, *args, **kwargs):
        return self._children[0]

    def derivative(self, *args, **kwargs):
        return ConstantZero(_parent=self._parent, **kwargs)


class ConstantZero(Scalar):
    def __init__(self, *args, **kwargs):
        super().__init__(0, **kwargs)

    # fmt: off
    def __neg__      (self                             ) : return self
    def __add__      (self, o: NumericType | Expression) : return o
    def __sub__      (self, o: NumericType | Expression) : return Expression(np.negative     ,  o  ) 
    def __mul__      (self, o: NumericType | Expression) : return self
    def __matmul__   (self, o: NumericType | Expression) : return self
    def __truediv__  (self, o: NumericType | Expression) : return self
    def __pow__      (self, o: NumericType | Expression) : return self
    def __radd__     (self, o: NumericType | Expression) : return o
    def __rsub__     (self, o: NumericType | Expression) : return o
    def __rmul__     (self, o: NumericType | Expression) : return self
    def __rmatmul__  (self, o: NumericType | Expression) : return self
    def __rtruediv__ (self, o: NumericType | Expression) : return Scalar(np.nan)
    def __rpow__     (self, o: NumericType | Expression) : return one
    def __abs__      (self                             ) : return self
    # fmt: on


class ConstantOne(Scalar):
    def __init__(self, *args, **kwargs):
        super().__init__(1, **kwargs)

    # fmt: off
    def __neg__      (self                             ) : return Scalar(-1)
    def __mul__      (self, o: NumericType | Expression) : return o
    def __matmul__   (self, o: NumericType | Expression) : return o
    def __pow__      (self, o: NumericType | Expression) : return self
    def __rmul__     (self, o: NumericType | Expression) : return o
    def __rmatmul__  (self, o: NumericType | Expression) : return o
    def __rtruediv__ (self, o: NumericType | Expression) : return o
    def __rpow__     (self, o: NumericType | Expression) : return o
    def __abs__      (self                             ) : return self
    # fmt: on


zero = ConstantZero()

one = ConstantOne()


class Derivative(Expression):
    """算符: 用于表示一个运算符，可以是函数，也可以是类的成员函数
    受 np.ufunc 启发而来。
    可以通过 ExprOp(op, method=method) 的方式构建一个 ExprOp 对象。

    """

    def __init__(self, *args, order=1, **kwargs):
        if len(args) == 0:
            raise RuntimeError(f"Need at least one position argument!")
        elif len(args) == 1:
            expr = args[0]
            args = []
        elif all([isinstance(a, array_type) for a in args]):
            y, *x = args
            expr = Expression(*x, y)
            args = []
        else:
            expr = None
        super().__init__(None, *args, **kwargs)

        self._order = order
        self._expr = expr

    @property
    def order(self) -> int | None:
        return self._order

    @property
    def domain(self) -> DomainBase:
        domain = super().domain
        if (domain is None or domain is _not_found_) and isinstance(self._expr, Expression):
            domain = self._expr.domain
        return domain

    def _render_latex_(self) -> str:
        expr: Expression = self._expr

        if expr is None or expr is _not_found_:
            return self.__label__

        match self._order:
            case 0:
                text = expr._render_latex_()
            case 1:
                text = f"d{expr._render_latex_()}"
            case -1:
                text = rf"\int \left({expr._render_latex_()} \right)"
            case -2:
                text = rf"\iint \left({expr._render_latex_()} \right)"
            case _:
                if self._order > 1:
                    text = rf"d_{{\left[{self._order}\right]}}{expr._render_latex_()}"
                elif self._order < 0:
                    text = rf"\intop^{{{-self._order}}}\left({expr._render_latex_()}\right)"
                else:
                    text = expr._render_latex_()
        return text

    def __eval__(self, *args: _T, **kwargs) -> _T:
        if len(self._children) > 0:
            y, *x = self._eval_children(*args)
            ppoly = interpolate(*x, y, **kwargs)

            if self._order > 0:
                res = ppoly.derivative(self._order)(*x)
            elif self._order < 0:
                res = ppoly.antiderivative(-self._order)(*x)
            else:
                res = ppoly(*x)

            return res

        elif self._op is None or self._op is _not_found_:
            try:
                ppoly = self._expr.__ppoly__()
            except Exception:
                y = self._expr(*args)
                x = args
                ppoly = interpolate(*x, y)

            if self._order > 0:
                self._op = ppoly.derivative(self._order)
            elif self._order < 0:
                self._op = ppoly.antiderivative(-self._order)
            else:
                self._op = ppoly

        return self._op(*args, **kwargs)


class Antiderivative(Derivative):
    def __init__(self, *args, order=1, **kwargs):
        super().__init__(*args, order=-order, **kwargs)


def derivative(*args, order=1, **kwargs):
    func = Derivative(*args, order=order, **kwargs)
    if all([isinstance(d, (array_type, float, int)) for d in args[1:]]):
        _, *x = args
        return func(*x)
    else:
        return func


def antiderivative(*args, order=1, **kwargs):
    return Antiderivative(*args, order=order, **kwargs)


class PartialDerivative(Derivative):
    def __repr__(self) -> str:
        return f"d_{{{self._order}}} ({Expression._repr_s(self._expr)})"


from ..numlib.smooth import smooth as _smooth

from scipy.signal import savgol_filter


class SmoothOp(Expression):
    def __init__(self, op, *args, **kwargs) -> None:
        super().__init__(op or savgol_filter, *args, options=kwargs)

    def __eval__(self, y: array_type, *args, **kwargs) -> typing.Any:
        if len(args) + len(kwargs) > 0:
            logger.warning(f"Ignore {args} {kwargs}")

        return self._op(y, **self._metadata.get("options", {}))

    def __call__(self, *args, **kwargs):
        if len(args) + len(kwargs) > 0:
            return super().__call__(*args, **kwargs)
        else:
            return self.__eval__(*self._children)


def smooth(expr, *args, op=None, **kwargs):
    if isinstance(expr, array_type):
        return SmoothOp(op, expr, *args, **kwargs)()
    else:
        return SmoothOp(op, expr, *args, **kwargs)
