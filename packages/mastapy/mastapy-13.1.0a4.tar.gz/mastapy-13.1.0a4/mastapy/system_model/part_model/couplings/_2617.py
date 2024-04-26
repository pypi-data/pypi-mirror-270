"""RollingRingAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.system_model.part_model import _2494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.part_model import _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssembly",)


Self = TypeVar("Self", bound="RollingRingAssembly")


class RollingRingAssembly(_2494.SpecialisedAssembly):
    """RollingRingAssembly

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssembly")

    class _Cast_RollingRingAssembly:
        """Special nested class for casting RollingRingAssembly to subclasses."""

        def __init__(
            self: "RollingRingAssembly._Cast_RollingRingAssembly",
            parent: "RollingRingAssembly",
        ):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "RollingRingAssembly._Cast_RollingRingAssembly",
        ) -> "_2494.SpecialisedAssembly":
            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "RollingRingAssembly._Cast_RollingRingAssembly",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(self: "RollingRingAssembly._Cast_RollingRingAssembly") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "RollingRingAssembly._Cast_RollingRingAssembly",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def rolling_ring_assembly(
            self: "RollingRingAssembly._Cast_RollingRingAssembly",
        ) -> "RollingRingAssembly":
            return self._parent

        def __getattr__(
            self: "RollingRingAssembly._Cast_RollingRingAssembly", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingAssembly.TYPE"):
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
    def rolling_rings(self: Self) -> "List[_2616.RollingRing]":
        """List[mastapy.system_model.part_model.couplings.RollingRing]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingRings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "RollingRingAssembly._Cast_RollingRingAssembly":
        return self._Cast_RollingRingAssembly(self)
