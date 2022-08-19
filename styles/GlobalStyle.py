from services.utils import PathUtils
from styles.theme import DarkTheme


global_style = f'''
QMainWindow::separator {{
    border: 2px solid #111111;
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
QLineEdit, QComboBox {{
    padding: 5px;
    margin: 0px;
}}
QComboBox::drop-down {{
    width: 24px;
    border: 0px;
}}
QComboBox::down-arrow {{
    width: 24px;
    height: 24px;
    image: url({PathUtils.icon('arrow_drop_down.png')});
}}
QPushButton {{
    padding: 5px;
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
'''
