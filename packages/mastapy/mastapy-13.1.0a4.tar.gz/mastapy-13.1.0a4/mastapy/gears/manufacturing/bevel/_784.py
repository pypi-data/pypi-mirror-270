"""ConicalGearMicroGeometryConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.bevel import _785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearMicroGeometryConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _796
    from mastapy.gears.analysis import _1231, _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalGearMicroGeometryConfig")


class ConicalGearMicroGeometryConfig(_785.ConicalGearMicroGeometryConfigBase):
    """ConicalGearMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMicroGeometryConfig")

    class _Cast_ConicalGearMicroGeometryConfig:
        """Special nested class for casting ConicalGearMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
            parent: "ConicalGearMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "_1231.GearImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def conical_pinion_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "_796.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalPinionMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "ConicalGearMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMicroGeometryConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig":
        return self._Cast_ConicalGearMicroGeometryConfig(self)
