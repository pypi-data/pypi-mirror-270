"""VirtualComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2482
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2480,
        _2481,
        _2489,
        _2490,
        _2495,
        _2462,
        _2486,
    )
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponent",)


Self = TypeVar("Self", bound="VirtualComponent")


class VirtualComponent(_2482.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponent")

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(
            self: "VirtualComponent._Cast_VirtualComponent", parent: "VirtualComponent"
        ):
            self._parent = parent

        @property
        def mountable_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2482.MountableComponent":
            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(self: "VirtualComponent._Cast_VirtualComponent") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def mass_disc(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2480.MassDisc":
            from mastapy.system_model.part_model import _2480

            return self._parent._cast(_2480.MassDisc)

        @property
        def measurement_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2481.MeasurementComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.MeasurementComponent)

        @property
        def point_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2489.PointLoad":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PointLoad)

        @property
        def power_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2490.PowerLoad":
            from mastapy.system_model.part_model import _2490

            return self._parent._cast(_2490.PowerLoad)

        @property
        def unbalanced_mass(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2495.UnbalancedMass":
            from mastapy.system_model.part_model import _2495

            return self._parent._cast(_2495.UnbalancedMass)

        @property
        def virtual_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "VirtualComponent":
            return self._parent

        def __getattr__(self: "VirtualComponent._Cast_VirtualComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "VirtualComponent._Cast_VirtualComponent":
        return self._Cast_VirtualComponent(self)
