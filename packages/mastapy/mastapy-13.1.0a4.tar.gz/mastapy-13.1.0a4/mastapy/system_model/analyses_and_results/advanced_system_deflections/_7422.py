"""TorqueConverterTurbineAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7339
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TorqueConverterTurbineAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2633
    from mastapy.system_model.analyses_and_results.static_loads import _7002
    from mastapy.system_model.analyses_and_results.system_deflections import _2854
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineAdvancedSystemDeflection")


class TorqueConverterTurbineAdvancedSystemDeflection(
    _7339.CouplingHalfAdvancedSystemDeflection
):
    """TorqueConverterTurbineAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineAdvancedSystemDeflection"
    )

    class _Cast_TorqueConverterTurbineAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
            parent: "TorqueConverterTurbineAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "TorqueConverterTurbineAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
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
        instance_to_wrap: "TorqueConverterTurbineAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2633.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7002.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "List[_2854.TorqueConverterTurbineSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection]

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
    ) -> "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection":
        return self._Cast_TorqueConverterTurbineAdvancedSystemDeflection(self)
