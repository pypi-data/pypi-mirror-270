"""ExternalCADModelSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ExternalCADModelSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.power_flows import _4108
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelSystemDeflection",)


Self = TypeVar("Self", bound="ExternalCADModelSystemDeflection")


class ExternalCADModelSystemDeflection(_2738.ComponentSystemDeflection):
    """ExternalCADModelSystemDeflection

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelSystemDeflection")

    class _Cast_ExternalCADModelSystemDeflection:
        """Special nested class for casting ExternalCADModelSystemDeflection to subclasses."""

        def __init__(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
            parent: "ExternalCADModelSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_system_deflection(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
        ) -> "ExternalCADModelSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6910.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4108.ExternalCADModelPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ExternalCADModelPowerFlow

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
    ) -> "ExternalCADModelSystemDeflection._Cast_ExternalCADModelSystemDeflection":
        return self._Cast_ExternalCADModelSystemDeflection(self)
