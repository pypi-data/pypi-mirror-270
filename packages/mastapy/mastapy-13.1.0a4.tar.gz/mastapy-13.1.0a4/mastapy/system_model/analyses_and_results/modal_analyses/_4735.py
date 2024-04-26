"""WormGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4660
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "WormGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2570
    from mastapy.system_model.analyses_and_results.static_loads import _7011
    from mastapy.system_model.analyses_and_results.system_deflections import _2860
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4734,
        _4733,
        _4705,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetModalAnalysis",)


Self = TypeVar("Self", bound="WormGearSetModalAnalysis")


class WormGearSetModalAnalysis(_4660.GearSetModalAnalysis):
    """WormGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetModalAnalysis")

    class _Cast_WormGearSetModalAnalysis:
        """Special nested class for casting WormGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
            parent: "WormGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "WormGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2570.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7011.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2860.WormGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_modal_analysis(self: Self) -> "List[_4734.WormGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis]

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
    def worm_gears_modal_analysis(self: Self) -> "List[_4734.WormGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_modal_analysis(self: Self) -> "List[_4733.WormGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis]

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
    def worm_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4733.WormGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis":
        return self._Cast_WormGearSetModalAnalysis(self)
