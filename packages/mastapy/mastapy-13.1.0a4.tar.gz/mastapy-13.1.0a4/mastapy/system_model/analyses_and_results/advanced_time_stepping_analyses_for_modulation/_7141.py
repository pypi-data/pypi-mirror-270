"""SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7075,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2833
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7103,
        _7072,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7075.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7075.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7075.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6983.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2833.SpringDamperConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
