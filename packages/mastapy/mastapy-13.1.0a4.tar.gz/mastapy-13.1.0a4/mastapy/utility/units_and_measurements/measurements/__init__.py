"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1625 import Acceleration
    from ._1626 import Angle
    from ._1627 import AnglePerUnitTemperature
    from ._1628 import AngleSmall
    from ._1629 import AngleVerySmall
    from ._1630 import AngularAcceleration
    from ._1631 import AngularCompliance
    from ._1632 import AngularJerk
    from ._1633 import AngularStiffness
    from ._1634 import AngularVelocity
    from ._1635 import Area
    from ._1636 import AreaSmall
    from ._1637 import CarbonEmissionFactor
    from ._1638 import CurrentDensity
    from ._1639 import CurrentPerLength
    from ._1640 import Cycles
    from ._1641 import Damage
    from ._1642 import DamageRate
    from ._1643 import DataSize
    from ._1644 import Decibel
    from ._1645 import Density
    from ._1646 import ElectricalResistance
    from ._1647 import ElectricalResistivity
    from ._1648 import ElectricCurrent
    from ._1649 import Energy
    from ._1650 import EnergyPerUnitArea
    from ._1651 import EnergyPerUnitAreaSmall
    from ._1652 import EnergySmall
    from ._1653 import Enum
    from ._1654 import FlowRate
    from ._1655 import Force
    from ._1656 import ForcePerUnitLength
    from ._1657 import ForcePerUnitPressure
    from ._1658 import ForcePerUnitTemperature
    from ._1659 import FractionMeasurementBase
    from ._1660 import FractionPerTemperature
    from ._1661 import Frequency
    from ._1662 import FuelConsumptionEngine
    from ._1663 import FuelEfficiencyVehicle
    from ._1664 import Gradient
    from ._1665 import HeatConductivity
    from ._1666 import HeatTransfer
    from ._1667 import HeatTransferCoefficientForPlasticGearTooth
    from ._1668 import HeatTransferResistance
    from ._1669 import Impulse
    from ._1670 import Index
    from ._1671 import Inductance
    from ._1672 import Integer
    from ._1673 import InverseShortLength
    from ._1674 import InverseShortTime
    from ._1675 import Jerk
    from ._1676 import KinematicViscosity
    from ._1677 import LengthLong
    from ._1678 import LengthMedium
    from ._1679 import LengthPerUnitTemperature
    from ._1680 import LengthShort
    from ._1681 import LengthToTheFourth
    from ._1682 import LengthVeryLong
    from ._1683 import LengthVeryShort
    from ._1684 import LengthVeryShortPerLengthShort
    from ._1685 import LinearAngularDamping
    from ._1686 import LinearAngularStiffnessCrossTerm
    from ._1687 import LinearDamping
    from ._1688 import LinearFlexibility
    from ._1689 import LinearStiffness
    from ._1690 import MagneticFieldStrength
    from ._1691 import MagneticFlux
    from ._1692 import MagneticFluxDensity
    from ._1693 import MagneticVectorPotential
    from ._1694 import MagnetomotiveForce
    from ._1695 import Mass
    from ._1696 import MassPerUnitLength
    from ._1697 import MassPerUnitTime
    from ._1698 import MomentOfInertia
    from ._1699 import MomentOfInertiaPerUnitLength
    from ._1700 import MomentPerUnitPressure
    from ._1701 import Number
    from ._1702 import Percentage
    from ._1703 import Power
    from ._1704 import PowerPerSmallArea
    from ._1705 import PowerPerUnitTime
    from ._1706 import PowerSmall
    from ._1707 import PowerSmallPerArea
    from ._1708 import PowerSmallPerMass
    from ._1709 import PowerSmallPerUnitAreaPerUnitTime
    from ._1710 import PowerSmallPerUnitTime
    from ._1711 import PowerSmallPerVolume
    from ._1712 import Pressure
    from ._1713 import PressurePerUnitTime
    from ._1714 import PressureVelocityProduct
    from ._1715 import PressureViscosityCoefficient
    from ._1716 import Price
    from ._1717 import PricePerUnitMass
    from ._1718 import QuadraticAngularDamping
    from ._1719 import QuadraticDrag
    from ._1720 import RescaledMeasurement
    from ._1721 import Rotatum
    from ._1722 import SafetyFactor
    from ._1723 import SpecificAcousticImpedance
    from ._1724 import SpecificHeat
    from ._1725 import SquareRootOfUnitForcePerUnitArea
    from ._1726 import StiffnessPerUnitFaceWidth
    from ._1727 import Stress
    from ._1728 import Temperature
    from ._1729 import TemperatureDifference
    from ._1730 import TemperaturePerUnitTime
    from ._1731 import Text
    from ._1732 import ThermalContactCoefficient
    from ._1733 import ThermalExpansionCoefficient
    from ._1734 import ThermoElasticFactor
    from ._1735 import Time
    from ._1736 import TimeShort
    from ._1737 import TimeVeryShort
    from ._1738 import Torque
    from ._1739 import TorqueConverterInverseK
    from ._1740 import TorqueConverterK
    from ._1741 import TorquePerCurrent
    from ._1742 import TorquePerSquareRootOfPower
    from ._1743 import TorquePerUnitTemperature
    from ._1744 import Velocity
    from ._1745 import VelocitySmall
    from ._1746 import Viscosity
    from ._1747 import Voltage
    from ._1748 import VoltagePerAngularVelocity
    from ._1749 import Volume
    from ._1750 import WearCoefficient
    from ._1751 import Yank
else:
    import_structure = {
        "_1625": ["Acceleration"],
        "_1626": ["Angle"],
        "_1627": ["AnglePerUnitTemperature"],
        "_1628": ["AngleSmall"],
        "_1629": ["AngleVerySmall"],
        "_1630": ["AngularAcceleration"],
        "_1631": ["AngularCompliance"],
        "_1632": ["AngularJerk"],
        "_1633": ["AngularStiffness"],
        "_1634": ["AngularVelocity"],
        "_1635": ["Area"],
        "_1636": ["AreaSmall"],
        "_1637": ["CarbonEmissionFactor"],
        "_1638": ["CurrentDensity"],
        "_1639": ["CurrentPerLength"],
        "_1640": ["Cycles"],
        "_1641": ["Damage"],
        "_1642": ["DamageRate"],
        "_1643": ["DataSize"],
        "_1644": ["Decibel"],
        "_1645": ["Density"],
        "_1646": ["ElectricalResistance"],
        "_1647": ["ElectricalResistivity"],
        "_1648": ["ElectricCurrent"],
        "_1649": ["Energy"],
        "_1650": ["EnergyPerUnitArea"],
        "_1651": ["EnergyPerUnitAreaSmall"],
        "_1652": ["EnergySmall"],
        "_1653": ["Enum"],
        "_1654": ["FlowRate"],
        "_1655": ["Force"],
        "_1656": ["ForcePerUnitLength"],
        "_1657": ["ForcePerUnitPressure"],
        "_1658": ["ForcePerUnitTemperature"],
        "_1659": ["FractionMeasurementBase"],
        "_1660": ["FractionPerTemperature"],
        "_1661": ["Frequency"],
        "_1662": ["FuelConsumptionEngine"],
        "_1663": ["FuelEfficiencyVehicle"],
        "_1664": ["Gradient"],
        "_1665": ["HeatConductivity"],
        "_1666": ["HeatTransfer"],
        "_1667": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1668": ["HeatTransferResistance"],
        "_1669": ["Impulse"],
        "_1670": ["Index"],
        "_1671": ["Inductance"],
        "_1672": ["Integer"],
        "_1673": ["InverseShortLength"],
        "_1674": ["InverseShortTime"],
        "_1675": ["Jerk"],
        "_1676": ["KinematicViscosity"],
        "_1677": ["LengthLong"],
        "_1678": ["LengthMedium"],
        "_1679": ["LengthPerUnitTemperature"],
        "_1680": ["LengthShort"],
        "_1681": ["LengthToTheFourth"],
        "_1682": ["LengthVeryLong"],
        "_1683": ["LengthVeryShort"],
        "_1684": ["LengthVeryShortPerLengthShort"],
        "_1685": ["LinearAngularDamping"],
        "_1686": ["LinearAngularStiffnessCrossTerm"],
        "_1687": ["LinearDamping"],
        "_1688": ["LinearFlexibility"],
        "_1689": ["LinearStiffness"],
        "_1690": ["MagneticFieldStrength"],
        "_1691": ["MagneticFlux"],
        "_1692": ["MagneticFluxDensity"],
        "_1693": ["MagneticVectorPotential"],
        "_1694": ["MagnetomotiveForce"],
        "_1695": ["Mass"],
        "_1696": ["MassPerUnitLength"],
        "_1697": ["MassPerUnitTime"],
        "_1698": ["MomentOfInertia"],
        "_1699": ["MomentOfInertiaPerUnitLength"],
        "_1700": ["MomentPerUnitPressure"],
        "_1701": ["Number"],
        "_1702": ["Percentage"],
        "_1703": ["Power"],
        "_1704": ["PowerPerSmallArea"],
        "_1705": ["PowerPerUnitTime"],
        "_1706": ["PowerSmall"],
        "_1707": ["PowerSmallPerArea"],
        "_1708": ["PowerSmallPerMass"],
        "_1709": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1710": ["PowerSmallPerUnitTime"],
        "_1711": ["PowerSmallPerVolume"],
        "_1712": ["Pressure"],
        "_1713": ["PressurePerUnitTime"],
        "_1714": ["PressureVelocityProduct"],
        "_1715": ["PressureViscosityCoefficient"],
        "_1716": ["Price"],
        "_1717": ["PricePerUnitMass"],
        "_1718": ["QuadraticAngularDamping"],
        "_1719": ["QuadraticDrag"],
        "_1720": ["RescaledMeasurement"],
        "_1721": ["Rotatum"],
        "_1722": ["SafetyFactor"],
        "_1723": ["SpecificAcousticImpedance"],
        "_1724": ["SpecificHeat"],
        "_1725": ["SquareRootOfUnitForcePerUnitArea"],
        "_1726": ["StiffnessPerUnitFaceWidth"],
        "_1727": ["Stress"],
        "_1728": ["Temperature"],
        "_1729": ["TemperatureDifference"],
        "_1730": ["TemperaturePerUnitTime"],
        "_1731": ["Text"],
        "_1732": ["ThermalContactCoefficient"],
        "_1733": ["ThermalExpansionCoefficient"],
        "_1734": ["ThermoElasticFactor"],
        "_1735": ["Time"],
        "_1736": ["TimeShort"],
        "_1737": ["TimeVeryShort"],
        "_1738": ["Torque"],
        "_1739": ["TorqueConverterInverseK"],
        "_1740": ["TorqueConverterK"],
        "_1741": ["TorquePerCurrent"],
        "_1742": ["TorquePerSquareRootOfPower"],
        "_1743": ["TorquePerUnitTemperature"],
        "_1744": ["Velocity"],
        "_1745": ["VelocitySmall"],
        "_1746": ["Viscosity"],
        "_1747": ["Voltage"],
        "_1748": ["VoltagePerAngularVelocity"],
        "_1749": ["Volume"],
        "_1750": ["WearCoefficient"],
        "_1751": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
