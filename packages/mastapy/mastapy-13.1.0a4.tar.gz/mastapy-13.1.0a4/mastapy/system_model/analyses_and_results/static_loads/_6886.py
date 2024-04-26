"""CycloidalDiscLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6835,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscLoadCase",)


Self = TypeVar("Self", bound="CycloidalDiscLoadCase")


class CycloidalDiscLoadCase(_6834.AbstractShaftLoadCase):
    """CycloidalDiscLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscLoadCase")

    class _Cast_CycloidalDiscLoadCase:
        """Special nested class for casting CycloidalDiscLoadCase to subclasses."""

        def __init__(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
            parent: "CycloidalDiscLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6834.AbstractShaftLoadCase":
            return self._parent._cast(_6834.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6835.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "CycloidalDiscLoadCase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase":
        return self._Cast_CycloidalDiscLoadCase(self)
