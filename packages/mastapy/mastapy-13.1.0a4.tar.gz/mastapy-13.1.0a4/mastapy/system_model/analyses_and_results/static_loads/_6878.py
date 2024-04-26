"""CouplingConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6859,
        _6865,
        _6956,
        _6983,
        _6999,
        _6876,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionLoadCase",)


Self = TypeVar("Self", bound="CouplingConnectionLoadCase")


class CouplingConnectionLoadCase(_6938.InterMountableComponentConnectionLoadCase):
    """CouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionLoadCase")

    class _Cast_CouplingConnectionLoadCase:
        """Special nested class for casting CouplingConnectionLoadCase to subclasses."""

        def __init__(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
            parent: "CouplingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6859.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6865.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.ConceptCouplingConnectionLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6956.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.PartToPartShearCouplingConnectionLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6983.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.SpringDamperConnectionLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6999.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6999

            return self._parent._cast(_6999.TorqueConverterConnectionLoadCase)

        @property
        def coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "CouplingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionLoadCase.TYPE"):
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
    ) -> "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase":
        return self._Cast_CouplingConnectionLoadCase(self)
