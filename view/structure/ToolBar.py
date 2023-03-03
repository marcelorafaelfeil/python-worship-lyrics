from PyQt6.QtWidgets import QToolBar
from actions.NewFileAction import NewLyricAction


class ToolBar(QToolBar):
    def __init__(self):
        super(ToolBar, self).__init__()

        self.addAction(NewLyricAction(self))
