"""AGMAGleasonConicalGearMeshCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4499,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4323
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4478,
        _4483,
        _4529,
        _4566,
        _4572,
        _4575,
        _4593,
        _4525,
        _4531,
        _4501,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundParametricStudyTool")


class AGMAGleasonConicalGearMeshCompoundParametricStudyTool(
    _4499.ConicalGearMeshCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
            parent: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4499.ConicalGearMeshCompoundParametricStudyTool":
            return self._parent._cast(_4499.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4525.GearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(_4525.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4531.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(
                _4531.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4501.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4478.BevelDifferentialGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(
                _4478.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4483.BevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.BevelGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4529.HypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4566.SpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(
                _4566.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4572.StraightBevelDiffGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4572,
            )

            return self._parent._cast(
                _4572.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4575.StraightBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4575,
            )

            return self._parent._cast(
                _4575.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4593.ZerolBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4593,
            )

            return self._parent._cast(
                _4593.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4323.AGMAGleasonConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4323.AGMAGleasonConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool(self)
