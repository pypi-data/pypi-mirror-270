"""AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7117,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7042,
        _7043,
        _7047,
        _7050,
        _7055,
        _7057,
        _7058,
        _7063,
        _7068,
        _7071,
        _7074,
        _7077,
        _7080,
        _7086,
        _7092,
        _7094,
        _7097,
        _7102,
        _7106,
        _7109,
        _7112,
        _7118,
        _7122,
        _7130,
        _7132,
        _7136,
        _7139,
        _7140,
        _7145,
        _7148,
        _7151,
        _7155,
        _7163,
        _7166,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7117.PartAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7043.AssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7047.BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.BoltedJointAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.ClutchAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7063.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7068.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7074.CouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7080.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7094.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7122.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7130.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7132.RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.SpringDamperAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7145,
            )

            return self._parent._cast(
                _7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7148,
            )

            return self._parent._cast(
                _7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7151.SynchroniserAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7151,
            )

            return self._parent._cast(
                _7151.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7155.TorqueConverterAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7155,
            )

            return self._parent._cast(
                _7155.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7163.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7163,
            )

            return self._parent._cast(
                _7163.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7166,
            )

            return self._parent._cast(
                _7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2708.AbstractAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation(
            self
        )
