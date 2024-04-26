"""BevelGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6854,
        _6855,
        _6851,
        _6982,
        _6988,
        _6991,
        _7014,
        _6875,
        _6922,
        _6979,
        _6833,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelGearSetLoadCase")


class BevelGearSetLoadCase(_6842.AGMAGleasonConicalGearSetLoadCase):
    """BevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetLoadCase")

    class _Cast_BevelGearSetLoadCase:
        """Special nested class for casting BevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
            parent: "BevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6842.AGMAGleasonConicalGearSetLoadCase":
            return self._parent._cast(_6842.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6875.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6922.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6851.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelDifferentialGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6982.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6988.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6991.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_7014.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7014

            return self._parent._cast(_7014.ZerolBevelGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "BevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2538.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

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
    ) -> "List[_6854.BevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase]

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
    def bevel_gears_load_case(self: Self) -> "List[_6854.BevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_load_case(
        self: Self,
    ) -> "List[_6855.BevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase]

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
    def bevel_meshes_load_case(self: Self) -> "List[_6855.BevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase":
        return self._Cast_BevelGearSetLoadCase(self)
