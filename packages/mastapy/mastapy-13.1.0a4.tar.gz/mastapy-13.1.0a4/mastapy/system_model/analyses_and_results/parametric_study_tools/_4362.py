"""CycloidalAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.system_deflections import _2758
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalAssemblyParametricStudyTool")


class CycloidalAssemblyParametricStudyTool(
    _4435.SpecialisedAssemblyParametricStudyTool
):
    """CycloidalAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyParametricStudyTool")

    class _Cast_CycloidalAssemblyParametricStudyTool:
        """Special nested class for casting CycloidalAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
            parent: "CycloidalAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
        ) -> "CycloidalAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

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
    ) -> "List[_2758.CycloidalAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection]

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
    ) -> "CycloidalAssemblyParametricStudyTool._Cast_CycloidalAssemblyParametricStudyTool":
        return self._Cast_CycloidalAssemblyParametricStudyTool(self)
