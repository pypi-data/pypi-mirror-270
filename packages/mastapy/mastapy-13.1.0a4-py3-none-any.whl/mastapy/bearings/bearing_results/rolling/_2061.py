"""LoadedSphericalRollerThrustBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2047
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerThrustBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2051
    from mastapy.bearings.bearing_results import _1972, _1975, _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerThrustBearingResults",)


Self = TypeVar("Self", bound="LoadedSphericalRollerThrustBearingResults")


class LoadedSphericalRollerThrustBearingResults(_2047.LoadedRollerBearingResults):
    """LoadedSphericalRollerThrustBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerThrustBearingResults"
    )

    class _Cast_LoadedSphericalRollerThrustBearingResults:
        """Special nested class for casting LoadedSphericalRollerThrustBearingResults to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
            parent: "LoadedSphericalRollerThrustBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "LoadedSphericalRollerThrustBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerThrustBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults":
        return self._Cast_LoadedSphericalRollerThrustBearingResults(self)
