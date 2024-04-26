"""CouplingHalfCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CouplingHalfCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6592,
        _6597,
        _6614,
        _6654,
        _6660,
        _6665,
        _6676,
        _6686,
        _6687,
        _6688,
        _6691,
        _6692,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCriticalSpeedAnalysis")


class CouplingHalfCriticalSpeedAnalysis(_6649.MountableComponentCriticalSpeedAnalysis):
    """CouplingHalfCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCriticalSpeedAnalysis")

    class _Cast_CouplingHalfCriticalSpeedAnalysis:
        """Special nested class for casting CouplingHalfCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
            parent: "CouplingHalfCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6592.ClutchHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6597.ConceptCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6614.CVTPulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.CVTPulleyCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def pulley_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6660.PulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.PulleyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6665.RollingRingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.RollingRingCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6676.SpringDamperHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6676,
            )

            return self._parent._cast(_6676.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6686.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6686,
            )

            return self._parent._cast(_6686.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6687.SynchroniserPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6687,
            )

            return self._parent._cast(_6687.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6688.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6688,
            )

            return self._parent._cast(_6688.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6691.TorqueConverterPumpCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6691,
            )

            return self._parent._cast(_6691.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "_6692.TorqueConverterTurbineCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6692,
            )

            return self._parent._cast(_6692.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "CouplingHalfCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCriticalSpeedAnalysis.TYPE"
    ):
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
    ) -> "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis":
        return self._Cast_CouplingHalfCriticalSpeedAnalysis(self)
