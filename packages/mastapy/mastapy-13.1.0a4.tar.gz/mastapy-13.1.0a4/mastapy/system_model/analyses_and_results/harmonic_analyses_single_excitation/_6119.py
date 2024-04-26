"""PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6133,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2305
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6037,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetaryConnectionHarmonicAnalysisOfSingleExcitation")


class PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(
    _6133.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6133.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6959.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(self)
