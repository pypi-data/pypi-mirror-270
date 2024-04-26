"""WormGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "WormGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _7009
    from mastapy.system_model.analyses_and_results.system_deflections import _2861
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4404,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearParametricStudyTool",)


Self = TypeVar("Self", bound="WormGearParametricStudyTool")


class WormGearParametricStudyTool(_4385.GearParametricStudyTool):
    """WormGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearParametricStudyTool")

    class _Cast_WormGearParametricStudyTool:
        """Special nested class for casting WormGearParametricStudyTool to subclasses."""

        def __init__(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
            parent: "WormGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_parametric_study_tool(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_4385.GearParametricStudyTool":
            return self._parent._cast(_4385.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_parametric_study_tool(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
        ) -> "WormGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7009.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

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
    ) -> "List[_2861.WormGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection]

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
    ) -> "WormGearParametricStudyTool._Cast_WormGearParametricStudyTool":
        return self._Cast_WormGearParametricStudyTool(self)
