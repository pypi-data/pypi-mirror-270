"""BevelGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.power_flows import _4071
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2724,
        _2830,
        _2836,
        _2839,
        _2862,
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
__all__ = ("BevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshSystemDeflection")


class BevelGearMeshSystemDeflection(_2712.AGMAGleasonConicalGearMeshSystemDeflection):
    """BevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshSystemDeflection")

    class _Cast_BevelGearMeshSystemDeflection:
        """Special nested class for casting BevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            parent: "BevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2724.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2830.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2839.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2862.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "BevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4071.BevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow

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
    ) -> "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection":
        return self._Cast_BevelGearMeshSystemDeflection(self)
