"""PartSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.math_utility import _1530
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2848,
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
    from mastapy.system_model.analyses_and_results.power_flows import _4137
    from mastapy.system_model.drawing import _2278
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartSystemDeflection",)


Self = TypeVar("Self", bound="PartSystemDeflection")


class PartSystemDeflection(_7573.PartFEAnalysis):
    """PartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartSystemDeflection")

    class _Cast_PartSystemDeflection:
        """Special nested class for casting PartSystemDeflection to subclasses."""

        def __init__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
            parent: "PartSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_fe_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2709.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2710.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2715.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2721.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2723.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2732.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2733.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2735.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2736.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2741.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2742.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2744.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2745.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2751.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2753.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2754.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2756.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2757.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2758.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2761.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2765.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2766.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2767.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2768.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2769.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2770.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2773.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2774.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(_2774.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2775.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(_2775.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2778.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2779.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2780.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2781.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2785.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2788.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2793.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(
                _2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2802.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2803.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2807.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2810.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2811.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2813.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2814.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2815.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2816.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2817.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2820.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2822.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2823.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2824.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2827.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2834.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2835.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2844.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2845.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2846.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2847.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2852.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2853.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2854.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2854,
            )

            return self._parent._cast(_2854.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2857.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2857,
            )

            return self._parent._cast(_2857.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2858.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2860.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2861.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "PartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingAxialForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2486.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_node_model(self: Self) -> "_1530.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection(self: Self) -> "_2848.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4137.PartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2278.SystemDeflectionViewable":
        """mastapy.system_model.drawing.SystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartSystemDeflection._Cast_PartSystemDeflection":
        return self._Cast_PartSystemDeflection(self)
