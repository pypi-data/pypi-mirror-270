"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1755 import AdHocCustomTable
    from ._1756 import AxisSettings
    from ._1757 import BlankRow
    from ._1758 import CadPageOrientation
    from ._1759 import CadPageSize
    from ._1760 import CadTableBorderType
    from ._1761 import ChartDefinition
    from ._1762 import SMTChartPointShape
    from ._1763 import CustomChart
    from ._1764 import CustomDrawing
    from ._1765 import CustomGraphic
    from ._1766 import CustomImage
    from ._1767 import CustomReport
    from ._1768 import CustomReportCadDrawing
    from ._1769 import CustomReportChart
    from ._1770 import CustomReportChartItem
    from ._1771 import CustomReportColumn
    from ._1772 import CustomReportColumns
    from ._1773 import CustomReportDefinitionItem
    from ._1774 import CustomReportHorizontalLine
    from ._1775 import CustomReportHtmlItem
    from ._1776 import CustomReportItem
    from ._1777 import CustomReportItemContainer
    from ._1778 import CustomReportItemContainerCollection
    from ._1779 import CustomReportItemContainerCollectionBase
    from ._1780 import CustomReportItemContainerCollectionItem
    from ._1781 import CustomReportKey
    from ._1782 import CustomReportMultiPropertyItem
    from ._1783 import CustomReportMultiPropertyItemBase
    from ._1784 import CustomReportNameableItem
    from ._1785 import CustomReportNamedItem
    from ._1786 import CustomReportPropertyItem
    from ._1787 import CustomReportStatusItem
    from ._1788 import CustomReportTab
    from ._1789 import CustomReportTabs
    from ._1790 import CustomReportText
    from ._1791 import CustomRow
    from ._1792 import CustomSubReport
    from ._1793 import CustomTable
    from ._1794 import DefinitionBooleanCheckOptions
    from ._1795 import DynamicCustomReportItem
    from ._1796 import FontStyle
    from ._1797 import FontWeight
    from ._1798 import HeadingSize
    from ._1799 import SimpleChartDefinition
    from ._1800 import UserTextRow
else:
    import_structure = {
        "_1755": ["AdHocCustomTable"],
        "_1756": ["AxisSettings"],
        "_1757": ["BlankRow"],
        "_1758": ["CadPageOrientation"],
        "_1759": ["CadPageSize"],
        "_1760": ["CadTableBorderType"],
        "_1761": ["ChartDefinition"],
        "_1762": ["SMTChartPointShape"],
        "_1763": ["CustomChart"],
        "_1764": ["CustomDrawing"],
        "_1765": ["CustomGraphic"],
        "_1766": ["CustomImage"],
        "_1767": ["CustomReport"],
        "_1768": ["CustomReportCadDrawing"],
        "_1769": ["CustomReportChart"],
        "_1770": ["CustomReportChartItem"],
        "_1771": ["CustomReportColumn"],
        "_1772": ["CustomReportColumns"],
        "_1773": ["CustomReportDefinitionItem"],
        "_1774": ["CustomReportHorizontalLine"],
        "_1775": ["CustomReportHtmlItem"],
        "_1776": ["CustomReportItem"],
        "_1777": ["CustomReportItemContainer"],
        "_1778": ["CustomReportItemContainerCollection"],
        "_1779": ["CustomReportItemContainerCollectionBase"],
        "_1780": ["CustomReportItemContainerCollectionItem"],
        "_1781": ["CustomReportKey"],
        "_1782": ["CustomReportMultiPropertyItem"],
        "_1783": ["CustomReportMultiPropertyItemBase"],
        "_1784": ["CustomReportNameableItem"],
        "_1785": ["CustomReportNamedItem"],
        "_1786": ["CustomReportPropertyItem"],
        "_1787": ["CustomReportStatusItem"],
        "_1788": ["CustomReportTab"],
        "_1789": ["CustomReportTabs"],
        "_1790": ["CustomReportText"],
        "_1791": ["CustomRow"],
        "_1792": ["CustomSubReport"],
        "_1793": ["CustomTable"],
        "_1794": ["DefinitionBooleanCheckOptions"],
        "_1795": ["DynamicCustomReportItem"],
        "_1796": ["FontStyle"],
        "_1797": ["FontWeight"],
        "_1798": ["HeadingSize"],
        "_1799": ["SimpleChartDefinition"],
        "_1800": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
