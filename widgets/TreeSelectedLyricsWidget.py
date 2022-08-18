from typing import List

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView, QMenu


class TreeSelectedLyricsWidget(QTreeWidget):
    item_default_flags = (
            Qt.ItemFlag.ItemNeverHasChildren | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsDragEnabled
            | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled
    )

    def __init__(self, columns: List[str]):
        super().__init__()
        self._on_select_item = None

        self.setColumnCount(2)
        self.setIndentation(0)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setHeaderLabels(columns)
        self.setItemsExpandable(False)
        self.doubleClicked.connect(self._doubleClicked)

    def addItem(self, labels: List[str], item):
        widget_item = QTreeWidgetItem(labels)
        widget_item.setData(0, Qt.ItemDataRole.UserRole, item)
        widget_item.setFlags(TreeSelectedLyricsWidget.item_default_flags)
        self.addTopLevelItem(widget_item)

    def onSelectItem(self, _fn):
        self._on_select_item = _fn

    def _doubleClicked(self, index: QtCore.QModelIndex) -> None:
        widget_item = self.itemFromIndex(index)
        self.sendToProjector(widget_item)

    def sendToProjector(self, widget_item):
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)
        widget_item.setFlags(TreeSelectedLyricsWidget.item_default_flags)

        if self._on_select_item is not None:
            self._on_select_item(item)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if self.dropIndicatorPosition() == QAbstractItemView.DropIndicatorPosition.OnItem:
            event.ignore()
        else:
            if event.source() == self:
                event.setDropAction(Qt.DropAction.MoveAction)

            QTreeWidget.dropEvent(self, event)
            event.acceptProposedAction()
            self.clearSelection()

    def _clear(self):
        self.clear()

    def _removeItem(self, item: QTreeWidgetItem):
        self.takeTopLevelItem(self.indexOfTopLevelItem(item))

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        clicked_item = self.itemAt(event.pos())

        action_clear_all = QAction()
        action_clear_all.setText('Limpar tudo')
        action_clear_all.triggered.connect(self._clear)

        action_remove_item = QAction()
        action_remove_item.setText('Remover')
        action_remove_item.triggered.connect(lambda: self._removeItem(clicked_item))

        action_project = QAction()
        action_project.setText('Projetar')
        action_project.triggered.connect(lambda: self.sendToProjector(clicked_item))

        menu = QMenu()

        if clicked_item is not None:
            menu.addAction(action_project)
            menu.addAction(action_remove_item)
            menu.addSeparator()

        menu.addAction(action_clear_all)

        menu.exec(event.globalPos())
