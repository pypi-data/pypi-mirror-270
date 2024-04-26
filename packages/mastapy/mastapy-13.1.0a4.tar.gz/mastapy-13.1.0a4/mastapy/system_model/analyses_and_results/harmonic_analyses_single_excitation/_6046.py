"""BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6051,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6850
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6039,
        _6067,
        _6093,
        _6100,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation"
)


class BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation(
    _6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation
):
    """BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6850.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation(
            self
        )
