"""PerMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility import _1608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "PerMachineSettings")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _68
    from mastapy.nodal_analysis.geometry_modeller_link import _167
    from mastapy.gears.materials import _603
    from mastapy.gears.ltca.cylindrical import _862
    from mastapy.gears.gear_designs.cylindrical import _1019
    from mastapy.utility import _1609, _1610
    from mastapy.utility.units_and_measurements import _1619
    from mastapy.utility.scripting import _1752
    from mastapy.utility.databases import _1842
    from mastapy.utility.cad_export import _1847
    from mastapy.bearings import _1916
    from mastapy.system_model.part_model import _2488


__docformat__ = "restructuredtext en"
__all__ = ("PerMachineSettings",)


Self = TypeVar("Self", bound="PerMachineSettings")


class PerMachineSettings(_1608.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE = _PER_MACHINE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerMachineSettings")

    class _Cast_PerMachineSettings:
        """Special nested class for casting PerMachineSettings to subclasses."""

        def __init__(
            self: "PerMachineSettings._Cast_PerMachineSettings",
            parent: "PerMachineSettings",
        ):
            self._parent = parent

        @property
        def persistent_singleton(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1608.PersistentSingleton":
            return self._parent._cast(_1608.PersistentSingleton)

        @property
        def fe_user_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_68.FEUserSettings":
            from mastapy.nodal_analysis import _68

            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_167.GeometryModellerSettings":
            from mastapy.nodal_analysis.geometry_modeller_link import _167

            return self._parent._cast(_167.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_603.GearMaterialExpertSystemFactorSettings":
            from mastapy.gears.materials import _603

            return self._parent._cast(_603.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_862.CylindricalGearFESettings":
            from mastapy.gears.ltca.cylindrical import _862

            return self._parent._cast(_862.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1019.CylindricalGearDefaults":
            from mastapy.gears.gear_designs.cylindrical import _1019

            return self._parent._cast(_1019.CylindricalGearDefaults)

        @property
        def program_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1609.ProgramSettings":
            from mastapy.utility import _1609

            return self._parent._cast(_1609.ProgramSettings)

        @property
        def pushbullet_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1610.PushbulletSettings":
            from mastapy.utility import _1610

            return self._parent._cast(_1610.PushbulletSettings)

        @property
        def measurement_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1619.MeasurementSettings":
            from mastapy.utility.units_and_measurements import _1619

            return self._parent._cast(_1619.MeasurementSettings)

        @property
        def scripting_setup(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1752.ScriptingSetup":
            from mastapy.utility.scripting import _1752

            return self._parent._cast(_1752.ScriptingSetup)

        @property
        def database_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1842.DatabaseSettings":
            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.DatabaseSettings)

        @property
        def cad_export_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1847.CADExportSettings":
            from mastapy.utility.cad_export import _1847

            return self._parent._cast(_1847.CADExportSettings)

        @property
        def skf_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1916.SKFSettings":
            from mastapy.bearings import _1916

            return self._parent._cast(_1916.SKFSettings)

        @property
        def planet_carrier_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_2488.PlanetCarrierSettings":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.PlanetCarrierSettings)

        @property
        def per_machine_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "PerMachineSettings":
            return self._parent

        def __getattr__(self: "PerMachineSettings._Cast_PerMachineSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerMachineSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def reset_to_defaults(self: Self):
        """Method does not return."""
        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self: Self) -> "PerMachineSettings._Cast_PerMachineSettings":
        return self._Cast_PerMachineSettings(self)
