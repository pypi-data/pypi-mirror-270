"""CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6002,
        _5908,
        _5940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
    _5929.CoaxialConnectionCompoundHarmonicAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5929.CoaxialConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5929.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_6002.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(
                _6002.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5908.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(
                _5908.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5940.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5750.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5750.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
            self
        )
