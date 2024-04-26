"""ZerolBevelGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2730
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ZerolBevelGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7014
    from mastapy.gears.rating.zerol_bevel import _378
    from mastapy.system_model.analyses_and_results.power_flows import _4189
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2864,
        _2862,
        _2713,
        _2748,
        _2783,
        _2829,
        _2708,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearSetSystemDeflection")


class ZerolBevelGearSetSystemDeflection(_2730.BevelGearSetSystemDeflection):
    """ZerolBevelGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetSystemDeflection")

    class _Cast_ZerolBevelGearSetSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
            parent: "ZerolBevelGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2730.BevelGearSetSystemDeflection":
            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
        ) -> "ZerolBevelGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2572.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7014.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_378.ZerolBevelGearSetRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_378.ZerolBevelGearSetRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4189.ZerolBevelGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_system_deflection(
        self: Self,
    ) -> "List[_2864.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_system_deflection(
        self: Self,
    ) -> "List[_2864.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_system_deflection(
        self: Self,
    ) -> "List[_2862.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_system_deflection(
        self: Self,
    ) -> "List[_2862.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection":
        return self._Cast_ZerolBevelGearSetSystemDeflection(self)
