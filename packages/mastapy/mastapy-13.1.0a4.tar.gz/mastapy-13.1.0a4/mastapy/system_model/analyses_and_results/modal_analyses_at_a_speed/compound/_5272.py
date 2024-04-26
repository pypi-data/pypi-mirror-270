"""AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5295,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5142,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5271,
        _5315,
        _5326,
        _5365,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysisAtASpeed")


class AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(
    _5295.ComponentCompoundModalAnalysisAtASpeed
):
    """AbstractShaftOrHousingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5295.ComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5295.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5271.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5315.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5326.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5365.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(_5365.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5142.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

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
    ) -> "List[_5142.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

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
    ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(self)
