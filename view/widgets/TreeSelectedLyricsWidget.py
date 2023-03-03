from typing import List

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView, QMenu

from view import styles
from services.utils import PathUtils
from actions.SelectedLyrics import RemoveAction


class TreeSelectedLyricsWidget(QTreeWidget):
    item_default_flags = (
            Qt.ItemFlag.ItemNeverHasChildren | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsDragEnabled
            | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled
    )

    def __init__(self, columns: List[str]):
        super().__init__()
        self._on_select_item = None
        self._on_focus = None
        self._on_focus_out = None

        self.setColumnCount(2)
        self.setIndentation(0)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setHeaderLabels(columns)
        self.setItemsExpandable(False)
        self.doubleClicked.connect(self._doubleClicked)

    def setOnFocus(self, _fn):
        self._on_focus = _fn

    def setOnFocusOut(self, _fn):
        self._on_focus_out = _fn

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        if self._on_focus is not None:
            self._on_focus()
        
        super(TreeSelectedLyricsWidget, self).focusInEvent(e)
        
    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        if self._on_focus_out is not None:
            self._on_focus_out()
            
        super(TreeSelectedLyricsWidget, self).focusOutEvent(e)

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

    def removeSelectedItem(self):
        if len(self.selectedItems()) > 0:
            self.takeTopLevelItem(self.indexOfTopLevelItem(self.selectedItems()[0]))

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        clicked_item = self.itemAt(event.pos())

        icon_action_clear_all = QIcon(PathUtils.icon('clear_all_red.png'))
        action_clear_all = QAction()
        action_clear_all.setText('Limpar tudo')
        action_clear_all.triggered.connect(self._clear)
        action_clear_all.setIcon(icon_action_clear_all)

        icon = QIcon(PathUtils.icon('delete_red.png'))
        action_remove_item = QAction()
        action_remove_item.setText('Remover')
        action_remove_item.triggered.connect(self.removeSelectedItem)
        action_remove_item.setIcon(icon)
        action_remove_item.setShortcut(QKeySequence(Qt.Key.Key_A))

        icon_action_project = QIcon(PathUtils.icon('smart_display_green.png'))
        action_project = QAction()
        action_project.setText('Projetar')
        action_project.triggered.connect(lambda: self.sendToProjector(clicked_item))
        action_project.setIcon(icon_action_project)

        menu = QMenu()

        if clicked_item is not None:
            menu.addAction(action_project)
            menu.addAction(RemoveAction())
            menu.addSeparator()

        menu.addAction(action_clear_all)

        menu.setShortcutEnabled(True)
        menu.setStyleSheet(styles.context_menu_style)
        menu.exec(event.globalPos())
