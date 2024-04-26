"""ConicalGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4941,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConicalGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4913,
        _4912,
        _4886,
        _4893,
        _4898,
        _4945,
        _4949,
        _4952,
        _4955,
        _4983,
        _4989,
        _4992,
        _5010,
        _4980,
        _4880,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConicalGearSetModalAnalysisAtAStiffness")


class ConicalGearSetModalAnalysisAtAStiffness(_4941.GearSetModalAnalysisAtAStiffness):
    """ConicalGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_ConicalGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting ConicalGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
            parent: "ConicalGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4941.GearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4941.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(
                _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4893.BevelDifferentialGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(
                _4893.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4898.BevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(_4898.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4945.HypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4945,
            )

            return self._parent._cast(_4945.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4949.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4952.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(
                _4952.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> (
            "_4955.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4983.SpiralBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4989,
            )

            return self._parent._cast(
                _4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4992.StraightBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(
                _4992.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_5010.ZerolBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5010,
            )

            return self._parent._cast(_5010.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "ConicalGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConicalGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4913.ConicalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4913.ConicalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4912.ConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4912.ConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness":
        return self._Cast_ConicalGearSetModalAnalysisAtAStiffness(self)
