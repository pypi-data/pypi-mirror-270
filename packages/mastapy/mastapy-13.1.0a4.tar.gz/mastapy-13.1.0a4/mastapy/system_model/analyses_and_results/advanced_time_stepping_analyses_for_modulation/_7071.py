"""ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7097,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7069,
        _7070,
        _7042,
        _7050,
        _7055,
        _7102,
        _7106,
        _7109,
        _7112,
        _7139,
        _7145,
        _7148,
        _7166,
        _7136,
        _7032,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2748
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConicalGearSetAdvancedTimeSteppingAnalysisForModulation")


class ConicalGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7097.GearSetAdvancedTimeSteppingAnalysisForModulation
):
    """ConicalGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConicalGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.GearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7097.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7145,
            )

            return self._parent._cast(
                _7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7148,
            )

            return self._parent._cast(
                _7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7166,
            )

            return self._parent._cast(
                _7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConicalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConicalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7070.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2748.ConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection

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
    ) -> "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation(self)
