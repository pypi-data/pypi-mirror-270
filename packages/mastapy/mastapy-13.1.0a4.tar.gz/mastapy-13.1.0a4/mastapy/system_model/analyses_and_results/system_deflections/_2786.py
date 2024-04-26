"""HypoidGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "HypoidGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _445
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.power_flows import _4120
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2747,
        _2782,
        _2790,
        _2750,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearMeshSystemDeflection")


class HypoidGearMeshSystemDeflection(_2712.AGMAGleasonConicalGearMeshSystemDeflection):
    """HypoidGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshSystemDeflection")

    class _Cast_HypoidGearMeshSystemDeflection:
        """Special nested class for casting HypoidGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
            parent: "HypoidGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "HypoidGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_445.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_445.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6933.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4120.HypoidGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection":
        return self._Cast_HypoidGearMeshSystemDeflection(self)
