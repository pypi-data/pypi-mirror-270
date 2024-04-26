"""NewtonRaphsonAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWTON_RAPHSON_ANALYSIS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewtonRaphsonAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _111


__docformat__ = "restructuredtext en"
__all__ = ("NewtonRaphsonAnalysis",)


Self = TypeVar("Self", bound="NewtonRaphsonAnalysis")


class NewtonRaphsonAnalysis(_0.APIBase):
    """NewtonRaphsonAnalysis

    This is a mastapy class.
    """

    TYPE = _NEWTON_RAPHSON_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewtonRaphsonAnalysis")

    class _Cast_NewtonRaphsonAnalysis:
        """Special nested class for casting NewtonRaphsonAnalysis to subclasses."""

        def __init__(
            self: "NewtonRaphsonAnalysis._Cast_NewtonRaphsonAnalysis",
            parent: "NewtonRaphsonAnalysis",
        ):
            self._parent = parent

        @property
        def newton_raphson_analysis(
            self: "NewtonRaphsonAnalysis._Cast_NewtonRaphsonAnalysis",
        ) -> "NewtonRaphsonAnalysis":
            return self._parent

        def __getattr__(
            self: "NewtonRaphsonAnalysis._Cast_NewtonRaphsonAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NewtonRaphsonAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sorted_errors(self: Self) -> "List[_111.NewtonRaphsonDegreeOfFreedomError]":
        """List[mastapy.nodal_analysis.system_solvers.NewtonRaphsonDegreeOfFreedomError]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SortedErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "NewtonRaphsonAnalysis._Cast_NewtonRaphsonAnalysis":
        return self._Cast_NewtonRaphsonAnalysis(self)
