"""CylindricalGearSystemDeflectionWithLTCAResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSystemDeflectionWithLTCAResults",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _863
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2773,
        _2784,
        _2805,
        _2738,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSystemDeflectionWithLTCAResults",)


Self = TypeVar("Self", bound="CylindricalGearSystemDeflectionWithLTCAResults")


class CylindricalGearSystemDeflectionWithLTCAResults(
    _2768.CylindricalGearSystemDeflection
):
    """CylindricalGearSystemDeflectionWithLTCAResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSystemDeflectionWithLTCAResults"
    )

    class _Cast_CylindricalGearSystemDeflectionWithLTCAResults:
        """Special nested class for casting CylindricalGearSystemDeflectionWithLTCAResults to subclasses."""

        def __init__(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
            parent: "CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2768.CylindricalGearSystemDeflection":
            return self._parent._cast(_2768.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "_2773.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.CylindricalPlanetGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "CylindricalGearSystemDeflectionWithLTCAResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
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
        instance_to_wrap: "CylindricalGearSystemDeflectionWithLTCAResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_ltca_results(
        self: Self,
    ) -> "_863.CylindricalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults":
        return self._Cast_CylindricalGearSystemDeflectionWithLTCAResults(self)
