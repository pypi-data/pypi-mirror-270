"""AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4882,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5012,
        _5056,
        _5067,
        _5106,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness")


class AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness(
    _5036.ComponentCompoundModalAnalysisAtAStiffness
):
    """AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
            parent: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.AbstractShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5056.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.FEPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "_5106.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(_5106.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4882.AbstractShaftOrHousingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftOrHousingModalAnalysisAtAStiffness]

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
    ) -> "List[_4882.AbstractShaftOrHousingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftOrHousingModalAnalysisAtAStiffness]

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
    ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness(self)
