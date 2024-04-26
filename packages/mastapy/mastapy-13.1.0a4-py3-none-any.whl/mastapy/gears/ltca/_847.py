"""GearLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _863
    from mastapy.gears.ltca.conical import _874
    from mastapy.gears.analysis import _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("GearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="GearLoadDistributionAnalysis")


class GearLoadDistributionAnalysis(_1229.GearImplementationAnalysis):
    """GearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearLoadDistributionAnalysis")

    class _Cast_GearLoadDistributionAnalysis:
        """Special nested class for casting GearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
            parent: "GearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_implementation_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "_1229.GearImplementationAnalysis":
            return self._parent._cast(_1229.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "_863.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "_874.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _874

            return self._parent._cast(_874.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "GearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearLoadDistributionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis":
        return self._Cast_GearLoadDistributionAnalysis(self)
