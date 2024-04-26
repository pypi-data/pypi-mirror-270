"""WormGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "WormGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _7010
    from mastapy.system_model.analyses_and_results.system_deflections import _2859
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4391,
        _4354,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="WormGearMeshParametricStudyTool")


class WormGearMeshParametricStudyTool(_4384.GearMeshParametricStudyTool):
    """WormGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshParametricStudyTool")

    class _Cast_WormGearMeshParametricStudyTool:
        """Special nested class for casting WormGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
            parent: "WormGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_parametric_study_tool(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_4384.GearMeshParametricStudyTool":
            return self._parent._cast(_4384.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_4391.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_4354.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
        ) -> "WormGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshParametricStudyTool.TYPE"):
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
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2859.WormGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshParametricStudyTool._Cast_WormGearMeshParametricStudyTool":
        return self._Cast_WormGearMeshParametricStudyTool(self)
