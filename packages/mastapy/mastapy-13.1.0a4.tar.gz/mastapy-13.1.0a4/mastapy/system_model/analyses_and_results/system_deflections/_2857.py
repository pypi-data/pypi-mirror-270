"""UnbalancedMassSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "UnbalancedMassSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2495
    from mastapy.system_model.analyses_and_results.static_loads import _7007
    from mastapy.system_model.analyses_and_results.power_flows import _4182
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2805,
        _2738,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassSystemDeflection",)


Self = TypeVar("Self", bound="UnbalancedMassSystemDeflection")


class UnbalancedMassSystemDeflection(_2858.VirtualComponentSystemDeflection):
    """UnbalancedMassSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassSystemDeflection")

    class _Cast_UnbalancedMassSystemDeflection:
        """Special nested class for casting UnbalancedMassSystemDeflection to subclasses."""

        def __init__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            parent: "UnbalancedMassSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2858.VirtualComponentSystemDeflection":
            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def unbalanced_mass_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "UnbalancedMassSystemDeflection":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2495.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7007.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4182.UnbalancedMassPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow

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
    ) -> "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection":
        return self._Cast_UnbalancedMassSystemDeflection(self)
