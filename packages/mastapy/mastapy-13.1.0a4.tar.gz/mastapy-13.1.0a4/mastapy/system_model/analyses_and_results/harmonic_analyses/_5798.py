"""HypoidGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HypoidGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.system_deflections import _2786
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5739,
        _5781,
        _5800,
        _5741,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshHarmonicAnalysis")


class HypoidGearMeshHarmonicAnalysis(_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis):
    """HypoidGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshHarmonicAnalysis")

    class _Cast_HypoidGearMeshHarmonicAnalysis:
        """Special nested class for casting HypoidGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
            parent: "HypoidGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            return self._parent._cast(_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_5739.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(_5739.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_5781.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_5800.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(
                _5800.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_5741.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(_5741.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
        ) -> "HypoidGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def system_deflection_results(self: Self) -> "_2786.HypoidGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection

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
    ) -> "HypoidGearMeshHarmonicAnalysis._Cast_HypoidGearMeshHarmonicAnalysis":
        return self._Cast_HypoidGearMeshHarmonicAnalysis(self)
