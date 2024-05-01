import logging
logger = logging.getLogger(__name__)

import typing
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QItemSelection, QModelIndex, Qt, QAbstractItemModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from silicon_analyser.grid import Grid
from silicon_analyser.treeitem import TreeItem
from silicon_analyser.helper.abstract.abstractmywindow import AbstractMyWindow

class PropertiesUtil:
    def __init__(self, myWindow: AbstractMyWindow,properties: QTableView):
        self._properties = properties
        self._myWindow = myWindow
        properties.model().dataChanged.connect(self.dataChanged)
    
    def dataChanged(self,*args,**kwargs):
        logger.info("dataChanged")
        valueCol: QModelIndex = args[0]
        if valueCol.column() != 1:
            return
        row = valueCol.row()
        model: QStandardItemModel = typing.cast(QStandardItemModel,self._properties.model())
        nameCol = model.item(row,0)
        name = nameCol.data(Qt.ItemDataRole.DisplayRole)
        value = valueCol.data(Qt.ItemDataRole.DisplayRole)
        logger.info(f"{name}: {value}")
        grid: Grid = self._myWindow.getTree().getSelectedGrid()
        if(name == "cols"):
            grid.cols = int(value)
            grid.recalcCell()
        if(name == "rows"):
            grid.rows = int(value)
            grid.recalcCell()
        if(name == "x"):
            grid.x = int(value)
        if(name == "y"):
            grid.y = int(value)
        if(name == "width"):
            grid.width = int(value)
            grid.recalcCell()
        if(name == "height"):
            grid.height = int(value)
            grid.recalcCell()
        if(name == "shearX"):
            grid.shearX = float(value)
        if(name == "shearY"):
            grid.shearY = float(value)
        self._myWindow.getImage().drawImage()
        self._myWindow.getSaving().triggerSaveGrids()
    
    def reloadPropertyWindow(self,selection: QItemSelection):
        table: QTableView = self._properties
        model = table.model()
        model.removeRows(0,model.rowCount())
        cnt = selection.count()
        if(cnt == 0):
            return
        sel = selection.takeFirst()
        if(len(sel.indexes())==0):
            return
        typeStr = sel.indexes()[0].data(TreeItem.TYPE)
        if(typeStr == TreeItem.TYPE_GRID):
            grid: Grid = sel.indexes()[0].data(TreeItem.OBJECT)
            self.reloadProperyWindowByGrid(grid)

    def reloadProperyWindowByGrid(self, grid: Grid):
        table: QTableView = self._properties
        model: QStandardItemModel = typing.cast(QStandardItemModel, table.model())
        rowPosition = model.rowCount()
        model.removeRows(0,model.rowCount())
        model.insertRow(rowPosition,[QStandardItem("name"),QStandardItem(grid.name)])
        if grid is not None:
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("x"),QStandardItem(f"{grid.x}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("y"),QStandardItem(f"{grid.y}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("cols"),QStandardItem(f"{grid.cols}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("rows"),QStandardItem(f"{grid.rows}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("width"),QStandardItem(f"{grid.width}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("height"),QStandardItem(f"{grid.height}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("shearX"),QStandardItem(f"{grid.shearX}")])
            rowPosition = model.rowCount()
            model.insertRow(rowPosition,[QStandardItem("shearY"),QStandardItem(f"{grid.shearY}")])

  