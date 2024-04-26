"""GearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "GearSetModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4659,
        _4658,
        _4601,
        _4608,
        _4613,
        _4626,
        _4629,
        _4645,
        _4654,
        _4664,
        _4668,
        _4671,
        _4674,
        _4690,
        _4708,
        _4714,
        _4717,
        _4735,
        _4738,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2783
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetModalAnalysis",)


Self = TypeVar("Self", bound="GearSetModalAnalysis")


class GearSetModalAnalysis(_4705.SpecialisedAssemblyModalAnalysis):
    """GearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetModalAnalysis")

    class _Cast_GearSetModalAnalysis:
        """Special nested class for casting GearSetModalAnalysis to subclasses."""

        def __init__(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
            parent: "GearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4608.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4613.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.BevelGearSetModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4626.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4645.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4654.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FaceGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4664.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(
                _4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def planetary_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4690.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PlanetaryGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4708.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4714.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4717.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelGearSetModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4735.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "_4738.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4738

            return self._parent._cast(_4738.ZerolBevelGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "GearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_modal_analysis(self: Self) -> "List[_4659.GearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_modal_analysis(self: Self) -> "List[_4658.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2783.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSetModalAnalysis._Cast_GearSetModalAnalysis":
        return self._Cast_GearSetModalAnalysis(self)
