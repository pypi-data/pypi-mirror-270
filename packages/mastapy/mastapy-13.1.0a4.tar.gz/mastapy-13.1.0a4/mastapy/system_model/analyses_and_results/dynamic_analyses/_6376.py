"""KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6374,
        _6375,
        _6337,
        _6365,
        _6403,
        _6303,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis")


class KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis(
    _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            return self._parent._cast(
                _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def conical_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6365.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_conical_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6375.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6375.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis(self)
