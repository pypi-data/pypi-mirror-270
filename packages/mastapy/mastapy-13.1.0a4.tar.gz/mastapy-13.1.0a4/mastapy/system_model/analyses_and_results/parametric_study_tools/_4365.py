"""CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2356
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.system_deflections import _2760
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"
)


class CycloidalDiscPlanetaryBearingConnectionParametricStudyTool(
    _4322.AbstractShaftToMountableComponentConnectionParametricStudyTool
):
    """CycloidalDiscPlanetaryBearingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
            parent: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_4322.AbstractShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4322.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_4354.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2356.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6887.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "List[_2760.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool(
            self
        )
