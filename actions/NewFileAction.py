from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination


class NewFileAction(QAction):
    def __init__(self, parent):
        super(NewFileAction, self).__init__(parent)

        self.setText('New File')
        self.triggered.connect(self._newFile)

        self.setShortcut(QKeySequence(QKeyCombination(Qt.Modifier.CTRL, Qt.Key.Key_N)))

    def _newFile(self):
        print('Ué...')

