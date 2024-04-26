"""PlasticGearVDI2736AbstractRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticGearVDI2736AbstractRateableMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _505, _506, _507
    from mastapy.gears.rating.cylindrical import _478
    from mastapy.gears.rating import _374


__docformat__ = "restructuredtext en"
__all__ = ("PlasticGearVDI2736AbstractRateableMesh",)


Self = TypeVar("Self", bound="PlasticGearVDI2736AbstractRateableMesh")


class PlasticGearVDI2736AbstractRateableMesh(_530.ISO6336RateableMesh):
    """PlasticGearVDI2736AbstractRateableMesh

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlasticGearVDI2736AbstractRateableMesh"
    )

    class _Cast_PlasticGearVDI2736AbstractRateableMesh:
        """Special nested class for casting PlasticGearVDI2736AbstractRateableMesh to subclasses."""

        def __init__(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
            parent: "PlasticGearVDI2736AbstractRateableMesh",
        ):
            self._parent = parent

        @property
        def iso6336_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_530.ISO6336RateableMesh":
            return self._parent._cast(_530.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_478.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _478

            return self._parent._cast(_478.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_374.RateableMesh":
            from mastapy.gears.rating import _374

            return self._parent._cast(_374.RateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_505.VDI2736MetalPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _505

            return self._parent._cast(_505.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_506.VDI2736PlasticMetalRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _506

            return self._parent._cast(_506.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_507.VDI2736PlasticPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _507

            return self._parent._cast(_507.VDI2736PlasticPlasticRateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "PlasticGearVDI2736AbstractRateableMesh":
            return self._parent

        def __getattr__(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
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
        self: Self, instance_to_wrap: "PlasticGearVDI2736AbstractRateableMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh":
        return self._Cast_PlasticGearVDI2736AbstractRateableMesh(self)
