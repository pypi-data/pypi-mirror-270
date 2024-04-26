"""SpringDamperConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6938, _6876
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionLoadCase",)


Self = TypeVar("Self", bound="SpringDamperConnectionLoadCase")


class SpringDamperConnectionLoadCase(_6878.CouplingConnectionLoadCase):
    """SpringDamperConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperConnectionLoadCase")

    class _Cast_SpringDamperConnectionLoadCase:
        """Special nested class for casting SpringDamperConnectionLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
            parent: "SpringDamperConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6878.CouplingConnectionLoadCase":
            return self._parent._cast(_6878.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "SpringDamperConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase":
        return self._Cast_SpringDamperConnectionLoadCase(self)
