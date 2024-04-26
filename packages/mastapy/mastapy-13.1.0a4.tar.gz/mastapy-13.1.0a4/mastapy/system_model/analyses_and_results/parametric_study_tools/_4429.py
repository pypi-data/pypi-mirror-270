"""RollingRingConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "RollingRingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2310
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.system_deflections import _2821
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="RollingRingConnectionParametricStudyTool")


class RollingRingConnectionParametricStudyTool(
    _4391.InterMountableComponentConnectionParametricStudyTool
):
    """RollingRingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionParametricStudyTool"
    )

    class _Cast_RollingRingConnectionParametricStudyTool:
        """Special nested class for casting RollingRingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
            parent: "RollingRingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_4391.InterMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4391.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_4354.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_parametric_study_tool(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
        ) -> "RollingRingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "RollingRingConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2310.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6973.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2821.RollingRingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[RollingRingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingConnectionParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionParametricStudyTool._Cast_RollingRingConnectionParametricStudyTool":
        return self._Cast_RollingRingConnectionParametricStudyTool(self)
