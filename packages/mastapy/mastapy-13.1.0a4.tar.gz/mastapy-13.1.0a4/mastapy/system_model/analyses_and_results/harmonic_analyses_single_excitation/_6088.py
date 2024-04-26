"""FaceGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6093,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "FaceGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6912
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6100,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="FaceGearMeshHarmonicAnalysisOfSingleExcitation")


class FaceGearMeshHarmonicAnalysisOfSingleExcitation(
    _6093.GearMeshHarmonicAnalysisOfSingleExcitation
):
    """FaceGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FaceGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6093.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
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
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "FaceGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6912.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshHarmonicAnalysisOfSingleExcitation._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FaceGearMeshHarmonicAnalysisOfSingleExcitation(self)
