"""KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4667
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4820,
        _4823,
        _4809,
        _4828,
        _4776,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis")


class KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis(
    _4783.ConicalGearCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4783.ConicalGearCompoundModalAnalysis":
            return self._parent._cast(_4783.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4809.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4828.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4776.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4820.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(
                _4820.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "_4823.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(
                _4823.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis]

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
    ) -> "List[_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis(self)
