"""DesignEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2218
    from mastapy.utility.model_validation import _1807, _1806
    from mastapy.utility.scripting import _1754
    from mastapy.system_model.connections_and_sockets import (
        _2283,
        _2286,
        _2287,
        _2290,
        _2291,
        _2299,
        _2305,
        _2310,
        _2313,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2317,
        _2319,
        _2321,
        _2323,
        _2325,
        _2327,
        _2329,
        _2331,
        _2333,
        _2336,
        _2337,
        _2338,
        _2341,
        _2343,
        _2345,
        _2347,
        _2349,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2353,
        _2356,
        _2359,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2360,
        _2362,
        _2364,
        _2366,
        _2368,
        _2370,
    )
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
        _2486,
        _2487,
        _2489,
        _2490,
        _2492,
        _2494,
        _2495,
        _2497,
    )
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
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2283.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2286.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.BeltConnection)

        @property
        def coaxial_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2287.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity") -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def cvt_belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2291.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2299.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2305.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2305

            return self._parent._cast(_2305.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2310.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2310

            return self._parent._cast(_2310.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2313.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2313

            return self._parent._cast(_2313.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2317.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2319.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2321.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2323.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2325.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2327.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2329.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity") -> "_2331.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2333.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2336.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2341.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2343.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2345.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2347.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2349.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2353.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2353

            return self._parent._cast(_2353.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2356.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2356

            return self._parent._cast(_2356.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2359.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2359

            return self._parent._cast(_2359.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2360.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2362.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2364.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2366.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2368.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2370.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity") -> "_2451.Assembly":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Assembly)

        @property
        def abstract_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def abstract_shaft(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2453.AbstractShaft":
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2454.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity") -> "_2457.Bearing":
            from mastapy.system_model.part_model import _2457

            return self._parent._cast(_2457.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity") -> "_2460.Bolt":
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.Bolt)

        @property
        def bolted_joint(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2461.BoltedJoint":
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity") -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity") -> "_2465.Connector":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity") -> "_2466.Datum":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Datum)

        @property
        def external_cad_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2470.ExternalCADModel":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity") -> "_2471.FEPart":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.FEPart)

        @property
        def flexible_pin_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2472.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.FlexiblePinAssembly)

        @property
        def guide_dxf_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2473.GuideDxfModel":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity") -> "_2480.MassDisc":
            from mastapy.system_model.part_model import _2480

            return self._parent._cast(_2480.MassDisc)

        @property
        def measurement_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2481.MeasurementComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.MeasurementComponent)

        @property
        def mountable_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity") -> "_2484.OilSeal":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def planet_carrier(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2487.PlanetCarrier":
            from mastapy.system_model.part_model import _2487

            return self._parent._cast(_2487.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity") -> "_2489.PointLoad":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity") -> "_2490.PowerLoad":
            from mastapy.system_model.part_model import _2490

            return self._parent._cast(_2490.PowerLoad)

        @property
        def root_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2492.RootAssembly":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.RootAssembly)

        @property
        def specialised_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def unbalanced_mass(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2495.UnbalancedMass":
            from mastapy.system_model.part_model import _2495

            return self._parent._cast(_2495.UnbalancedMass)

        @property
        def virtual_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2497.VirtualComponent":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity") -> "_2500.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2500

            return self._parent._cast(_2500.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2533.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2534.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2535.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2536.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2538.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelGearSet)

        @property
        def concept_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2539.ConceptGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.ConceptGear)

        @property
        def concept_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2540.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.ConceptGearSet)

        @property
        def conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2541.ConicalGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConicalGear)

        @property
        def conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def cylindrical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2543.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.CylindricalGear)

        @property
        def cylindrical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2544.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2545.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2546.FaceGear":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.FaceGear)

        @property
        def face_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2547.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity") -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity") -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2552.HypoidGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.HypoidGear)

        @property
        def hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2553.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2554.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2560.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2561.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2562.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2563.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2564.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2565.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2566.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2567.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2568.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2569.WormGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.WormGear)

        @property
        def worm_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2570.WormGearSet":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.WormGearSet)

        @property
        def zerol_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2571.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2572.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2586.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2586

            return self._parent._cast(_2586.CycloidalAssembly)

        @property
        def cycloidal_disc(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2587.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2587

            return self._parent._cast(_2587.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity") -> "_2588.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity") -> "_2594.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity") -> "_2596.Clutch":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity") -> "_2597.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.ClutchHalf)

        @property
        def concept_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2599.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2600.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity") -> "_2602.Coupling":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.Coupling)

        @property
        def coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2603.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity") -> "_2605.CVT":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2606.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2607.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2608.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2610.Pulley":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Pulley)

        @property
        def rolling_ring(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2616.RollingRing":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2617.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2617

            return self._parent._cast(_2617.RollingRingAssembly)

        @property
        def shaft_hub_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2618.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.ShaftHubConnection)

        @property
        def spring_damper(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2623.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2623

            return self._parent._cast(_2623.SpringDamper)

        @property
        def spring_damper_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2624.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2624

            return self._parent._cast(_2624.SpringDamperHalf)

        @property
        def synchroniser(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2625.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2625

            return self._parent._cast(_2625.Synchroniser)

        @property
        def synchroniser_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2627.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2628.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2629.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.SynchroniserSleeve)

        @property
        def torque_converter(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2630.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2630

            return self._parent._cast(_2630.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2631.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2633.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2633

            return self._parent._cast(_2633.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

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
    def design_properties(self: Self) -> "_2218.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1807.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1806.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1754.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)
