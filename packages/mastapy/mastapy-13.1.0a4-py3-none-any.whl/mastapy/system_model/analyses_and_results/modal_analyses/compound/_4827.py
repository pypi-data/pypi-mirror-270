"""MeasurementComponentCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4873
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "MeasurementComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.modal_analyses import _4676
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4828,
        _4776,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundModalAnalysis")


class MeasurementComponentCompoundModalAnalysis(
    _4873.VirtualComponentCompoundModalAnalysis
):
    """MeasurementComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundModalAnalysis"
    )

    class _Cast_MeasurementComponentCompoundModalAnalysis:
        """Special nested class for casting MeasurementComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
            parent: "MeasurementComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_4873.VirtualComponentCompoundModalAnalysis":
            return self._parent._cast(_4873.VirtualComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_4828.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_4776.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
        ) -> "MeasurementComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4676.MeasurementComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4676.MeasurementComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentCompoundModalAnalysis._Cast_MeasurementComponentCompoundModalAnalysis":
        return self._Cast_MeasurementComponentCompoundModalAnalysis(self)
