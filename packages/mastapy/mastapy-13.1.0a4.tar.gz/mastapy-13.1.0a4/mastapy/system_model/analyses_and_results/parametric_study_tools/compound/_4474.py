"""BearingCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4502,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BearingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1966
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.static_loads import _6846
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4327
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4543,
        _4491,
        _4545,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BearingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BearingCompoundParametricStudyTool")


class BearingCompoundParametricStudyTool(_4502.ConnectorCompoundParametricStudyTool):
    """BearingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingCompoundParametricStudyTool")

    class _Cast_BearingCompoundParametricStudyTool:
        """Special nested class for casting BearingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
            parent: "BearingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connector_compound_parametric_study_tool(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_4502.ConnectorCompoundParametricStudyTool":
            return self._parent._cast(_4502.ConnectorCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_4543.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_4491.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_compound_parametric_study_tool(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
        ) -> "BearingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BearingCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_duty_cycle_results(self: Self) -> "_1966.LoadedBearingDutyCycle":
        """mastapy.bearings.bearing_results.LoadedBearingDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2457.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6846.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4327.BearingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[BearingCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BearingCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4327.BearingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingCompoundParametricStudyTool._Cast_BearingCompoundParametricStudyTool":
        return self._Cast_BearingCompoundParametricStudyTool(self)
