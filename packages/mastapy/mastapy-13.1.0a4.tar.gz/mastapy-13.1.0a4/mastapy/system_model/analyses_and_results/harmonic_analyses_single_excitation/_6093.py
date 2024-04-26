"""GearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6100,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6039,
        _6046,
        _6051,
        _6064,
        _6067,
        _6082,
        _6088,
        _6098,
        _6102,
        _6105,
        _6108,
        _6136,
        _6142,
        _6145,
        _6160,
        _6163,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearMeshHarmonicAnalysisOfSingleExcitation")


class GearMeshHarmonicAnalysisOfSingleExcitation(
    _6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """GearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6145,
            )

            return self._parent._cast(
                _6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.WormGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6160,
            )

            return self._parent._cast(
                _6160.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6163,
            )

            return self._parent._cast(
                _6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearMeshHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2331.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearMeshHarmonicAnalysisOfSingleExcitation(self)
