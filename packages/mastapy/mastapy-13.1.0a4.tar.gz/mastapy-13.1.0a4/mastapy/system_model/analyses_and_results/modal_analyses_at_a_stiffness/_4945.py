"""HypoidGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4886,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "HypoidGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.static_loads import _6934
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4944,
        _4943,
        _4914,
        _4941,
        _4980,
        _4880,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="HypoidGearSetModalAnalysisAtAStiffness")


class HypoidGearSetModalAnalysisAtAStiffness(
    _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
):
    """HypoidGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_HypoidGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting HypoidGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
            parent: "HypoidGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4914.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4941.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "HypoidGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "HypoidGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6934.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4944.HypoidGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4944.HypoidGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4943.HypoidGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4943.HypoidGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness":
        return self._Cast_HypoidGearSetModalAnalysisAtAStiffness(self)
