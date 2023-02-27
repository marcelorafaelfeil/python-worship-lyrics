from typing import List

import qtawesome
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView, QMenu, QMessageBox

import styles
from actions.Lyrics import RefreshAction
from core import ApplicationContext
from entity.Lyric import Lyric
from services.LyricsFileManagementService import LyricsFileManagementService
from services.utils import PathUtils


class TreeLyricsWidget(QTreeWidget):
    item_default_flags = (
            Qt.ItemFlag.ItemNeverHasChildren | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsDragEnabled
            | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled
    )

    def __init__(self, columns: List[str]):
        super().__init__()
        self.lyrics_service = ApplicationContext.lyrics_service

        self.setColumnCount(2)
        self.setIndentation(0)
        self.setSortingEnabled(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setDragEnabled(True)
        self.setHeaderLabels(columns)
        self.setItemsExpandable(False)
        self.doubleClicked.connect(self._on_double_click)

        if self.lyrics_service.data is not None:
            self.set_items(self.lyrics_service.data)

        self.lyrics_service.lyrics.subscribe(lambda items: self.set_items(items))

    def set_items(self, data: List[Lyric]):
        self.clear()
        items = []

        for lyric in data:
            item = QTreeWidgetItem([lyric.name, lyric.author])
            item.setData(0, Qt.ItemDataRole.UserRole, lyric)
            items.append(item)

        self.insertTopLevelItems(0, items)

    def _on_double_click(self, index: QtCore.QModelIndex) -> None:
        widget_item = self.itemFromIndex(index)
        self.send_to_selected_area(widget_item)

    def send_to_selected_area(self, widget_item: QTreeWidgetItem):
        item: Lyric = widget_item.data(0, Qt.ItemDataRole.UserRole)
        self.lyrics_service.prepare_lyric.on_next(item)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if self.dropIndicatorPosition() == QAbstractItemView.DropIndicatorPosition.OnItem:
            event.ignore()
        else:
            if event.source() == self:
                event.setDropAction(Qt.DropAction.MoveAction)

            QTreeWidget.dropEvent(self, event)
            event.acceptProposedAction()
            self.clearSelection()

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:

        icon_action_use = QIcon(PathUtils.icon('present_to_all_cian.png'))
        action_use = QAction('Usar')
        action_use.triggered.connect(self.use_lyric_action)
        action_use.setIcon(icon_action_use)

        icon_edit_action = QIcon(qtawesome.icon('mdi6.file-edit-outline'))
        edit_action = QAction('Editar')
        edit_action.triggered.connect(self.edit_lyric_action)
        edit_action.setIcon(icon_edit_action)

        icon_remove_action = QIcon(qtawesome.icon('mdi6.trash-can-outline', color='#EB5151'))
        remove_action = QAction('Remover')
        remove_action.triggered.connect(self.alert_remove_lyric)
        remove_action.setIcon(icon_remove_action)

        if len(self.selectedItems()) > 1:
            action_use.setText(f'Usar as {len(self.selectedItems())} letras selecionadas')

        menu = QMenu()
        menu.addAction(action_use)
        menu.addAction(edit_action)
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

    def _alert(self, text):
        alert = QMessageBox(self)
        alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        alert.setText(text)

        alert.show()

    def use_lyric_action(self):
        for item in self.selectedItems():
            self.send_to_selected_area(item)

    def remove_lyrics(self):
        for selected_item in self.selectedItems():
            item = selected_item.data(0, Qt.ItemDataRole.UserRole)

            if item is not None:
                LyricsFileManagementService.remove_lyric(Lyric(item['name'], item['author'], None, item['path']))

        ApplicationContext.lyrics_service.refresh()

    def edit_lyric_action(self):
        if len(self.selectedItems()) > 1:
            self._alert("É possível editar apenas uma música por vez.")
            return
        elif len(self.selectedItems()) == 0:
            return

        selected_item = self.selectedItems()[0]
        item = selected_item.data(0, Qt.ItemDataRole.UserRole)
        lyric = LyricsFileManagementService.get_lyric_by_path(item['path'])

        screen = ApplicationContext.window_new_lyric
        screen.update_lyric(Lyric(item['name'], item['author'], lyric, item['path']))
