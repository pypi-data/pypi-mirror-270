"""StraightBevelDiffGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5846
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5910,
        _5938,
        _5964,
        _5970,
        _5940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshCompoundHarmonicAnalysis")


class StraightBevelDiffGearMeshCompoundHarmonicAnalysis(
    _5922.BevelGearMeshCompoundHarmonicAnalysis
):
    """StraightBevelDiffGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
            parent: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5922.BevelGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5922.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5910.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(
                _5910.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5938.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5964.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5970.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(
                _5970.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_5940.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
        ) -> "StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2343.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5846.StraightBevelDiffGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5846.StraightBevelDiffGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysis(self)
