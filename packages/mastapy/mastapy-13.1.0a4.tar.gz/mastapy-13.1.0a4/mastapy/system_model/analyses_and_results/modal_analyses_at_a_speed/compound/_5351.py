"""PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5308,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5221,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5335,
        _5305,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"
)


class PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed(
    _5308.CouplingConnectionCompoundModalAnalysisAtASpeed
):
    """PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
            parent: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5308.CouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5308.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5305.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2366.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2366.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartToPartShearCouplingConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartToPartShearCouplingConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
        return (
            self._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed(
                self
            )
        )
