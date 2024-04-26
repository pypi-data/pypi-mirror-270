"""KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4667
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.system_deflections import _2799
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4628,
        _4659,
        _4681,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis")


class KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis(
    _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis(self)
