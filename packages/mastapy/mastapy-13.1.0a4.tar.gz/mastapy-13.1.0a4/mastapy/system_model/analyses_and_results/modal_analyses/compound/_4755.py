"""AGMAGleasonConicalGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4600
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4762,
        _4765,
        _4766,
        _4767,
        _4813,
        _4850,
        _4856,
        _4859,
        _4862,
        _4863,
        _4877,
        _4809,
        _4828,
        _4776,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundModalAnalysis")


class AGMAGleasonConicalGearCompoundModalAnalysis(
    _4783.ConicalGearCompoundModalAnalysis
):
    """AGMAGleasonConicalGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
            parent: "AGMAGleasonConicalGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4783.ConicalGearCompoundModalAnalysis":
            return self._parent._cast(_4783.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4809.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4828.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4776.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4762.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4765.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(
                _4765.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4766.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(
                _4766.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4767.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.BevelGearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4813.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.HypoidGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4850.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4856.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4859.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4859,
            )

            return self._parent._cast(_4859.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4862.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4862,
            )

            return self._parent._cast(
                _4862.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4863.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4863,
            )

            return self._parent._cast(_4863.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4877.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4877,
            )

            return self._parent._cast(_4877.ZerolBevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4600.AGMAGleasonConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis]

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
    ) -> "List[_4600.AGMAGleasonConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundModalAnalysis(self)
