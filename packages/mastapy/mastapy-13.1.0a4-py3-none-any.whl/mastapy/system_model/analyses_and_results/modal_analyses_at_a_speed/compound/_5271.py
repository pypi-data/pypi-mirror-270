"""AbstractShaftCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5272,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5141,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5315,
        _5365,
        _5295,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftCompoundModalAnalysisAtASpeed")


class AbstractShaftCompoundModalAnalysisAtASpeed(
    _5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
):
    """AbstractShaftCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractShaftCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_5295.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(_5295.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_5315.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "_5365.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(_5365.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5141.AbstractShaftModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftModalAnalysisAtASpeed]

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
    ) -> "List[_5141.AbstractShaftModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftModalAnalysisAtASpeed]

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
    ) -> "AbstractShaftCompoundModalAnalysisAtASpeed._Cast_AbstractShaftCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftCompoundModalAnalysisAtASpeed(self)
