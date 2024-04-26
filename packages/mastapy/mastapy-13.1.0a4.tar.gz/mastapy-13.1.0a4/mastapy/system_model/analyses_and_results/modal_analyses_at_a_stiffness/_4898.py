"""BevelGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4886,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4897,
        _4896,
        _4893,
        _4983,
        _4989,
        _4992,
        _5010,
        _4914,
        _4941,
        _4980,
        _4880,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearSetModalAnalysisAtAStiffness")


class BevelGearSetModalAnalysisAtAStiffness(
    _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
):
    """BevelGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
            parent: "BevelGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4914.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4941.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4893.BevelDifferentialGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(
                _4893.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4983.SpiralBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4989,
            )

            return self._parent._cast(
                _4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4992.StraightBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(
                _4992.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "_5010.ZerolBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5010,
            )

            return self._parent._cast(_5010.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
        ) -> "BevelGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearSetModalAnalysisAtAStiffness.TYPE"
    ):
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
    def agma_gleason_conical_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4897.BevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearModalAnalysisAtAStiffness]

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
    def bevel_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4897.BevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearModalAnalysisAtAStiffness]

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
    def agma_gleason_conical_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4896.BevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearMeshModalAnalysisAtAStiffness]

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
    def bevel_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4896.BevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearMeshModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearSetModalAnalysisAtAStiffness._Cast_BevelGearSetModalAnalysisAtAStiffness":
        return self._Cast_BevelGearSetModalAnalysisAtAStiffness(self)
