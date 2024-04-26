"""AbstractShaftAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7034,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.system_deflections import _2710
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7081,
        _7133,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="AbstractShaftAdvancedTimeSteppingAnalysisForModulation")


class AbstractShaftAdvancedTimeSteppingAnalysisForModulation(
    _7034.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7034.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7034.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7081.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7133.ShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2710.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

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
    ) -> "AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation(self)
