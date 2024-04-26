"""PartModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "PartModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4677,
        _4595,
        _4596,
        _4597,
        _4600,
        _4601,
        _4602,
        _4603,
        _4605,
        _4607,
        _4608,
        _4609,
        _4610,
        _4612,
        _4613,
        _4614,
        _4615,
        _4617,
        _4618,
        _4620,
        _4622,
        _4623,
        _4625,
        _4626,
        _4628,
        _4629,
        _4631,
        _4634,
        _4635,
        _4637,
        _4638,
        _4639,
        _4641,
        _4644,
        _4645,
        _4646,
        _4647,
        _4651,
        _4653,
        _4654,
        _4655,
        _4656,
        _4659,
        _4660,
        _4661,
        _4663,
        _4664,
        _4667,
        _4668,
        _4670,
        _4671,
        _4673,
        _4674,
        _4675,
        _4676,
        _4681,
        _4683,
        _4687,
        _4688,
        _4690,
        _4691,
        _4692,
        _4693,
        _4694,
        _4695,
        _4697,
        _4699,
        _4700,
        _4701,
        _4702,
        _4705,
        _4707,
        _4708,
        _4710,
        _4711,
        _4713,
        _4714,
        _4716,
        _4717,
        _4718,
        _4719,
        _4720,
        _4721,
        _4722,
        _4723,
        _4725,
        _4726,
        _4727,
        _4728,
        _4729,
        _4734,
        _4735,
        _4737,
        _4738,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4749,
        _4747,
        _4750,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.drawing import _2269
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartModalAnalysis",)


Self = TypeVar("Self", bound="PartModalAnalysis")


class PartModalAnalysis(_7574.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartModalAnalysis")

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
            parent: "PartModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4596.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4597.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4600.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4602.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4603.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4605.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4607.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4608.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4612.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4613.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4614.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4615.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4617.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4618.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4622.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4623.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4625.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4626.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4631.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4634.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4635.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4637.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4638.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4639.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4641.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4644.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4645.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4646.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4647.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(_4647.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4651.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4653.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4654.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4655.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4656.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4661.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4663.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4664.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(
                _4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(
                _4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(
                _4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4675.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4676.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4683.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4687.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4688.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4690.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4691.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4692.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4693.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4694.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4695.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4697.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4699.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4700.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4701.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4702.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4707.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4708.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4710.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4711.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4713.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4714.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4716.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4717.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4718.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4719.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4720.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4721.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4721

            return self._parent._cast(_4721.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4722.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4723.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4725.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4726.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4727.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4728.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4728

            return self._parent._cast(_4728.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4729.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4729

            return self._parent._cast(_4729.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4734.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4734

            return self._parent._cast(_4734.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4735.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4737.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4737

            return self._parent._cast(_4737.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4738.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4738

            return self._parent._cast(_4738.ZerolBevelGearSetModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "PartModalAnalysis":
            return self._parent

        def __getattr__(self: "PartModalAnalysis._Cast_PartModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def modal_analysis(self: Self) -> "_4677.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: Self,
    ) -> "List[_4749.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_excitation_details(
        self: Self,
    ) -> "List[_4747.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_modes(self: Self) -> "List[_4750.SingleModeResults]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleModeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_excitation_details(
        self: Self,
    ) -> "List[_4747.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2808.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2269.ModalAnalysisViewable":
        """mastapy.system_model.drawing.ModalAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartModalAnalysis._Cast_PartModalAnalysis":
        return self._Cast_PartModalAnalysis(self)
