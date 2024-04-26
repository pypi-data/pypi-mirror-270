"""CycloidalDiscCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5271,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5185,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5272,
        _5295,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundModalAnalysisAtASpeed")


class CycloidalDiscCompoundModalAnalysisAtASpeed(
    _5271.AbstractShaftCompoundModalAnalysisAtASpeed
):
    """CycloidalDiscCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CycloidalDiscCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
            parent: "CycloidalDiscCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5271.AbstractShaftCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5271.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(
                _5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5295.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(_5295.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "CycloidalDiscCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_5185.CycloidalDiscModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscModalAnalysisAtASpeed]

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
    ) -> "List[_5185.CycloidalDiscModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscModalAnalysisAtASpeed]

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
    ) -> "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed(self)
