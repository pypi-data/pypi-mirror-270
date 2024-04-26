"""CouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6860,
        _6866,
        _6883,
        _6957,
        _6967,
        _6974,
        _6984,
        _6994,
        _6996,
        _6997,
        _7001,
        _7002,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfLoadCase",)


Self = TypeVar("Self", bound="CouplingHalfLoadCase")


class CouplingHalfLoadCase(_6951.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfLoadCase")

    class _Cast_CouplingHalfLoadCase:
        """Special nested class for casting CouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
            parent: "CouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6860.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6866.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConceptCouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6883.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.CVTPulleyLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6957.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.PartToPartShearCouplingHalfLoadCase)

        @property
        def pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6967.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.PulleyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6974.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.RollingRingLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6984.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.SpringDamperHalfLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6994.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6996.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6997.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_7001.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7001

            return self._parent._cast(_7001.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_7002.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7002

            return self._parent._cast(_7002.TorqueConverterTurbineLoadCase)

        @property
        def coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "CouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfLoadCase.TYPE"):
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
    def cast_to(self: Self) -> "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase":
        return self._Cast_CouplingHalfLoadCase(self)
