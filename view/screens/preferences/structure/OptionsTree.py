from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem

from view.screens.preferences.forms import ListForms as forms


class OptionsTree(QTreeWidget):
    def __init__(self, parent, _on_option_selected=None):
        super(OptionsTree, self).__init__()

        self._on_option_selected = _on_option_selected
        self._default_item: QTreeWidgetItem | None = None
        self.setHeaderHidden(True)
        self._loadItems()
        self.setMinimumWidth(250)

        self.currentItemChanged.connect(self._onSelect)

    def _loadItems(self):
        items = self._loadOptions(forms.options)
        self.insertTopLevelItems(0, items)

    def _loadOptions(self, list_forms):
        list_items = []

        for form in list_forms:
            item = QTreeWidgetItem()
            item.setText(0, form['label'])
            if 'options' in form:
                item.addChildren(self._loadOptions(form['options']))
            else:
                item.setData(0, Qt.ItemDataRole.UserRole, form['widget'])

            list_items.append(item)

            if form == forms.default_option:
                self._default_item = list_items[-1]

        return list_items

    def _onSelect(self, widget_item: QTreeWidgetItem):
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)
        self._on_option_selected(item)

    def selectDefault(self):
        self.setCurrentItem(self._default_item)
