"""KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5303,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5206,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5340,
        _5343,
        _5329,
        _5335,
        _5305,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed(
    _5303.ConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5303.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5329.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(_5329.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5305.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5340.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5343.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(
                _5343.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed(
            self
        )
