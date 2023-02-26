from typing import List

import qtawesome
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QKeyCombination
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView, QMenu, QMessageBox

import styles
from actions.Lyrics import RefreshAction
from core import ApplicationContext
from entity.Lyric import Lyric
from services.LyricsManagementService import LyricsManagementService
from services.utils import PathUtils


class TreeLyricsWidget(QTreeWidget):
    item_default_flags = (
            Qt.ItemFlag.ItemNeverHasChildren | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsDragEnabled
            | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled
    )

    def __init__(self, columns: List[str], items):
        super().__init__()
        self._on_select_item = None

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

        icon_action_use = QIcon(PathUtils.icon('present_to_all_cian.png'))
        action_use = QAction('Usar')
        action_use.triggered.connect(self.useSelectedLyrics)
        action_use.setIcon(icon_action_use)

        icon_remove_action = QIcon(qtawesome.icon('mdi6.trash-can-outline', color='#EB5151'))
        remove_action = QAction('Remover')
        remove_action.triggered.connect(self.alert_remove_lyric)
        remove_action.setIcon(icon_remove_action)

        if len(self.selectedItems()) > 1:
            action_use.setText(f'Usar as {len(self.selectedItems())} letras selecionadas')

        menu = QMenu()
        menu.addAction(action_use)
        menu.addAction(RefreshAction())
        menu.addAction(remove_action)

        menu.setStyleSheet(styles.context_menu_style)
        menu.exec(event.globalPos())

    def alert_remove_lyric(self):
        alert = QMessageBox(self)
        alert.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        alert.setText("Tem certeza que deseja remover essa letra?")
        alert.accepted.connect(self.remove_lyrics)

        alert.show()

    def remove_lyrics(self):
        for selected_item in self.selectedItems():
            item = selected_item.data(0, Qt.ItemDataRole.UserRole)

            if item is not None:
                LyricsManagementService.remove_lyric(Lyric(item['name'], item['author'], None, item['path']))

        ApplicationContext.lyric_handler.refresh()
