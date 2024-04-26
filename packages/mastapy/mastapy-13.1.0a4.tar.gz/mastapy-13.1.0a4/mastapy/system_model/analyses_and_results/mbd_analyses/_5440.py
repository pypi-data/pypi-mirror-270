"""CouplingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5423,
        _5429,
        _5492,
        _5518,
        _5533,
        _5438,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionMultibodyDynamicsAnalysis")


class CouplingConnectionMultibodyDynamicsAnalysis(
    _5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """CouplingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
            parent: "CouplingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5423.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(_5423.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5429.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(
                _5429.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5492.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5518.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(
                _5518.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5533.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5533

            return self._parent._cast(
                _5533.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2364.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_CouplingConnectionMultibodyDynamicsAnalysis(self)
