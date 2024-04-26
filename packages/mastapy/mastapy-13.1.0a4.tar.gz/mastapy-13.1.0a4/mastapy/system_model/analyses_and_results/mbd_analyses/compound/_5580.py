"""ComponentCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ComponentCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5556,
        _5557,
        _5559,
        _5563,
        _5566,
        _5569,
        _5570,
        _5571,
        _5574,
        _5578,
        _5583,
        _5584,
        _5587,
        _5591,
        _5594,
        _5597,
        _5600,
        _5602,
        _5605,
        _5606,
        _5607,
        _5608,
        _5611,
        _5613,
        _5616,
        _5617,
        _5621,
        _5624,
        _5627,
        _5630,
        _5631,
        _5632,
        _5633,
        _5637,
        _5640,
        _5641,
        _5642,
        _5643,
        _5644,
        _5647,
        _5650,
        _5651,
        _5654,
        _5659,
        _5660,
        _5663,
        _5666,
        _5667,
        _5669,
        _5670,
        _5671,
        _5674,
        _5675,
        _5676,
        _5677,
        _5678,
        _5681,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundMultibodyDynamicsAnalysis")


class ComponentCompoundMultibodyDynamicsAnalysis(
    _5634.PartCompoundMultibodyDynamicsAnalysis
):
    """ComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
            parent: "ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.AbstractShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.BearingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(_5563.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(
                _5566.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5569.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5571.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5574.BoltCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(_5574.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5578.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(_5578.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5587.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(
                _5587.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.ConnectorCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5594.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5597.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(_5597.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5600.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.DatumCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(_5606.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5611.FEPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(_5611.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(_5613.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(
                _5616.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5621.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5624.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.MassDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(_5630.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5631.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5633.OilSealCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(_5633.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5637.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5640.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.PointLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(_5641.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.PowerLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(_5642.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(_5643.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.RingPinsCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(_5644.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5647.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.ShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(_5650.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5654.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5660.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5660,
            )

            return self._parent._cast(
                _5660.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5663.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5663,
            )

            return self._parent._cast(
                _5663.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5666.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5666,
            )

            return self._parent._cast(
                _5666.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5667.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5667,
            )

            return self._parent._cast(
                _5667.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5669.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5669,
            )

            return self._parent._cast(
                _5669.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5670.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5670,
            )

            return self._parent._cast(
                _5670.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5671.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5671,
            )

            return self._parent._cast(
                _5671.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5674.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5674,
            )

            return self._parent._cast(
                _5674.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5675.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5675,
            )

            return self._parent._cast(
                _5675.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5676.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5676,
            )

            return self._parent._cast(
                _5676.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5677.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5677,
            )

            return self._parent._cast(
                _5677.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5678.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5678,
            )

            return self._parent._cast(_5678.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5681.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5681,
            )

            return self._parent._cast(
                _5681.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5428.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    ) -> "List[_5428.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    ) -> "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ComponentCompoundMultibodyDynamicsAnalysis(self)
