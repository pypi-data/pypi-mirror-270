"""GenericMatrix"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_MATRIX = python_net_import("SMT.MastaAPI.MathUtility", "GenericMatrix")

if TYPE_CHECKING:
    from mastapy.math_utility import (
        _1506,
        _1508,
        _1509,
        _1510,
        _1521,
        _1536,
        _1537,
        _1538,
        _1543,
        _1548,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GenericMatrix",)


Self = TypeVar("Self", bound="GenericMatrix")
TElement = TypeVar("TElement", bound="object")
TMatrix = TypeVar("TMatrix", bound="GenericMatrix")


class GenericMatrix(_0.APIBase, Generic[TElement, TMatrix]):
    """GenericMatrix

    This is a mastapy class.

    Generic Types:
        TElement
        TMatrix
    """

    TYPE = _GENERIC_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GenericMatrix")

    class _Cast_GenericMatrix:
        """Special nested class for casting GenericMatrix to subclasses."""

        def __init__(
            self: "GenericMatrix._Cast_GenericMatrix", parent: "GenericMatrix"
        ):
            self._parent = parent

        @property
        def complex_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1506.ComplexMatrix":
            from mastapy.math_utility import _1506

            return self._parent._cast(_1506.ComplexMatrix)

        @property
        def complex_vector(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1508.ComplexVector":
            from mastapy.math_utility import _1508

            return self._parent._cast(_1508.ComplexVector)

        @property
        def complex_vector_3d(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1509.ComplexVector3D":
            from mastapy.math_utility import _1509

            return self._parent._cast(_1509.ComplexVector3D)

        @property
        def complex_vector_6d(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1510.ComplexVector6D":
            from mastapy.math_utility import _1510

            return self._parent._cast(_1510.ComplexVector6D)

        @property
        def euler_parameters(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1521.EulerParameters":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.EulerParameters)

        @property
        def quaternion(self: "GenericMatrix._Cast_GenericMatrix") -> "_1536.Quaternion":
            from mastapy.math_utility import _1536

            return self._parent._cast(_1536.Quaternion)

        @property
        def real_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1537.RealMatrix":
            from mastapy.math_utility import _1537

            return self._parent._cast(_1537.RealMatrix)

        @property
        def real_vector(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1538.RealVector":
            from mastapy.math_utility import _1538

            return self._parent._cast(_1538.RealVector)

        @property
        def square_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1543.SquareMatrix":
            from mastapy.math_utility import _1543

            return self._parent._cast(_1543.SquareMatrix)

        @property
        def vector_6d(self: "GenericMatrix._Cast_GenericMatrix") -> "_1548.Vector6D":
            from mastapy.math_utility import _1548

            return self._parent._cast(_1548.Vector6D)

        @property
        def generic_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "GenericMatrix":
            return self._parent

        def __getattr__(self: "GenericMatrix._Cast_GenericMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GenericMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @property
    def number_of_entries(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfEntries

        if temp is None:
            return 0

        return temp

    @property
    def number_of_rows(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfRows

        if temp is None:
            return 0

        return temp

    @property
    def data(self: Self) -> "List[TElement]":
        """List[TElement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def get_column_at(self: Self, index: "int") -> "List[TElement]":
        """List[TElement]

        Args:
            index (int)
        """
        index = int(index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetColumnAt(index if index else 0)
        )

    @enforce_parameter_types
    def get_row_at(self: Self, row_index: "int") -> "List[TElement]":
        """List[TElement]

        Args:
            row_index (int)
        """
        row_index = int(row_index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetRowAt(row_index if row_index else 0)
        )

    @property
    def cast_to(self: Self) -> "GenericMatrix._Cast_GenericMatrix":
        return self._Cast_GenericMatrix(self)
