"""BeltDriveAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7136,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6848
    from mastapy.system_model.analyses_and_results.system_deflections import _2723
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7077,
        _7032,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BeltDriveAdvancedTimeSteppingAnalysisForModulation")


class BeltDriveAdvancedTimeSteppingAnalysisForModulation(
    _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """BeltDriveAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BeltDriveAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
            parent: "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BeltDriveAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6848.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2723.BeltDriveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection

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
    ) -> "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation(self)
