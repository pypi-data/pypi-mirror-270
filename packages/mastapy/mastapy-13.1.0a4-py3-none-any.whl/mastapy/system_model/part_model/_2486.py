"""Part"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")

if TYPE_CHECKING:
    from mastapy.math_utility import _1530
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model.part_model import (
        _2451,
        _2452,
        _2453,
        _2454,
        _2457,
        _2460,
        _2461,
        _2462,
        _2465,
        _2466,
        _2470,
        _2471,
        _2472,
        _2473,
        _2480,
        _2481,
        _2482,
        _2484,
        _2487,
        _2489,
        _2490,
        _2492,
        _2494,
        _2495,
        _2497,
    )
    from mastapy.system_model.import_export import _2260
    from mastapy.system_model.part_model.shaft_model import _2500
    from mastapy.system_model.part_model.gears import (
        _2531,
        _2532,
        _2533,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2550,
        _2552,
        _2553,
        _2554,
        _2555,
        _2556,
        _2557,
        _2558,
        _2559,
        _2560,
        _2561,
        _2562,
        _2563,
        _2564,
        _2565,
        _2566,
        _2567,
        _2568,
        _2569,
        _2570,
        _2571,
        _2572,
    )
    from mastapy.system_model.part_model.cycloidal import _2586, _2587, _2588
    from mastapy.system_model.part_model.couplings import (
        _2594,
        _2596,
        _2597,
        _2599,
        _2600,
        _2602,
        _2603,
        _2605,
        _2606,
        _2607,
        _2608,
        _2610,
        _2616,
        _2617,
        _2618,
        _2623,
        _2624,
        _2625,
        _2627,
        _2628,
        _2629,
        _2630,
        _2631,
        _2633,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Part",)


Self = TypeVar("Self", bound="Part")


class Part(_2221.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE = _PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Part")

    class _Cast_Part:
        """Special nested class for casting Part to subclasses."""

        def __init__(self: "Part._Cast_Part", parent: "Part"):
            self._parent = parent

        @property
        def design_entity(self: "Part._Cast_Part") -> "_2221.DesignEntity":
            return self._parent._cast(_2221.DesignEntity)

        @property
        def assembly(self: "Part._Cast_Part") -> "_2451.Assembly":
            return self._parent._cast(_2451.Assembly)

        @property
        def abstract_assembly(self: "Part._Cast_Part") -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def abstract_shaft(self: "Part._Cast_Part") -> "_2453.AbstractShaft":
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "Part._Cast_Part",
        ) -> "_2454.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractShaftOrHousing)

        @property
        def bearing(self: "Part._Cast_Part") -> "_2457.Bearing":
            from mastapy.system_model.part_model import _2457

            return self._parent._cast(_2457.Bearing)

        @property
        def bolt(self: "Part._Cast_Part") -> "_2460.Bolt":
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.Bolt)

        @property
        def bolted_joint(self: "Part._Cast_Part") -> "_2461.BoltedJoint":
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.BoltedJoint)

        @property
        def component(self: "Part._Cast_Part") -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def connector(self: "Part._Cast_Part") -> "_2465.Connector":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Connector)

        @property
        def datum(self: "Part._Cast_Part") -> "_2466.Datum":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Datum)

        @property
        def external_cad_model(self: "Part._Cast_Part") -> "_2470.ExternalCADModel":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.ExternalCADModel)

        @property
        def fe_part(self: "Part._Cast_Part") -> "_2471.FEPart":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.FEPart)

        @property
        def flexible_pin_assembly(
            self: "Part._Cast_Part",
        ) -> "_2472.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "Part._Cast_Part") -> "_2473.GuideDxfModel":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.GuideDxfModel)

        @property
        def mass_disc(self: "Part._Cast_Part") -> "_2480.MassDisc":
            from mastapy.system_model.part_model import _2480

            return self._parent._cast(_2480.MassDisc)

        @property
        def measurement_component(
            self: "Part._Cast_Part",
        ) -> "_2481.MeasurementComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.MeasurementComponent)

        @property
        def mountable_component(self: "Part._Cast_Part") -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def oil_seal(self: "Part._Cast_Part") -> "_2484.OilSeal":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.OilSeal)

        @property
        def planet_carrier(self: "Part._Cast_Part") -> "_2487.PlanetCarrier":
            from mastapy.system_model.part_model import _2487

            return self._parent._cast(_2487.PlanetCarrier)

        @property
        def point_load(self: "Part._Cast_Part") -> "_2489.PointLoad":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PointLoad)

        @property
        def power_load(self: "Part._Cast_Part") -> "_2490.PowerLoad":
            from mastapy.system_model.part_model import _2490

            return self._parent._cast(_2490.PowerLoad)

        @property
        def root_assembly(self: "Part._Cast_Part") -> "_2492.RootAssembly":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.RootAssembly)

        @property
        def specialised_assembly(
            self: "Part._Cast_Part",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "Part._Cast_Part") -> "_2495.UnbalancedMass":
            from mastapy.system_model.part_model import _2495

            return self._parent._cast(_2495.UnbalancedMass)

        @property
        def virtual_component(self: "Part._Cast_Part") -> "_2497.VirtualComponent":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.VirtualComponent)

        @property
        def shaft(self: "Part._Cast_Part") -> "_2500.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2500

            return self._parent._cast(_2500.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "Part._Cast_Part",
        ) -> "_2533.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2534.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2535.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2536.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Part._Cast_Part") -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def bevel_gear_set(self: "Part._Cast_Part") -> "_2538.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelGearSet)

        @property
        def concept_gear(self: "Part._Cast_Part") -> "_2539.ConceptGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.ConceptGear)

        @property
        def concept_gear_set(self: "Part._Cast_Part") -> "_2540.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.ConceptGearSet)

        @property
        def conical_gear(self: "Part._Cast_Part") -> "_2541.ConicalGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConicalGear)

        @property
        def conical_gear_set(self: "Part._Cast_Part") -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def cylindrical_gear(self: "Part._Cast_Part") -> "_2543.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "Part._Cast_Part") -> "_2544.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2545.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalPlanetGear)

        @property
        def face_gear(self: "Part._Cast_Part") -> "_2546.FaceGear":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.FaceGear)

        @property
        def face_gear_set(self: "Part._Cast_Part") -> "_2547.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.FaceGearSet)

        @property
        def gear(self: "Part._Cast_Part") -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def gear_set(self: "Part._Cast_Part") -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def hypoid_gear(self: "Part._Cast_Part") -> "_2552.HypoidGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.HypoidGear)

        @property
        def hypoid_gear_set(self: "Part._Cast_Part") -> "_2553.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2554.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "Part._Cast_Part",
        ) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Part._Cast_Part",
        ) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "Part._Cast_Part") -> "_2560.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "Part._Cast_Part") -> "_2561.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2562.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "Part._Cast_Part",
        ) -> "_2563.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2564.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "Part._Cast_Part") -> "_2565.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2566.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2567.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2568.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelSunGear)

        @property
        def worm_gear(self: "Part._Cast_Part") -> "_2569.WormGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.WormGear)

        @property
        def worm_gear_set(self: "Part._Cast_Part") -> "_2570.WormGearSet":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.WormGearSet)

        @property
        def zerol_bevel_gear(self: "Part._Cast_Part") -> "_2571.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "Part._Cast_Part") -> "_2572.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "Part._Cast_Part") -> "_2586.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2586

            return self._parent._cast(_2586.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "Part._Cast_Part") -> "_2587.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2587

            return self._parent._cast(_2587.CycloidalDisc)

        @property
        def ring_pins(self: "Part._Cast_Part") -> "_2588.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.RingPins)

        @property
        def belt_drive(self: "Part._Cast_Part") -> "_2594.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.BeltDrive)

        @property
        def clutch(self: "Part._Cast_Part") -> "_2596.Clutch":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.Clutch)

        @property
        def clutch_half(self: "Part._Cast_Part") -> "_2597.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.ClutchHalf)

        @property
        def concept_coupling(self: "Part._Cast_Part") -> "_2599.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2600.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.ConceptCouplingHalf)

        @property
        def coupling(self: "Part._Cast_Part") -> "_2602.Coupling":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.Coupling)

        @property
        def coupling_half(self: "Part._Cast_Part") -> "_2603.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.CouplingHalf)

        @property
        def cvt(self: "Part._Cast_Part") -> "_2605.CVT":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CVT)

        @property
        def cvt_pulley(self: "Part._Cast_Part") -> "_2606.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "Part._Cast_Part",
        ) -> "_2607.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2608.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Part._Cast_Part") -> "_2610.Pulley":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Pulley)

        @property
        def rolling_ring(self: "Part._Cast_Part") -> "_2616.RollingRing":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "Part._Cast_Part",
        ) -> "_2617.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2617

            return self._parent._cast(_2617.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "Part._Cast_Part") -> "_2618.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.ShaftHubConnection)

        @property
        def spring_damper(self: "Part._Cast_Part") -> "_2623.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2623

            return self._parent._cast(_2623.SpringDamper)

        @property
        def spring_damper_half(self: "Part._Cast_Part") -> "_2624.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2624

            return self._parent._cast(_2624.SpringDamperHalf)

        @property
        def synchroniser(self: "Part._Cast_Part") -> "_2625.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2625

            return self._parent._cast(_2625.Synchroniser)

        @property
        def synchroniser_half(self: "Part._Cast_Part") -> "_2627.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserHalf)

        @property
        def synchroniser_part(self: "Part._Cast_Part") -> "_2628.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "Part._Cast_Part") -> "_2629.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.SynchroniserSleeve)

        @property
        def torque_converter(self: "Part._Cast_Part") -> "_2630.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2630

            return self._parent._cast(_2630.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "Part._Cast_Part",
        ) -> "_2631.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "Part._Cast_Part",
        ) -> "_2633.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2633

            return self._parent._cast(_2633.TorqueConverterTurbine)

        @property
        def part(self: "Part._Cast_Part") -> "Part":
            return self._parent

        def __getattr__(self: "Part._Cast_Part", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Part.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_full_model(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingFullModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_isometric_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def drawing_number(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DrawingNumber

        if temp is None:
            return ""

        return temp

    @drawing_number.setter
    @enforce_parameter_types
    def drawing_number(self: Self, value: "str"):
        self.wrapped.DrawingNumber = str(value) if value is not None else ""

    @property
    def editable_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditableName

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: Self, value: "str"):
        self.wrapped.EditableName = str(value) if value is not None else ""

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def mass_properties_from_design(self: Self) -> "_1530.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_design_including_planetary_duplicates(
        self: Self,
    ) -> "_1530.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesignIncludingPlanetaryDuplicates

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connections(self: Self) -> "List[_2290.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def local_connections(self: Self) -> "List[_2290.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def connections_to(self: Self, part: "Part") -> "List[_2290.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Args:
            part (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ConnectionsTo(part.wrapped if part else None)
        )

    @enforce_parameter_types
    def copy_to(self: Self, container: "_2451.Assembly") -> "Part":
        """mastapy.system_model.part_model.Part

        Args:
            container (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.CopyTo(container.wrapped if container else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_geometry_export_options(self: Self) -> "_2260.GeometryExportOptions":
        """mastapy.system_model.import_export.GeometryExportOptions"""
        method_result = self.wrapped.CreateGeometryExportOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_connections(self: Self):
        """Method does not return."""
        self.wrapped.DeleteConnections()

    @property
    def cast_to(self: Self) -> "Part._Cast_Part":
        return self._Cast_Part(self)
