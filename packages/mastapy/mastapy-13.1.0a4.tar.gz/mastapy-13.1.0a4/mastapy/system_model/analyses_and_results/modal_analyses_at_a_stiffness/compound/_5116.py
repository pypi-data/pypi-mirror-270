"""StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5027,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4988,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5122,
        _5123,
        _5015,
        _5043,
        _5069,
        _5088,
        _5036,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundModalAnalysisAtAStiffness")


class StraightBevelDiffGearCompoundModalAnalysisAtAStiffness(
    _5027.BevelGearCompoundModalAnalysisAtAStiffness
):
    """StraightBevelDiffGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
            parent: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.BevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5027.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5122.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5122,
            )

            return self._parent._cast(
                _5122.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5123.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5123,
            )

            return self._parent._cast(
                _5123.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
        ) -> "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4988.StraightBevelDiffGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelDiffGearModalAnalysisAtAStiffness]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4988.StraightBevelDiffGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelDiffGearModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelDiffGearCompoundModalAnalysisAtAStiffness(self)
