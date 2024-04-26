"""WormGearMeshModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4658
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "WormGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _7010
    from mastapy.system_model.analyses_and_results.system_deflections import _2859
    from mastapy.system_model.analyses_and_results.modal_analyses import _4665, _4630
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshModalAnalysis")


class WormGearMeshModalAnalysis(_4658.GearMeshModalAnalysis):
    """WormGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshModalAnalysis")

    class _Cast_WormGearMeshModalAnalysis:
        """Special nested class for casting WormGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
            parent: "WormGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_4658.GearMeshModalAnalysis":
            return self._parent._cast(_4658.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_4665.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_4630.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis",
        ) -> "WormGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7010.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2859.WormGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshModalAnalysis._Cast_WormGearMeshModalAnalysis":
        return self._Cast_WormGearMeshModalAnalysis(self)
