"""BevelGearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6706,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6713,
        _6801,
        _6807,
        _6810,
        _6828,
        _6734,
        _6760,
        _6766,
        _6736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundCriticalSpeedAnalysis")


class BevelGearMeshCompoundCriticalSpeedAnalysis(
    _6706.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
):
    """BevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "BevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6706.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6706.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6734.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6760.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6766.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6736.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6713.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(
                _6713.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6801.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(
                _6801.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6807.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6807,
            )

            return self._parent._cast(
                _6807.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6810.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6810,
            )

            return self._parent._cast(
                _6810.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6828.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6828,
            )

            return self._parent._cast(
                _6828.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "BevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6586.BevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6586.BevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis(self)
