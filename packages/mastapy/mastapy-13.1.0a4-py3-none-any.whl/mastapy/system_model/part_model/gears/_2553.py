"""HypoidGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _995
    from mastapy.system_model.part_model.gears import _2552, _2542, _2550
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSet",)


Self = TypeVar("Self", bound="HypoidGearSet")


class HypoidGearSet(_2532.AGMAGleasonConicalGearSet):
    """HypoidGearSet

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSet")

    class _Cast_HypoidGearSet:
        """Special nested class for casting HypoidGearSet to subclasses."""

        def __init__(
            self: "HypoidGearSet._Cast_HypoidGearSet", parent: "HypoidGearSet"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def gear_set(self: "HypoidGearSet._Cast_HypoidGearSet") -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(self: "HypoidGearSet._Cast_HypoidGearSet") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def hypoid_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "HypoidGearSet":
            return self._parent

        def __getattr__(self: "HypoidGearSet._Cast_HypoidGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_995.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_set_design(self: Self) -> "_995.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears(self: Self) -> "List[_2552.HypoidGear]":
        """List[mastapy.system_model.part_model.gears.HypoidGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes(self: Self) -> "List[_2333.HypoidGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSet._Cast_HypoidGearSet":
        return self._Cast_HypoidGearSet(self)
