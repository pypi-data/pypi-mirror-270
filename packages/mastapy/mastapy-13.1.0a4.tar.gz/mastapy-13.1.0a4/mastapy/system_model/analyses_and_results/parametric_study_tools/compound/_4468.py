"""AbstractShaftOrHousingCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4491,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4467,
        _4511,
        _4522,
        _4561,
        _4545,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundParametricStudyTool")


class AbstractShaftOrHousingCompoundParametricStudyTool(
    _4491.ComponentCompoundParametricStudyTool
):
    """AbstractShaftOrHousingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundParametricStudyTool"
    )

    class _Cast_AbstractShaftOrHousingCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftOrHousingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
            parent: "AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4491.ComponentCompoundParametricStudyTool":
            return self._parent._cast(_4491.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4467.AbstractShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.AbstractShaftCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4511.CycloidalDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.CycloidalDiscCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4522.FEPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.FEPartCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "_4561.ShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(_4561.ShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "AbstractShaftOrHousingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "AbstractShaftOrHousingCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4320.AbstractShaftOrHousingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4320.AbstractShaftOrHousingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool":
        return self._Cast_AbstractShaftOrHousingCompoundParametricStudyTool(self)
