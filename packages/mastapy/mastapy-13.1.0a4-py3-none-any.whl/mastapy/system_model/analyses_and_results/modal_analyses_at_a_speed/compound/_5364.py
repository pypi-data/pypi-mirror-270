"""RootAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5277,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5235,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5270,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RootAssemblyCompoundModalAnalysisAtASpeed")


class RootAssemblyCompoundModalAnalysisAtASpeed(
    _5277.AssemblyCompoundModalAnalysisAtASpeed
):
    """RootAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_RootAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting RootAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
            parent: "RootAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5277.AssemblyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5277.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5270.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "RootAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5235.RootAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RootAssemblyModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5235.RootAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RootAssemblyModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_RootAssemblyCompoundModalAnalysisAtASpeed(self)
