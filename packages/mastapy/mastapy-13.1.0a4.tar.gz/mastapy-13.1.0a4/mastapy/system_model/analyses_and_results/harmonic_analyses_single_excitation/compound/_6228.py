"""HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6170,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6098,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6198,
        _6224,
        _6230,
        _6200,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation")


class HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation(
    _6170.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
):
    """HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6170.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6170.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6198.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6230.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6230,
            )

            return self._parent._cast(
                _6230.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HypoidGearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HypoidGearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation(self)
