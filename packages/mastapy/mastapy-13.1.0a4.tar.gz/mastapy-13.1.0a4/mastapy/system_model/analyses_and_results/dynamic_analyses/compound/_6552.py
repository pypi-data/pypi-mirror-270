"""TorqueConverterConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6472
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "TorqueConverterConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6422
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6499,
        _6469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCompoundDynamicAnalysis")


class TorqueConverterConnectionCompoundDynamicAnalysis(
    _6472.CouplingConnectionCompoundDynamicAnalysis
):
    """TorqueConverterConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionCompoundDynamicAnalysis"
    )

    class _Cast_TorqueConverterConnectionCompoundDynamicAnalysis:
        """Special nested class for casting TorqueConverterConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
            parent: "TorqueConverterConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_6472.CouplingConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6472.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_6499.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
        ) -> "TorqueConverterConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_6422.TorqueConverterConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis]

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
    ) -> "List[_6422.TorqueConverterConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis]

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
    ) -> "TorqueConverterConnectionCompoundDynamicAnalysis._Cast_TorqueConverterConnectionCompoundDynamicAnalysis":
        return self._Cast_TorqueConverterConnectionCompoundDynamicAnalysis(self)
