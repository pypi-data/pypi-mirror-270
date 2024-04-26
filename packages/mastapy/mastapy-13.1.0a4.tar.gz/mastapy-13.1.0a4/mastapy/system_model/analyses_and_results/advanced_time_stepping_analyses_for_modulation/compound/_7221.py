"""FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7226,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7091,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7232,
        _7202,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7226.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7226.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7226.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7232.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7202.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "List[_7091.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7091.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
