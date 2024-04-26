"""GearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5145,
        _5152,
        _5154,
        _5155,
        _5157,
        _5170,
        _5173,
        _5188,
        _5190,
        _5194,
        _5203,
        _5207,
        _5210,
        _5213,
        _5241,
        _5247,
        _5250,
        _5252,
        _5253,
        _5265,
        _5268,
        _5165,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearModalAnalysisAtASpeed")


class GearModalAnalysisAtASpeed(_5218.MountableComponentModalAnalysisAtASpeed):
    """GearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearModalAnalysisAtASpeed")

    class _Cast_GearModalAnalysisAtASpeed:
        """Special nested class for casting GearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
            parent: "GearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5152.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(
                _5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5155.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(
                _5155.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5157.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.BevelGearModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5170.ConceptGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5173.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConicalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5188.CylindricalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5190.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5194.FaceGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.FaceGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5203.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(
                _5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(
                _5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(
                _5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5241.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5247.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5250.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(_5250.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5252.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(
                _5252.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5253.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5265.WormGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5265,
            )

            return self._parent._cast(_5265.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5268.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5268,
            )

            return self._parent._cast(_5268.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "GearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed":
        return self._Cast_GearModalAnalysisAtASpeed(self)
