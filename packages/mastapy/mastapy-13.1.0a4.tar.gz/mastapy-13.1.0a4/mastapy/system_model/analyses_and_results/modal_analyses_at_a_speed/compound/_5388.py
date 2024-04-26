"""TorqueConverterConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5308,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5258,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5335,
        _5305,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCompoundModalAnalysisAtASpeed")


class TorqueConverterConnectionCompoundModalAnalysisAtASpeed(
    _5308.CouplingConnectionCompoundModalAnalysisAtASpeed
):
    """TorqueConverterConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
            parent: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5308.CouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5308.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5305.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
        ) -> "TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_5258.TorqueConverterConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5258.TorqueConverterConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterConnectionModalAnalysisAtASpeed]

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
    ) -> "TorqueConverterConnectionCompoundModalAnalysisAtASpeed._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterConnectionCompoundModalAnalysisAtASpeed(self)
