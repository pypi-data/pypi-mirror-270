"""ConceptGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConceptGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6463,
        _6464,
        _6532,
        _6434,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundDynamicAnalysis")


class ConceptGearSetCompoundDynamicAnalysis(_6494.GearSetCompoundDynamicAnalysis):
    """ConceptGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundDynamicAnalysis"
    )

    class _Cast_ConceptGearSetCompoundDynamicAnalysis:
        """Special nested class for casting ConceptGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
            parent: "ConceptGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_dynamic_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_6494.GearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6494.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_6532.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_6434.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
        ) -> "ConceptGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2540.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_6334.ConceptGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis]

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
    def concept_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6463.ConceptGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6464.ConceptGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6334.ConceptGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis]

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
    ) -> "ConceptGearSetCompoundDynamicAnalysis._Cast_ConceptGearSetCompoundDynamicAnalysis":
        return self._Cast_ConceptGearSetCompoundDynamicAnalysis(self)
