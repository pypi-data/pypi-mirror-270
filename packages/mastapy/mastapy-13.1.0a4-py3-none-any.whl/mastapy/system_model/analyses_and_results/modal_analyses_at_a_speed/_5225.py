"""PlanetaryGearSetModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5200,
        _5239,
        _5140,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysisAtASpeed")


class PlanetaryGearSetModalAnalysisAtASpeed(
    _5189.CylindricalGearSetModalAnalysisAtASpeed
):
    """PlanetaryGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryGearSetModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
            parent: "PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_5189.CylindricalGearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5189.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_5200.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_5239.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_5140.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "PlanetaryGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2560.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed":
        return self._Cast_PlanetaryGearSetModalAnalysisAtASpeed(self)
