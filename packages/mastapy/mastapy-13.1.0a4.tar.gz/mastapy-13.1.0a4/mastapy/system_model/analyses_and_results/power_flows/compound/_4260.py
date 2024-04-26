"""KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2337
    from mastapy.system_model.analyses_and_results.power_flows import _4127
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4223,
        _4249,
        _4255,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow")


class KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow(
    _4257.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_4257.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow":
            return self._parent._cast(
                _4257.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_4223.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_4249.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_4255.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(
                _4255.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "List[_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

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
    ) -> "List[_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow(self)
