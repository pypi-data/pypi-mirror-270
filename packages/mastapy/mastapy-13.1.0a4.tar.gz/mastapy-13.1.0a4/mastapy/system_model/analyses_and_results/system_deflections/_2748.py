"""ConicalGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2749,
        _2747,
        _2713,
        _2725,
        _2730,
        _2787,
        _2792,
        _2795,
        _2798,
        _2831,
        _2837,
        _2840,
        _2863,
        _2829,
        _2708,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4089
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSetSystemDeflection")


class ConicalGearSetSystemDeflection(_2783.GearSetSystemDeflection):
    """ConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetSystemDeflection")

    class _Cast_ConicalGearSetSystemDeflection:
        """Special nested class for casting ConicalGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
            parent: "ConicalGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2783.GearSetSystemDeflection":
            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "ConicalGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetSystemDeflection.TYPE"):
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
    def gears_system_deflection(
        self: Self,
    ) -> "List[_2749.ConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_system_deflection(
        self: Self,
    ) -> "List[_2749.ConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_system_deflection(
        self: Self,
    ) -> "List[_2747.ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_system_deflection(
        self: Self,
    ) -> "List[_2747.ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4089.ConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection":
        return self._Cast_ConicalGearSetSystemDeflection(self)
