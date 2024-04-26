"""FaceGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "FaceGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.modal_analyses import _4653
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4828,
        _4776,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="FaceGearCompoundModalAnalysis")


class FaceGearCompoundModalAnalysis(_4809.GearCompoundModalAnalysis):
    """FaceGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearCompoundModalAnalysis")

    class _Cast_FaceGearCompoundModalAnalysis:
        """Special nested class for casting FaceGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
            parent: "FaceGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_4809.GearCompoundModalAnalysis":
            return self._parent._cast(_4809.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_4828.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_4776.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
        ) -> "FaceGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

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
    ) -> "List[_4653.FaceGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4653.FaceGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis]

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
    ) -> "FaceGearCompoundModalAnalysis._Cast_FaceGearCompoundModalAnalysis":
        return self._Cast_FaceGearCompoundModalAnalysis(self)
