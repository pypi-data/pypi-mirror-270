"""InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6200,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6100,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6170,
        _6174,
        _6177,
        _6182,
        _6187,
        _6192,
        _6195,
        _6198,
        _6203,
        _6205,
        _6213,
        _6219,
        _6224,
        _6228,
        _6232,
        _6235,
        _6238,
        _6246,
        _6255,
        _6258,
        _6265,
        _6268,
        _6271,
        _6274,
        _6283,
        _6289,
        _6292,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6170.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6174.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6177.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6187.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6187,
            )

            return self._parent._cast(
                _6187.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6192.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6195.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6198.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6203.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6205.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6213.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6219.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6228.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6228,
            )

            return self._parent._cast(
                _6228.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6232.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6235.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6238.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6238,
            )

            return self._parent._cast(
                _6238.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6246.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6255.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6265.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6265,
            )

            return self._parent._cast(
                _6265.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6268.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6268,
            )

            return self._parent._cast(
                _6268.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6271.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6271,
            )

            return self._parent._cast(
                _6271.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6274.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6274,
            )

            return self._parent._cast(
                _6274.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6283.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6283,
            )

            return self._parent._cast(
                _6283.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6289.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6289,
            )

            return self._parent._cast(
                _6289.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6292.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6292,
            )

            return self._parent._cast(
                _6292.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
