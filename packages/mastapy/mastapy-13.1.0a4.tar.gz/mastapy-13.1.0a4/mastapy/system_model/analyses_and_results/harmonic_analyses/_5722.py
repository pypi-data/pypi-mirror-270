"""BevelGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.system_deflections import _2729
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5717,
        _5839,
        _5846,
        _5849,
        _5868,
        _5739,
        _5781,
        _5800,
        _5741,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshHarmonicAnalysis")


class BevelGearMeshHarmonicAnalysis(_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis):
    """BevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshHarmonicAnalysis")

    class _Cast_BevelGearMeshHarmonicAnalysis:
        """Special nested class for casting BevelGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
            parent: "BevelGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            return self._parent._cast(_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5739.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(_5739.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5781.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5800.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(
                _5800.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5741.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(_5741.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5717.BevelDifferentialGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5839.SpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5846.StraightBevelDiffGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5849.StraightBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5849,
            )

            return self._parent._cast(_5849.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "_5868.ZerolBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5868,
            )

            return self._parent._cast(_5868.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
        ) -> "BevelGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshHarmonicAnalysis.TYPE"):
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
    ) -> "BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis":
        return self._Cast_BevelGearMeshHarmonicAnalysis(self)
