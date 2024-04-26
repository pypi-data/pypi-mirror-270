"""MountableComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2462
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2453,
        _2463,
        _2457,
        _2465,
        _2480,
        _2481,
        _2484,
        _2487,
        _2489,
        _2490,
        _2495,
        _2497,
        _2486,
    )
    from mastapy.system_model.connections_and_sockets import _2290, _2294, _2287
    from mastapy.system_model.part_model.gears import (
        _2531,
        _2533,
        _2535,
        _2536,
        _2537,
        _2539,
        _2541,
        _2543,
        _2545,
        _2546,
        _2548,
        _2552,
        _2554,
        _2556,
        _2558,
        _2561,
        _2563,
        _2565,
        _2567,
        _2568,
        _2569,
        _2571,
    )
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.part_model.couplings import (
        _2597,
        _2600,
        _2603,
        _2606,
        _2608,
        _2610,
        _2616,
        _2618,
        _2624,
        _2627,
        _2628,
        _2629,
        _2631,
        _2633,
    )
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2462.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2462.Component":
            return self._parent._cast(_2462.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bearing(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2457.Bearing":
            from mastapy.system_model.part_model import _2457

            return self._parent._cast(_2457.Bearing)

        @property
        def connector(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2465.Connector":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Connector)

        @property
        def mass_disc(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2480.MassDisc":
            from mastapy.system_model.part_model import _2480

            return self._parent._cast(_2480.MassDisc)

        @property
        def measurement_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2481.MeasurementComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.MeasurementComponent)

        @property
        def oil_seal(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2484.OilSeal":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.OilSeal)

        @property
        def planet_carrier(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2487.PlanetCarrier":
            from mastapy.system_model.part_model import _2487

            return self._parent._cast(_2487.PlanetCarrier)

        @property
        def point_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2489.PointLoad":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PointLoad)

        @property
        def power_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2490.PowerLoad":
            from mastapy.system_model.part_model import _2490

            return self._parent._cast(_2490.PowerLoad)

        @property
        def unbalanced_mass(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2495.UnbalancedMass":
            from mastapy.system_model.part_model import _2495

            return self._parent._cast(_2495.UnbalancedMass)

        @property
        def virtual_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2497.VirtualComponent":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2533.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2535.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2536.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def concept_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2539.ConceptGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.ConceptGear)

        @property
        def conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2541.ConicalGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConicalGear)

        @property
        def cylindrical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2543.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2545.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalPlanetGear)

        @property
        def face_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2546.FaceGear":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent") -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2552.HypoidGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2554.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2561.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2563.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2565.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2567.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2568.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelSunGear)

        @property
        def worm_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2569.WormGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.WormGear)

        @property
        def zerol_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2571.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.ZerolBevelGear)

        @property
        def ring_pins(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2588.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.RingPins)

        @property
        def clutch_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2597.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2600.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.ConceptCouplingHalf)

        @property
        def coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2603.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.CouplingHalf)

        @property
        def cvt_pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2606.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2608.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.PartToPartShearCouplingHalf)

        @property
        def pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2610.Pulley":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Pulley)

        @property
        def rolling_ring(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2616.RollingRing":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.RollingRing)

        @property
        def shaft_hub_connection(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2618.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.ShaftHubConnection)

        @property
        def spring_damper_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2624.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2624

            return self._parent._cast(_2624.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2627.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2628.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2629.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2631.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2633.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2633

            return self._parent._cast(_2633.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2294.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2453.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2453.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2463.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)
