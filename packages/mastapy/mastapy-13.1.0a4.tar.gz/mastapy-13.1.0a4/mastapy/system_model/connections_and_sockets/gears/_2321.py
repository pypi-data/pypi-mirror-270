"""BevelGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1191
    from mastapy.system_model.connections_and_sockets.gears import (
        _2319,
        _2341,
        _2343,
        _2345,
        _2349,
        _2325,
        _2331,
    )
    from mastapy.system_model.connections_and_sockets import _2299, _2290
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMesh",)


Self = TypeVar("Self", bound="BevelGearMesh")


class BevelGearMesh(_2317.AGMAGleasonConicalGearMesh):
    """BevelGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMesh")

    class _Cast_BevelGearMesh:
        """Special nested class for casting BevelGearMesh to subclasses."""

        def __init__(
            self: "BevelGearMesh._Cast_BevelGearMesh", parent: "BevelGearMesh"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2317.AGMAGleasonConicalGearMesh":
            return self._parent._cast(_2317.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2325.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConicalGearMesh)

        @property
        def gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh") -> "_2331.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2299.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def connection(self: "BevelGearMesh._Cast_BevelGearMesh") -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2319.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.BevelDifferentialGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2341.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2343.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2345.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2349.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.ZerolBevelGearMesh)

        @property
        def bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "BevelGearMesh":
            return self._parent

        def __getattr__(self: "BevelGearMesh._Cast_BevelGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self: Self) -> "_1191.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_mesh_design(self: Self) -> "_1191.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearMesh._Cast_BevelGearMesh":
        return self._Cast_BevelGearMesh(self)
