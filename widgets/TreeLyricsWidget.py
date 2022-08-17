from typing import List

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView, QMenu


class TreeLyricsWidget(QTreeWidget):
    item_default_flags = (
            Qt.ItemFlag.ItemNeverHasChildren | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsDragEnabled
            | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled
    )

    def __init__(self, columns: List[str], items):
        super().__init__()
        self._on_select_item = None
        self._refresh = None

        self.setColumnCount(2)
        self.setIndentation(0)
        self.setSortingEnabled(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setDragEnabled(True)
        self.setHeaderLabels(columns)
        self.setItemsExpandable(False)
        self.doubleClicked.connect(self._doubleClicked)

        if items is not None:
            self.setItems(items)

    def setItems(self, data):
        self.clear()
        items = []

        for lyric in data:
            item = QTreeWidgetItem([lyric['name'], lyric['author']])
            item.setData(0, Qt.ItemDataRole.UserRole, lyric)
            items.append(item)

        self.insertTopLevelItems(0, items)

    def onSelectItem(self, _fn):
        self._on_select_item = _fn

    def onRefresh(self, _fn):
        self._refresh = _fn

    def _doubleClicked(self, index: QtCore.QModelIndex) -> None:
        widget_item = self.itemFromIndex(index)
        self.sendToUseArea(widget_item)

    def sendToUseArea(self, widget_item: QTreeWidgetItem):
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)

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

    def useSelectedLyrics(self):
        for item in self.selectedItems():
            self.sendToUseArea(item)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        action_use = QAction('Usar')
        action_use.triggered.connect(self.useSelectedLyrics)

        if len(self.selectedItems()) > 1:
            action_use.setText(f'Usar as {len(self.selectedItems())} letras selecionadas')

        menu = QMenu()
        menu.addAction(action_use)

        if self._refresh is not None:
            action_refresh = QAction('Atualizar')
            action_refresh.triggered.connect(self._refresh)
            menu.addAction(action_refresh)

        menu.exec(event.globalPos())
