"""AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5164,
        _5184,
        _5186,
        _5224,
        _5238,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"
)


class AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed(
    _5175.ConnectionModalAnalysisAtASpeed
):
    """AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
            parent: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5164.CoaxialConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5184.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5186.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5224.PlanetaryConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5238.ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(
                _5238.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2283.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed(
                self
            )
        )
