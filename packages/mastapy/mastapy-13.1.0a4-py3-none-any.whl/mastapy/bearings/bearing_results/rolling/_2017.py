"""LoadedBallBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2020
from mastapy.bearings.bearing_results import _1977
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.utility.property import _1856
    from mastapy.bearings.bearing_results import _1974, _1966


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedBallBearingDutyCycle")


class LoadedBallBearingDutyCycle(_1977.LoadedRollingBearingDutyCycle):
    """LoadedBallBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBallBearingDutyCycle")

    class _Cast_LoadedBallBearingDutyCycle:
        """Special nested class for casting LoadedBallBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
            parent: "LoadedBallBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
        ) -> "_1977.LoadedRollingBearingDutyCycle":
            return self._parent._cast(_1977.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
        ) -> "_1974.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
        ) -> "_1966.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBearingDutyCycle)

        @property
        def loaded_ball_bearing_duty_cycle(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
        ) -> "LoadedBallBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBallBearingDutyCycle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def track_truncation_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_inner_summary(
        self: Self,
    ) -> "_1856.DutyCyclePropertySummaryPercentage[_2020.LoadedBallBearingResults]":
        """mastapy.utility.property.DutyCyclePropertySummaryPercentage[mastapy.bearings.bearing_results.rolling.LoadedBallBearingResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationInnerSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _2020.LoadedBallBearingResults
        ](temp)

    @property
    def track_truncation_outer_summary(
        self: Self,
    ) -> "_1856.DutyCyclePropertySummaryPercentage[_2020.LoadedBallBearingResults]":
        """mastapy.utility.property.DutyCyclePropertySummaryPercentage[mastapy.bearings.bearing_results.rolling.LoadedBallBearingResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationOuterSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _2020.LoadedBallBearingResults
        ](temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle":
        return self._Cast_LoadedBallBearingDutyCycle(self)
