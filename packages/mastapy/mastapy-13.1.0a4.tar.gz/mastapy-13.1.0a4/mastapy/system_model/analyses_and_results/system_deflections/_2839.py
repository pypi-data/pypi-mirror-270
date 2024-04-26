"""StraightBevelGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "StraightBevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel import _402
    from mastapy.system_model.connections_and_sockets.gears import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6990
    from mastapy.system_model.analyses_and_results.power_flows import _4168
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2712,
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
__all__ = ("StraightBevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelGearMeshSystemDeflection")


class StraightBevelGearMeshSystemDeflection(_2729.BevelGearMeshSystemDeflection):
    """StraightBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshSystemDeflection"
    )

    class _Cast_StraightBevelGearMeshSystemDeflection:
        """Special nested class for casting StraightBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
            parent: "StraightBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2729.BevelGearMeshSystemDeflection":
            return self._parent._cast(_2729.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
        ) -> "StraightBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_402.StraightBevelGearMeshRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_402.StraightBevelGearMeshRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2345.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6990.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4168.StraightBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow

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
    ) -> "StraightBevelGearMeshSystemDeflection._Cast_StraightBevelGearMeshSystemDeflection":
        return self._Cast_StraightBevelGearMeshSystemDeflection(self)
