"""OilSealSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2751
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "OilSealSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.power_flows import _4136
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
__all__ = ("OilSealSystemDeflection",)


Self = TypeVar("Self", bound="OilSealSystemDeflection")


class OilSealSystemDeflection(_2751.ConnectorSystemDeflection):
    """OilSealSystemDeflection

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealSystemDeflection")

    class _Cast_OilSealSystemDeflection:
        """Special nested class for casting OilSealSystemDeflection to subclasses."""

        def __init__(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
            parent: "OilSealSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2751.ConnectorSystemDeflection":
            return self._parent._cast(_2751.ConnectorSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def oil_seal_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "OilSealSystemDeflection":
            return self._parent

        def __getattr__(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reliability_for_oil_seal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityForOilSeal

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2484.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6953.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4136.OilSealPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.OilSealPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "OilSealSystemDeflection._Cast_OilSealSystemDeflection":
        return self._Cast_OilSealSystemDeflection(self)
