"""CylindricalGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5190,
        _5218,
        _5165,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearModalAnalysisAtASpeed")


class CylindricalGearModalAnalysisAtASpeed(_5199.GearModalAnalysisAtASpeed):
    """CylindricalGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearModalAnalysisAtASpeed")

    class _Cast_CylindricalGearModalAnalysisAtASpeed:
        """Special nested class for casting CylindricalGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
            parent: "CylindricalGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5190.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "CylindricalGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CylindricalGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6888.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed":
        return self._Cast_CylindricalGearModalAnalysisAtASpeed(self)
