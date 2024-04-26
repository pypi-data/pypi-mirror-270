"""BevelGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4325
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4336,
        _4335,
        _4332,
        _4438,
        _4444,
        _4447,
        _4465,
        _4353,
        _4386,
        _4435,
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="BevelGearSetParametricStudyTool")


class BevelGearSetParametricStudyTool(
    _4325.AGMAGleasonConicalGearSetParametricStudyTool
):
    """BevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetParametricStudyTool")

    class _Cast_BevelGearSetParametricStudyTool:
        """Special nested class for casting BevelGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
            parent: "BevelGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4325.AGMAGleasonConicalGearSetParametricStudyTool":
            return self._parent._cast(
                _4325.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4353.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4386.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4332.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialGearSetParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4438.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4444.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4447.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "_4465.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4465,
            )

            return self._parent._cast(_4465.ZerolBevelGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "BevelGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2538.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4336.BevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4336.BevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4335.BevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4335.BevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool":
        return self._Cast_BevelGearSetParametricStudyTool(self)
