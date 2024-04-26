"""RollingRingLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RollingRingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingLoadCase",)


Self = TypeVar("Self", bound="RollingRingLoadCase")


class RollingRingLoadCase(_6879.CouplingHalfLoadCase):
    """RollingRingLoadCase

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingLoadCase")

    class _Cast_RollingRingLoadCase:
        """Special nested class for casting RollingRingLoadCase to subclasses."""

        def __init__(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
            parent: "RollingRingLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_load_case(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase",
        ) -> "RollingRingLoadCase":
            return self._parent

        def __getattr__(
            self: "RollingRingLoadCase._Cast_RollingRingLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "RollingRingLoadCase._Cast_RollingRingLoadCase":
        return self._Cast_RollingRingLoadCase(self)
