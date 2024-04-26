"""ConceptGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6919
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6938, _6876
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshLoadCase",)


Self = TypeVar("Self", bound="ConceptGearMeshLoadCase")


class ConceptGearMeshLoadCase(_6919.GearMeshLoadCase):
    """ConceptGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshLoadCase")

    class _Cast_ConceptGearMeshLoadCase:
        """Special nested class for casting ConceptGearMeshLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
            parent: "ConceptGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_6919.GearMeshLoadCase":
            return self._parent._cast(_6919.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_load_case(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase",
        ) -> "ConceptGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase":
        return self._Cast_ConceptGearMeshLoadCase(self)
