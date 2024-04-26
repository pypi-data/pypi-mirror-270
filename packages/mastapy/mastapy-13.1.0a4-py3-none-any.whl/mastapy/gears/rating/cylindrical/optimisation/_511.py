"""SafetyFactorOptimisationStepResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationStepResult",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _375
    from mastapy.gears.rating.cylindrical.optimisation import _512, _513, _514


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationStepResult",)


Self = TypeVar("Self", bound="SafetyFactorOptimisationStepResult")


class SafetyFactorOptimisationStepResult(_0.APIBase):
    """SafetyFactorOptimisationStepResult

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorOptimisationStepResult")

    class _Cast_SafetyFactorOptimisationStepResult:
        """Special nested class for casting SafetyFactorOptimisationStepResult to subclasses."""

        def __init__(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
            parent: "SafetyFactorOptimisationStepResult",
        ):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result_angle(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
        ) -> "_512.SafetyFactorOptimisationStepResultAngle":
            from mastapy.gears.rating.cylindrical.optimisation import _512

            return self._parent._cast(_512.SafetyFactorOptimisationStepResultAngle)

        @property
        def safety_factor_optimisation_step_result_number(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
        ) -> "_513.SafetyFactorOptimisationStepResultNumber":
            from mastapy.gears.rating.cylindrical.optimisation import _513

            return self._parent._cast(_513.SafetyFactorOptimisationStepResultNumber)

        @property
        def safety_factor_optimisation_step_result_short_length(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
        ) -> "_514.SafetyFactorOptimisationStepResultShortLength":
            from mastapy.gears.rating.cylindrical.optimisation import _514

            return self._parent._cast(
                _514.SafetyFactorOptimisationStepResultShortLength
            )

        @property
        def safety_factor_optimisation_step_result(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
        ) -> "SafetyFactorOptimisationStepResult":
            return self._parent

        def __getattr__(
            self: "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
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
        self: Self, instance_to_wrap: "SafetyFactorOptimisationStepResult.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normalised_safety_factors(self: Self) -> "_375.SafetyFactorResults":
        """mastapy.gears.rating.SafetyFactorResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def safety_factors(self: Self) -> "_375.SafetyFactorResults":
        """mastapy.gears.rating.SafetyFactorResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult":
        return self._Cast_SafetyFactorOptimisationStepResult(self)
