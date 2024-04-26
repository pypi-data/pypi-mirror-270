"""StraightBevelPlanetGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4443
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "StraightBevelPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4336,
        _4324,
        _4352,
        _4385,
        _4404,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearParametricStudyTool")


class StraightBevelPlanetGearParametricStudyTool(
    _4443.StraightBevelDiffGearParametricStudyTool
):
    """StraightBevelPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearParametricStudyTool"
    )

    class _Cast_StraightBevelPlanetGearParametricStudyTool:
        """Special nested class for casting StraightBevelPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
            parent: "StraightBevelPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4443.StraightBevelDiffGearParametricStudyTool":
            return self._parent._cast(_4443.StraightBevelDiffGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4336.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4324.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4352.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4385.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "StraightBevelPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool":
        return self._Cast_StraightBevelPlanetGearParametricStudyTool(self)
