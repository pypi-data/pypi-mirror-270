"""ConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6096,
        _6037,
        _6039,
        _6043,
        _6046,
        _6051,
        _6055,
        _6058,
        _6060,
        _6064,
        _6067,
        _6071,
        _6074,
        _6078,
        _6080,
        _6082,
        _6088,
        _6093,
        _6098,
        _6100,
        _6102,
        _6105,
        _6108,
        _6116,
        _6119,
        _6126,
        _6128,
        _6133,
        _6136,
        _6138,
        _6142,
        _6145,
        _6153,
        _6160,
        _6163,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConnectionHarmonicAnalysisOfSingleExcitation")


class ConnectionHarmonicAnalysisOfSingleExcitation(
    _7567.ConnectionStaticLoadAnalysisCase
):
    """ConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "ConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.BeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.ClutchConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6060.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
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
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6116.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.RollingRingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6145,
            )

            return self._parent._cast(
                _6145.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6153.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6153,
            )

            return self._parent._cast(
                _6153.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.WormGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6160,
            )

            return self._parent._cast(
                _6160.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6163,
            )

            return self._parent._cast(
                _6163.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "ConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "_6096.HarmonicAnalysisOfSingleExcitation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConnectionHarmonicAnalysisOfSingleExcitation(self)
