"""KlingelnbergCycloPalloidConicalGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6374,
        _6377,
        _6363,
        _6382,
        _6328,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearDynamicAnalysis")


class KlingelnbergCycloPalloidConicalGearDynamicAnalysis(
    _6335.ConicalGearDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(
                _6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "_6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(
                _6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearDynamicAnalysis.TYPE",
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
    ) -> "KlingelnbergCycloPalloidConicalGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearDynamicAnalysis(self)
