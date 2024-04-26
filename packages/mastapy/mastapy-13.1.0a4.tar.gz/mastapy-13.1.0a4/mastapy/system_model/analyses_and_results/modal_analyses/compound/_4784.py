"""ConicalGearMeshCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4810
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConicalGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4627
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4756,
        _4763,
        _4768,
        _4814,
        _4818,
        _4821,
        _4824,
        _4851,
        _4857,
        _4860,
        _4878,
        _4816,
        _4786,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundModalAnalysis")


class ConicalGearMeshCompoundModalAnalysis(_4810.GearMeshCompoundModalAnalysis):
    """ConicalGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshCompoundModalAnalysis")

    class _Cast_ConicalGearMeshCompoundModalAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
            parent: "ConicalGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4810.GearMeshCompoundModalAnalysis":
            return self._parent._cast(_4810.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4816.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4786.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4756.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(
                _4756.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4763.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(
                _4763.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4768.BevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.BevelGearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4814.HypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4818.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(
                _4818.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4821.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(
                _4821.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4824.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(
                _4824.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4851.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4857.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(
                _4857.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4860.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4860,
            )

            return self._parent._cast(_4860.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "_4878.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4878,
            )

            return self._parent._cast(_4878.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
        ) -> "ConicalGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearMeshCompoundModalAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4627.ConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis]

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
    ) -> "List[_4627.ConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis]

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
    ) -> "ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis":
        return self._Cast_ConicalGearMeshCompoundModalAnalysis(self)
