"""CylindricalGearLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.ltca import _847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _467
    from mastapy.gears.gear_two_d_fe_analysis import _905
    from mastapy.gears.analysis import _1229, _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearLoadDistributionAnalysis")


class CylindricalGearLoadDistributionAnalysis(_847.GearLoadDistributionAnalysis):
    """CylindricalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearLoadDistributionAnalysis"
    )

    class _Cast_CylindricalGearLoadDistributionAnalysis:
        """Special nested class for casting CylindricalGearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
            parent: "CylindricalGearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_load_distribution_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "_847.GearLoadDistributionAnalysis":
            return self._parent._cast(_847.GearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "_1229.GearImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "CylindricalGearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_467.CylindricalGearRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tiff_analysis(self: Self) -> "_905.CylindricalGearTIFFAnalysis":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTIFFAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis":
        return self._Cast_CylindricalGearLoadDistributionAnalysis(self)
