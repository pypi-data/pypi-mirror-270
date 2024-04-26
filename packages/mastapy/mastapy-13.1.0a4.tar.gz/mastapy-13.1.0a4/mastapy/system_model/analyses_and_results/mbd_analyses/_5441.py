"""CouplingHalfMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5424,
        _5430,
        _5445,
        _5493,
        _5500,
        _5505,
        _5519,
        _5529,
        _5531,
        _5532,
        _5536,
        _5538,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfMultibodyDynamicsAnalysis")


class CouplingHalfMultibodyDynamicsAnalysis(
    _5488.MountableComponentMultibodyDynamicsAnalysis
):
    """CouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
            parent: "CouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5424.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5430.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(
                _5430.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5445.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5500.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.PulleyMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5505.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(_5505.RollingRingMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5519.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5529.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5531.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5531

            return self._parent._cast(_5531.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5532.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5532

            return self._parent._cast(_5532.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5536.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5536

            return self._parent._cast(
                _5536.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5538.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5538

            return self._parent._cast(
                _5538.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfMultibodyDynamicsAnalysis.TYPE"
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
    ) -> "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfMultibodyDynamicsAnalysis(self)
