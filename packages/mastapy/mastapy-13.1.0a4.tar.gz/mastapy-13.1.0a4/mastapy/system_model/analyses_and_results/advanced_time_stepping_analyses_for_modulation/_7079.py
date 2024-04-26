"""CVTPulleyAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7126,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.system_deflections import _2756
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7076,
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CVTPulleyAdvancedTimeSteppingAnalysisForModulation")


class CVTPulleyAdvancedTimeSteppingAnalysisForModulation(
    _7126.PulleyAdvancedTimeSteppingAnalysisForModulation
):
    """CVTPulleyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CVTPulleyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
            parent: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.PulleyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7126.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CVTPulleyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2756.CVTPulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection

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
    ) -> "CVTPulleyAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CVTPulleyAdvancedTimeSteppingAnalysisForModulation(self)
