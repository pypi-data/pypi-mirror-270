"""ConceptGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearLoadCase",)


Self = TypeVar("Self", bound="ConceptGearLoadCase")


class ConceptGearLoadCase(_6917.GearLoadCase):
    """ConceptGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearLoadCase")

    class _Cast_ConceptGearLoadCase:
        """Special nested class for casting ConceptGearLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
            parent: "ConceptGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_6917.GearLoadCase":
            return self._parent._cast(_6917.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "ConceptGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearLoadCase._Cast_ConceptGearLoadCase":
        return self._Cast_ConceptGearLoadCase(self)
