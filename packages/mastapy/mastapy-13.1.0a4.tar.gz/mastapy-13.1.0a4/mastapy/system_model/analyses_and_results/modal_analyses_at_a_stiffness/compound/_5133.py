"""VirtualComponentCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5088,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5004,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5086,
        _5087,
        _5097,
        _5098,
        _5132,
        _5036,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="VirtualComponentCompoundModalAnalysisAtAStiffness")


class VirtualComponentCompoundModalAnalysisAtAStiffness(
    _5088.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """VirtualComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_VirtualComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting VirtualComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
            parent: "VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5088.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(_5036.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(_5086.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5087.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(_5097.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(_5098.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5132.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5132,
            )

            return self._parent._cast(
                _5132.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "VirtualComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "VirtualComponentCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5004.VirtualComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.VirtualComponentModalAnalysisAtAStiffness]

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
    ) -> "List[_5004.VirtualComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.VirtualComponentModalAnalysisAtAStiffness]

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
    ) -> "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness(self)
