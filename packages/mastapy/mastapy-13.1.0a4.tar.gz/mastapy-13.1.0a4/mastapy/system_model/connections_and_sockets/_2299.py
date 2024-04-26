"""InterMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2290
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2286, _2291, _2310
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
    from mastapy.system_model.connections_and_sockets.cycloidal import _2359
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2360,
        _2362,
        _2364,
        _2366,
        _2368,
        _2370,
    )
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


Self = TypeVar("Self", bound="InterMountableComponentConnection")


class InterMountableComponentConnection(_2290.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterMountableComponentConnection")

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            parent: "InterMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2290.Connection":
            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2286.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.BeltConnection)

        @property
        def cvt_belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2291.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.CVTBeltConnection)

        @property
        def rolling_ring_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2310.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2310

            return self._parent._cast(_2310.RollingRingConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2317.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2319.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2321.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2323.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2325.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2327.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2329.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.FaceGearMesh)

        @property
        def gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2331.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2333.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2336.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2341.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2343.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2345.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2347.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2349.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.ZerolBevelGearMesh)

        @property
        def ring_pins_to_disc_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2359.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2359

            return self._parent._cast(_2359.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2360.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2362.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2364.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2366.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2368.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2370.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.TorqueConverterConnection)

        @property
        def inter_mountable_component_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "InterMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnection._Cast_InterMountableComponentConnection":
        return self._Cast_InterMountableComponentConnection(self)
