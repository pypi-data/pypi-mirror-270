"""PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7097,
        _7136,
        _7032,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2560.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )
