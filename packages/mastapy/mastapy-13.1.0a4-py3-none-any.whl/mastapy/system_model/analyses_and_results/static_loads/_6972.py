"""RollingRingAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2617
    from mastapy.system_model.analyses_and_results.static_loads import _6833, _6955
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyLoadCase",)


Self = TypeVar("Self", bound="RollingRingAssemblyLoadCase")


class RollingRingAssemblyLoadCase(_6979.SpecialisedAssemblyLoadCase):
    """RollingRingAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyLoadCase")

    class _Cast_RollingRingAssemblyLoadCase:
        """Special nested class for casting RollingRingAssemblyLoadCase to subclasses."""

        def __init__(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
            parent: "RollingRingAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_load_case(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
        ) -> "RollingRingAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyLoadCase._Cast_RollingRingAssemblyLoadCase":
        return self._Cast_RollingRingAssemblyLoadCase(self)
