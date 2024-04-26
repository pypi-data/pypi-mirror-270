"""CouplingHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4681
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CouplingHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.system_deflections import _2753
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4617,
        _4622,
        _4638,
        _4687,
        _4694,
        _4699,
        _4710,
        _4720,
        _4722,
        _4723,
        _4726,
        _4727,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfModalAnalysis")


class CouplingHalfModalAnalysis(_4681.MountableComponentModalAnalysis):
    """CouplingHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfModalAnalysis")

    class _Cast_CouplingHalfModalAnalysis:
        """Special nested class for casting CouplingHalfModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
            parent: "CouplingHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4617.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4622.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.ConceptCouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4638.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.CVTPulleyModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4687.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4694.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.PulleyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4699.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.RollingRingModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4710.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.SpringDamperHalfModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4720.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4722.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4723.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4726.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4727.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.TorqueConverterTurbineModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "CouplingHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2753.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis":
        return self._Cast_CouplingHalfModalAnalysis(self)
