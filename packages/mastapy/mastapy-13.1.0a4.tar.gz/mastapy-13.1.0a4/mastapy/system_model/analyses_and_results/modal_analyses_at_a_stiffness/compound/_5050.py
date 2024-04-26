"""CouplingHalfCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5088,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4918,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5034,
        _5039,
        _5053,
        _5093,
        _5099,
        _5103,
        _5115,
        _5125,
        _5126,
        _5127,
        _5130,
        _5131,
        _5036,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtAStiffness")


class CouplingHalfCompoundModalAnalysisAtAStiffness(
    _5088.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """CouplingHalfCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingHalfCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
            parent: "CouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5088.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5039.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(_5053.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5093.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5099.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(_5099.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5103.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5115.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5125.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5125,
            )

            return self._parent._cast(
                _5125.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5126.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5126,
            )

            return self._parent._cast(
                _5126.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5127.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5127,
            )

            return self._parent._cast(
                _5127.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5130.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5130,
            )

            return self._parent._cast(
                _5130.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5131.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5131,
            )

            return self._parent._cast(
                _5131.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "CouplingHalfCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CouplingHalfCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4918.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4918.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness":
        return self._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness(self)
