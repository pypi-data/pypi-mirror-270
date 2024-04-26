"""LoadedDetailedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1975
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DETAILED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedDetailedBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials import _274
    from mastapy.bearings.bearing_results.rolling import (
        _2001,
        _2004,
        _2007,
        _2012,
        _2015,
        _2020,
        _2023,
        _2027,
        _2030,
        _2035,
        _2039,
        _2042,
        _2047,
        _2051,
        _2054,
        _2058,
        _2061,
        _2066,
        _2069,
        _2072,
        _2075,
    )
    from mastapy.bearings.bearing_results.fluid_film import (
        _2137,
        _2138,
        _2139,
        _2140,
        _2142,
        _2145,
        _2146,
    )
    from mastapy.bearings.bearing_results import _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDetailedBearingResults",)


Self = TypeVar("Self", bound="LoadedDetailedBearingResults")


class LoadedDetailedBearingResults(_1975.LoadedNonLinearBearingResults):
    """LoadedDetailedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_DETAILED_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedDetailedBearingResults")

    class _Cast_LoadedDetailedBearingResults:
        """Special nested class for casting LoadedDetailedBearingResults to subclasses."""

        def __init__(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
            parent: "LoadedDetailedBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2001.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(_2001.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2004.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(
                _2004.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2007.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(
                _2007.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2020.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2023.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2027.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2030.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2035.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2039.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2042.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2054.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2058.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2061.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2066.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2069.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2069

            return self._parent._cast(_2069.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2072.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2075.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2137.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2137

            return self._parent._cast(_2137.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2138.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2138

            return self._parent._cast(_2138.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2139.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2140.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2142.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2145.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2145

            return self._parent._cast(_2145.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2146.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2146

            return self._parent._cast(_2146.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "LoadedDetailedBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedDetailedBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lubricant_flow_rate(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantFlowRate

        if temp is None:
            return 0.0

        return temp

    @lubricant_flow_rate.setter
    @enforce_parameter_types
    def lubricant_flow_rate(self: Self, value: "float"):
        self.wrapped.LubricantFlowRate = float(value) if value is not None else 0.0

    @property
    def oil_sump_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilSumpTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_sump_temperature.setter
    @enforce_parameter_types
    def oil_sump_temperature(self: Self, value: "float"):
        self.wrapped.OilSumpTemperature = float(value) if value is not None else 0.0

    @property
    def operating_air_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OperatingAirTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_air_temperature.setter
    @enforce_parameter_types
    def operating_air_temperature(self: Self, value: "float"):
        self.wrapped.OperatingAirTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def temperature_when_assembled(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureWhenAssembled

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    @enforce_parameter_types
    def temperature_when_assembled(self: Self, value: "float"):
        self.wrapped.TemperatureWhenAssembled = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubrication(self: Self) -> "_274.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Lubrication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults":
        return self._Cast_LoadedDetailedBearingResults(self)
