"""PartCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PartCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5814
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5905,
        _5906,
        _5907,
        _5909,
        _5911,
        _5912,
        _5913,
        _5915,
        _5916,
        _5918,
        _5919,
        _5920,
        _5921,
        _5923,
        _5924,
        _5925,
        _5926,
        _5928,
        _5930,
        _5931,
        _5933,
        _5934,
        _5936,
        _5937,
        _5939,
        _5941,
        _5942,
        _5944,
        _5946,
        _5947,
        _5948,
        _5950,
        _5952,
        _5954,
        _5955,
        _5956,
        _5957,
        _5958,
        _5960,
        _5961,
        _5962,
        _5963,
        _5965,
        _5966,
        _5967,
        _5969,
        _5971,
        _5973,
        _5974,
        _5976,
        _5977,
        _5979,
        _5980,
        _5981,
        _5982,
        _5983,
        _5985,
        _5987,
        _5989,
        _5990,
        _5991,
        _5992,
        _5993,
        _5994,
        _5996,
        _5997,
        _5999,
        _6000,
        _6001,
        _6003,
        _6004,
        _6006,
        _6007,
        _6009,
        _6010,
        _6012,
        _6013,
        _6015,
        _6016,
        _6017,
        _6018,
        _6019,
        _6020,
        _6021,
        _6022,
        _6024,
        _6025,
        _6026,
        _6027,
        _6028,
        _6030,
        _6031,
        _6033,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartCompoundHarmonicAnalysis")


class PartCompoundHarmonicAnalysis(_7572.PartCompoundAnalysis):
    """PartCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundHarmonicAnalysis")

    class _Cast_PartCompoundHarmonicAnalysis:
        """Special nested class for casting PartCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
            parent: "PartCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5905.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5906.AbstractShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5907.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(
                _5907.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(
                _5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(
                _5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5912.AssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5913.BearingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5915.BeltDriveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5916.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(
                _5916.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5918.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(
                _5918.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5919.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(
                _5919.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5920.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(
                _5920.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5921.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5923.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5924.BoltCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5925.BoltedJointCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5926.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5928.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5931.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5933.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5934.ConceptGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5936.ConceptGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5937.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5939.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5941.ConnectorCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5942.CouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5944.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(_5944.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5946.CVTCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(_5946.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5947.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5948.CycloidalAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(_5948.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5950.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(_5950.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5952.CylindricalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(_5952.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5954.CylindricalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5955.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5956.DatumCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5957.ExternalCADModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5958.FaceGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5960.FaceGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5961.FEPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(_5961.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5962.FlexiblePinAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5963.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5965.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5966.GuideDxfModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5967.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5969.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(_5969.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5971.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(
                _5971.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5973.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(
                _5973.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5974.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(
                _5974.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5976.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(
                _5976.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5977.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(
                _5977.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(
                _5979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5980.MassDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5981.MeasurementComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5983.OilSealCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5985.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5987.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(
                _5987.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5989.PlanetaryGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5990.PlanetCarrierCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(_5990.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5991.PointLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5992.PowerLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5993.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(_5993.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5994.RingPinsCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(_5994.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5996.RollingRingAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(_5996.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5997.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_5999.RootAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(_5999.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6000.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6001.ShaftHubConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6003.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6004.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6006.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6007.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(_6007.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6009.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(_6009.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6010.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6010,
            )

            return self._parent._cast(
                _6010.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6012.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6012,
            )

            return self._parent._cast(
                _6012.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6013.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6013,
            )

            return self._parent._cast(_6013.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6015.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6015,
            )

            return self._parent._cast(
                _6015.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6016.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6016,
            )

            return self._parent._cast(
                _6016.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6017.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6017,
            )

            return self._parent._cast(
                _6017.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6018.SynchroniserCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6018,
            )

            return self._parent._cast(_6018.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6019.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6019,
            )

            return self._parent._cast(_6019.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6020.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6020,
            )

            return self._parent._cast(_6020.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6021.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6021,
            )

            return self._parent._cast(_6021.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6022.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6022,
            )

            return self._parent._cast(_6022.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6024.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6024,
            )

            return self._parent._cast(_6024.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6025.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6025,
            )

            return self._parent._cast(
                _6025.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6026.UnbalancedMassCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6026,
            )

            return self._parent._cast(_6026.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6027.VirtualComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6027,
            )

            return self._parent._cast(_6027.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6028.WormGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6028,
            )

            return self._parent._cast(_6028.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6030.WormGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6030,
            )

            return self._parent._cast(_6030.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6031.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6031,
            )

            return self._parent._cast(_6031.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "_6033.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6033,
            )

            return self._parent._cast(_6033.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "PartCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5814.PartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5814.PartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis":
        return self._Cast_PartCompoundHarmonicAnalysis(self)
