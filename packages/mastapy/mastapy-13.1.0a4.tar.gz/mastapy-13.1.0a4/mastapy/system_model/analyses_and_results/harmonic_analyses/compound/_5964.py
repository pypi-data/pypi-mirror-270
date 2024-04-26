"""GearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5970
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "GearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5910,
        _5917,
        _5922,
        _5935,
        _5938,
        _5953,
        _5959,
        _5968,
        _5972,
        _5975,
        _5978,
        _6005,
        _6011,
        _6014,
        _6029,
        _6032,
        _5940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundHarmonicAnalysis")


class GearMeshCompoundHarmonicAnalysis(
    _5970.InterMountableComponentConnectionCompoundHarmonicAnalysis
):
    """GearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundHarmonicAnalysis")

    class _Cast_GearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting GearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
            parent: "GearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5970.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5970.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5940.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5910.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(
                _5910.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5917.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(
                _5917.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5922.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5935.ConceptGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5938.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5953.CylindricalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5959.FaceGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5968.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5972.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(
                _5972.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_5975.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(
                _5975.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> (
            "_5978.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(
                _5978.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_6005.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(_6005.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_6011.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6011,
            )

            return self._parent._cast(
                _6011.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_6014.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6014,
            )

            return self._parent._cast(
                _6014.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_6029.WormGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6029,
            )

            return self._parent._cast(_6029.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "_6032.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6032,
            )

            return self._parent._cast(_6032.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "GearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_5781.GearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5781.GearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis":
        return self._Cast_GearMeshCompoundHarmonicAnalysis(self)
