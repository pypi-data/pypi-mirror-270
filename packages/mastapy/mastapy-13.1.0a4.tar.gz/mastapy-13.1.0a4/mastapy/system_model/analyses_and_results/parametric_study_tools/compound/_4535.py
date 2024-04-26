"""KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4532,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4498,
        _4524,
        _4543,
        _4491,
        _4545,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool(
    _4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            return self._parent._cast(
                _4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4498.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4524.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4543.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4491.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6942.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4396.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4396.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool(
            self
        )
