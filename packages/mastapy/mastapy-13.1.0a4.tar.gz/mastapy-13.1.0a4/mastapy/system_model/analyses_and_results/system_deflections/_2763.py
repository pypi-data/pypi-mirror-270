"""CylindricalGearMeshSystemDeflectionTimestep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearMeshSystemDeflectionTimestep",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _865
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2782,
        _2790,
        _2750,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearMeshSystemDeflectionTimestep")


class CylindricalGearMeshSystemDeflectionTimestep(
    _2762.CylindricalGearMeshSystemDeflection
):
    """CylindricalGearMeshSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearMeshSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearMeshSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
            parent: "CylindricalGearMeshSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2762.CylindricalGearMeshSystemDeflection":
            return self._parent._cast(_2762.CylindricalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "CylindricalGearMeshSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_contact_lines(
        self: Self,
    ) -> "List[_865.CylindricalGearMeshLoadedContactLine]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep":
        return self._Cast_CylindricalGearMeshSystemDeflectionTimestep(self)
