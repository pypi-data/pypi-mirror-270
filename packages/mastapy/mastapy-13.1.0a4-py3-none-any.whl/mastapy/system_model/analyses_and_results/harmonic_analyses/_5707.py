"""AbstractShaftOrHousingHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftOrHousingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.system_deflections import _2709
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5706,
        _5751,
        _5776,
        _5832,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingHarmonicAnalysis")


class AbstractShaftOrHousingHarmonicAnalysis(_5731.ComponentHarmonicAnalysis):
    """AbstractShaftOrHousingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingHarmonicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingHarmonicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
            parent: "AbstractShaftOrHousingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5706.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.AbstractShaftHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5751.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.CycloidalDiscHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5776.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.FEPartHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "_5832.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.ShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
        ) -> "AbstractShaftOrHousingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2709.AbstractShaftOrHousingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection

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
    ) -> "AbstractShaftOrHousingHarmonicAnalysis._Cast_AbstractShaftOrHousingHarmonicAnalysis":
        return self._Cast_AbstractShaftOrHousingHarmonicAnalysis(self)
