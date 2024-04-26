"""ConicalGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.system_deflections import _2747
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5710,
        _5717,
        _5722,
        _5798,
        _5802,
        _5805,
        _5808,
        _5839,
        _5846,
        _5849,
        _5868,
        _5800,
        _5741,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshHarmonicAnalysis")


class ConicalGearMeshHarmonicAnalysis(_5781.GearMeshHarmonicAnalysis):
    """ConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshHarmonicAnalysis")

    class _Cast_ConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            parent: "ConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5781.GearMeshHarmonicAnalysis":
            return self._parent._cast(_5781.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5800.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(
                _5800.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5741.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(_5741.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5717.BevelDifferentialGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5722.BevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5798.HypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5802.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(
                _5802.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5805.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(
                _5805.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5808.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(
                _5808.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5839.SpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5846.StraightBevelDiffGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5849.StraightBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5849,
            )

            return self._parent._cast(_5849.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5868.ZerolBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5868,
            )

            return self._parent._cast(_5868.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "ConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2747.ConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection

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
    ) -> "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis":
        return self._Cast_ConicalGearMeshHarmonicAnalysis(self)
