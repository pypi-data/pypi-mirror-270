"""MountableComponentModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5165
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5145,
        _5148,
        _5152,
        _5154,
        _5155,
        _5157,
        _5162,
        _5167,
        _5170,
        _5173,
        _5176,
        _5178,
        _5182,
        _5188,
        _5190,
        _5194,
        _5199,
        _5203,
        _5207,
        _5210,
        _5213,
        _5215,
        _5216,
        _5219,
        _5222,
        _5226,
        _5227,
        _5228,
        _5229,
        _5230,
        _5234,
        _5236,
        _5241,
        _5244,
        _5247,
        _5250,
        _5252,
        _5253,
        _5254,
        _5256,
        _5257,
        _5260,
        _5261,
        _5262,
        _5263,
        _5265,
        _5268,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="MountableComponentModalAnalysisAtASpeed")


class MountableComponentModalAnalysisAtASpeed(_5165.ComponentModalAnalysisAtASpeed):
    """MountableComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentModalAnalysisAtASpeed"
    )

    class _Cast_MountableComponentModalAnalysisAtASpeed:
        """Special nested class for casting MountableComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
            parent: "MountableComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5148.BearingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.BearingModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5152.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(
                _5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5155.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(
                _5155.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5157.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.BevelGearModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5162.ClutchHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.ClutchHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5167.ConceptCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5170.ConceptGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5173.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConicalGearModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5176.ConnectorModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5178.CouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.CouplingHalfModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5182.CVTPulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(_5182.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5188.CylindricalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5190.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5194.FaceGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.FaceGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5203.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(
                _5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(
                _5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(
                _5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5215.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5216.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5219.OilSealModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.OilSealModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5222.PartToPartShearCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(
                _5222.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5226.PlanetCarrierModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5227.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5228.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5229.PulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5230.RingPinsModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5234.RollingRingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.RollingRingModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5236.ShaftHubConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5241.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5244.SpringDamperHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5247.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5250.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(_5250.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5252.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(
                _5252.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5253.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5254.SynchroniserHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5254,
            )

            return self._parent._cast(_5254.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5256.SynchroniserPartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5256,
            )

            return self._parent._cast(_5256.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5257.SynchroniserSleeveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5257,
            )

            return self._parent._cast(_5257.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5260.TorqueConverterPumpModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5260,
            )

            return self._parent._cast(_5260.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5261.TorqueConverterTurbineModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5261,
            )

            return self._parent._cast(_5261.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5262.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5262,
            )

            return self._parent._cast(_5262.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5263.VirtualComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5263,
            )

            return self._parent._cast(_5263.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5265.WormGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5265,
            )

            return self._parent._cast(_5265.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "_5268.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5268,
            )

            return self._parent._cast(_5268.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "MountableComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "MountableComponentModalAnalysisAtASpeed.TYPE"
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
    ) -> "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed":
        return self._Cast_MountableComponentModalAnalysisAtASpeed(self)
