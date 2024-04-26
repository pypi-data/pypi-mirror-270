"""KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6502
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6503,
        _6504,
        _6468,
        _6494,
        _6532,
        _6434,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis(
    _6502.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6502.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(
                _6502.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6468.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6494.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6532.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6434.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6503.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis(
            self
        )
