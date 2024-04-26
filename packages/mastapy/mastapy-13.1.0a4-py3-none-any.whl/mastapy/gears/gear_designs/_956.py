"""GearDesignComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_COMPONENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "GearDesignComponent"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1754
    from mastapy.gears.gear_designs import _955, _957, _958
    from mastapy.gears.gear_designs.zerol_bevel import _960, _961, _962, _963
    from mastapy.gears.gear_designs.worm import _964, _965, _966, _967, _968
    from mastapy.gears.gear_designs.straight_bevel import _969, _970, _971, _972
    from mastapy.gears.gear_designs.straight_bevel_diff import _973, _974, _975, _976
    from mastapy.gears.gear_designs.spiral_bevel import _977, _978, _979, _980
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import (
        _981,
        _982,
        _983,
        _984,
    )
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _985, _986, _987, _988
    from mastapy.gears.gear_designs.klingelnberg_conical import _989, _990, _991, _992
    from mastapy.gears.gear_designs.hypoid import _993, _994, _995, _996
    from mastapy.gears.gear_designs.face import _997, _999, _1002, _1003, _1005
    from mastapy.gears.gear_designs.cylindrical import _1020, _1026, _1036, _1049, _1050
    from mastapy.gears.gear_designs.conical import _1164, _1165, _1166, _1169
    from mastapy.gears.gear_designs.concept import _1186, _1187, _1188
    from mastapy.gears.gear_designs.bevel import _1190, _1191, _1192, _1193
    from mastapy.gears.gear_designs.agma_gleason_conical import (
        _1203,
        _1204,
        _1205,
        _1206,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignComponent",)


Self = TypeVar("Self", bound="GearDesignComponent")


class GearDesignComponent(_0.APIBase):
    """GearDesignComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignComponent")

    class _Cast_GearDesignComponent:
        """Special nested class for casting GearDesignComponent to subclasses."""

        def __init__(
            self: "GearDesignComponent._Cast_GearDesignComponent",
            parent: "GearDesignComponent",
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_955.GearDesign":
            from mastapy.gears.gear_designs import _955

            return self._parent._cast(_955.GearDesign)

        @property
        def gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_957.GearMeshDesign":
            from mastapy.gears.gear_designs import _957

            return self._parent._cast(_957.GearMeshDesign)

        @property
        def gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_958.GearSetDesign":
            from mastapy.gears.gear_designs import _958

            return self._parent._cast(_958.GearSetDesign)

        @property
        def zerol_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_960.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _960

            return self._parent._cast(_960.ZerolBevelGearDesign)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_961.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _961

            return self._parent._cast(_961.ZerolBevelGearMeshDesign)

        @property
        def zerol_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_962.ZerolBevelGearSetDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _962

            return self._parent._cast(_962.ZerolBevelGearSetDesign)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_963.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _963

            return self._parent._cast(_963.ZerolBevelMeshedGearDesign)

        @property
        def worm_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_964.WormDesign":
            from mastapy.gears.gear_designs.worm import _964

            return self._parent._cast(_964.WormDesign)

        @property
        def worm_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_965.WormGearDesign":
            from mastapy.gears.gear_designs.worm import _965

            return self._parent._cast(_965.WormGearDesign)

        @property
        def worm_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_966.WormGearMeshDesign":
            from mastapy.gears.gear_designs.worm import _966

            return self._parent._cast(_966.WormGearMeshDesign)

        @property
        def worm_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_967.WormGearSetDesign":
            from mastapy.gears.gear_designs.worm import _967

            return self._parent._cast(_967.WormGearSetDesign)

        @property
        def worm_wheel_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_968.WormWheelDesign":
            from mastapy.gears.gear_designs.worm import _968

            return self._parent._cast(_968.WormWheelDesign)

        @property
        def straight_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_969.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _969

            return self._parent._cast(_969.StraightBevelGearDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_970.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _970

            return self._parent._cast(_970.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_971.StraightBevelGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel import _971

            return self._parent._cast(_971.StraightBevelGearSetDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_972.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _972

            return self._parent._cast(_972.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_973.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _973

            return self._parent._cast(_973.StraightBevelDiffGearDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_974.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _974

            return self._parent._cast(_974.StraightBevelDiffGearMeshDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_975.StraightBevelDiffGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _975

            return self._parent._cast(_975.StraightBevelDiffGearSetDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_976.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _976

            return self._parent._cast(_976.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_977.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _977

            return self._parent._cast(_977.SpiralBevelGearDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_978.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _978

            return self._parent._cast(_978.SpiralBevelGearMeshDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_979.SpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _979

            return self._parent._cast(_979.SpiralBevelGearSetDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_980.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _980

            return self._parent._cast(_980.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_981.KlingelnbergCycloPalloidSpiralBevelGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _981

            return self._parent._cast(
                _981.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_982.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _982

            return self._parent._cast(
                _982.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_983.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _983

            return self._parent._cast(
                _983.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_984.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _984

            return self._parent._cast(
                _984.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_985.KlingelnbergCycloPalloidHypoidGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _985

            return self._parent._cast(_985.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_986.KlingelnbergCycloPalloidHypoidGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _986

            return self._parent._cast(_986.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_987.KlingelnbergCycloPalloidHypoidGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _987

            return self._parent._cast(_987.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_988.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _988

            return self._parent._cast(
                _988.KlingelnbergCycloPalloidHypoidMeshedGearDesign
            )

        @property
        def klingelnberg_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_989.KlingelnbergConicalGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _989

            return self._parent._cast(_989.KlingelnbergConicalGearDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_990.KlingelnbergConicalGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _990

            return self._parent._cast(_990.KlingelnbergConicalGearMeshDesign)

        @property
        def klingelnberg_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_991.KlingelnbergConicalGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _991

            return self._parent._cast(_991.KlingelnbergConicalGearSetDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_992.KlingelnbergConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _992

            return self._parent._cast(_992.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_993.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _993

            return self._parent._cast(_993.HypoidGearDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_994.HypoidGearMeshDesign":
            from mastapy.gears.gear_designs.hypoid import _994

            return self._parent._cast(_994.HypoidGearMeshDesign)

        @property
        def hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_995.HypoidGearSetDesign":
            from mastapy.gears.gear_designs.hypoid import _995

            return self._parent._cast(_995.HypoidGearSetDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_996.HypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.hypoid import _996

            return self._parent._cast(_996.HypoidMeshedGearDesign)

        @property
        def face_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_997.FaceGearDesign":
            from mastapy.gears.gear_designs.face import _997

            return self._parent._cast(_997.FaceGearDesign)

        @property
        def face_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_999.FaceGearMeshDesign":
            from mastapy.gears.gear_designs.face import _999

            return self._parent._cast(_999.FaceGearMeshDesign)

        @property
        def face_gear_pinion_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1002.FaceGearPinionDesign":
            from mastapy.gears.gear_designs.face import _1002

            return self._parent._cast(_1002.FaceGearPinionDesign)

        @property
        def face_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1003.FaceGearSetDesign":
            from mastapy.gears.gear_designs.face import _1003

            return self._parent._cast(_1003.FaceGearSetDesign)

        @property
        def face_gear_wheel_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1005.FaceGearWheelDesign":
            from mastapy.gears.gear_designs.face import _1005

            return self._parent._cast(_1005.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1020.CylindricalGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1020

            return self._parent._cast(_1020.CylindricalGearDesign)

        @property
        def cylindrical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1026.CylindricalGearMeshDesign":
            from mastapy.gears.gear_designs.cylindrical import _1026

            return self._parent._cast(_1026.CylindricalGearMeshDesign)

        @property
        def cylindrical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1036.CylindricalGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1036

            return self._parent._cast(_1036.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1049.CylindricalPlanetaryGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1049

            return self._parent._cast(_1049.CylindricalPlanetaryGearSetDesign)

        @property
        def cylindrical_planet_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1050.CylindricalPlanetGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1050

            return self._parent._cast(_1050.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1164.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1164

            return self._parent._cast(_1164.ConicalGearDesign)

        @property
        def conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1165.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalGearMeshDesign)

        @property
        def conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1166.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1166

            return self._parent._cast(_1166.ConicalGearSetDesign)

        @property
        def conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1169.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1169

            return self._parent._cast(_1169.ConicalMeshedGearDesign)

        @property
        def concept_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1186.ConceptGearDesign":
            from mastapy.gears.gear_designs.concept import _1186

            return self._parent._cast(_1186.ConceptGearDesign)

        @property
        def concept_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1187.ConceptGearMeshDesign":
            from mastapy.gears.gear_designs.concept import _1187

            return self._parent._cast(_1187.ConceptGearMeshDesign)

        @property
        def concept_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1188.ConceptGearSetDesign":
            from mastapy.gears.gear_designs.concept import _1188

            return self._parent._cast(_1188.ConceptGearSetDesign)

        @property
        def bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1190.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1190

            return self._parent._cast(_1190.BevelGearDesign)

        @property
        def bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1191.BevelGearMeshDesign":
            from mastapy.gears.gear_designs.bevel import _1191

            return self._parent._cast(_1191.BevelGearMeshDesign)

        @property
        def bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1192.BevelGearSetDesign":
            from mastapy.gears.gear_designs.bevel import _1192

            return self._parent._cast(_1192.BevelGearSetDesign)

        @property
        def bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1193.BevelMeshedGearDesign":
            from mastapy.gears.gear_designs.bevel import _1193

            return self._parent._cast(_1193.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1203.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1203

            return self._parent._cast(_1203.AGMAGleasonConicalGearDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1204.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1204

            return self._parent._cast(_1204.AGMAGleasonConicalGearMeshDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1205.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1205

            return self._parent._cast(_1205.AGMAGleasonConicalGearSetDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1206.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1206

            return self._parent._cast(_1206.AGMAGleasonConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "GearDesignComponent":
            return self._parent

        def __getattr__(
            self: "GearDesignComponent._Cast_GearDesignComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def user_specified_data(self: Self) -> "_1754.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "GearDesignComponent._Cast_GearDesignComponent":
        return self._Cast_GearDesignComponent(self)
