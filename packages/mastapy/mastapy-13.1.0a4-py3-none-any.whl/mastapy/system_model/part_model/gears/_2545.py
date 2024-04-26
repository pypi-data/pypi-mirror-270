"""CylindricalPlanetGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGear",)


Self = TypeVar("Self", bound="CylindricalPlanetGear")


class CylindricalPlanetGear(_2543.CylindricalGear):
    """CylindricalPlanetGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGear")

    class _Cast_CylindricalPlanetGear:
        """Special nested class for casting CylindricalPlanetGear to subclasses."""

        def __init__(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
            parent: "CylindricalPlanetGear",
        ):
            self._parent = parent

        @property
        def cylindrical_gear(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2543.CylindricalGear":
            return self._parent._cast(_2543.CylindricalGear)

        @property
        def gear(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def mountable_component(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def cylindrical_planet_gear(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear",
        ) -> "CylindricalPlanetGear":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGear._Cast_CylindricalPlanetGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalPlanetGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalPlanetGear._Cast_CylindricalPlanetGear":
        return self._Cast_CylindricalPlanetGear(self)
