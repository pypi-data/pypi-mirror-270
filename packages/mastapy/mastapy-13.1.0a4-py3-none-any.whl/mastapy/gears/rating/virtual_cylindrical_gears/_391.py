"""KlingelnbergHypoidVirtualCylindricalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _393
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "KlingelnbergHypoidVirtualCylindricalGear",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _395, _396


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergHypoidVirtualCylindricalGear",)


Self = TypeVar("Self", bound="KlingelnbergHypoidVirtualCylindricalGear")


class KlingelnbergHypoidVirtualCylindricalGear(_393.KlingelnbergVirtualCylindricalGear):
    """KlingelnbergHypoidVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergHypoidVirtualCylindricalGear"
    )

    class _Cast_KlingelnbergHypoidVirtualCylindricalGear:
        """Special nested class for casting KlingelnbergHypoidVirtualCylindricalGear to subclasses."""

        def __init__(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
            parent: "KlingelnbergHypoidVirtualCylindricalGear",
        ):
            self._parent = parent

        @property
        def klingelnberg_virtual_cylindrical_gear(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
        ) -> "_393.KlingelnbergVirtualCylindricalGear":
            return self._parent._cast(_393.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
        ) -> "_395.VirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _395

            return self._parent._cast(_395.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
        ) -> "_396.VirtualCylindricalGearBasic":
            from mastapy.gears.rating.virtual_cylindrical_gears import _396

            return self._parent._cast(_396.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
        ) -> "KlingelnbergHypoidVirtualCylindricalGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear",
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
        self: Self, instance_to_wrap: "KlingelnbergHypoidVirtualCylindricalGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear":
        return self._Cast_KlingelnbergHypoidVirtualCylindricalGear(self)
