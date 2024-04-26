"""AGMAGleasonConicalGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4330,
        _4335,
        _4388,
        _4436,
        _4442,
        _4445,
        _4463,
        _4384,
        _4391,
        _4354,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshParametricStudyTool")


class AGMAGleasonConicalGearMeshParametricStudyTool(
    _4351.ConicalGearMeshParametricStudyTool
):
    """AGMAGleasonConicalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearMeshParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
            parent: "AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4351.ConicalGearMeshParametricStudyTool":
            return self._parent._cast(_4351.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4384.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4391.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4354.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4330.BevelDifferentialGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(
                _4330.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4335.BevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.BevelGearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4388.HypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4388,
            )

            return self._parent._cast(_4388.HypoidGearMeshParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4436.SpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.SpiralBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4442.StraightBevelDiffGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(
                _4442.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4445.StraightBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4445,
            )

            return self._parent._cast(_4445.StraightBevelGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4463.ZerolBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4463,
            )

            return self._parent._cast(_4463.ZerolBevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "AGMAGleasonConicalGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2317.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearMeshParametricStudyTool(self)
