"""CouplingConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5161,
        _5166,
        _5221,
        _5243,
        _5258,
        _5175,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingConnectionModalAnalysisAtASpeed")


class CouplingConnectionModalAnalysisAtASpeed(
    _5205.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """CouplingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionModalAnalysisAtASpeed"
    )

    class _Cast_CouplingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CouplingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
            parent: "CouplingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5205.InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5205.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5161.ClutchConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5166.ConceptCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(
                _5166.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(
                _5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5243.SpringDamperConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5258.TorqueConverterConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5258,
            )

            return self._parent._cast(
                _5258.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "CouplingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2364.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed":
        return self._Cast_CouplingConnectionModalAnalysisAtASpeed(self)
