"""BeltConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4531,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BeltConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2286
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4328
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4506,
        _4501,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BeltConnectionCompoundParametricStudyTool")


class BeltConnectionCompoundParametricStudyTool(
    _4531.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """BeltConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundParametricStudyTool"
    )

    class _Cast_BeltConnectionCompoundParametricStudyTool:
        """Special nested class for casting BeltConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
            parent: "BeltConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4531.InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4531.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4501.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4506.CVTBeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(
                _4506.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "BeltConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2286.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2286.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4328.BeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4328.BeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool":
        return self._Cast_BeltConnectionCompoundParametricStudyTool(self)
