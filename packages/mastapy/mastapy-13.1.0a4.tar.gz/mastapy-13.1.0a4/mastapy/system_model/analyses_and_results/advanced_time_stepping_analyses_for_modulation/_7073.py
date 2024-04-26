"""ConnectorAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7115,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.system_deflections import _2751
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7045,
        _7116,
        _7134,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConnectorAdvancedTimeSteppingAnalysisForModulation")


class ConnectorAdvancedTimeSteppingAnalysisForModulation(
    _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
):
    """ConnectorAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConnectorAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7116.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConnectorAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConnectorAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2751.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

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
    ) -> "ConnectorAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConnectorAdvancedTimeSteppingAnalysisForModulation(self)
