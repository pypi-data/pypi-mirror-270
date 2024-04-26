"""CouplingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3807,
        _3812,
        _3868,
        _3890,
        _3908,
        _3821,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionStabilityAnalysis")


class CouplingConnectionStabilityAnalysis(
    _3853.InterMountableComponentConnectionStabilityAnalysis
):
    """CouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionStabilityAnalysis")

    class _Cast_CouplingConnectionStabilityAnalysis:
        """Special nested class for casting CouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
            parent: "CouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3853.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3853.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3821.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3807.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3812.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3868.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(
                _3868.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def spring_damper_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3890.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.SpringDamperConnectionStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3908.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3908,
            )

            return self._parent._cast(_3908.TorqueConverterConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "CouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionStabilityAnalysis.TYPE"
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
    ) -> (
        "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis"
    ):
        return self._Cast_CouplingConnectionStabilityAnalysis(self)
