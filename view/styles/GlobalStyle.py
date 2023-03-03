from services.utils import PathUtils
from view.styles.theme import DarkTheme

global_style = f'''
QMainWindow::separator {{
    width: 2px;
    background-color: {DarkTheme().window().color().darker(150).name()};
}}
QHeaderView::section {{
    background-color: {DarkTheme().window().color().name()};
    color: {DarkTheme().text().color().name()};
    padding: 3px 5px;
    border: 0px;
}}
QHeaderView::section:first {{
    border-right: 1px solid #111111;
}}

QLineEdit, QPlainTextEdit {{
    border: 3px solid {DarkTheme().base().color().name()};
    background-color: {DarkTheme().base().color().name()};
    margin: 0px;
    padding: 3px;
}}
QLineEdit:focus, QPlainTextEdit:focus {{
    border: 3px solid {DarkTheme().link().color().name()};
    border-radius: 2px;
}}
QLineEdit, QComboBox {{
    padding: 3px;
    margin: 0px;
}}

QComboBox {{
    padding: 5px;
    background-color: {DarkTheme().window().color().darker(150).name()};
    border: 1px solid #FF0000;
    border-radius: 3px;
}}

QComboBox::drop-down {{
    width: 24px;
    border: 0px;
}}
QComboBox::down-arrow {{
    width: 18px;
    height: 18px;
    image: url('assets/icons/arrow_drop_down.png');
}}

QPushButton {{
    border-radius: 3px;
    padding: 5px;
    color: #FFFFFF;
    border: 1px solid #43475d;
}}
QPushButton:disabled {{
    color: rgba(255, 255, 255, 0.3);
    background-color: rgba({DarkTheme().window().color().lighter(180).name()}, 0.5);
}}
QPushButton:hover {{
    background-color: {DarkTheme().window().color().lighter(180).name()};
}}

QDialogButtonBox QPushButton {{
    min-width: 80px;
}}

QScrollBar:vertical {{
    background: {DarkTheme().base().color().name()};
    width: 5px;
    margin: 0px;
}}
QScrollBar::handle:vertical {{
    background: {DarkTheme().window().color().name()};
    min-height: 20px;
}}
QScrollBar::add-line:vertical {{
    height: 0px;
}}
QScrollBar::sub-line:vertical {{
    height: 0px;
}}
QScrollBar:horizontal {{
    background: {DarkTheme().base().color().name()};
    height: 5px;
    margin: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {DarkTheme().window().color().name()};
    min-width: 20px;
}}
QScrollBar::add-line:horizontal {{
    height: 0px;
}}
QScrollBar::sub-line:horizontal {{
    height: 0px;
}}

QTreeView {{
    font-size: 12px;
}}
QTreeView::item {{
    padding: 3px 0;
}}

QMessageBox {{
    background-color: {DarkTheme().window().color().name()};
    color: {DarkTheme().text().color().name()};
}}
QMessageBox QPushButton {{
    background-color: {DarkTheme().window().color().darker(150).name()};
}}

WLTitleBar > QWidget {{
    border-bottom: 2px solid {DarkTheme().window().color().darker(150).name()};
}}

QMenuBar {{
    background-color: transparent;
    color: {DarkTheme().windowText().color().name()};
    padding: 5px 15px;
}}
QMenuBar::item {{
    padding: 2px 8px;
    background-color: transparent;
    border-radius: 5px;
}}
QMenuBar::item:selected {{
    background-color: {DarkTheme().window().color().lighter(140).name()};
    color: {DarkTheme().highlightedText().color().name()}
}}
QMenu {{
    background-color: {DarkTheme().window().color().name()};
    color: {DarkTheme().windowText().color().name()};
    padding: 8px;
}}
QMenu::icon {{
    padding-left: 10px;
}}
QMenu::item {{
    padding: 3px 10px;
}}
QMenu::item:selected {{
    background-color: {DarkTheme().window().color().lighter(140).name()};
    border-radius: 3px;
}}
QMenu::item:disabled {{
    color: {DarkTheme().windowText().color().darker(150).name()};
}}
QMenu::item:disabled:selected {{
    background-color: transparent;
}}
'''
