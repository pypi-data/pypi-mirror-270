"""TorqueConverterParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2630
    from mastapy.system_model.analyses_and_results.static_loads import _7000
    from mastapy.system_model.analyses_and_results.system_deflections import _2853
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4435,
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterParametricStudyTool")


class TorqueConverterParametricStudyTool(_4358.CouplingParametricStudyTool):
    """TorqueConverterParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterParametricStudyTool")

    class _Cast_TorqueConverterParametricStudyTool:
        """Special nested class for casting TorqueConverterParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
            parent: "TorqueConverterParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_parametric_study_tool(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_4358.CouplingParametricStudyTool":
            return self._parent._cast(_4358.CouplingParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_parametric_study_tool(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
        ) -> "TorqueConverterParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool",
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
        self: Self, instance_to_wrap: "TorqueConverterParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7000.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

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
    ) -> "List[_2853.TorqueConverterSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection]

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
    ) -> "TorqueConverterParametricStudyTool._Cast_TorqueConverterParametricStudyTool":
        return self._Cast_TorqueConverterParametricStudyTool(self)
