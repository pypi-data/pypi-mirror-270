"""BevelDifferentialGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1192
    from mastapy.system_model.part_model.gears import _2537, _2532, _2542, _2550
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSet",)


Self = TypeVar("Self", bound="BevelDifferentialGearSet")


class BevelDifferentialGearSet(_2538.BevelGearSet):
    """BevelDifferentialGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearSet")

    class _Cast_BevelDifferentialGearSet:
        """Special nested class for casting BevelDifferentialGearSet to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
            parent: "BevelDifferentialGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2538.BevelGearSet":
            return self._parent._cast(_2538.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "BevelDifferentialGearSet":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_1192.BevelGearSetDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_set_design(self: Self) -> "_1192.BevelGearSetDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears(self: Self) -> "List[_2537.BevelGear]":
        """List[mastapy.system_model.part_model.gears.BevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes(self: Self) -> "List[_2321.BevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.BevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet":
        return self._Cast_BevelDifferentialGearSet(self)
