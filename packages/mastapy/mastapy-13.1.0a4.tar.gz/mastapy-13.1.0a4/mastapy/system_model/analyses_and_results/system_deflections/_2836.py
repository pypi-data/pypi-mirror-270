"""StraightBevelDiffGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "StraightBevelDiffGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel_diff import _405
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6987
    from mastapy.system_model.analyses_and_results.power_flows import _4165
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
__all__ = ("StraightBevelDiffGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshSystemDeflection")


class StraightBevelDiffGearMeshSystemDeflection(_2729.BevelGearMeshSystemDeflection):
    """StraightBevelDiffGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearMeshSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
            parent: "StraightBevelDiffGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2729.BevelGearMeshSystemDeflection":
            return self._parent._cast(_2729.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
        ) -> "StraightBevelDiffGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_405.StraightBevelDiffGearMeshRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_405.StraightBevelDiffGearMeshRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2343.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6987.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4165.StraightBevelDiffGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearMeshPowerFlow

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
    ) -> "StraightBevelDiffGearMeshSystemDeflection._Cast_StraightBevelDiffGearMeshSystemDeflection":
        return self._Cast_StraightBevelDiffGearMeshSystemDeflection(self)
