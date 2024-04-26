"""AbstractAssemblyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6309,
        _6310,
        _6313,
        _6316,
        _6321,
        _6323,
        _6325,
        _6330,
        _6334,
        _6337,
        _6341,
        _6344,
        _6346,
        _6352,
        _6360,
        _6362,
        _6365,
        _6369,
        _6373,
        _6376,
        _6379,
        _6386,
        _6389,
        _6396,
        _6399,
        _6403,
        _6406,
        _6408,
        _6412,
        _6415,
        _6418,
        _6423,
        _6430,
        _6433,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyDynamicAnalysis")


class AbstractAssemblyDynamicAnalysis(_6384.PartDynamicAnalysis):
    """AbstractAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyDynamicAnalysis")

    class _Cast_AbstractAssemblyDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            parent: "AbstractAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6309.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6310.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.AssemblyDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6313.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6316.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6321.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6323.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6325.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6330.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6334.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6341.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6344.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6346.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(_6346.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6352.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6360.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6362.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6365.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6369.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(
                _6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6386.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6389.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6396.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.RollingRingAssemblyDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6399.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.RootAssemblyDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6406.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6408.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6412.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6415.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6418.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6418

            return self._parent._cast(_6418.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6423.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6423

            return self._parent._cast(_6423.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6430.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6430

            return self._parent._cast(_6430.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6433.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6433

            return self._parent._cast(_6433.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "AbstractAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis":
        return self._Cast_AbstractAssemblyDynamicAnalysis(self)
