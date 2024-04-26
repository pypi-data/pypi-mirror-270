"""PulleyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PulleyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.system_deflections import _2816
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4361,
        _4404,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PulleyParametricStudyTool",)


Self = TypeVar("Self", bound="PulleyParametricStudyTool")


class PulleyParametricStudyTool(_4357.CouplingHalfParametricStudyTool):
    """PulleyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PULLEY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyParametricStudyTool")

    class _Cast_PulleyParametricStudyTool:
        """Special nested class for casting PulleyParametricStudyTool to subclasses."""

        def __init__(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
            parent: "PulleyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_4357.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4357.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "_4361.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.CVTPulleyParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool",
        ) -> "PulleyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6967.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2816.PulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PulleyParametricStudyTool._Cast_PulleyParametricStudyTool":
        return self._Cast_PulleyParametricStudyTool(self)
