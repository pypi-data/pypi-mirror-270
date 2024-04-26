"""TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.static_loads import _6999
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6100,
        _6069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation"
)


class TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation(
    _6071.CouplingConnectionHarmonicAnalysisOfSingleExcitation
):
    """TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6071.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6999.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
