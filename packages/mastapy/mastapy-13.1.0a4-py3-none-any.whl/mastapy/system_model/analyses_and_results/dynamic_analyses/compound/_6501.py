"""KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6467
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6504,
        _6507,
        _6493,
        _6499,
        _6469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis(
    _6467.ConicalGearMeshCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6467.ConicalGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6467.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6493.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6499.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(
                _6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(
                _6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6372.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]

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
    ) -> "List[_6372.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis(
                self
            )
        )
