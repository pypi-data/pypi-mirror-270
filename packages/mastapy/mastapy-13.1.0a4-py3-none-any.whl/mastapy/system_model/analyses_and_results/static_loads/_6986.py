"""StraightBevelDiffGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6992,
        _6993,
        _6840,
        _6871,
        _6917,
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearLoadCase",)


Self = TypeVar("Self", bound="StraightBevelDiffGearLoadCase")


class StraightBevelDiffGearLoadCase(_6854.BevelGearLoadCase):
    """StraightBevelDiffGearLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearLoadCase")

    class _Cast_StraightBevelDiffGearLoadCase:
        """Special nested class for casting StraightBevelDiffGearLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
            parent: "StraightBevelDiffGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6871.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6917.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6992.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6993.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.StraightBevelSunGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "StraightBevelDiffGearLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase":
        return self._Cast_StraightBevelDiffGearLoadCase(self)
