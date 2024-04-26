"""ConnectorHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5812
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConnectorHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.system_deflections import _2751
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5713,
        _5813,
        _5833,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectorHarmonicAnalysis")


class ConnectorHarmonicAnalysis(_5812.MountableComponentHarmonicAnalysis):
    """ConnectorHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorHarmonicAnalysis")

    class _Cast_ConnectorHarmonicAnalysis:
        """Special nested class for casting ConnectorHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
            parent: "ConnectorHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5713.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.BearingHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5813.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.OilSealHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5833.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.ShaftHubConnectionHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "ConnectorHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2751.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

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
    ) -> "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis":
        return self._Cast_ConnectorHarmonicAnalysis(self)
