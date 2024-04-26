"""StraightBevelPlanetGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)

if TYPE_CHECKING:
    from mastapy.gears import _347
    from mastapy.system_model.part_model.gears import _2537, _2531, _2541, _2548
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGear",)


Self = TypeVar("Self", bound="StraightBevelPlanetGear")


class StraightBevelPlanetGear(_2563.StraightBevelDiffGear):
    """StraightBevelPlanetGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGear")

    class _Cast_StraightBevelPlanetGear:
        """Special nested class for casting StraightBevelPlanetGear to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
            parent: "StraightBevelPlanetGear",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2563.StraightBevelDiffGear":
            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def bevel_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2541.ConicalGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConicalGear)

        @property
        def gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2548.Gear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.Gear)

        @property
        def mountable_component(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def straight_bevel_planet_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "StraightBevelPlanetGear":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelPlanetGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_details(self: Self) -> "_347.PlanetaryDetail":
        """mastapy.gears.PlanetaryDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear":
        return self._Cast_StraightBevelPlanetGear(self)
