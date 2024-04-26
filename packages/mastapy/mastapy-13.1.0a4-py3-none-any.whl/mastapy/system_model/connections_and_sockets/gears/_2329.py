"""FaceGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999
    from mastapy.system_model.connections_and_sockets import _2299, _2290
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMesh",)


Self = TypeVar("Self", bound="FaceGearMesh")


class FaceGearMesh(_2331.GearMesh):
    """FaceGearMesh

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMesh")

    class _Cast_FaceGearMesh:
        """Special nested class for casting FaceGearMesh to subclasses."""

        def __init__(self: "FaceGearMesh._Cast_FaceGearMesh", parent: "FaceGearMesh"):
            self._parent = parent

        @property
        def gear_mesh(self: "FaceGearMesh._Cast_FaceGearMesh") -> "_2331.GearMesh":
            return self._parent._cast(_2331.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "FaceGearMesh._Cast_FaceGearMesh",
        ) -> "_2299.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def connection(self: "FaceGearMesh._Cast_FaceGearMesh") -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "FaceGearMesh._Cast_FaceGearMesh",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def face_gear_mesh(self: "FaceGearMesh._Cast_FaceGearMesh") -> "FaceGearMesh":
            return self._parent

        def __getattr__(self: "FaceGearMesh._Cast_FaceGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: Self, value: "float"):
        self.wrapped.PinionDropAngle = float(value) if value is not None else 0.0

    @property
    def wheel_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: Self, value: "float"):
        self.wrapped.WheelDropAngle = float(value) if value is not None else 0.0

    @property
    def active_gear_mesh_design(self: Self) -> "_999.FaceGearMeshDesign":
        """mastapy.gears.gear_designs.face.FaceGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear_mesh_design(self: Self) -> "_999.FaceGearMeshDesign":
        """mastapy.gears.gear_designs.face.FaceGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearMesh._Cast_FaceGearMesh":
        return self._Cast_FaceGearMesh(self)
