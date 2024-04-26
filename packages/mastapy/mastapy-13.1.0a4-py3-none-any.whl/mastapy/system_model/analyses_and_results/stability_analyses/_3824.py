"""CouplingHalfStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3808,
        _3813,
        _3828,
        _3869,
        _3876,
        _3881,
        _3891,
        _3904,
        _3905,
        _3906,
        _3909,
        _3911,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfStabilityAnalysis")


class CouplingHalfStabilityAnalysis(_3865.MountableComponentStabilityAnalysis):
    """CouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfStabilityAnalysis")

    class _Cast_CouplingHalfStabilityAnalysis:
        """Special nested class for casting CouplingHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            parent: "CouplingHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3808.ClutchHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3813.ConceptCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.ConceptCouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3828.CVTPulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.CVTPulleyStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3869.PartToPartShearCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(
                _3869.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3876.PulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.PulleyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3881.RollingRingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.RollingRingStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3891.SpringDamperHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.SpringDamperHalfStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3904.SynchroniserHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3904,
            )

            return self._parent._cast(_3904.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3905.SynchroniserPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3905,
            )

            return self._parent._cast(_3905.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3906.SynchroniserSleeveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3906,
            )

            return self._parent._cast(_3906.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3909.TorqueConverterPumpStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3909,
            )

            return self._parent._cast(_3909.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "_3911.TorqueConverterTurbineStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3911,
            )

            return self._parent._cast(_3911.TorqueConverterTurbineStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "CouplingHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis":
        return self._Cast_CouplingHalfStabilityAnalysis(self)
