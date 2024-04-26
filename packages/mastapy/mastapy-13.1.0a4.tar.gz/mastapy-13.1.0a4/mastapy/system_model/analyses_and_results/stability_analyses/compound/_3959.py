"""CouplingHalfCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CouplingHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3824
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3943,
        _3948,
        _3962,
        _4002,
        _4008,
        _4012,
        _4024,
        _4034,
        _4035,
        _4036,
        _4039,
        _4040,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundStabilityAnalysis")


class CouplingHalfCompoundStabilityAnalysis(
    _3997.MountableComponentCompoundStabilityAnalysis
):
    """CouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundStabilityAnalysis"
    )

    class _Cast_CouplingHalfCompoundStabilityAnalysis:
        """Special nested class for casting CouplingHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
            parent: "CouplingHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3943.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3948.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(
                _3948.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_3962.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(_3962.CVTPulleyCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4008.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.PulleyCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4012.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.RollingRingCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4024.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4034.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4034,
            )

            return self._parent._cast(_4034.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4035.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4035,
            )

            return self._parent._cast(_4035.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4036.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4036,
            )

            return self._parent._cast(_4036.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4039.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4039,
            )

            return self._parent._cast(
                _4039.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "_4040.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4040,
            )

            return self._parent._cast(
                _4040.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "CouplingHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3824.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    ) -> "List[_3824.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    ) -> "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis":
        return self._Cast_CouplingHalfCompoundStabilityAnalysis(self)
