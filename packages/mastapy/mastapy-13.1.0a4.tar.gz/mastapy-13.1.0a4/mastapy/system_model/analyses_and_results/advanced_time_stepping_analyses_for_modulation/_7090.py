"""FaceGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7095,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6911
    from mastapy.system_model.analyses_and_results.system_deflections import _2779
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="FaceGearAdvancedTimeSteppingAnalysisForModulation")


class FaceGearAdvancedTimeSteppingAnalysisForModulation(
    _7095.GearAdvancedTimeSteppingAnalysisForModulation
):
    """FaceGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FaceGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "FaceGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "FaceGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6911.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2779.FaceGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection

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
    ) -> "FaceGearAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_FaceGearAdvancedTimeSteppingAnalysisForModulation(self)
