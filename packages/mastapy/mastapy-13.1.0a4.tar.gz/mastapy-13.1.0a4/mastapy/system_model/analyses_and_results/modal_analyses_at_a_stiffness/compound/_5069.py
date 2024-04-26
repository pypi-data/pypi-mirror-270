"""GearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5088,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "GearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4940,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5015,
        _5022,
        _5025,
        _5026,
        _5027,
        _5040,
        _5043,
        _5058,
        _5061,
        _5064,
        _5073,
        _5077,
        _5080,
        _5083,
        _5110,
        _5116,
        _5119,
        _5122,
        _5123,
        _5134,
        _5137,
        _5036,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearCompoundModalAnalysisAtAStiffness")


class GearCompoundModalAnalysisAtAStiffness(
    _5088.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """GearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_GearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
            parent: "GearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5088.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(
                _5025.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(
                _5026.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(_5027.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5040.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(_5064.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(_5073.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5077.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(
                _5077.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5080.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5083.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(
                _5083.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5110.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5116.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5119.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5119,
            )

            return self._parent._cast(
                _5119.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5122.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5122,
            )

            return self._parent._cast(
                _5122.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5123.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5123,
            )

            return self._parent._cast(
                _5123.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5134.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5134,
            )

            return self._parent._cast(_5134.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "_5137.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5137,
            )

            return self._parent._cast(
                _5137.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "GearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "GearCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4940.GearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearModalAnalysisAtAStiffness]

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
    ) -> "List[_4940.GearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearModalAnalysisAtAStiffness]

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
    ) -> "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness":
        return self._Cast_GearCompoundModalAnalysisAtAStiffness(self)
