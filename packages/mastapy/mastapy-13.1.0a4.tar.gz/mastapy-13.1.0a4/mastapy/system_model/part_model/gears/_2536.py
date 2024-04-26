"""BevelDifferentialSunGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537, _2531, _2541, _2548
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGear",)


Self = TypeVar("Self", bound="BevelDifferentialSunGear")


class BevelDifferentialSunGear(_2533.BevelDifferentialGear):
    """BevelDifferentialSunGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialSunGear")

    class _Cast_BevelDifferentialSunGear:
        """Special nested class for casting BevelDifferentialSunGear to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
            parent: "BevelDifferentialSunGear",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2533.BevelDifferentialGear":
            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2541.ConicalGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConicalGear)

        @property
        def gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_sun_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "BevelDifferentialSunGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialSunGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear":
        return self._Cast_BevelDifferentialSunGear(self)
