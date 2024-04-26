"""LoadedNonBarrelRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2047
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedNonBarrelRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2090,
        _2012,
        _2015,
        _2027,
        _2039,
        _2066,
        _2051,
    )
    from mastapy.bearings.bearing_results import _1972, _1975, _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingResults")


class LoadedNonBarrelRollerBearingResults(_2047.LoadedRollerBearingResults):
    """LoadedNonBarrelRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingResults")

    class _Cast_LoadedNonBarrelRollerBearingResults:
        """Special nested class for casting LoadedNonBarrelRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
            parent: "LoadedNonBarrelRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2027.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2039.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedNeedleRollerBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "_2066.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "LoadedNonBarrelRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedNonBarrelRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def smt_rib_stress(self: Self) -> "_2090.SMTRibStressResults":
        """mastapy.bearings.bearing_results.rolling.SMTRibStressResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SMTRibStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults"
    ):
        return self._Cast_LoadedNonBarrelRollerBearingResults(self)
