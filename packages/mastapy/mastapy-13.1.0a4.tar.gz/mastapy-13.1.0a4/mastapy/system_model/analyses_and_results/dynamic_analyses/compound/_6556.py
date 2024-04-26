"""VirtualComponentCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "VirtualComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6427
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6509,
        _6510,
        _6520,
        _6521,
        _6555,
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundDynamicAnalysis")


class VirtualComponentCompoundDynamicAnalysis(
    _6511.MountableComponentCompoundDynamicAnalysis
):
    """VirtualComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundDynamicAnalysis"
    )

    class _Cast_VirtualComponentCompoundDynamicAnalysis:
        """Special nested class for casting VirtualComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
            parent: "VirtualComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6509.MassDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6510.MeasurementComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(_6510.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6520.PointLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6521.PowerLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.PowerLoadCompoundDynamicAnalysis)

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "_6555.UnbalancedMassCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6555,
            )

            return self._parent._cast(_6555.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "VirtualComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6427.VirtualComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis]

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
    ) -> "List[_6427.VirtualComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis]

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
    ) -> "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis":
        return self._Cast_VirtualComponentCompoundDynamicAnalysis(self)
