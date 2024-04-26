"""ConicalMeshManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _795, _801
    from mastapy.gears.analysis import _1235, _1232, _1226


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalMeshManufacturingConfig")


class ConicalMeshManufacturingConfig(_794.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshManufacturingConfig")

    class _Cast_ConicalMeshManufacturingConfig:
        """Special nested class for casting ConicalMeshManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
            parent: "ConicalMeshManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_794.ConicalMeshMicroGeometryConfigBase":
            return self._parent._cast(_794.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1235.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1232.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "ConicalMeshManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_config(self: Self) -> "_795.ConicalPinionManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalPinionManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_config(self: Self) -> "_801.ConicalWheelManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalWheelManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig":
        return self._Cast_ConicalMeshManufacturingConfig(self)
