"""SynchroniserDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6995
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303, _6384
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserDynamicAnalysis")


class SynchroniserDynamicAnalysis(_6403.SpecialisedAssemblyDynamicAnalysis):
    """SynchroniserDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserDynamicAnalysis")

    class _Cast_SynchroniserDynamicAnalysis:
        """Special nested class for casting SynchroniserDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
            parent: "SynchroniserDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
        ) -> "SynchroniserDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserDynamicAnalysis.TYPE"):
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
    def assembly_load_case(self: Self) -> "_6995.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

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
    ) -> "SynchroniserDynamicAnalysis._Cast_SynchroniserDynamicAnalysis":
        return self._Cast_SynchroniserDynamicAnalysis(self)
