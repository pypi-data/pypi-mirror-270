"""CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6189,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6078,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6262,
        _6168,
        _6200,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6189.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6189.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6189.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6262.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6168.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6168,
            )

            return self._parent._cast(
                _6168.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
