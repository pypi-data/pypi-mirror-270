"""BevelDifferentialGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5157
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6849
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5154,
        _5155,
        _5145,
        _5173,
        _5199,
        _5218,
        _5165,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialGearModalAnalysisAtASpeed")


class BevelDifferentialGearModalAnalysisAtASpeed(_5157.BevelGearModalAnalysisAtASpeed):
    """BevelDifferentialGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialGearModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
            parent: "BevelDifferentialGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5157.BevelGearModalAnalysisAtASpeed":
            return self._parent._cast(_5157.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5173.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(
                _5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "_5155.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(
                _5155.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
        ) -> "BevelDifferentialGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6849.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearModalAnalysisAtASpeed._Cast_BevelDifferentialGearModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialGearModalAnalysisAtASpeed(self)
