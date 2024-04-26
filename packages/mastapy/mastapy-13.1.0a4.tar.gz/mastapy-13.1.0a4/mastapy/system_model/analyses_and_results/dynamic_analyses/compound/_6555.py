"""UnbalancedMassCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "UnbalancedMassCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2495
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6511,
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundDynamicAnalysis")


class UnbalancedMassCompoundDynamicAnalysis(
    _6556.VirtualComponentCompoundDynamicAnalysis
):
    """UnbalancedMassCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundDynamicAnalysis"
    )

    class _Cast_UnbalancedMassCompoundDynamicAnalysis:
        """Special nested class for casting UnbalancedMassCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
            parent: "UnbalancedMassCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_6556.VirtualComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6556.VirtualComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
        ) -> "UnbalancedMassCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2495.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_6426.UnbalancedMassDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis]

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
    ) -> "List[_6426.UnbalancedMassDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis]

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
    ) -> "UnbalancedMassCompoundDynamicAnalysis._Cast_UnbalancedMassCompoundDynamicAnalysis":
        return self._Cast_UnbalancedMassCompoundDynamicAnalysis(self)
