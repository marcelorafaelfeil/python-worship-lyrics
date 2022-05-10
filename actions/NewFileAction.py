from PyQt6.QtGui import QAction


class NewFileAction(QAction):
    def __init__(self, parent):
        super(NewFileAction, self).__init__(parent)

        self.setText('New File')

