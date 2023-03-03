from view.styles.theme import DarkTheme

title_content_style = f'''
#TabTitle {{
    padding: 5px;
    background-color: {DarkTheme().window().color().name()};
}}
'''

title_action_style = f'''
QPushButton {{
    width: 12px;
    height: 12px;
    padding: 5px;
    border: 0px;
}}
QPushButton:hover {{
    background-color: rgba(232, 93, 202, 0.3);
    border: 1px solid rgba(232, 93, 202, 0.5)
}}
'''
