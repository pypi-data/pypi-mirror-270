"""CoaxialConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4904,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5055,
        _5014,
        _5046,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundModalAnalysisAtAStiffness")


class CoaxialConnectionCompoundModalAnalysisAtAStiffness(
    _5108.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """CoaxialConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CoaxialConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5108.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            return self._parent._cast(
                _5108.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5014.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CoaxialConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CoaxialConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_4904.CoaxialConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CoaxialConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4904.CoaxialConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CoaxialConnectionModalAnalysisAtAStiffness]

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
    ) -> "CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness(self)
