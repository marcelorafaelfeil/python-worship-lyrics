from view.styles.theme import DarkTheme


search_content_style = f'''
#SearchContent {{
    border-bottom: 1px solid #111111;
}}
#SearchContent QLineEdit {{
    padding: 5px;
    margin: 0px;
    border-radius: 0x;
}}
#SearchContent QPushButton {{
    padding: 5px;
    border: 1px solid {DarkTheme().base().color().name()};
    background-color: {DarkTheme().base().color().name()};
    margin-right: 1px;
    border-radius: 0x;
}}
#SearchContent QComboBox {{
    border-radius: 0x;
}}
'''
