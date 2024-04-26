"""LoadedAxialThrustCylindricalRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2042
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustCylindricalRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2015, _2047, _2051
    from mastapy.bearings.bearing_results import _1972, _1975, _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustCylindricalRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedAxialThrustCylindricalRollerBearingResults")


class LoadedAxialThrustCylindricalRollerBearingResults(
    _2042.LoadedNonBarrelRollerBearingResults
):
    """LoadedAxialThrustCylindricalRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustCylindricalRollerBearingResults"
    )

    class _Cast_LoadedAxialThrustCylindricalRollerBearingResults:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
            parent: "LoadedAxialThrustCylindricalRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_2042.LoadedNonBarrelRollerBearingResults":
            return self._parent._cast(_2042.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
        ) -> "LoadedAxialThrustCylindricalRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults",
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
        self: Self,
        instance_to_wrap: "LoadedAxialThrustCylindricalRollerBearingResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustCylindricalRollerBearingResults._Cast_LoadedAxialThrustCylindricalRollerBearingResults":
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingResults(self)
