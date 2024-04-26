"""ConceptCouplingConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4917,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConceptCouplingConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.static_loads import _6865
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4946,
        _4915,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionModalAnalysisAtAStiffness")


class ConceptCouplingConnectionModalAnalysisAtAStiffness(
    _4917.CouplingConnectionModalAnalysisAtAStiffness
):
    """ConceptCouplingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptCouplingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
            parent: "ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_4917.CouplingConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4917.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_4946.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_4915.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
        ) -> "ConceptCouplingConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "ConceptCouplingConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6865.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness":
        return self._Cast_ConceptCouplingConnectionModalAnalysisAtAStiffness(self)
