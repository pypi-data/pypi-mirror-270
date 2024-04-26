"""FlexiblePinAssemblyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "FlexiblePinAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303, _6384
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyDynamicAnalysis")


class FlexiblePinAssemblyDynamicAnalysis(_6403.SpecialisedAssemblyDynamicAnalysis):
    """FlexiblePinAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyDynamicAnalysis")

    class _Cast_FlexiblePinAssemblyDynamicAnalysis:
        """Special nested class for casting FlexiblePinAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
            parent: "FlexiblePinAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
        ) -> "FlexiblePinAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "FlexiblePinAssemblyDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6915.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyDynamicAnalysis._Cast_FlexiblePinAssemblyDynamicAnalysis":
        return self._Cast_FlexiblePinAssemblyDynamicAnalysis(self)
