"""KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6500
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6466,
        _6492,
        _6511,
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis(
    _6500.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6500.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            return self._parent._cast(
                _6500.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6466.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6492.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]

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
    ) -> "List[_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis(
            self
        )
