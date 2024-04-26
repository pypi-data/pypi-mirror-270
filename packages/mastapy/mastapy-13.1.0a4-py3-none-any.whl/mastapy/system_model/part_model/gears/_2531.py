"""AGMAGleasonConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2533,
        _2535,
        _2536,
        _2537,
        _2552,
        _2561,
        _2563,
        _2565,
        _2567,
        _2568,
        _2571,
        _2548,
    )
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGear",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGear")


class AGMAGleasonConicalGear(_2541.ConicalGear):
    """AGMAGleasonConicalGear

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGear")

    class _Cast_AGMAGleasonConicalGear:
        """Special nested class for casting AGMAGleasonConicalGear to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
            parent: "AGMAGleasonConicalGear",
        ):
            self._parent = parent

        @property
        def conical_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2541.ConicalGear":
            return self._parent._cast(_2541.ConicalGear)

        @property
        def gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def mountable_component(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2533.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2535.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2536.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def hypoid_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2552.HypoidGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.HypoidGear)

        @property
        def spiral_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2561.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2563.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2565.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2567.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2568.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2571.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.ZerolBevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "AGMAGleasonConicalGear":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear":
        return self._Cast_AGMAGleasonConicalGear(self)
