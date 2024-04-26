"""ConicalMeshMicroGeometryConfigBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.manufacturing.bevel import _785, _792, _793
    from mastapy.gears.analysis import _1232, _1226


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshMicroGeometryConfigBase",)


Self = TypeVar("Self", bound="ConicalMeshMicroGeometryConfigBase")


class ConicalMeshMicroGeometryConfigBase(_1235.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshMicroGeometryConfigBase")

    class _Cast_ConicalMeshMicroGeometryConfigBase:
        """Special nested class for casting ConicalMeshMicroGeometryConfigBase to subclasses."""

        def __init__(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
            parent: "ConicalMeshMicroGeometryConfigBase",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1235.GearMeshImplementationDetail":
            return self._parent._cast(_1235.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1232.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_792.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_793.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "ConicalMeshMicroGeometryConfigBase":
            return self._parent

        def __getattr__(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
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
        self: Self, instance_to_wrap: "ConicalMeshMicroGeometryConfigBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh(self: Self) -> "_1165.ConicalGearMeshDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_config(self: Self) -> "_785.ConicalGearMicroGeometryConfigBase":
        """mastapy.gears.manufacturing.bevel.ConicalGearMicroGeometryConfigBase

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
    ) -> "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase":
        return self._Cast_ConicalMeshMicroGeometryConfigBase(self)
