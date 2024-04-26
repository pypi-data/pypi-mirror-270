"""AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5940
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5929,
        _5949,
        _5951,
        _5988,
        _6002,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
)


class AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis(
    _5940.ConnectionCompoundHarmonicAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5940.ConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5940.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5929.CoaxialConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5949.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5951.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(
                _5951.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5988.PlanetaryConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(_5988.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_6002.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(
                _6002.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5708.AbstractShaftToMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5708.AbstractShaftToMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis(
            self
        )
