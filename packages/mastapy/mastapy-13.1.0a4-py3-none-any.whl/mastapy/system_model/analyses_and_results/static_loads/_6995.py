"""SynchroniserLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SynchroniserLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6833, _6955
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserLoadCase",)


Self = TypeVar("Self", bound="SynchroniserLoadCase")


class SynchroniserLoadCase(_6979.SpecialisedAssemblyLoadCase):
    """SynchroniserLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserLoadCase")

    class _Cast_SynchroniserLoadCase:
        """Special nested class for casting SynchroniserLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
            parent: "SynchroniserLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_load_case(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase",
        ) -> "SynchroniserLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserLoadCase._Cast_SynchroniserLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2625.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SynchroniserLoadCase._Cast_SynchroniserLoadCase":
        return self._Cast_SynchroniserLoadCase(self)
