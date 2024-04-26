"""ConicalGearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConicalGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6439,
        _6446,
        _6451,
        _6497,
        _6501,
        _6504,
        _6507,
        _6534,
        _6540,
        _6543,
        _6561,
        _6499,
        _6469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundDynamicAnalysis")


class ConicalGearMeshCompoundDynamicAnalysis(_6493.GearMeshCompoundDynamicAnalysis):
    """ConicalGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundDynamicAnalysis"
    )

    class _Cast_ConicalGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
            parent: "ConicalGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6493.GearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6493.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6499.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(
                _6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6446.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(
                _6446.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6451.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6497.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(
                _6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(
                _6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6534.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6543.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(
                _6543.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6561.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6561,
            )

            return self._parent._cast(_6561.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
        ) -> "ConicalGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearMeshCompoundDynamicAnalysis]

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
    ) -> "List[_6336.ConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis]

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
    ) -> "List[_6336.ConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis]

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
    ) -> "ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis":
        return self._Cast_ConicalGearMeshCompoundDynamicAnalysis(self)
