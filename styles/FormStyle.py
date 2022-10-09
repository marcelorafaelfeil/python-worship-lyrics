from services.utils import PathUtils
from styles.theme import DarkTheme

input_style = f'''
QLineEdit {{
    border: 3px solid {DarkTheme().base().color().name()};
    background-color: {DarkTheme().base().color().name()};
    margin: 0px;
    padding: 3px;
}}
QLineEdit:focus {{
    border: 3px solid {DarkTheme().link().color().name()};
    border-radius: 2px;
}}
'''

spinbox_style = f'''
QSpinBox {{
    border: 3px solid {DarkTheme().base().color().name()};
    background-color: {DarkTheme().base().color().name()};
    margin: 0px;
    padding: 3px;
}}
QSpinBox:focus {{
    border: 3px solid {DarkTheme().link().color().name()};
    border-radius: 2px;
}}
QSpinBox::up-button, QSpinBox::down-button {{
    width: 15px;
}}
QSpinBox::up-arrow {{
    image: url({PathUtils.icon('arrow_drop_up_cropped.png')});
    width: 7px;
    height: 7px;
}}
QSpinBox::down-arrow {{
    image: url({PathUtils.icon('arrow_drop_down_cropped.png')});
    width: 7px;
    height: 7px;
}}
'''

checkbox_style = f'''
QCheckBox::indicator {{
    width: 12px;
    height: 12px;
    border: 1px solid {DarkTheme().base().color().lighter(350).name()};
    border-radius: 2px;
    margin: 0px;
    margin-left: 2px;
    margin-right: 5px;
}}
QCheckBox::indicator:checked {{
    border: 1px solid {DarkTheme().link().color().name()};
    background-color: {DarkTheme().link().color().name()};
    image: url({PathUtils.icon('check-bold-12.png')});
}}
'''

radiobutton_style = f'''
QRadioButton::indicator {{
    width: 12px;
    height: 12px;
    border: 1px solid {DarkTheme().base().color().lighter(350).name()};
    border-radius: 7px;
    margin: 0px;
    margin-left: 2px;
    margin-right: 5px;
}}

QRadioButton::indicator::checked {{
    border: 1px solid {DarkTheme().link().color().name()};
    image: url({PathUtils.icon('radio_bullet.png')});
}}
'''
