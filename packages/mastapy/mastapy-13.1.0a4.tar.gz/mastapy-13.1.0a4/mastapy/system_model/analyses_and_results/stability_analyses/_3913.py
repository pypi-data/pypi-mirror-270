"""VirtualComponentStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "VirtualComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3863,
        _3864,
        _3874,
        _3875,
        _3912,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentStabilityAnalysis")


class VirtualComponentStabilityAnalysis(_3865.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentStabilityAnalysis")

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
            parent: "VirtualComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3863.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3864.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3874.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3875.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3912.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3912,
            )

            return self._parent._cast(_3912.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "VirtualComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis":
        return self._Cast_VirtualComponentStabilityAnalysis(self)
