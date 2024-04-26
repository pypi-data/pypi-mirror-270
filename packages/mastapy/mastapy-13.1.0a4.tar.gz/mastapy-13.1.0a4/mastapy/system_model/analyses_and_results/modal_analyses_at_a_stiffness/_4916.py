"""ConnectorModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4959,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConnectorModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4888,
        _4960,
        _4977,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConnectorModalAnalysisAtAStiffness")


class ConnectorModalAnalysisAtAStiffness(
    _4959.MountableComponentModalAnalysisAtAStiffness
):
    """ConnectorModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysisAtAStiffness")

    class _Cast_ConnectorModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectorModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
            parent: "ConnectorModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4888.BearingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.BearingModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4960.OilSealModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.OilSealModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "_4977.ShaftHubConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "ConnectorModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConnectorModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness":
        return self._Cast_ConnectorModalAnalysisAtAStiffness(self)
