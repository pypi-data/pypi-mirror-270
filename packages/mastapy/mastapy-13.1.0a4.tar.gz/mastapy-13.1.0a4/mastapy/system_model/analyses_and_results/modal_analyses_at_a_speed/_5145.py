"""AGMAGleasonConicalGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5173
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5152,
        _5154,
        _5155,
        _5157,
        _5203,
        _5241,
        _5247,
        _5250,
        _5252,
        _5253,
        _5268,
        _5199,
        _5218,
        _5165,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysisAtASpeed")


class AGMAGleasonConicalGearModalAnalysisAtASpeed(
    _5173.ConicalGearModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5173.ConicalGearModalAnalysisAtASpeed":
            return self._parent._cast(_5173.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5152.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(
                _5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5155.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(
                _5155.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5157.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.BevelGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5203.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.HypoidGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5241.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5247.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5250.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(_5250.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5252.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(
                _5252.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5253.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5268.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5268,
            )

            return self._parent._cast(_5268.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearModalAnalysisAtASpeed.TYPE"
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
    ) -> "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed(self)
