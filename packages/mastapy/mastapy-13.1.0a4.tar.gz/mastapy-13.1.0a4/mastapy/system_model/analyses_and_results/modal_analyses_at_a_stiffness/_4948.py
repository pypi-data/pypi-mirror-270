"""KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4913,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4951,
        _4954,
        _4940,
        _4959,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness(
    _4913.ConicalGearModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4913.ConicalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4913.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4940.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(
                _4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "_4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness(
            self
        )
