"""CouplingHalfCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4634
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4774,
        _4779,
        _4793,
        _4833,
        _4839,
        _4843,
        _4855,
        _4865,
        _4866,
        _4867,
        _4870,
        _4871,
        _4776,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysis")


class CouplingHalfCompoundModalAnalysis(_4828.MountableComponentCompoundModalAnalysis):
    """CouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysis")

    class _Cast_CouplingHalfCompoundModalAnalysis:
        """Special nested class for casting CouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
            parent: "CouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4828.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4828.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4776.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4774.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4779.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4793.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(_4793.CVTPulleyCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4833.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(
                _4833.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4839.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.PulleyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4843.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.RollingRingCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4855.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.SpringDamperHalfCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4865.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4865,
            )

            return self._parent._cast(_4865.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4866.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4866,
            )

            return self._parent._cast(_4866.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4867.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4867,
            )

            return self._parent._cast(_4867.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4870.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4870,
            )

            return self._parent._cast(_4870.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4871.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4871,
            )

            return self._parent._cast(_4871.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "CouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4634.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "List[_4634.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis":
        return self._Cast_CouplingHalfCompoundModalAnalysis(self)
