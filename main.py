import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

from actions.NewFileAction import NewFileAction
from core import ApplicationContext
from structure import PresentationScreen
from widgets import LyricsWidget, SelectedListLyricsWidget, CurrentLyricWidget
from widgets.tab import Tab, TabTitle

app_style = """
QMainWindow::separator {
    border: 2px solid #111111;
}
"""

window_style = """
background-color: #282A37;
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        context = ApplicationContext()

        self.setStyleSheet(window_style)
        self.setWindowTitle('Worship Lyrics')
        self.resize(QSize(1024, 600))

        context.lyricsHandle().loadLyrics()
        lyrics_list = context.lyricsHandle().getLyricsList()

        lyrics_tab = Tab(self)
        lyrics_tab.setTitleBarWidget(TabTitle('Letras'))
        lyrics_tab.setBody(LyricsWidget(context, lyrics_list))

        selected_lyrics_tab = Tab(self)
        selected_lyrics_tab.setTitleBarWidget(TabTitle('Letras selecionadas'))
        selected_lyrics_tab.setBody(SelectedListLyricsWidget(context))

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, lyrics_tab)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, selected_lyrics_tab)
        self.setDockOptions(QMainWindow.DockOption.AnimatedDocks | QMainWindow.DockOption.GroupedDragging)

        self.setCentralWidget(PresentationScreen(context))

        lyric_bar_tab = Tab(self)
        lyric_bar_tab.setTitleBarWidget(TabTitle('Letra selecionada'))
        lyric_bar_tab.setBody(CurrentLyricWidget(context), False)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, lyric_bar_tab)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(NewFileAction(self))


app = QApplication(sys.argv)
app.setStyleSheet(app_style)
app.setDesktopSettingsAware(True)

window = MainWindow()
window.show()

app.exec()

