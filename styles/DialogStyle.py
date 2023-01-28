from styles.theme import DarkTheme


btn_default_color = DarkTheme().window().color().lighter(150).name()

dialog_style = f'''
QPushButton {{
    background-color: {btn_default_color};
    min-width: 80px;
}}
QPushButton::disabled {{
    background-color: blued;
}}
'''
