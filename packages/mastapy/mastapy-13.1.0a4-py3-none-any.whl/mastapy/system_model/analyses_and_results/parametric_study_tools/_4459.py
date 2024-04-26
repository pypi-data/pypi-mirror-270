"""VirtualComponentParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "VirtualComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4401,
        _4402,
        _4423,
        _4424,
        _4458,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentParametricStudyTool",)


Self = TypeVar("Self", bound="VirtualComponentParametricStudyTool")


class VirtualComponentParametricStudyTool(_4404.MountableComponentParametricStudyTool):
    """VirtualComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentParametricStudyTool")

    class _Cast_VirtualComponentParametricStudyTool:
        """Special nested class for casting VirtualComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
            parent: "VirtualComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4401.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4402.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.MeasurementComponentParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4423.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4424.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.PowerLoadParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4458.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4458,
            )

            return self._parent._cast(_4458.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "VirtualComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
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
        self: Self, instance_to_wrap: "VirtualComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> (
        "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool"
    ):
        return self._Cast_VirtualComponentParametricStudyTool(self)
