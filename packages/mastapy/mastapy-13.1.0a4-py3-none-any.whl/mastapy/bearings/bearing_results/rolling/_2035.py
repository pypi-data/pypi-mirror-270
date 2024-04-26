"""LoadedFourPointContactBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2020
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedFourPointContactBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1990, _2051
    from mastapy.bearings.bearing_results import _1972, _1975, _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFourPointContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedFourPointContactBallBearingResults")


class LoadedFourPointContactBallBearingResults(_2020.LoadedBallBearingResults):
    """LoadedFourPointContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedFourPointContactBallBearingResults"
    )

    class _Cast_LoadedFourPointContactBallBearingResults:
        """Special nested class for casting LoadedFourPointContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
            parent: "LoadedFourPointContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_2020.LoadedBallBearingResults":
            return self._parent._cast(_2020.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "LoadedFourPointContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedFourPointContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def raceway_control(self: Self) -> "_1990.FrictionModelForGyroscopicMoment":
        """mastapy.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RacewayControl

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.FrictionModelForGyroscopicMoment",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._1990",
            "FrictionModelForGyroscopicMoment",
        )(value)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults":
        return self._Cast_LoadedFourPointContactBallBearingResults(self)
