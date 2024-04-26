"""AbstractShaftParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractShaftParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4364,
        _4433,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftParametricStudyTool")


class AbstractShaftParametricStudyTool(_4320.AbstractShaftOrHousingParametricStudyTool):
    """AbstractShaftParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftParametricStudyTool")

    class _Cast_AbstractShaftParametricStudyTool:
        """Special nested class for casting AbstractShaftParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
            parent: "AbstractShaftParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4320.AbstractShaftOrHousingParametricStudyTool":
            return self._parent._cast(_4320.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4364.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.CycloidalDiscParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4433.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.ShaftParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "AbstractShaftParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool":
        return self._Cast_AbstractShaftParametricStudyTool(self)
