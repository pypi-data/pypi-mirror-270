"""ConicalGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4087
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4195,
        _4202,
        _4207,
        _4253,
        _4257,
        _4260,
        _4263,
        _4290,
        _4296,
        _4299,
        _4317,
        _4255,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundPowerFlow")


class ConicalGearMeshCompoundPowerFlow(_4249.GearMeshCompoundPowerFlow):
    """ConicalGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshCompoundPowerFlow")

    class _Cast_ConicalGearMeshCompoundPowerFlow:
        """Special nested class for casting ConicalGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
            parent: "ConicalGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4249.GearMeshCompoundPowerFlow":
            return self._parent._cast(_4249.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4255.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(
                _4255.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4195.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4202.BevelDifferentialGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4207.BevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.BevelGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4253.HypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4257.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4260.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(
                _4260.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4263.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(
                _4263.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4290.SpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4296.StraightBevelDiffGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4299.StraightBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4299,
            )

            return self._parent._cast(_4299.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "_4317.ZerolBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4317,
            )

            return self._parent._cast(_4317.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "ConicalGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_4087.ConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow]

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
    ) -> "List[_4087.ConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow]

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
    ) -> "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow":
        return self._Cast_ConicalGearMeshCompoundPowerFlow(self)
