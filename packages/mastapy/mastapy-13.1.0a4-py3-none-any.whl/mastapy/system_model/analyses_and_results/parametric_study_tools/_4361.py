"""CVTPulleyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CVTPulleyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4357,
        _4404,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyParametricStudyTool",)


Self = TypeVar("Self", bound="CVTPulleyParametricStudyTool")


class CVTPulleyParametricStudyTool(_4425.PulleyParametricStudyTool):
    """CVTPulleyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyParametricStudyTool")

    class _Cast_CVTPulleyParametricStudyTool:
        """Special nested class for casting CVTPulleyParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
            parent: "CVTPulleyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def pulley_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4425.PulleyParametricStudyTool":
            return self._parent._cast(_4425.PulleyParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4357.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "CVTPulleyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool":
        return self._Cast_CVTPulleyParametricStudyTool(self)
