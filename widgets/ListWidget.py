from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QListWidget, QAbstractScrollArea


class ListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

    def minimumSizeHint(self) -> QSize:
        return QSize(-1, -1)

    def viewportSizeHint(self) -> QSize:
        if self.model().rowCount() == 0:
            return QSize(self.width(), 0)
        height = sum(self.sizeHintForRow(i) for i in range(self.count()) if not self.item(i).isHidden())
        width = super().viewportSizeHint().width()
        return QSize(width, height)

