"""SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2341
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5514
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5560,
        _5588,
        _5614,
        _5620,
        _5590,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis")


class SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis(
    _5572.BevelGearMeshCompoundMultibodyDynamicsAnalysis
):
    """SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5572.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5588.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(_5614.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(_5590.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2341.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

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
    ) -> "List[_5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis(self)
