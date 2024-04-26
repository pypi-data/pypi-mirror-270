"""ComponentModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4961,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ComponentModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4881,
        _4882,
        _4885,
        _4888,
        _4892,
        _4894,
        _4895,
        _4897,
        _4900,
        _4902,
        _4907,
        _4910,
        _4913,
        _4916,
        _4918,
        _4922,
        _4925,
        _4928,
        _4930,
        _4931,
        _4933,
        _4935,
        _4937,
        _4940,
        _4942,
        _4944,
        _4948,
        _4951,
        _4954,
        _4956,
        _4957,
        _4959,
        _4960,
        _4963,
        _4967,
        _4968,
        _4969,
        _4970,
        _4971,
        _4975,
        _4977,
        _4978,
        _4982,
        _4985,
        _4988,
        _4991,
        _4993,
        _4994,
        _4995,
        _4997,
        _4998,
        _5001,
        _5002,
        _5003,
        _5004,
        _5006,
        _5009,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ComponentModalAnalysisAtAStiffness")


class ComponentModalAnalysisAtAStiffness(_4961.PartModalAnalysisAtAStiffness):
    """ComponentModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentModalAnalysisAtAStiffness")

    class _Cast_ComponentModalAnalysisAtAStiffness:
        """Special nested class for casting ComponentModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
            parent: "ComponentModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4881.AbstractShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4882.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(
                _4882.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4885.AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(
                _4885.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4888.BearingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.BearingModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4892.BevelDifferentialGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(
                _4892.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(
                _4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4895.BevelDifferentialSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(
                _4895.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4897.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.BevelGearModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4900.BoltModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4902.ClutchHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4907.ConceptCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4907,
            )

            return self._parent._cast(
                _4907.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4910.ConceptGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.ConceptGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4913.ConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConicalGearModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4916.ConnectorModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4918.CouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4922.CVTPulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4925.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(_4925.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4928.CylindricalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(_4928.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4930.CylindricalPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(
                _4930.CylindricalPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def datum_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4931.DatumModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(_4931.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4933.ExternalCADModelModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4935.FaceGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.FaceGearModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4937.FEPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.FEPartModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4940.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.GearModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4942.GuideDxfModelModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4944.HypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.HypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(
                _4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(
                _4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4956.MassDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4957.MeasurementComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4960.OilSealModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.OilSealModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4963.PartToPartShearCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4967.PlanetCarrierModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(_4967.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4968.PointLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(_4968.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4969.PowerLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(_4969.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4970.PulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(_4970.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4971.RingPinsModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4975.RollingRingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(_4975.RollingRingModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4977.ShaftHubConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4978.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(_4978.ShaftModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4982.SpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4985.SpringDamperHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4988.StraightBevelDiffGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4988,
            )

            return self._parent._cast(
                _4988.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4991.StraightBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4991,
            )

            return self._parent._cast(_4991.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4993.StraightBevelPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4993,
            )

            return self._parent._cast(
                _4993.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4994.StraightBevelSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4994,
            )

            return self._parent._cast(
                _4994.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4995.SynchroniserHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4995,
            )

            return self._parent._cast(_4995.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4997.SynchroniserPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4997,
            )

            return self._parent._cast(_4997.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_4998.SynchroniserSleeveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4998,
            )

            return self._parent._cast(_4998.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5001.TorqueConverterPumpModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5001,
            )

            return self._parent._cast(
                _5001.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5002.TorqueConverterTurbineModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5002,
            )

            return self._parent._cast(
                _5002.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5003.UnbalancedMassModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5003,
            )

            return self._parent._cast(_5003.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5004.VirtualComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5004,
            )

            return self._parent._cast(_5004.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5006.WormGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5006,
            )

            return self._parent._cast(_5006.WormGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "_5009.ZerolBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5009,
            )

            return self._parent._cast(_5009.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
        ) -> "ComponentModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ComponentModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness":
        return self._Cast_ComponentModalAnalysisAtAStiffness(self)
