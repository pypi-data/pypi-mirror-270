"""PointLoadAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PointLoadAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PointLoadAdvancedSystemDeflection")


class PointLoadAdvancedSystemDeflection(_7425.VirtualComponentAdvancedSystemDeflection):
    """PointLoadAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadAdvancedSystemDeflection")

    class _Cast_PointLoadAdvancedSystemDeflection:
        """Special nested class for casting PointLoadAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
            parent: "PointLoadAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7425.VirtualComponentAdvancedSystemDeflection":
            return self._parent._cast(_7425.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def point_load_advanced_system_deflection(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
        ) -> "PointLoadAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PointLoadAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

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
    ) -> "List[_2814.PointLoadSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection":
        return self._Cast_PointLoadAdvancedSystemDeflection(self)
