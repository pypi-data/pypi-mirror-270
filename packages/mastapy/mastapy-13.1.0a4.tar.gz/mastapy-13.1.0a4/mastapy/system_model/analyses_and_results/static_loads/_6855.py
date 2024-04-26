"""BevelGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6841
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6850,
        _6981,
        _6987,
        _6990,
        _7013,
        _6873,
        _6919,
        _6938,
        _6876,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshLoadCase",)


Self = TypeVar("Self", bound="BevelGearMeshLoadCase")


class BevelGearMeshLoadCase(_6841.AGMAGleasonConicalGearMeshLoadCase):
    """BevelGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshLoadCase")

    class _Cast_BevelGearMeshLoadCase:
        """Special nested class for casting BevelGearMeshLoadCase to subclasses."""

        def __init__(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
            parent: "BevelGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6841.AGMAGleasonConicalGearMeshLoadCase":
            return self._parent._cast(_6841.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6873.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6919.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(_6919.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6850.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelDifferentialGearMeshLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6981.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6987.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6990.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_7013.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7013

            return self._parent._cast(_7013.ZerolBevelGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "BevelGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase":
        return self._Cast_BevelGearMeshLoadCase(self)
