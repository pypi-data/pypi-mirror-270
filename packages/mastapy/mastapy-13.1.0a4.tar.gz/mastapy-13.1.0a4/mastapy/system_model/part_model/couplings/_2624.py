"""SpringDamperHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalf",)


Self = TypeVar("Self", bound="SpringDamperHalf")


class SpringDamperHalf(_2603.CouplingHalf):
    """SpringDamperHalf

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalf")

    class _Cast_SpringDamperHalf:
        """Special nested class for casting SpringDamperHalf to subclasses."""

        def __init__(
            self: "SpringDamperHalf._Cast_SpringDamperHalf", parent: "SpringDamperHalf"
        ):
            self._parent = parent

        @property
        def coupling_half(
            self: "SpringDamperHalf._Cast_SpringDamperHalf",
        ) -> "_2603.CouplingHalf":
            return self._parent._cast(_2603.CouplingHalf)

        @property
        def mountable_component(
            self: "SpringDamperHalf._Cast_SpringDamperHalf",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "SpringDamperHalf._Cast_SpringDamperHalf",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(self: "SpringDamperHalf._Cast_SpringDamperHalf") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "SpringDamperHalf._Cast_SpringDamperHalf",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def spring_damper_half(
            self: "SpringDamperHalf._Cast_SpringDamperHalf",
        ) -> "SpringDamperHalf":
            return self._parent

        def __getattr__(self: "SpringDamperHalf._Cast_SpringDamperHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpringDamperHalf._Cast_SpringDamperHalf":
        return self._Cast_SpringDamperHalf(self)
