"""ConicalGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4386
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConicalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4352,
        _4351,
        _4325,
        _4332,
        _4337,
        _4390,
        _4394,
        _4397,
        _4400,
        _4438,
        _4444,
        _4447,
        _4465,
        _4435,
        _4319,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearSetParametricStudyTool")


class ConicalGearSetParametricStudyTool(_4386.GearSetParametricStudyTool):
    """ConicalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetParametricStudyTool")

    class _Cast_ConicalGearSetParametricStudyTool:
        """Special nested class for casting ConicalGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
            parent: "ConicalGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4386.GearSetParametricStudyTool":
            return self._parent._cast(_4386.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4319.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4325.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(
                _4325.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4332.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4337.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.BevelGearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4390.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4394.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4397.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4400.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(
                _4400.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4438.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4444.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4447.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4465.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4465,
            )

            return self._parent._cast(_4465.ZerolBevelGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "ConicalGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConicalGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4352.ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4352.ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4351.ConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4351.ConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool":
        return self._Cast_ConicalGearSetParametricStudyTool(self)
