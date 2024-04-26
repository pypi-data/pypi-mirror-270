"""CoaxialConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4979,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CoaxialConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4924,
        _4883,
        _4915,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CoaxialConnectionModalAnalysisAtAStiffness")


class CoaxialConnectionModalAnalysisAtAStiffness(
    _4979.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
):
    """CoaxialConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_CoaxialConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
            parent: "CoaxialConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4979.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4979.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4883.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(
                _4883.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4915.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4924.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "CoaxialConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CoaxialConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6863.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness":
        return self._Cast_CoaxialConnectionModalAnalysisAtAStiffness(self)
