"""KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5207,
        _5206,
        _5211,
        _5214,
        _5200,
        _5239,
        _5140,
        _5220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed(
    _5174.ConicalGearSetModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5174.ConicalGearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5174.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5200.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5239.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5140.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5211.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(
                _5211.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(
                _5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed(
            self
        )
