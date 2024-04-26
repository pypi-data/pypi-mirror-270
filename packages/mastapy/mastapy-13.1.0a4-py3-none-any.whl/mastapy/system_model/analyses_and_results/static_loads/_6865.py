"""ConceptCouplingConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.static_loads import _6938, _6876
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionLoadCase",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionLoadCase")


class ConceptCouplingConnectionLoadCase(_6878.CouplingConnectionLoadCase):
    """ConceptCouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingConnectionLoadCase")

    class _Cast_ConceptCouplingConnectionLoadCase:
        """Special nested class for casting ConceptCouplingConnectionLoadCase to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
            parent: "ConceptCouplingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_6878.CouplingConnectionLoadCase":
            return self._parent._cast(_6878.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_load_case(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
        ) -> "ConceptCouplingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionLoadCase.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase":
        return self._Cast_ConceptCouplingConnectionLoadCase(self)
