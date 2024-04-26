"""KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3988
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.stability_analyses import _3858
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3989,
        _3990,
        _3954,
        _3980,
        _4018,
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis(
    _3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3954.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis.TYPE",
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
    ) -> "List[_3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_3989.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_3990.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundStabilityAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis(
                self
            )
        )
