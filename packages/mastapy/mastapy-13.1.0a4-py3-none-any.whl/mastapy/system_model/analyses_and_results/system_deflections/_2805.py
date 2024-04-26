"""MountableComponentSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "MountableComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2780,
        _2714,
        _2721,
        _2726,
        _2727,
        _2728,
        _2731,
        _2735,
        _2741,
        _2745,
        _2749,
        _2751,
        _2753,
        _2756,
        _2768,
        _2769,
        _2770,
        _2773,
        _2779,
        _2784,
        _2788,
        _2793,
        _2796,
        _2799,
        _2802,
        _2803,
        _2807,
        _2810,
        _2813,
        _2814,
        _2815,
        _2816,
        _2817,
        _2822,
        _2824,
        _2832,
        _2834,
        _2838,
        _2841,
        _2842,
        _2843,
        _2844,
        _2845,
        _2846,
        _2852,
        _2854,
        _2857,
        _2858,
        _2861,
        _2864,
        _2808,
    )
    from mastapy.system_model.fe import _2403
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentSystemDeflection")


class MountableComponentSystemDeflection(_2738.ComponentSystemDeflection):
    """MountableComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentSystemDeflection")

    class _Cast_MountableComponentSystemDeflection:
        """Special nested class for casting MountableComponentSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
            parent: "MountableComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2721.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2735.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2741.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2745.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2751.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2753.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2756.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CVTPulleySystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2768.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2769.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2770.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2773.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2779.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FaceGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2788.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2793.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(
                _2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2802.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2803.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MeasurementComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2807.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2810.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2813.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2814.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2815.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2816.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2817.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2822.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2824.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.ShaftHubConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2834.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2844.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2845.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2846.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2852.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2854.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2854,
            )

            return self._parent._cast(_2854.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2857.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2857,
            )

            return self._parent._cast(_2857.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2858.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2861.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "MountableComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DipFactor

        if temp is None:
            return 0.0

        return temp

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
    def inner_fe_part(self: Self) -> "_2780.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_substructure_nodes(self: Self) -> "List[_2403.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4135.MountableComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection":
        return self._Cast_MountableComponentSystemDeflection(self)
