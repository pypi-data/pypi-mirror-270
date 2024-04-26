"""WormGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "WormGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5865
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5970,
        _5940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshCompoundHarmonicAnalysis")


class WormGearMeshCompoundHarmonicAnalysis(_5964.GearMeshCompoundHarmonicAnalysis):
    """WormGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshCompoundHarmonicAnalysis")

    class _Cast_WormGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting WormGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
            parent: "WormGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_5964.GearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5964.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_5970.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(
                _5970.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_5940.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "WormGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2347.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2347.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

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
    ) -> "List[_5865.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

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
    ) -> "List[_5865.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

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
    ) -> "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis":
        return self._Cast_WormGearMeshCompoundHarmonicAnalysis(self)
