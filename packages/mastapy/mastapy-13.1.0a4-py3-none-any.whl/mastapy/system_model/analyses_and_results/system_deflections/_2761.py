"""CycloidalDiscSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CycloidalDiscSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.power_flows import _4101
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2709,
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
__all__ = ("CycloidalDiscSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalDiscSystemDeflection")


class CycloidalDiscSystemDeflection(_2710.AbstractShaftSystemDeflection):
    """CycloidalDiscSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscSystemDeflection")

    class _Cast_CycloidalDiscSystemDeflection:
        """Special nested class for casting CycloidalDiscSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
            parent: "CycloidalDiscSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_system_deflection(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2710.AbstractShaftSystemDeflection":
            return self._parent._cast(_2710.AbstractShaftSystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2709.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.AbstractShaftOrHousingSystemDeflection)

        @property
        def component_system_deflection(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_system_deflection(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
        ) -> "CycloidalDiscSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6886.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4101.CycloidalDiscPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CycloidalDiscPowerFlow

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
    ) -> "CycloidalDiscSystemDeflection._Cast_CycloidalDiscSystemDeflection":
        return self._Cast_CycloidalDiscSystemDeflection(self)
