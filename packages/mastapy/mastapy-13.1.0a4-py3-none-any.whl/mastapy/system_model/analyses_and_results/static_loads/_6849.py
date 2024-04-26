"""BevelDifferentialGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6852,
        _6853,
        _6840,
        _6871,
        _6917,
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearLoadCase")


class BevelDifferentialGearLoadCase(_6854.BevelGearLoadCase):
    """BevelDifferentialGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearLoadCase")

    class _Cast_BevelDifferentialGearLoadCase:
        """Special nested class for casting BevelDifferentialGearLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
            parent: "BevelDifferentialGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6871.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6917.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6852.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "_6853.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "BevelDifferentialGearLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase":
        return self._Cast_BevelDifferentialGearLoadCase(self)
