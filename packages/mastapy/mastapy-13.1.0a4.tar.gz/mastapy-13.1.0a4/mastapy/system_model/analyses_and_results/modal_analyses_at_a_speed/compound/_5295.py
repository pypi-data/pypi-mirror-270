"""ComponentCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5349,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ComponentCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5165,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5271,
        _5272,
        _5274,
        _5278,
        _5281,
        _5284,
        _5285,
        _5286,
        _5289,
        _5293,
        _5298,
        _5299,
        _5302,
        _5306,
        _5309,
        _5312,
        _5315,
        _5317,
        _5320,
        _5321,
        _5322,
        _5323,
        _5326,
        _5328,
        _5331,
        _5332,
        _5336,
        _5339,
        _5342,
        _5345,
        _5346,
        _5347,
        _5348,
        _5352,
        _5355,
        _5356,
        _5357,
        _5358,
        _5359,
        _5362,
        _5365,
        _5366,
        _5369,
        _5374,
        _5375,
        _5378,
        _5381,
        _5382,
        _5384,
        _5385,
        _5386,
        _5389,
        _5390,
        _5391,
        _5392,
        _5393,
        _5396,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ComponentCompoundModalAnalysisAtASpeed")


class ComponentCompoundModalAnalysisAtASpeed(_5349.PartCompoundModalAnalysisAtASpeed):
    """ComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
            parent: "ComponentCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5271.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(
                _5272.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5274.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5278.BearingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.BearingCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5281.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5284.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(
                _5284.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5285.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(
                _5285.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5286.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5289.BoltCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5289,
            )

            return self._parent._cast(_5289.BoltCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5298.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5299.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(_5299.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5302.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5306.ConnectorCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5309.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5312.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(_5312.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5315.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5317.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5320.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5321.DatumCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(_5321.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5322.ExternalCADModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(
                _5322.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5323.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5326.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5331.GuideDxfModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5332.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5336.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(
                _5336.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5339.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5342.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(_5345.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5346.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5347.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5348.OilSealCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(_5348.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5352.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5355.PlanetCarrierCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(_5355.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5356.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5357.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(_5357.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5358.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(_5358.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5359.RingPinsCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(_5359.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5362.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(_5362.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5365.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(_5365.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5366.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5374.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5375.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5378.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(
                _5378.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5381.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(
                _5381.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5382.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5384.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5384,
            )

            return self._parent._cast(
                _5384.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5385.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5385,
            )

            return self._parent._cast(
                _5385.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5386.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5386,
            )

            return self._parent._cast(
                _5386.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5389.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5389,
            )

            return self._parent._cast(
                _5389.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5390.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5390,
            )

            return self._parent._cast(
                _5390.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5391.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5391,
            )

            return self._parent._cast(_5391.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5392.VirtualComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5392,
            )

            return self._parent._cast(
                _5392.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5393.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5393,
            )

            return self._parent._cast(_5393.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5396.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5396,
            )

            return self._parent._cast(_5396.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "ComponentCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ComponentCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5165.ComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ComponentModalAnalysisAtASpeed]

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
    ) -> "List[_5165.ComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ComponentModalAnalysisAtASpeed]

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
    ) -> "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed":
        return self._Cast_ComponentCompoundModalAnalysisAtASpeed(self)
