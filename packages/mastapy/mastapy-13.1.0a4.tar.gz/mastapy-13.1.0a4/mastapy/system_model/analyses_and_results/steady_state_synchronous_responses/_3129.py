"""TorqueConverterSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "TorqueConverterSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2630
    from mastapy.system_model.analyses_and_results.static_loads import _7000
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3105,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="TorqueConverterSteadyStateSynchronousResponse")


class TorqueConverterSteadyStateSynchronousResponse(
    _3045.CouplingSteadyStateSynchronousResponse
):
    """TorqueConverterSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterSteadyStateSynchronousResponse"
    )

    class _Cast_TorqueConverterSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
            parent: "TorqueConverterSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3045.CouplingSteadyStateSynchronousResponse":
            return self._parent._cast(_3045.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "TorqueConverterSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7000.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterSteadyStateSynchronousResponse(self)
