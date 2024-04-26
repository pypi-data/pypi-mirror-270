"""SpecialisedAssemblyAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SpecialisedAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7305,
        _7309,
        _7312,
        _7317,
        _7319,
        _7320,
        _7325,
        _7330,
        _7333,
        _7337,
        _7340,
        _7343,
        _7349,
        _7356,
        _7358,
        _7361,
        _7365,
        _7369,
        _7372,
        _7375,
        _7382,
        _7386,
        _7394,
        _7403,
        _7404,
        _7409,
        _7412,
        _7415,
        _7419,
        _7428,
        _7431,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyAdvancedSystemDeflection")


class SpecialisedAssemblyAdvancedSystemDeflection(
    _7296.AbstractAssemblyAdvancedSystemDeflection
):
    """SpecialisedAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def belt_drive_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7309.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7312.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(
                _7312.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7317.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7319.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7320.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7325.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7330.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7337.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.CouplingAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7340.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.CVTAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7343.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7349.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7356.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.FaceGearSetAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7358.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7361.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.GearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7365.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(
                _7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(
                _7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7382.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7386.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7394.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(_7394.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7403.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7404.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.SpringDamperAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7409.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7412.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(
                _7412.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7415.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7415,
            )

            return self._parent._cast(_7415.SynchroniserAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7419.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7419,
            )

            return self._parent._cast(_7419.TorqueConverterAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7428.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7428,
            )

            return self._parent._cast(_7428.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "_7431.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7431,
            )

            return self._parent._cast(_7431.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyAdvancedSystemDeflection(self)
