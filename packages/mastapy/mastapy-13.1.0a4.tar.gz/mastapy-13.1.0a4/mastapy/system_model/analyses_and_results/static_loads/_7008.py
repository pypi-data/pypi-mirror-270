"""VirtualComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6948,
        _6949,
        _6965,
        _6966,
        _7007,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentLoadCase",)


Self = TypeVar("Self", bound="VirtualComponentLoadCase")


class VirtualComponentLoadCase(_6951.MountableComponentLoadCase):
    """VirtualComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentLoadCase")

    class _Cast_VirtualComponentLoadCase:
        """Special nested class for casting VirtualComponentLoadCase to subclasses."""

        def __init__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
            parent: "VirtualComponentLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6948.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6949.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.MeasurementComponentLoadCase)

        @property
        def point_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6965.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6966.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.PowerLoadLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_7007.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "VirtualComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase":
        return self._Cast_VirtualComponentLoadCase(self)
