"""BevelGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4612,
        _4611,
        _4608,
        _4708,
        _4714,
        _4717,
        _4738,
        _4629,
        _4660,
        _4705,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2730
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetModalAnalysis")


class BevelGearSetModalAnalysis(_4601.AGMAGleasonConicalGearSetModalAnalysis):
    """BevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetModalAnalysis")

    class _Cast_BevelGearSetModalAnalysis:
        """Special nested class for casting BevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
            parent: "BevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4608.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4708.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4714.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4717.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "_4738.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4738

            return self._parent._cast(_4738.ZerolBevelGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "BevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2538.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_modal_analysis(
        self: Self,
    ) -> "List[_4612.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_gears_modal_analysis(self: Self) -> "List[_4612.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4611.BevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4611.BevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2730.BevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection

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
    ) -> "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis":
        return self._Cast_BevelGearSetModalAnalysis(self)
