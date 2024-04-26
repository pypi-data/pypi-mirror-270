"""SynchroniserPartCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5050,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4997,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5125,
        _5127,
        _5088,
        _5036,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundModalAnalysisAtAStiffness")


class SynchroniserPartCompoundModalAnalysisAtAStiffness(
    _5050.CouplingHalfCompoundModalAnalysisAtAStiffness
):
    """SynchroniserPartCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserPartCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
            parent: "SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5050.CouplingHalfCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5050.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5125.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5125,
            )

            return self._parent._cast(
                _5125.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5127.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5127,
            )

            return self._parent._cast(
                _5127.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "SynchroniserPartCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SynchroniserPartCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4997.SynchroniserPartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserPartModalAnalysisAtAStiffness]

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
    ) -> "List[_4997.SynchroniserPartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserPartModalAnalysisAtAStiffness]

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
    ) -> "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness(self)
