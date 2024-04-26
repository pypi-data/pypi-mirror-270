"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5338,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5214,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5342,
        _5343,
        _5304,
        _5330,
        _5368,
        _5270,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed(
    _5338.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5338.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            return self._parent._cast(
                _5338.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5304.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5330.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5270.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5342.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundModalAnalysisAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5343.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundModalAnalysisAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed(
            self
        )
