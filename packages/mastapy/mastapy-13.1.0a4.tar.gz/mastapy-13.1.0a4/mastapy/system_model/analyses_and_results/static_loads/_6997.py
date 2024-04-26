"""SynchroniserSleeveLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6996
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6879,
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveLoadCase",)


Self = TypeVar("Self", bound="SynchroniserSleeveLoadCase")


class SynchroniserSleeveLoadCase(_6996.SynchroniserPartLoadCase):
    """SynchroniserSleeveLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveLoadCase")

    class _Cast_SynchroniserSleeveLoadCase:
        """Special nested class for casting SynchroniserSleeveLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
            parent: "SynchroniserSleeveLoadCase",
        ):
            self._parent = parent

        @property
        def synchroniser_part_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_6996.SynchroniserPartLoadCase":
            return self._parent._cast(_6996.SynchroniserPartLoadCase)

        @property
        def coupling_half_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6879

            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "SynchroniserSleeveLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleeveLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase":
        return self._Cast_SynchroniserSleeveLoadCase(self)
