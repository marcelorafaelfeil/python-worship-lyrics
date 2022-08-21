from styles.theme import DarkTheme


header_style = f'''
#HeaderForm QLabel {{
    color: {DarkTheme().text().color().name()};
    font-weight: bold;
}}

