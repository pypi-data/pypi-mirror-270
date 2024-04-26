"""ZerolBevelGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ZerolBevelGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7012
    from mastapy.system_model.analyses_and_results.system_deflections import _2864
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
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
__all__ = ("ZerolBevelGearParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearParametricStudyTool")


class ZerolBevelGearParametricStudyTool(_4336.BevelGearParametricStudyTool):
    """ZerolBevelGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearParametricStudyTool")

    class _Cast_ZerolBevelGearParametricStudyTool:
        """Special nested class for casting ZerolBevelGearParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
            parent: "ZerolBevelGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4336.BevelGearParametricStudyTool":
            return self._parent._cast(_4336.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4324.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4352.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4385.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "ZerolBevelGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "ZerolBevelGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7012.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2864.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool":
        return self._Cast_ZerolBevelGearParametricStudyTool(self)
