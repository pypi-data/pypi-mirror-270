"""ConicalPinionMicroGeometryConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_PINION_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalPinionMicroGeometryConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _790, _785
    from mastapy.gears.analysis import _1231, _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("ConicalPinionMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalPinionMicroGeometryConfig")


class ConicalPinionMicroGeometryConfig(_784.ConicalGearMicroGeometryConfig):
    """ConicalPinionMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalPinionMicroGeometryConfig")

    class _Cast_ConicalPinionMicroGeometryConfig:
        """Special nested class for casting ConicalPinionMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
            parent: "ConicalPinionMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "_784.ConicalGearMicroGeometryConfig":
            return self._parent._cast(_784.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "_1231.GearImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def conical_pinion_micro_geometry_config(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
        ) -> "ConicalPinionMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalPinionMicroGeometryConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(
        self: Self,
    ) -> "_790.ConicalMeshFlankNURBSMicroGeometryConfig":
        """mastapy.gears.manufacturing.bevel.ConicalMeshFlankNURBSMicroGeometryConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_convex_ib_configuration(
        self: Self,
    ) -> "_790.ConicalMeshFlankNURBSMicroGeometryConfig":
        """mastapy.gears.manufacturing.bevel.ConicalMeshFlankNURBSMicroGeometryConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig":
        return self._Cast_ConicalPinionMicroGeometryConfig(self)
