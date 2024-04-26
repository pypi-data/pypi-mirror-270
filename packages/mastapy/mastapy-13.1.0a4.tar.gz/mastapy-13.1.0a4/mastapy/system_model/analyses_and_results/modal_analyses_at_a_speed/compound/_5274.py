"""AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5302,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5145,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5281,
        _5284,
        _5285,
        _5286,
        _5332,
        _5369,
        _5375,
        _5378,
        _5381,
        _5382,
        _5396,
        _5328,
        _5347,
        _5295,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed(
    _5302.ConicalGearCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5302.ConicalGearCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5302.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5347.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5295.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(_5295.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5281.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5284.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(
                _5284.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5285.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(
                _5285.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5286.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5332.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5375.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5378.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(
                _5378.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5381.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(
                _5381.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5382.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5396.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5396,
            )

            return self._parent._cast(_5396.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed(self)
