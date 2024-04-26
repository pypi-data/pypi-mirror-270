"""StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6987
    from mastapy.system_model.analyses_and_results.system_deflections import _2836
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7041,
        _7070,
        _7096,
        _7103,
        _7072,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7054.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7054.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7041.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7096.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def system_deflection_results(
        self: Self,
    ) -> "_2836.StraightBevelDiffGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection

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
    ) -> "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation(
            self
        )
