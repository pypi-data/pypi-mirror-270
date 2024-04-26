"""FaceGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _881
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Face", "FaceGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1236, _1227


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetLoadCase",)


Self = TypeVar("Self", bound="FaceGearSetLoadCase")


class FaceGearSetLoadCase(_881.GearSetLoadCaseBase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetLoadCase")

    class _Cast_FaceGearSetLoadCase:
        """Special nested class for casting FaceGearSetLoadCase to subclasses."""

        def __init__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
            parent: "FaceGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_881.GearSetLoadCaseBase":
            return self._parent._cast(_881.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def face_gear_set_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "FaceGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase":
        return self._Cast_FaceGearSetLoadCase(self)
