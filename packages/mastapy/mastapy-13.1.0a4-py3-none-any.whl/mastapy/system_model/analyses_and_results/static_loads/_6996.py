"""SynchroniserPartLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6994,
        _6997,
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartLoadCase",)


Self = TypeVar("Self", bound="SynchroniserPartLoadCase")


class SynchroniserPartLoadCase(_6879.CouplingHalfLoadCase):
    """SynchroniserPartLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartLoadCase")

    class _Cast_SynchroniserPartLoadCase:
        """Special nested class for casting SynchroniserPartLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
            parent: "SynchroniserPartLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6994.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.SynchroniserHalfLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6997.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.SynchroniserSleeveLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "SynchroniserPartLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2628.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase":
        return self._Cast_SynchroniserPartLoadCase(self)
