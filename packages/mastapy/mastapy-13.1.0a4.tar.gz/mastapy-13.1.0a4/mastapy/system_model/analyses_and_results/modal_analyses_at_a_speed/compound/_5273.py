"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5143,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5294,
        _5314,
        _5316,
        _5353,
        _5367,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5305.ConnectionCompoundModalAnalysisAtASpeed
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5305.ConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5305.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CoaxialConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(
                _5294.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5314.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5316.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(
                _5316.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5353.PlanetaryConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5367.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5143.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5143.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
            self
        )
