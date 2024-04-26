"""ZerolBevelGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.stability_analyses import _3917
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3925,
        _3953,
        _3979,
        _3985,
        _3955,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundStabilityAnalysis")


class ZerolBevelGearMeshCompoundStabilityAnalysis(
    _3937.BevelGearMeshCompoundStabilityAnalysis
):
    """ZerolBevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_ZerolBevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
            parent: "ZerolBevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3937.BevelGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3937.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3925.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(
                _3925.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3953.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3979.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3985.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3955.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "ZerolBevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_3917.ZerolBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearMeshStabilityAnalysis]

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
    ) -> "List[_3917.ZerolBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearMeshStabilityAnalysis]

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
    ) -> "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis(self)
