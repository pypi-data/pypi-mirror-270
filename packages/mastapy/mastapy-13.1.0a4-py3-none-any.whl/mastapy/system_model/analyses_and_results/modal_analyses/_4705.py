"""SpecialisedAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4595
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpecialisedAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.system_deflections import _2829
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4601,
        _4605,
        _4608,
        _4613,
        _4614,
        _4618,
        _4623,
        _4626,
        _4629,
        _4635,
        _4637,
        _4639,
        _4645,
        _4654,
        _4656,
        _4660,
        _4664,
        _4668,
        _4671,
        _4674,
        _4688,
        _4690,
        _4697,
        _4708,
        _4711,
        _4714,
        _4717,
        _4721,
        _4725,
        _4735,
        _4738,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysis")


class SpecialisedAssemblyModalAnalysis(_4595.AbstractAssemblyModalAnalysis):
    """SpecialisedAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysis")

    class _Cast_SpecialisedAssemblyModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            parent: "SpecialisedAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4605.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4608.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4613.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4614.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4618.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4623.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4626.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4635.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4637.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4639.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4645.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4654.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4656.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4664.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(
                _4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4688.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4690.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4697.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.RollingRingAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4708.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4711.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4714.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4717.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4721.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4721

            return self._parent._cast(_4721.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4725.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4735.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4738.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4738

            return self._parent._cast(_4738.ZerolBevelGearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "SpecialisedAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2829.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

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
    ) -> "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis":
        return self._Cast_SpecialisedAssemblyModalAnalysis(self)
