"""SpringDamperConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3958
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpringDamperConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.stability_analyses import _3890
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3985,
        _3955,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundStabilityAnalysis")


class SpringDamperConnectionCompoundStabilityAnalysis(
    _3958.CouplingConnectionCompoundStabilityAnalysis
):
    """SpringDamperConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundStabilityAnalysis"
    )

    class _Cast_SpringDamperConnectionCompoundStabilityAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
            parent: "SpringDamperConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_stability_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_3958.CouplingConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3958.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_3985.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_3955.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
        ) -> "SpringDamperConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "SpringDamperConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2368.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2368.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_3890.SpringDamperConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpringDamperConnectionStabilityAnalysis]

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
    ) -> "List[_3890.SpringDamperConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpringDamperConnectionStabilityAnalysis]

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
    ) -> "SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis":
        return self._Cast_SpringDamperConnectionCompoundStabilityAnalysis(self)
