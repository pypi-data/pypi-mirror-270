"""RingPinsLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6843,
        _6864,
        _6955,
    )
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsLoadCase",)


Self = TypeVar("Self", bound="RingPinsLoadCase")


class RingPinsLoadCase(_6951.MountableComponentLoadCase):
    """RingPinsLoadCase

    This is a mastapy class.
    """

    TYPE = _RING_PINS_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsLoadCase")

    class _Cast_RingPinsLoadCase:
        """Special nested class for casting RingPinsLoadCase to subclasses."""

        def __init__(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase", parent: "RingPinsLoadCase"
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def ring_pins_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "RingPinsLoadCase":
            return self._parent

        def __getattr__(self: "RingPinsLoadCase._Cast_RingPinsLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_ring_pins_manufacturing_error(
        self: Self,
    ) -> "_6843.AllRingPinsManufacturingError":
        """mastapy.system_model.analyses_and_results.static_loads.AllRingPinsManufacturingError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllRingPinsManufacturingError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2588.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsLoadCase._Cast_RingPinsLoadCase":
        return self._Cast_RingPinsLoadCase(self)
