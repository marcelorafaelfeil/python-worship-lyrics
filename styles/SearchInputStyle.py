from styles.theme import DarkTheme


search_content_style = f'''
#SearchContent {{
    border-bottom: 1px solid #111111;
}}
#SearchContent QLineEdit {{
    padding: 5px;
    margin: 0px;
}}
#SearchContent QPushButton {{
    padding: 5px;
    border: 1px solid {DarkTheme().base().color().name()};
    background-color: {DarkTheme().base().color().name()};
    margin-right: 2px;
}}
'''
