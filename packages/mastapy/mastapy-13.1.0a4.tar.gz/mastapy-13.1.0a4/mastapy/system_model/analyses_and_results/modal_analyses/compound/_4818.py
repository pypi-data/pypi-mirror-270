"""KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4666
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4821,
        _4824,
        _4810,
        _4816,
        _4786,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis(
    _4784.ConicalGearMeshCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4784.ConicalGearMeshCompoundModalAnalysis":
            return self._parent._cast(_4784.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4810.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(_4810.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4816.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4786.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4821.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(
                _4821.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4824.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(
                _4824.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

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
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis(
            self
        )
