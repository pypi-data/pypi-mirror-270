"""RollingRingAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7339
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "RollingRingAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.static_loads import _6974
    from mastapy.system_model.analyses_and_results.system_deflections import _2822
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAdvancedSystemDeflection")


class RollingRingAdvancedSystemDeflection(_7339.CouplingHalfAdvancedSystemDeflection):
    """RollingRingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAdvancedSystemDeflection")

    class _Cast_RollingRingAdvancedSystemDeflection:
        """Special nested class for casting RollingRingAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
            parent: "RollingRingAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
        ) -> "RollingRingAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6974.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2822.RollingRingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[RollingRingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RollingRingAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "RollingRingAdvancedSystemDeflection._Cast_RollingRingAdvancedSystemDeflection"
    ):
        return self._Cast_RollingRingAdvancedSystemDeflection(self)
