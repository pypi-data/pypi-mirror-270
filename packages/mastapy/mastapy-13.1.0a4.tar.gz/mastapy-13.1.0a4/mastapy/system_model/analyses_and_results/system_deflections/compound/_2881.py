"""AssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _50
    from mastapy.system_model.part_model import _2451
    from mastapy.gears.analysis import _1237
    from mastapy.shafts import _40
    from mastapy.system_model.analyses_and_results.system_deflections import _2715
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2882,
        _2884,
        _2887,
        _2894,
        _2893,
        _2915,
        _2895,
        _2900,
        _2905,
        _2917,
        _2919,
        _2923,
        _2931,
        _2930,
        _2932,
        _2939,
        _2946,
        _2949,
        _2950,
        _2951,
        _2953,
        _2955,
        _2960,
        _2961,
        _2962,
        _2964,
        _2966,
        _2972,
        _2970,
        _2977,
        _2978,
        _2983,
        _2986,
        _2989,
        _2993,
        _2997,
        _3001,
        _3004,
        _2969,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AssemblyCompoundSystemDeflection")


class AssemblyCompoundSystemDeflection(_2874.AbstractAssemblyCompoundSystemDeflection):
    """AssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AssemblyCompoundSystemDeflection")

    class _Cast_AssemblyCompoundSystemDeflection:
        """Special nested class for casting AssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
            parent: "AssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_compound_system_deflection(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "_2969.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.RootAssemblyCompoundSystemDeflection)

        @property
        def assembly_compound_system_deflection(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
        ) -> "AssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AssemblyCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def overall_duty_cycle_bearing_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallDutyCycleBearingReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_duty_cycle_gear_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallDutyCycleGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_duty_cycle_shaft_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallDutyCycleShaftReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_oil_seal_duty_cycle_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallOilSealDutyCycleReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_system_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallSystemReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_settings(self: Self) -> "_50.AnalysisSettingsItem":
        """mastapy.nodal_analysis.AnalysisSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2451.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2451.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_for_all_gear_sets(self: Self) -> "_1237.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingForAllGearSets

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings(self: Self) -> "_40.ShaftSettingsItem":
        """mastapy.shafts.ShaftSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2715.AssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bearings(self: Self) -> "List[_2882.BearingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BearingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def belt_drives(self: Self) -> "List[_2884.BeltDriveCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BeltDriveCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gear_sets(
        self: Self,
    ) -> "List[_2887.BevelDifferentialGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolted_joints(self: Self) -> "List[_2894.BoltedJointCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BoltedJointCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolts(self: Self) -> "List[_2893.BoltCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BoltCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cv_ts(self: Self) -> "List[_2915.CVTCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CVTCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def clutches(self: Self) -> "List[_2895.ClutchCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ClutchCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_couplings(
        self: Self,
    ) -> "List[_2900.ConceptCouplingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gear_sets(
        self: Self,
    ) -> "List[_2905.ConceptGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_assemblies(
        self: Self,
    ) -> "List[_2917.CycloidalAssemblyCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalAssemblyCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_discs(
        self: Self,
    ) -> "List[_2919.CycloidalDiscCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: Self,
    ) -> "List[_2923.CylindricalGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(self: Self) -> "List[_2931.FEPartCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.FEPartCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_sets(self: Self) -> "List[_2930.FaceGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.FaceGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_assemblies(
        self: Self,
    ) -> "List[_2932.FlexiblePinAssemblyCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.FlexiblePinAssemblyCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_sets(
        self: Self,
    ) -> "List[_2939.HypoidGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.HypoidGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(
        self: Self,
    ) -> "List[_2946.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(
        self: Self,
    ) -> (
        "List[_2949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]"
    ):
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_discs(self: Self) -> "List[_2950.MassDiscCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.MassDiscCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurement_components(
        self: Self,
    ) -> "List[_2951.MeasurementComponentCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.MeasurementComponentCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def oil_seals(self: Self) -> "List[_2953.OilSealCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.OilSealCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def part_to_part_shear_couplings(
        self: Self,
    ) -> "List[_2955.PartToPartShearCouplingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_carriers(
        self: Self,
    ) -> "List[_2960.PlanetCarrierCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.PlanetCarrierCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(self: Self) -> "List[_2961.PointLoadCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.PointLoadCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(self: Self) -> "List[_2962.PowerLoadCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.PowerLoadCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_pins(self: Self) -> "List[_2964.RingPinsCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.RingPinsCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_bearings(self: Self) -> "List[_2882.BearingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BearingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingBearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_ring_assemblies(
        self: Self,
    ) -> "List[_2966.RollingRingAssemblyCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingAssemblyCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_hub_connections(
        self: Self,
    ) -> "List[_2972.ShaftHubConnectionCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftHubConnectionCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts(self: Self) -> "List[_2970.ShaftCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gear_sets(
        self: Self,
    ) -> "List[_2977.SpiralBevelGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dampers(
        self: Self,
    ) -> "List[_2978.SpringDamperCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.SpringDamperCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gear_sets(
        self: Self,
    ) -> "List[_2983.StraightBevelDiffGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gear_sets(
        self: Self,
    ) -> "List[_2986.StraightBevelGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def synchronisers(self: Self) -> "List[_2989.SynchroniserCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.SynchroniserCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_converters(
        self: Self,
    ) -> "List[_2993.TorqueConverterCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.TorqueConverterCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unbalanced_masses(
        self: Self,
    ) -> "List[_2997.UnbalancedMassCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.UnbalancedMassCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: Self) -> "List[_3001.WormGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.WormGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gear_sets(
        self: Self,
    ) -> "List[_3004.ZerolBevelGearSetCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearSetCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_2715.AssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AssemblyCompoundSystemDeflection._Cast_AssemblyCompoundSystemDeflection":
        return self._Cast_AssemblyCompoundSystemDeflection(self)
