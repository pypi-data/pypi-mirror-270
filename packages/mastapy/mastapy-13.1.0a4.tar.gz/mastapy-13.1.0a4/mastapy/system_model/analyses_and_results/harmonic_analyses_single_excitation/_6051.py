"""BevelGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6039,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BevelGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6046,
        _6136,
        _6142,
        _6145,
        _6163,
        _6067,
        _6093,
        _6100,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BevelGearMeshHarmonicAnalysisOfSingleExcitation")


class BevelGearMeshHarmonicAnalysisOfSingleExcitation(
    _6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
):
    """BevelGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
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
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6145,
            )

            return self._parent._cast(
                _6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6163,
            )

            return self._parent._cast(
                _6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelGearMeshHarmonicAnalysisOfSingleExcitation(self)
