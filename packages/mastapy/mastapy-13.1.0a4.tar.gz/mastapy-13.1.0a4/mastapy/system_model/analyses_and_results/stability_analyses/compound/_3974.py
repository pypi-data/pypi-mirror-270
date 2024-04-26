"""FaceGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "FaceGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.stability_analyses import _3841
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3985,
        _3955,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshCompoundStabilityAnalysis")


class FaceGearMeshCompoundStabilityAnalysis(_3979.GearMeshCompoundStabilityAnalysis):
    """FaceGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_FaceGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting FaceGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
            parent: "FaceGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_stability_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_3979.GearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3979.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_3985.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_3955.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
        ) -> "FaceGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2329.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2329.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

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
    ) -> "List[_3841.FaceGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearMeshStabilityAnalysis]

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
    ) -> "List[_3841.FaceGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearMeshStabilityAnalysis]

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
    ) -> "FaceGearMeshCompoundStabilityAnalysis._Cast_FaceGearMeshCompoundStabilityAnalysis":
        return self._Cast_FaceGearMeshCompoundStabilityAnalysis(self)
