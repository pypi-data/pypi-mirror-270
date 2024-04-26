"""ComponentModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4596,
        _4597,
        _4600,
        _4603,
        _4607,
        _4609,
        _4610,
        _4612,
        _4615,
        _4617,
        _4622,
        _4625,
        _4628,
        _4631,
        _4634,
        _4638,
        _4641,
        _4644,
        _4646,
        _4647,
        _4651,
        _4653,
        _4655,
        _4659,
        _4661,
        _4663,
        _4667,
        _4670,
        _4673,
        _4675,
        _4676,
        _4681,
        _4683,
        _4687,
        _4691,
        _4692,
        _4693,
        _4694,
        _4695,
        _4699,
        _4701,
        _4702,
        _4707,
        _4710,
        _4713,
        _4716,
        _4718,
        _4719,
        _4720,
        _4722,
        _4723,
        _4726,
        _4727,
        _4728,
        _4729,
        _4734,
        _4737,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentModalAnalysis",)


Self = TypeVar("Self", bound="ComponentModalAnalysis")


class ComponentModalAnalysis(_4685.PartModalAnalysis):
    """ComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentModalAnalysis")

    class _Cast_ComponentModalAnalysis:
        """Special nested class for casting ComponentModalAnalysis to subclasses."""

        def __init__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
            parent: "ComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4596.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4597.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4600.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4603.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4607.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4612.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4615.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4617.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4622.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4625.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4631.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4634.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4638.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.CVTPulleyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4641.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4644.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4646.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4647.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(_4647.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4651.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4653.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FaceGearModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4655.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.FEPartModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4661.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4663.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(
                _4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(
                _4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4675.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4676.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4683.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4687.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4691.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4692.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4693.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4694.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4695.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4699.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4701.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4702.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.ShaftModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4707.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4710.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4713.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4716.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4718.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4719.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4720.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4722.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4723.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4726.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4727.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4728.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4728

            return self._parent._cast(_4728.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4729.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4729

            return self._parent._cast(_4729.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4734.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4734

            return self._parent._cast(_4734.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4737.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4737

            return self._parent._cast(_4737.ZerolBevelGearModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "ComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2738.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentModalAnalysis._Cast_ComponentModalAnalysis":
        return self._Cast_ComponentModalAnalysis(self)
