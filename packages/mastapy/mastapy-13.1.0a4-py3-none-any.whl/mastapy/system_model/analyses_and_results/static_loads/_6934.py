"""HypoidGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6932,
        _6933,
        _6875,
        _6922,
        _6979,
        _6833,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetLoadCase",)


Self = TypeVar("Self", bound="HypoidGearSetLoadCase")


class HypoidGearSetLoadCase(_6842.AGMAGleasonConicalGearSetLoadCase):
    """HypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetLoadCase")

    class _Cast_HypoidGearSetLoadCase:
        """Special nested class for casting HypoidGearSetLoadCase to subclasses."""

        def __init__(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
            parent: "HypoidGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6842.AGMAGleasonConicalGearSetLoadCase":
            return self._parent._cast(_6842.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6875.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6922.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_load_case(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase",
        ) -> "HypoidGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_load_case(
        self: Self,
    ) -> "List[_6932.HypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_load_case(self: Self) -> "List[_6932.HypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_load_case(
        self: Self,
    ) -> "List[_6933.HypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_load_case(self: Self) -> "List[_6933.HypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase":
        return self._Cast_HypoidGearSetLoadCase(self)
