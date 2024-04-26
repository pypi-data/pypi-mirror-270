"""MountableComponentHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6059,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "MountableComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6038,
        _6042,
        _6045,
        _6048,
        _6049,
        _6050,
        _6056,
        _6061,
        _6063,
        _6066,
        _6070,
        _6072,
        _6076,
        _6081,
        _6084,
        _6087,
        _6092,
        _6097,
        _6101,
        _6104,
        _6107,
        _6110,
        _6111,
        _6114,
        _6117,
        _6121,
        _6122,
        _6123,
        _6124,
        _6125,
        _6129,
        _6132,
        _6135,
        _6139,
        _6141,
        _6144,
        _6147,
        _6148,
        _6149,
        _6151,
        _6152,
        _6155,
        _6156,
        _6157,
        _6158,
        _6159,
        _6162,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysisOfSingleExcitation")


class MountableComponentHarmonicAnalysisOfSingleExcitation(
    _6059.ComponentHarmonicAnalysisOfSingleExcitation
):
    """MountableComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_MountableComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MountableComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
            parent: "MountableComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(_6042.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6056.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6063.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6072.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6081.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6084.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(_6087.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6101.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6107.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6111.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6114.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(_6114.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6121.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(_6122.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6123.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(_6123.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(_6124.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(_6125.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6129.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6141,
            )

            return self._parent._cast(
                _6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6148,
            )

            return self._parent._cast(
                _6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6149,
            )

            return self._parent._cast(
                _6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6151,
            )

            return self._parent._cast(
                _6151.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6155.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6155,
            )

            return self._parent._cast(
                _6155.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6156.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6156,
            )

            return self._parent._cast(
                _6156.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6157,
            )

            return self._parent._cast(
                _6157.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6158.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6158,
            )

            return self._parent._cast(
                _6158.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6159.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6159,
            )

            return self._parent._cast(_6159.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6162,
            )

            return self._parent._cast(
                _6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "MountableComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation(self)
