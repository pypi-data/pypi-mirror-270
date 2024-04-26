"""KlingelnbergCycloPalloidConicalGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4629
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4667,
        _4666,
        _4671,
        _4674,
        _4660,
        _4705,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2792
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetModalAnalysis")


class KlingelnbergCycloPalloidConicalGearSetModalAnalysis(
    _4629.ConicalGearSetModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "_4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(
                _4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_modal_analysis(
        self: Self,
    ) -> "List[_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_gears_modal_analysis(
        self: Self,
    ) -> "List[_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis(self)
