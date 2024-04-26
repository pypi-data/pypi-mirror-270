"""CouplingHalfSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2805
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingHalfSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.power_flows import _4093
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2735,
        _2741,
        _2756,
        _2810,
        _2816,
        _2822,
        _2834,
        _2844,
        _2845,
        _2846,
        _2852,
        _2854,
        _2738,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfSystemDeflection")


class CouplingHalfSystemDeflection(_2805.MountableComponentSystemDeflection):
    """CouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfSystemDeflection")

    class _Cast_CouplingHalfSystemDeflection:
        """Special nested class for casting CouplingHalfSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
            parent: "CouplingHalfSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2735.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2741.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.ConceptCouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2756.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CVTPulleySystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2810.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2816.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.PulleySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2822.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.RollingRingSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2834.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.SpringDamperHalfSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2844.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2845.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2846.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2852.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "_2854.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2854,
            )

            return self._parent._cast(_2854.TorqueConverterTurbineSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "CouplingHalfSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfSystemDeflection.TYPE"):
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
    def power_flow_results(self: Self) -> "_4093.CouplingHalfPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection":
        return self._Cast_CouplingHalfSystemDeflection(self)
