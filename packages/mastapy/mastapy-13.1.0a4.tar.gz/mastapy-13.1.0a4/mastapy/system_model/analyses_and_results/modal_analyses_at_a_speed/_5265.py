"""WormGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "WormGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _7009
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5218,
        _5165,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearModalAnalysisAtASpeed")


class WormGearModalAnalysisAtASpeed(_5199.GearModalAnalysisAtASpeed):
    """WormGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearModalAnalysisAtASpeed")

    class _Cast_WormGearModalAnalysisAtASpeed:
        """Special nested class for casting WormGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
            parent: "WormGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "WormGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7009.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

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
    ) -> "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed":
        return self._Cast_WormGearModalAnalysisAtASpeed(self)
