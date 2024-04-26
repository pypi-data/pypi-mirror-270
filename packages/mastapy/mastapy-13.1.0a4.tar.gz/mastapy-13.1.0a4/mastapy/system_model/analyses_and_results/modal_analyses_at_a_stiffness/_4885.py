"""AGMAGleasonConicalGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4913,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AGMAGleasonConicalGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4892,
        _4894,
        _4895,
        _4897,
        _4944,
        _4982,
        _4988,
        _4991,
        _4993,
        _4994,
        _5009,
        _4940,
        _4959,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysisAtAStiffness")


class AGMAGleasonConicalGearModalAnalysisAtAStiffness(
    _4913.ConicalGearModalAnalysisAtAStiffness
):
    """AGMAGleasonConicalGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness"
    )

    class _Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
            parent: "AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4913.ConicalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4913.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4940.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4892.BevelDifferentialGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(
                _4892.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(
                _4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4895.BevelDifferentialSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(
                _4895.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4897.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.BevelGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4944.HypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.HypoidGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4982.SpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4988.StraightBevelDiffGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4988,
            )

            return self._parent._cast(
                _4988.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4991.StraightBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4991,
            )

            return self._parent._cast(_4991.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4993.StraightBevelPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4993,
            )

            return self._parent._cast(
                _4993.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4994.StraightBevelSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4994,
            )

            return self._parent._cast(
                _4994.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_5009.ZerolBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5009,
            )

            return self._parent._cast(_5009.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "AGMAGleasonConicalGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness":
        return self._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness(self)
