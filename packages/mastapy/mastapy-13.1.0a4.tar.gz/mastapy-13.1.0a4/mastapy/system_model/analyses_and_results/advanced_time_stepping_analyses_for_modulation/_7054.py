"""BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.system_deflections import _2729
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7049,
        _7138,
        _7144,
        _7147,
        _7165,
        _7070,
        _7096,
        _7103,
        _7072,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BevelGearMeshAdvancedTimeSteppingAnalysisForModulation")


class BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7041.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7041.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7041.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7096.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7049.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7144.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7144,
            )

            return self._parent._cast(
                _7144.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7147,
            )

            return self._parent._cast(
                _7147.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7165,
            )

            return self._parent._cast(
                _7165.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
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
    def system_deflection_results(self: Self) -> "_2729.BevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
