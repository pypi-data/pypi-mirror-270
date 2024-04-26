"""AbstractAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4325,
        _4326,
        _4329,
        _4332,
        _4337,
        _4338,
        _4342,
        _4347,
        _4350,
        _4353,
        _4358,
        _4360,
        _4362,
        _4368,
        _4381,
        _4383,
        _4386,
        _4390,
        _4394,
        _4397,
        _4400,
        _4419,
        _4421,
        _4428,
        _4431,
        _4435,
        _4438,
        _4441,
        _4444,
        _4447,
        _4451,
        _4455,
        _4462,
        _4465,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractAssemblyParametricStudyTool")


class AbstractAssemblyParametricStudyTool(_4416.PartParametricStudyTool):
    """AbstractAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyParametricStudyTool")

    class _Cast_AbstractAssemblyParametricStudyTool:
        """Special nested class for casting AbstractAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
            parent: "AbstractAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4325.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(
                _4325.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4326.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.AssemblyParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4329.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4332.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4337.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4338.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4342.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4347.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4350.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4350,
            )

            return self._parent._cast(_4350.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4353.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4358.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4360.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4362.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4368.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(_4368.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4381.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4383.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4386.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4390.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4394.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4397.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4400.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(
                _4400.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4419.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4421.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4428.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.RollingRingAssemblyParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4431.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.RootAssemblyParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4435.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4438.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4441.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4444.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4447.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4451.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4451,
            )

            return self._parent._cast(_4451.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4455.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4455,
            )

            return self._parent._cast(_4455.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4462.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4462,
            )

            return self._parent._cast(_4462.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4465.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4465,
            )

            return self._parent._cast(_4465.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "AbstractAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractAssemblyParametricStudyTool.TYPE"
    ):
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
    ) -> (
        "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool"
    ):
        return self._Cast_AbstractAssemblyParametricStudyTool(self)
