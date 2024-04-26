"""NewtonRaphsonDegreeOfFreedomError"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWTON_RAPHSON_DEGREE_OF_FREEDOM_ERROR = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewtonRaphsonDegreeOfFreedomError"
)


__docformat__ = "restructuredtext en"
__all__ = ("NewtonRaphsonDegreeOfFreedomError",)


Self = TypeVar("Self", bound="NewtonRaphsonDegreeOfFreedomError")


class NewtonRaphsonDegreeOfFreedomError(_0.APIBase):
    """NewtonRaphsonDegreeOfFreedomError

    This is a mastapy class.
    """

    TYPE = _NEWTON_RAPHSON_DEGREE_OF_FREEDOM_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewtonRaphsonDegreeOfFreedomError")

    class _Cast_NewtonRaphsonDegreeOfFreedomError:
        """Special nested class for casting NewtonRaphsonDegreeOfFreedomError to subclasses."""

        def __init__(
            self: "NewtonRaphsonDegreeOfFreedomError._Cast_NewtonRaphsonDegreeOfFreedomError",
            parent: "NewtonRaphsonDegreeOfFreedomError",
        ):
            self._parent = parent

        @property
        def newton_raphson_degree_of_freedom_error(
            self: "NewtonRaphsonDegreeOfFreedomError._Cast_NewtonRaphsonDegreeOfFreedomError",
        ) -> "NewtonRaphsonDegreeOfFreedomError":
            return self._parent

        def __getattr__(
            self: "NewtonRaphsonDegreeOfFreedomError._Cast_NewtonRaphsonDegreeOfFreedomError",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "NewtonRaphsonDegreeOfFreedomError.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def residual(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Residual

        if temp is None:
            return 0.0

        return temp

    @property
    def scaled_residual(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScaledResidual

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "NewtonRaphsonDegreeOfFreedomError._Cast_NewtonRaphsonDegreeOfFreedomError":
        return self._Cast_NewtonRaphsonDegreeOfFreedomError(self)
