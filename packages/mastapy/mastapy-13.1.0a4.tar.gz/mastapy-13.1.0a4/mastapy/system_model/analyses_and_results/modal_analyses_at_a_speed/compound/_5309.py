"""CouplingHalfCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5347,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5178,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5293,
        _5298,
        _5312,
        _5352,
        _5358,
        _5362,
        _5374,
        _5384,
        _5385,
        _5386,
        _5389,
        _5390,
        _5295,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtASpeed")


class CouplingHalfCompoundModalAnalysisAtASpeed(
    _5347.MountableComponentCompoundModalAnalysisAtASpeed
):
    """CouplingHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CouplingHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
            parent: "CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5347.MountableComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5347.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5295.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(_5295.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5298.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5312.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(_5312.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5352.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5358.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(_5358.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5362.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(_5362.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5374.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5384.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5384,
            )

            return self._parent._cast(
                _5384.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5385.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5385,
            )

            return self._parent._cast(
                _5385.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5386.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5386,
            )

            return self._parent._cast(
                _5386.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5389.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5389,
            )

            return self._parent._cast(
                _5389.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5390.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5390,
            )

            return self._parent._cast(
                _5390.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5178.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5178.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_CouplingHalfCompoundModalAnalysisAtASpeed(self)
