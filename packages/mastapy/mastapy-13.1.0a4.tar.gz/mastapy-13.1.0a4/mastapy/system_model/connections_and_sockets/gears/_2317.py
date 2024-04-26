"""AGMAGleasonConicalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2325
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2319,
        _2321,
        _2333,
        _2341,
        _2343,
        _2345,
        _2349,
        _2331,
    )
    from mastapy.system_model.connections_and_sockets import _2299, _2290
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMesh",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMesh")


class AGMAGleasonConicalGearMesh(_2325.ConicalGearMesh):
    """AGMAGleasonConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMesh")

    class _Cast_AGMAGleasonConicalGearMesh:
        """Special nested class for casting AGMAGleasonConicalGearMesh to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            parent: "AGMAGleasonConicalGearMesh",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2325.ConicalGearMesh":
            return self._parent._cast(_2325.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2331.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2299.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2319.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2321.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2333.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.HypoidGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2341.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2343.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2345.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2349.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.ZerolBevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "AGMAGleasonConicalGearMesh":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh":
        return self._Cast_AGMAGleasonConicalGearMesh(self)
