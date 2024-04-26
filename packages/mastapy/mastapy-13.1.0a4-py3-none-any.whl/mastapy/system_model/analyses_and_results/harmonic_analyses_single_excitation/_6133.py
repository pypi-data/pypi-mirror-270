"""ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6037,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2313
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6058,
        _6078,
        _6119,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


class ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = (
        _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6037.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
