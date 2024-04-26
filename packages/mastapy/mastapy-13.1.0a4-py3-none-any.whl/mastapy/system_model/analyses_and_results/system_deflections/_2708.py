"""AbstractAssemblySystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2808
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2738,
        _2713,
        _2715,
        _2723,
        _2725,
        _2730,
        _2732,
        _2736,
        _2742,
        _2744,
        _2748,
        _2754,
        _2757,
        _2758,
        _2765,
        _2766,
        _2767,
        _2778,
        _2781,
        _2783,
        _2787,
        _2792,
        _2795,
        _2798,
        _2811,
        _2820,
        _2823,
        _2829,
        _2831,
        _2835,
        _2837,
        _2840,
        _2847,
        _2853,
        _2860,
        _2863,
    )
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2871,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4055
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblySystemDeflection")


class AbstractAssemblySystemDeflection(_2808.PartSystemDeflection):
    """AbstractAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblySystemDeflection")

    class _Cast_AbstractAssemblySystemDeflection:
        """Special nested class for casting AbstractAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            parent: "AbstractAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def part_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2715.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.AssemblySystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2723.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2732.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2736.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2742.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2744.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2754.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2757.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2758.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2765.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2766.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2767.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2778.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2781.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2811.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2820.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.RollingRingAssemblySystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2823.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.RootAssemblySystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2835.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2847.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2853.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2860.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "AbstractAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblySystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def components_with_unknown_mass_properties(
        self: Self,
    ) -> "List[_2738.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(
        self: Self,
    ) -> "List[_2738.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(
        self: Self,
    ) -> "List[_2871.RigidlyConnectedComponentGroupSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.RigidlyConnectedComponentGroupSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4055.AbstractAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection":
        return self._Cast_AbstractAssemblySystemDeflection(self)
