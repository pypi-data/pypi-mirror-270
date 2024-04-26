"""ConicalGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4524,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConicalGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4470,
        _4477,
        _4480,
        _4481,
        _4482,
        _4528,
        _4532,
        _4535,
        _4538,
        _4565,
        _4571,
        _4574,
        _4577,
        _4578,
        _4592,
        _4543,
        _4491,
        _4545,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearCompoundParametricStudyTool")


class ConicalGearCompoundParametricStudyTool(_4524.GearCompoundParametricStudyTool):
    """ConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearCompoundParametricStudyTool"
    )

    class _Cast_ConicalGearCompoundParametricStudyTool:
        """Special nested class for casting ConicalGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
            parent: "ConicalGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4524.GearCompoundParametricStudyTool":
            return self._parent._cast(_4524.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4543.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4491.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4470.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4477.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(
                _4477.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4480.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(
                _4480.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4481.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(
                _4481.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4482.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.BevelGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4528.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(
                _4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4565.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4571.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4574.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(
                _4574.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4577.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(
                _4577.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4578.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4578,
            )

            return self._parent._cast(
                _4578.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "_4592.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4592,
            )

            return self._parent._cast(_4592.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
        ) -> "ConicalGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4352.ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4352.ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearCompoundParametricStudyTool._Cast_ConicalGearCompoundParametricStudyTool":
        return self._Cast_ConicalGearCompoundParametricStudyTool(self)
