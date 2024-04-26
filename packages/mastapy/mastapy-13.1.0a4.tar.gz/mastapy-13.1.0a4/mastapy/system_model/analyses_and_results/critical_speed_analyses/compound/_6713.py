"""BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6718,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6581
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6706,
        _6734,
        _6760,
        _6766,
        _6736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis")


class BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis(
    _6718.BevelGearMeshCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    )

    class _Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6718.BevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6718.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6706.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(
                _6706.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6734.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6760.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6766.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6736.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6581.BevelDifferentialGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearMeshCriticalSpeedAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6581.BevelDifferentialGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearMeshCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis(self)
