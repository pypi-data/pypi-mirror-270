"""ZerolBevelGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4898,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ZerolBevelGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7014
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5009,
        _5008,
        _4886,
        _4914,
        _4941,
        _4980,
        _4880,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ZerolBevelGearSetModalAnalysisAtAStiffness")


class ZerolBevelGearSetModalAnalysisAtAStiffness(
    _4898.BevelGearSetModalAnalysisAtAStiffness
):
    """ZerolBevelGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_ZerolBevelGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting ZerolBevelGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
            parent: "ZerolBevelGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4898.BevelGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4898.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(
                _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4914.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4941.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
        ) -> "ZerolBevelGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetModalAnalysisAtAStiffness.TYPE"
    ):
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
    def bevel_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5009.ZerolBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5009.ZerolBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5008.ZerolBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5008.ZerolBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness":
        return self._Cast_ZerolBevelGearSetModalAnalysisAtAStiffness(self)
