"""SpecialisedAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6842,
        _6848,
        _6851,
        _6856,
        _6857,
        _6861,
        _6867,
        _6870,
        _6875,
        _6880,
        _6882,
        _6884,
        _6892,
        _6913,
        _6915,
        _6922,
        _6934,
        _6941,
        _6944,
        _6947,
        _6958,
        _6960,
        _6972,
        _6982,
        _6985,
        _6988,
        _6991,
        _6995,
        _7000,
        _7011,
        _7014,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyLoadCase",)


Self = TypeVar("Self", bound="SpecialisedAssemblyLoadCase")


class SpecialisedAssemblyLoadCase(_6833.AbstractAssemblyLoadCase):
    """SpecialisedAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyLoadCase")

    class _Cast_SpecialisedAssemblyLoadCase:
        """Special nested class for casting SpecialisedAssemblyLoadCase to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            parent: "SpecialisedAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6842.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.AGMAGleasonConicalGearSetLoadCase)

        @property
        def belt_drive_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6848.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6851.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6856.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6857.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6861.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6867.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6870.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6875.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6880.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(_6880.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6882.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6884.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6892.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6913.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6915.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6922.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6934.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(
                _6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(
                _6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6958.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6960.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6972.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.RollingRingAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6982.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6985.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6988.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6991.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_6995.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_7000.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7000

            return self._parent._cast(_7000.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_7011.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7011

            return self._parent._cast(_7011.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "_7014.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7014

            return self._parent._cast(_7014.ZerolBevelGearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "SpecialisedAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase":
        return self._Cast_SpecialisedAssemblyLoadCase(self)
