"""SpringDamperHalfCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6473
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpringDamperHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2624
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6511,
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundDynamicAnalysis")


class SpringDamperHalfCompoundDynamicAnalysis(
    _6473.CouplingHalfCompoundDynamicAnalysis
):
    """SpringDamperHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundDynamicAnalysis"
    )

    class _Cast_SpringDamperHalfCompoundDynamicAnalysis:
        """Special nested class for casting SpringDamperHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
            parent: "SpringDamperHalfCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_6473.CouplingHalfCompoundDynamicAnalysis":
            return self._parent._cast(_6473.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
        ) -> "SpringDamperHalfCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperHalfCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2624.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6409.SpringDamperHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6409.SpringDamperHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfCompoundDynamicAnalysis._Cast_SpringDamperHalfCompoundDynamicAnalysis":
        return self._Cast_SpringDamperHalfCompoundDynamicAnalysis(self)
