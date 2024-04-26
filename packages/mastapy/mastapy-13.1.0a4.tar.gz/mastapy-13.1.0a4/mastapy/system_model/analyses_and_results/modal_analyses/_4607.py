"""BevelDifferentialGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelDifferentialGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6849
    from mastapy.system_model.analyses_and_results.system_deflections import _2726
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4609,
        _4610,
        _4600,
        _4628,
        _4659,
        _4681,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearModalAnalysis")


class BevelDifferentialGearModalAnalysis(_4612.BevelGearModalAnalysis):
    """BevelDifferentialGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearModalAnalysis")

    class _Cast_BevelDifferentialGearModalAnalysis:
        """Special nested class for casting BevelDifferentialGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
            parent: "BevelDifferentialGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4612.BevelGearModalAnalysis":
            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4600.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
        ) -> "BevelDifferentialGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6849.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "_2726.BevelDifferentialGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection

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
    ) -> "BevelDifferentialGearModalAnalysis._Cast_BevelDifferentialGearModalAnalysis":
        return self._Cast_BevelDifferentialGearModalAnalysis(self)
