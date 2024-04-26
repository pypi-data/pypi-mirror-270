"""AGMAGleasonConicalGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AGMAGleasonConicalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.system_deflections import _2714
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4607,
        _4609,
        _4610,
        _4612,
        _4663,
        _4707,
        _4713,
        _4716,
        _4718,
        _4719,
        _4737,
        _4659,
        _4681,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysis")


class AGMAGleasonConicalGearModalAnalysis(_4628.ConicalGearModalAnalysis):
    """AGMAGleasonConicalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysis")

    class _Cast_AGMAGleasonConicalGearModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
            parent: "AGMAGleasonConicalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4607.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4612.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4663.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.HypoidGearModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4707.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4713.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4716.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4718.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4719.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.StraightBevelSunGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "_4737.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4737

            return self._parent._cast(_4737.ZerolBevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "AGMAGleasonConicalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

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
    ) -> (
        "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis"
    ):
        return self._Cast_AGMAGleasonConicalGearModalAnalysis(self)
