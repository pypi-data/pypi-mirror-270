"""LoadedRollingBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1901, _1892
    from mastapy.bearings.bearing_results.rolling.abma import _2135
    from mastapy.bearings.bearing_results.rolling import (
        _1987,
        _1996,
        _1998,
        _1991,
        _2078,
        _2052,
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
        _2054,
        _2058,
        _2061,
        _2066,
        _2069,
        _2072,
        _2075,
    )
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
        _2121,
        _2122,
        _2124,
    )
    from mastapy.bearings.bearing_results.rolling.fitting import _2128, _2130, _2131
    from mastapy.bearings.bearing_results.rolling.skf_module import _2116
    from mastapy.bearings.bearing_results import _1975, _1967


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingResults",)


Self = TypeVar("Self", bound="LoadedRollingBearingResults")


class LoadedRollingBearingResults(_1972.LoadedDetailedBearingResults):
    """LoadedRollingBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingResults")

    class _Cast_LoadedRollingBearingResults:
        """Special nested class for casting LoadedRollingBearingResults to subclasses."""

        def __init__(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
            parent: "LoadedRollingBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2001.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(_2001.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2004.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(
                _2004.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2007.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(
                _2007.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2020.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2023.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2027.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2030.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2035.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2039.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2042.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2054.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2058.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2061.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2066.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2069.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2069

            return self._parent._cast(_2069.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2072.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2075.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedToroidalRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "LoadedRollingBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_to_radial_load_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialToRadialLoadRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cage_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CageAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_element_diameter_due_to_thermal_expansion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInElementDiameterDueToThermalExpansion

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_operating_radial_internal_clearance_due_to_element_thermal_expansion(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ChangeInOperatingRadialInternalClearanceDueToElementThermalExpansion
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def drag_loss_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DragLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElementTemperature

        if temp is None:
            return 0.0

        return temp

    @element_temperature.setter
    @enforce_parameter_types
    def element_temperature(self: Self, value: "float"):
        self.wrapped.ElementTemperature = float(value) if value is not None else 0.0

    @property
    def fluid_film_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluidFilmDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def fluid_film_temperature_source(
        self: Self,
    ) -> "_1901.FluidFilmTemperatureOptions":
        """mastapy.bearings.FluidFilmTemperatureOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluidFilmTemperatureSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.FluidFilmTemperatureOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1901", "FluidFilmTemperatureOptions"
        )(value)

    @property
    def frequency_of_over_rolling_on_inner_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnInnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def frequency_of_over_rolling_on_outer_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnOuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def frequency_of_over_rolling_on_rolling_element(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnRollingElement

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_moment_of_drag_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalMomentOfDragLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_moment_of_seals(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalMomentOfSeals

        if temp is None:
            return 0.0

        return temp

    @property
    def include_centrifugal_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeCentrifugalEffects

        if temp is None:
            return False

        return temp

    @property
    def include_centrifugal_ring_expansion(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeCentrifugalRingExpansion

        if temp is None:
            return False

        return temp

    @property
    def include_fitting_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeFittingEffects

        if temp is None:
            return False

        return temp

    @property
    def include_gear_blank_elastic_distortion(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return False

        return temp

    @property
    def include_inner_race_deflections(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeInnerRaceDeflections

        if temp is None:
            return False

        return temp

    @property
    def include_thermal_expansion_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeThermalExpansionEffects

        if temp is None:
            return False

        return temp

    @property
    def is_inner_ring_rotating_relative_to_load(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsInnerRingRotatingRelativeToLoad

        if temp is None:
            return False

        return temp

    @property
    def is_outer_ring_rotating_relative_to_load(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsOuterRingRotatingRelativeToLoad

        if temp is None:
            return False

        return temp

    @property
    def kinematic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def kinematic_viscosity_of_oil_for_efficiency_calculations(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosityOfOilForEfficiencyCalculations

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_film_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantFilmTemperature

        if temp is None:
            return 0.0

        return temp

    @lubricant_film_temperature.setter
    @enforce_parameter_types
    def lubricant_film_temperature(self: Self, value: "float"):
        self.wrapped.LubricantFilmTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubricant_windage_and_churning_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantWindageAndChurningTemperature

        if temp is None:
            return 0.0

        return temp

    @lubricant_windage_and_churning_temperature.setter
    @enforce_parameter_types
    def lubricant_windage_and_churning_temperature(self: Self, value: "float"):
        self.wrapped.LubricantWindageAndChurningTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_normal_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_elements_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElementsInContact

        if temp is None:
            return 0

        return temp

    @property
    def oil_dip_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDipCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def ratio_of_operating_element_diameter_to_element_pcd(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatioOfOperatingElementDiameterToElementPCD

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_frictional_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingFrictionalMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_friction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingFrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_frictional_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingFrictionalMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_factor_dmn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactorDmn

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_factor_dn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactorDn

        if temp is None:
            return 0.0

        return temp

    @property
    def static_equivalent_load_capacity_ratio_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticEquivalentLoadCapacityRatioLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def surrounding_lubricant_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurroundingLubricantDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaInner

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaRight

        if temp is None:
            return 0.0

        return temp

    @property
    def total_frictional_moment_from_skf_loss_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalFrictionalMomentFromSKFLossMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma(self: Self) -> "_2135.ANSIABMAResults":
        """mastapy.bearings.bearing_results.rolling.abma.ANSIABMAResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din7322010(self: Self) -> "_1987.DIN7322010Results":
        """mastapy.bearings.bearing_results.rolling.DIN7322010Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN7322010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso2812007(self: Self) -> "_2121.ISO2812007Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISO2812007Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso762006(self: Self) -> "_2122.ISO762006Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISO762006Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO762006

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417912001(self: Self) -> "_1996.ISOTR1417912001Results":
        """mastapy.bearings.bearing_results.rolling.ISOTR1417912001Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417912001

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417922001(self: Self) -> "_1998.ISOTR1417922001Results":
        """mastapy.bearings.bearing_results.rolling.ISOTR1417922001Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417922001

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isots162812008(self: Self) -> "_2124.ISOTS162812008Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISOTS162812008Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_fitting_at_assembly(
        self: Self,
    ) -> "_2128.InnerRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.InnerRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingFittingAtAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_fitting_at_operating_conditions(
        self: Self,
    ) -> "_2128.InnerRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.InnerRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingFittingAtOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_operating_internal_clearance(self: Self) -> "_1991.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_static_contact_stress(self: Self) -> "_2078.MaximumStaticContactStress":
        """mastapy.bearings.bearing_results.rolling.MaximumStaticContactStress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_operating_internal_clearance(self: Self) -> "_1991.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_fitting_at_assembly(
        self: Self,
    ) -> "_2130.OuterRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.OuterRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingFittingAtAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_fitting_at_operating_conditions(
        self: Self,
    ) -> "_2130.OuterRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.OuterRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingFittingAtOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def skf_module_results(self: Self) -> "_2116.SKFModuleResults":
        """mastapy.bearings.bearing_results.rolling.skf_module.SKFModuleResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFModuleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_mounting_results(self: Self) -> "List[_2131.RingFittingThermalResults]":
        """List[mastapy.bearings.bearing_results.rolling.fitting.RingFittingThermalResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllMountingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rows(self: Self) -> "List[_2052.LoadedRollingBearingRow]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedRollingBearingRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults":
        return self._Cast_LoadedRollingBearingResults(self)
