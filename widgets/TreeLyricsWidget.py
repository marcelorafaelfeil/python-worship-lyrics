from typing import List

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QTreeWidget, QAbstractItemView, QTreeWidgetItem, QAbstractItemView


class TreeLyricsWidget(QTreeWidget):
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
        widget_item.setFlags(TreeLyricsWidget.item_default_flags)
        self.addTopLevelItem(widget_item)

    def onSelectItem(self, _fn):
        self._on_select_item = _fn

    def _doubleClicked(self, index: QtCore.QModelIndex) -> None:
        widget_item = self.itemFromIndex(index)
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)
        widget_item.setFlags(TreeLyricsWidget.item_default_flags)

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
