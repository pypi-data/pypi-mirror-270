"""BevelLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case.conical import _892
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Bevel", "BevelLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case import _880
    from mastapy.gears.analysis import _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("BevelLoadCase",)


Self = TypeVar("Self", bound="BevelLoadCase")


class BevelLoadCase(_892.ConicalGearLoadCase):
    """BevelLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelLoadCase")

    class _Cast_BevelLoadCase:
        """Special nested class for casting BevelLoadCase to subclasses."""

        def __init__(
            self: "BevelLoadCase._Cast_BevelLoadCase", parent: "BevelLoadCase"
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "_892.ConicalGearLoadCase":
            return self._parent._cast(_892.ConicalGearLoadCase)

        @property
        def gear_load_case_base(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "_880.GearLoadCaseBase":
            from mastapy.gears.load_case import _880

            return self._parent._cast(_880.GearLoadCaseBase)

        @property
        def gear_design_analysis(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def bevel_load_case(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "BevelLoadCase":
            return self._parent

        def __getattr__(self: "BevelLoadCase._Cast_BevelLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelLoadCase._Cast_BevelLoadCase":
        return self._Cast_BevelLoadCase(self)
