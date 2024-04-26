"""UnbalancedMass"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model import _2497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMass",)


Self = TypeVar("Self", bound="UnbalancedMass")


class UnbalancedMass(_2497.VirtualComponent):
    """UnbalancedMass

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMass")

    class _Cast_UnbalancedMass:
        """Special nested class for casting UnbalancedMass to subclasses."""

        def __init__(
            self: "UnbalancedMass._Cast_UnbalancedMass", parent: "UnbalancedMass"
        ):
            self._parent = parent

        @property
        def virtual_component(
            self: "UnbalancedMass._Cast_UnbalancedMass",
        ) -> "_2497.VirtualComponent":
            return self._parent._cast(_2497.VirtualComponent)

        @property
        def mountable_component(
            self: "UnbalancedMass._Cast_UnbalancedMass",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(self: "UnbalancedMass._Cast_UnbalancedMass") -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(self: "UnbalancedMass._Cast_UnbalancedMass") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "UnbalancedMass._Cast_UnbalancedMass",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def unbalanced_mass(
            self: "UnbalancedMass._Cast_UnbalancedMass",
        ) -> "UnbalancedMass":
            return self._parent

        def __getattr__(self: "UnbalancedMass._Cast_UnbalancedMass", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "UnbalancedMass._Cast_UnbalancedMass":
        return self._Cast_UnbalancedMass(self)
