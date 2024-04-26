"""KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4948,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4913,
        _4940,
        _4959,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness(
    _4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4913.ConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4940.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness(
                self
            )
        )
