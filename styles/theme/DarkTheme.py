from PyQt6.QtGui import QPalette, QColor


class DarkTheme(QPalette):
    def __init__(self):
        super(DarkTheme, self).__init__()

        self.setColor(QPalette.ColorRole.Window, QColor('#282A37'))
        self.setColor(QPalette.ColorRole.Base, QColor('#191A22'))
        self.setColor(QPalette.ColorRole.Text, QColor('#EFEFEF'))
        self.setColor(QPalette.ColorRole.WindowText, QColor('#EFEFEF'))
        self.setColor(QPalette.ColorRole.Button, QColor('#282A37'))
        self.setColor(QPalette.ColorRole.Highlight, QColor(38, 40, 52))
        self.setColor(QPalette.ColorRole.HighlightedText, QColor(150, 236, 234))
        self.setColor(QPalette.ColorRole.PlaceholderText, QColor('#CCCCCC'))
