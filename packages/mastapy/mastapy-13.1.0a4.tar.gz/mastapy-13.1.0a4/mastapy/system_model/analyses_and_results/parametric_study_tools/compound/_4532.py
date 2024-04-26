"""KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4498,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4535,
        _4538,
        _4524,
        _4543,
        _4491,
        _4545,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool(
    _4498.ConicalGearCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4498.ConicalGearCompoundParametricStudyTool":
            return self._parent._cast(_4498.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4524.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4543.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4491.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "_4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4393.KlingelnbergCycloPalloidConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearParametricStudyTool]

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
    ) -> "List[_4393.KlingelnbergCycloPalloidConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearParametricStudyTool]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool(
                self
            )
        )
