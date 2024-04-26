"""CylindricalRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalRateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500, _505, _506, _507
    from mastapy.gears.rating.cylindrical.iso6336 import _529, _530
    from mastapy.gears.rating.cylindrical.agma import _543


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRateableMesh",)


Self = TypeVar("Self", bound="CylindricalRateableMesh")


class CylindricalRateableMesh(_374.RateableMesh):
    """CylindricalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalRateableMesh")

    class _Cast_CylindricalRateableMesh:
        """Special nested class for casting CylindricalRateableMesh to subclasses."""

        def __init__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
            parent: "CylindricalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_374.RateableMesh":
            return self._parent._cast(_374.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_500.PlasticGearVDI2736AbstractRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500

            return self._parent._cast(_500.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_505.VDI2736MetalPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _505

            return self._parent._cast(_505.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_506.VDI2736PlasticMetalRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _506

            return self._parent._cast(_506.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_507.VDI2736PlasticPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _507

            return self._parent._cast(_507.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_529.ISO6336MetalRateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _529

            return self._parent._cast(_529.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_530.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _530

            return self._parent._cast(_530.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_543.AGMA2101RateableMesh":
            from mastapy.gears.rating.cylindrical.agma import _543

            return self._parent._cast(_543.AGMA2101RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "CylindricalRateableMesh":
            return self._parent

        def __getattr__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalRateableMesh._Cast_CylindricalRateableMesh":
        return self._Cast_CylindricalRateableMesh(self)
