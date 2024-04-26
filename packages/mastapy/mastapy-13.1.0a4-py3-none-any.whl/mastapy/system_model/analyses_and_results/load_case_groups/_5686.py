"""AbstractStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2457, _2471, _2489, _2490
from mastapy.system_model.analyses_and_results.static_loads import (
    _6846,
    _6888,
    _6890,
    _6892,
    _6914,
    _6917,
    _6919,
    _6922,
    _6965,
    _6966,
)
from mastapy.system_model.part_model.gears import _2544, _2543, _2550, _2548
from mastapy.system_model.connections_and_sockets.gears import _2327, _2331
from mastapy.system_model.analyses_and_results.load_case_groups import _5685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5699,
        _5702,
        _5703,
    )
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5684,
        _5689,
        _5690,
        _5693,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6831, _6844
    from mastapy.system_model.analyses_and_results import (
        _2704,
        _2699,
        _2681,
        _2691,
        _2701,
        _2694,
        _2684,
        _2700,
        _2683,
        _2688,
        _2642,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="AbstractStaticLoadCaseGroup")


class AbstractStaticLoadCaseGroup(_5685.AbstractLoadCaseGroup):
    """AbstractStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractStaticLoadCaseGroup")

    class _Cast_AbstractStaticLoadCaseGroup:
        """Special nested class for casting AbstractStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
            parent: "AbstractStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def abstract_load_case_group(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "_5685.AbstractLoadCaseGroup":
            return self._parent._cast(_5685.AbstractLoadCaseGroup)

        @property
        def abstract_design_state_load_case_group(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "_5684.AbstractDesignStateLoadCaseGroup":
            return self._parent._cast(_5684.AbstractDesignStateLoadCaseGroup)

        @property
        def design_state(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "_5689.DesignState":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5689

            return self._parent._cast(_5689.DesignState)

        @property
        def duty_cycle(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "_5690.DutyCycle":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5690

            return self._parent._cast(_5690.DutyCycle)

        @property
        def sub_group_in_single_design_state(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "_5693.SubGroupInSingleDesignState":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5693

            return self._parent._cast(_5693.SubGroupInSingleDesignState)

        @property
        def abstract_static_load_case_group(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
        ) -> "AbstractStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max_number_of_load_cases_to_display(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaxNumberOfLoadCasesToDisplay

        if temp is None:
            return 0

        return temp

    @max_number_of_load_cases_to_display.setter
    @enforce_parameter_types
    def max_number_of_load_cases_to_display(self: Self, value: "int"):
        self.wrapped.MaxNumberOfLoadCasesToDisplay = (
            int(value) if value is not None else 0
        )

    @property
    def bearings(
        self: Self,
    ) -> (
        "List[_5699.ComponentStaticLoadCaseGroup[_2457.Bearing, _6846.BearingLoadCase]]"
    ):
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.Bearing, mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase]]

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
    def cylindrical_gear_sets(
        self: Self,
    ) -> "List[_5702.GearSetStaticLoadCaseGroup[_2544.CylindricalGearSet, _2543.CylindricalGear, _6888.CylindricalGearLoadCase, _2327.CylindricalGearMesh, _6890.CylindricalGearMeshLoadCase, _6892.CylindricalGearSetLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy.system_model.part_model.gears.CylindricalGearSet, mastapy.system_model.part_model.gears.CylindricalGear, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase, mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase]]

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
    def design_states(self: Self) -> "List[_5684.AbstractDesignStateLoadCaseGroup]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.AbstractDesignStateLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(
        self: Self,
    ) -> "List[_5699.ComponentStaticLoadCaseGroup[_2471.FEPart, _6914.FEPartLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.FEPart, mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase]]

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
    def gear_sets(
        self: Self,
    ) -> "List[_5702.GearSetStaticLoadCaseGroup[_2550.GearSet, _2548.Gear, _6917.GearLoadCase, _2331.GearMesh, _6919.GearMeshLoadCase, _6922.GearSetLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy.system_model.part_model.gears.GearSet, mastapy.system_model.part_model.gears.Gear, mastapy.system_model.analyses_and_results.static_loads.GearLoadCase, mastapy.system_model.connections_and_sockets.gears.GearMesh, mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase, mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def parts_with_excitations(self: Self) -> "List[_5703.PartStaticLoadCaseGroup]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.PartStaticLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartsWithExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(
        self: Self,
    ) -> "List[_5699.ComponentStaticLoadCaseGroup[_2489.PointLoad, _6965.PointLoadLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.PointLoad, mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase]]

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
    def power_loads(
        self: Self,
    ) -> "List[_5699.ComponentStaticLoadCaseGroup[_2490.PowerLoad, _6966.PowerLoadLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.PowerLoad, mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase]]

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
    def static_loads(self: Self) -> "List[_6831.StaticLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def static_loads_limited_by_max_number_of_load_cases_to_display(
        self: Self,
    ) -> "List[_6831.StaticLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def compound_system_deflection(
        self: Self,
    ) -> "_2704.CompoundSystemDeflectionAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundSystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_power_flow(self: Self) -> "_2699.CompoundPowerFlowAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundPowerFlowAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundPowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_system_deflection(
        self: Self,
    ) -> "_2681.CompoundAdvancedSystemDeflectionAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundAdvancedSystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundAdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_harmonic_analysis(self: Self) -> "_2691.CompoundHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundHarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundHarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_steady_state_synchronous_response(
        self: Self,
    ) -> "_2701.CompoundSteadyStateSynchronousResponseAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundSteadyStateSynchronousResponseAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_modal_analysis(self: Self) -> "_2694.CompoundModalAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_critical_speed_analysis(
        self: Self,
    ) -> "_2684.CompoundCriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundCriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_stability_analysis(self: Self) -> "_2700.CompoundStabilityAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundStabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundStabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "_2683.CompoundAdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.CompoundAdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_dynamic_model_for_modal_analysis(
        self: Self,
    ) -> "_2688.CompoundDynamicModelForModalAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundDynamicModelForModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundDynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_all_load_cases(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    def run_power_flow(self: Self):
        """Method does not return."""
        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    @enforce_parameter_types
    def analysis_of(
        self: Self, analysis_type: "_6844.AnalysisType"
    ) -> "_2642.CompoundAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundAnalysis

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup":
        return self._Cast_AbstractStaticLoadCaseGroup(self)
