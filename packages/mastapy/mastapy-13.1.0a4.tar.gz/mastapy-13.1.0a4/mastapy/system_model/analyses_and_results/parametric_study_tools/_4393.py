"""KlingelnbergCycloPalloidConicalGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4396,
        _4399,
        _4385,
        _4404,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearParametricStudyTool")


class KlingelnbergCycloPalloidConicalGearParametricStudyTool(
    _4352.ConicalGearParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4352.ConicalGearParametricStudyTool":
            return self._parent._cast(_4352.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4385.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4396.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(
                _4396.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4399.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(
                _4399.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool(self)
