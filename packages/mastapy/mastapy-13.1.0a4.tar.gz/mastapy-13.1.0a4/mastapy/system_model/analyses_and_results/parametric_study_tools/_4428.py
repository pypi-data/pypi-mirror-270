"""RollingRingAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "RollingRingAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2617
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.system_deflections import _2820
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="RollingRingAssemblyParametricStudyTool")


class RollingRingAssemblyParametricStudyTool(
    _4435.SpecialisedAssemblyParametricStudyTool
):
    """RollingRingAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyParametricStudyTool"
    )

    class _Cast_RollingRingAssemblyParametricStudyTool:
        """Special nested class for casting RollingRingAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
            parent: "RollingRingAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
        ) -> "RollingRingAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6972.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "List[_2820.RollingRingAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection]

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
    ) -> "RollingRingAssemblyParametricStudyTool._Cast_RollingRingAssemblyParametricStudyTool":
        return self._Cast_RollingRingAssemblyParametricStudyTool(self)
