"""BevelDifferentialGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelDifferentialGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.power_flows import _4066
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4195,
        _4223,
        _4249,
        _4255,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundPowerFlow")


class BevelDifferentialGearMeshCompoundPowerFlow(_4207.BevelGearMeshCompoundPowerFlow):
    """BevelDifferentialGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshCompoundPowerFlow"
    )

    class _Cast_BevelDifferentialGearMeshCompoundPowerFlow:
        """Special nested class for casting BevelDifferentialGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
            parent: "BevelDifferentialGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4207.BevelGearMeshCompoundPowerFlow":
            return self._parent._cast(_4207.BevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4195.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4223.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4249.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4255.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(
                _4255.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
        ) -> "BevelDifferentialGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "List[_4066.BevelDifferentialGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearMeshPowerFlow]

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
    ) -> "List[_4066.BevelDifferentialGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearMeshPowerFlow]

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
    ) -> "BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow":
        return self._Cast_BevelDifferentialGearMeshCompoundPowerFlow(self)
