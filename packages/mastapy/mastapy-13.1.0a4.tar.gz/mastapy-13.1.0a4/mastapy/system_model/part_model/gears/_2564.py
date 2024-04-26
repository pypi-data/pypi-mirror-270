"""StraightBevelDiffGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _975
    from mastapy.system_model.part_model.gears import _2563, _2532, _2542, _2550
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSet",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSet")


class StraightBevelDiffGearSet(_2538.BevelGearSet):
    """StraightBevelDiffGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSet")

    class _Cast_StraightBevelDiffGearSet:
        """Special nested class for casting StraightBevelDiffGearSet to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
            parent: "StraightBevelDiffGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2538.BevelGearSet":
            return self._parent._cast(_2538.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def straight_bevel_diff_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "StraightBevelDiffGearSet":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_975.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_set_design(
        self: Self,
    ) -> "_975.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears(self: Self) -> "List[_2563.StraightBevelDiffGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes(
        self: Self,
    ) -> "List[_2343.StraightBevelDiffGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet":
        return self._Cast_StraightBevelDiffGearSet(self)
