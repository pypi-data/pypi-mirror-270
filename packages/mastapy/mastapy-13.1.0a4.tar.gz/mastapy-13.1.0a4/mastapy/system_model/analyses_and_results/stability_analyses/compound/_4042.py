"""VirtualComponentCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "VirtualComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3913
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3995,
        _3996,
        _4006,
        _4007,
        _4041,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundStabilityAnalysis")


class VirtualComponentCompoundStabilityAnalysis(
    _3997.MountableComponentCompoundStabilityAnalysis
):
    """VirtualComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundStabilityAnalysis"
    )

    class _Cast_VirtualComponentCompoundStabilityAnalysis:
        """Special nested class for casting VirtualComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
            parent: "VirtualComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3995.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3996.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(
                _3996.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def point_load_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_4006.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_4007.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.PowerLoadCompoundStabilityAnalysis)

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_4041.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4041,
            )

            return self._parent._cast(_4041.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "VirtualComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3913.VirtualComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.VirtualComponentStabilityAnalysis]

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
    ) -> "List[_3913.VirtualComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.VirtualComponentStabilityAnalysis]

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
    ) -> "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis":
        return self._Cast_VirtualComponentCompoundStabilityAnalysis(self)
