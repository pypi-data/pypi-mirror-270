"""ZerolBevelGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ZerolBevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7014
    from mastapy.system_model.analyses_and_results.system_deflections import _2863
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4737,
        _4736,
        _4601,
        _4629,
        _4660,
        _4705,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetModalAnalysis")


class ZerolBevelGearSetModalAnalysis(_4613.BevelGearSetModalAnalysis):
    """ZerolBevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetModalAnalysis")

    class _Cast_ZerolBevelGearSetModalAnalysis:
        """Special nested class for casting ZerolBevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
            parent: "ZerolBevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4613.BevelGearSetModalAnalysis":
            return self._parent._cast(_4613.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "ZerolBevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2572.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7014.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2863.ZerolBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_modal_analysis(
        self: Self,
    ) -> "List[_4737.ZerolBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis]

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
    def zerol_bevel_gears_modal_analysis(
        self: Self,
    ) -> "List[_4737.ZerolBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4736.ZerolBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis]

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
    def zerol_bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4736.ZerolBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis":
        return self._Cast_ZerolBevelGearSetModalAnalysis(self)
