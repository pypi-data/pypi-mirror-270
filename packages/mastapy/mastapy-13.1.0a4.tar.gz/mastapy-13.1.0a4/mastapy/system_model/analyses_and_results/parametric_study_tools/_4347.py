"""ConceptCouplingParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConceptCouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6867
    from mastapy.system_model.analyses_and_results.system_deflections import _2742
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4435,
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptCouplingParametricStudyTool")


class ConceptCouplingParametricStudyTool(_4358.CouplingParametricStudyTool):
    """ConceptCouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingParametricStudyTool")

    class _Cast_ConceptCouplingParametricStudyTool:
        """Special nested class for casting ConceptCouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
            parent: "ConceptCouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_4358.CouplingParametricStudyTool":
            return self._parent._cast(_4358.CouplingParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "ConceptCouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConceptCouplingParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2599.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6867.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2742.ConceptCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool":
        return self._Cast_ConceptCouplingParametricStudyTool(self)
