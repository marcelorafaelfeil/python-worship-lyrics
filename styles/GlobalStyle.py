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
    background-color: {DarkTheme().window().color().name()};
    border: 1px solid #43475d;
}}

QComboBox::drop-down {{
    width: 24px;
    border: 0px;
}}
QComboBox::down-arrow {{
    width: 24px;
    height: 24px;
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
'''
