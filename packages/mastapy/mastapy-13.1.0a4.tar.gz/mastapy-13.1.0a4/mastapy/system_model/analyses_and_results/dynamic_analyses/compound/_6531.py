"""ShaftToMountableComponentConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6437
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6458,
        _6478,
        _6517,
        _6469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundDynamicAnalysis"
)


class ShaftToMountableComponentConnectionCompoundDynamicAnalysis(
    _6437.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
):
    """ShaftToMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6437.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6437.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6458.CoaxialConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6478.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6517.PlanetaryConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6402.ShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6402.ShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis(
            self
        )
