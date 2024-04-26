"""SpringDamperConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SpringDamperConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2833
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5741
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionHarmonicAnalysis")


class SpringDamperConnectionHarmonicAnalysis(_5743.CouplingConnectionHarmonicAnalysis):
    """SpringDamperConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionHarmonicAnalysis"
    )

    class _Cast_SpringDamperConnectionHarmonicAnalysis:
        """Special nested class for casting SpringDamperConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
            parent: "SpringDamperConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_5743.CouplingConnectionHarmonicAnalysis":
            return self._parent._cast(_5743.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_5800.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(
                _5800.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_5741.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(_5741.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
        ) -> "SpringDamperConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6983.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2833.SpringDamperConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection

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
    ) -> "SpringDamperConnectionHarmonicAnalysis._Cast_SpringDamperConnectionHarmonicAnalysis":
        return self._Cast_SpringDamperConnectionHarmonicAnalysis(self)
