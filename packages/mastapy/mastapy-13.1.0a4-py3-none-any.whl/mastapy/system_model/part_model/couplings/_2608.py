"""PartToPartShearCouplingHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalf",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalf")


class PartToPartShearCouplingHalf(_2603.CouplingHalf):
    """PartToPartShearCouplingHalf

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCouplingHalf")

    class _Cast_PartToPartShearCouplingHalf:
        """Special nested class for casting PartToPartShearCouplingHalf to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
            parent: "PartToPartShearCouplingHalf",
        ):
            self._parent = parent

        @property
        def coupling_half(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "_2603.CouplingHalf":
            return self._parent._cast(_2603.CouplingHalf)

        @property
        def mountable_component(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def part_to_part_shear_coupling_half(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
        ) -> "PartToPartShearCouplingHalf":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartToPartShearCouplingHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf":
        return self._Cast_PartToPartShearCouplingHalf(self)
