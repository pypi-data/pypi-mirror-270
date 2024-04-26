"""CylindricalGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4659
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CylindricalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.system_deflections import _2768
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4646,
        _4681,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearModalAnalysis")


class CylindricalGearModalAnalysis(_4659.GearModalAnalysis):
    """CylindricalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearModalAnalysis")

    class _Cast_CylindricalGearModalAnalysis:
        """Special nested class for casting CylindricalGearModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
            parent: "CylindricalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4659.GearModalAnalysis":
            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4646.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.CylindricalPlanetGearModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "CylindricalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6888.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

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
    ) -> "_2768.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis":
        return self._Cast_CylindricalGearModalAnalysis(self)
