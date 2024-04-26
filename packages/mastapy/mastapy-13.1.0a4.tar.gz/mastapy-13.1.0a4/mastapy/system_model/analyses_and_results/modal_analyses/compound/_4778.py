"""ConceptCouplingConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4789
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConceptCouplingConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.modal_analyses import _4621
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4816,
        _4786,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundModalAnalysis")


class ConceptCouplingConnectionCompoundModalAnalysis(
    _4789.CouplingConnectionCompoundModalAnalysis
):
    """ConceptCouplingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundModalAnalysis"
    )

    class _Cast_ConceptCouplingConnectionCompoundModalAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
            parent: "ConceptCouplingConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_4789.CouplingConnectionCompoundModalAnalysis":
            return self._parent._cast(_4789.CouplingConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_4816.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_4786.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
        ) -> "ConceptCouplingConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2362.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2362.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4621.ConceptCouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4621.ConceptCouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundModalAnalysis(self)
