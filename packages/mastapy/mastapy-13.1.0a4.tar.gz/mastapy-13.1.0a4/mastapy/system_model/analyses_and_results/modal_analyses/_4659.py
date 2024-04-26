"""GearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4681
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "GearModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.system_deflections import _2784
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4600,
        _4607,
        _4609,
        _4610,
        _4612,
        _4625,
        _4628,
        _4644,
        _4646,
        _4653,
        _4663,
        _4667,
        _4670,
        _4673,
        _4707,
        _4713,
        _4716,
        _4718,
        _4719,
        _4734,
        _4737,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearModalAnalysis",)


Self = TypeVar("Self", bound="GearModalAnalysis")


class GearModalAnalysis(_4681.MountableComponentModalAnalysis):
    """GearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearModalAnalysis")

    class _Cast_GearModalAnalysis:
        """Special nested class for casting GearModalAnalysis to subclasses."""

        def __init__(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
            parent: "GearModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4600.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4607.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4612.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4625.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4644.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4646.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.CylindricalPlanetGearModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4653.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FaceGearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4663.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(
                _4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(
                _4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4707.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4713.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4716.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4718.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4719.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.StraightBevelSunGearModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4734.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4734

            return self._parent._cast(_4734.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "_4737.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4737

            return self._parent._cast(_4737.ZerolBevelGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "GearModalAnalysis":
            return self._parent

        def __getattr__(self: "GearModalAnalysis._Cast_GearModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2784.GearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearModalAnalysis._Cast_GearModalAnalysis":
        return self._Cast_GearModalAnalysis(self)
