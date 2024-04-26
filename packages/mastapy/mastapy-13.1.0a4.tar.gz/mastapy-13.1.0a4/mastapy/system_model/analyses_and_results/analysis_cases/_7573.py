"""PartFEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartFEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2708,
        _2709,
        _2710,
        _2713,
        _2714,
        _2715,
        _2721,
        _2723,
        _2725,
        _2726,
        _2727,
        _2728,
        _2730,
        _2731,
        _2732,
        _2733,
        _2735,
        _2736,
        _2738,
        _2741,
        _2742,
        _2744,
        _2745,
        _2748,
        _2749,
        _2751,
        _2753,
        _2754,
        _2756,
        _2757,
        _2758,
        _2761,
        _2765,
        _2766,
        _2767,
        _2768,
        _2769,
        _2770,
        _2773,
        _2774,
        _2775,
        _2778,
        _2779,
        _2780,
        _2781,
        _2783,
        _2784,
        _2785,
        _2787,
        _2788,
        _2792,
        _2793,
        _2795,
        _2796,
        _2798,
        _2799,
        _2802,
        _2803,
        _2805,
        _2807,
        _2808,
        _2810,
        _2811,
        _2813,
        _2814,
        _2815,
        _2816,
        _2817,
        _2820,
        _2822,
        _2823,
        _2824,
        _2827,
        _2829,
        _2831,
        _2832,
        _2834,
        _2835,
        _2837,
        _2838,
        _2840,
        _2841,
        _2842,
        _2843,
        _2844,
        _2845,
        _2846,
        _2847,
        _2852,
        _2853,
        _2854,
        _2857,
        _2858,
        _2860,
        _2861,
        _2863,
        _2864,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6303,
        _6304,
        _6305,
        _6307,
        _6309,
        _6310,
        _6311,
        _6313,
        _6314,
        _6316,
        _6317,
        _6318,
        _6319,
        _6321,
        _6322,
        _6323,
        _6325,
        _6326,
        _6328,
        _6330,
        _6331,
        _6332,
        _6334,
        _6335,
        _6337,
        _6339,
        _6341,
        _6342,
        _6344,
        _6345,
        _6346,
        _6348,
        _6350,
        _6352,
        _6353,
        _6354,
        _6357,
        _6358,
        _6360,
        _6361,
        _6362,
        _6363,
        _6365,
        _6366,
        _6367,
        _6369,
        _6371,
        _6373,
        _6374,
        _6376,
        _6377,
        _6379,
        _6380,
        _6381,
        _6382,
        _6383,
        _6384,
        _6386,
        _6387,
        _6389,
        _6390,
        _6391,
        _6392,
        _6393,
        _6394,
        _6396,
        _6398,
        _6399,
        _6400,
        _6401,
        _6403,
        _6404,
        _6406,
        _6408,
        _6409,
        _6410,
        _6412,
        _6413,
        _6415,
        _6416,
        _6417,
        _6418,
        _6419,
        _6420,
        _6421,
        _6423,
        _6424,
        _6425,
        _6426,
        _6427,
        _6428,
        _6430,
        _6431,
        _6433,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartFEAnalysis",)


Self = TypeVar("Self", bound="PartFEAnalysis")


class PartFEAnalysis(_7574.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartFEAnalysis")

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(
            self: "PartFEAnalysis._Cast_PartFEAnalysis", parent: "PartFEAnalysis"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2709.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2710.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2715.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2721.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2723.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2732.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2733.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2735.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2736.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2741.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2742.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2744.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2745.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2751.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2753.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2754.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2756.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2757.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2758.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2761.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2765.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2766.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2767.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2768.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2769.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2770.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2773.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2774.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(_2774.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2775.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(_2775.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2778.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2779.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2780.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2781.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2785.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2788.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2793.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(
                _2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2802.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2803.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2807.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2810.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2811.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2813.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2814.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2815.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2816.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2817.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2820.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2822.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2823.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2824.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2827.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2834.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2835.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2844.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2845.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2846.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2847.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2852.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2853.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2854.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2854,
            )

            return self._parent._cast(_2854.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2857.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2857,
            )

            return self._parent._cast(_2857.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2858.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2860.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2861.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6304.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6305.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6307.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6309.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6310.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6311.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6313.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6314.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6316.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6317.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6318.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6321.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6322.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6323.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6325.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6326.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6330.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6331.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6332.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6334.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6339.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6341.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6342.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6344.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6345.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6346.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(_6346.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6348.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6350.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6352.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6353.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6354.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6357.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6358.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6360.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6361.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6362.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6365.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6366.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6367.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6369.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(
                _6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(
                _6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(
                _6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(
                _6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6380.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6381.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6383.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6386.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6387.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6389.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6390.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6391.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6392.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6393.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6394.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6396.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6398.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6399.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6400.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6401.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6404.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6406.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6408.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6409.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6410.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6412.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6413.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6415.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6416.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6417.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6417

            return self._parent._cast(_6417.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6418.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6418

            return self._parent._cast(_6418.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6419.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6420.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6420

            return self._parent._cast(_6420.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6421.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6423.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6423

            return self._parent._cast(_6423.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6424.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6424

            return self._parent._cast(_6424.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6425.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6425

            return self._parent._cast(_6425.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6426.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426

            return self._parent._cast(_6426.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6427.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6427

            return self._parent._cast(_6427.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6428.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6428

            return self._parent._cast(_6428.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6430.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6430

            return self._parent._cast(_6430.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6431.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6431

            return self._parent._cast(_6431.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6433.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6433

            return self._parent._cast(_6433.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "PartFEAnalysis":
            return self._parent

        def __getattr__(self: "PartFEAnalysis._Cast_PartFEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PartFEAnalysis._Cast_PartFEAnalysis":
        return self._Cast_PartFEAnalysis(self)
