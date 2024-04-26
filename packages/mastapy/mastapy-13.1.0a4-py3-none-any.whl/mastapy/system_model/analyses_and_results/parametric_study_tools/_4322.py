"""AbstractShaftToMountableComponentConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
        "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4343,
        _4363,
        _4365,
        _4420,
        _4434,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionParametricStudyTool",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionParametricStudyTool"
)


class AbstractShaftToMountableComponentConnectionParametricStudyTool(
    _4354.ConnectionParametricStudyTool
):
    """AbstractShaftToMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
            parent: "AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4354.ConnectionParametricStudyTool":
            return self._parent._cast(_4354.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4343.CoaxialConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CoaxialConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4363.CycloidalDiscCentralBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(
                _4363.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4365.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(
                _4365.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4420.PlanetaryConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.PlanetaryConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4434.ShaftToMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(
                _4434.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "AbstractShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2283.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool(
                self
            )
        )
