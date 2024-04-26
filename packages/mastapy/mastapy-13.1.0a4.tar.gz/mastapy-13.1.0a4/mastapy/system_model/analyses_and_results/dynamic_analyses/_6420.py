"""SynchroniserPartDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserPartDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6419,
        _6421,
        _6382,
        _6328,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartDynamicAnalysis")


class SynchroniserPartDynamicAnalysis(_6342.CouplingHalfDynamicAnalysis):
    """SynchroniserPartDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartDynamicAnalysis")

    class _Cast_SynchroniserPartDynamicAnalysis:
        """Special nested class for casting SynchroniserPartDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            parent: "SynchroniserPartDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6342.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6342.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6419.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6421.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.SynchroniserSleeveDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "SynchroniserPartDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartDynamicAnalysis.TYPE"):
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
    ) -> "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis":
        return self._Cast_SynchroniserPartDynamicAnalysis(self)
