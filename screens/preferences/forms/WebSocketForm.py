import functools
import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from screens.preferences.forms import SettingsForm
from widgets import Label
from widgets.form import Input, Row, RadioButton, SpinBox
from .FormHeader import FormHeader


class WebSocketForm(SettingsForm):
    _use_custom_key: str = SettingsForm._settings_prefix_key + '.use_custom'
    _host_key: str = SettingsForm._settings_prefix_key + '.host'
    _port_key: str = SettingsForm._settings_prefix_key + '.port'

    def __init__(self):
        SettingsForm.__init__(self)

        self.values = self._current_config['websocket']
        self.websocket_form: {QWidget} = {}
        self.websocket_labels: {Label} = {}

        layout = QVBoxLayout()
        layout.addWidget(FormHeader('WebSocket'))
        layout.addWidget(self._renderForm(), 1)

        self.setLayout(layout)

    def _renderForm(self) -> QWidget:
        form = self.websocket_form

        form_content_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        not_use_custom = QVBoxLayout()
        use_custom_row = QVBoxLayout()

        not_use_custom_radio = RadioButton('Não usar configurações personalizadas')
        not_use_custom_radio.setChecked(not self.values['use_custom'])

        use_custom_radio = RadioButton('Usar configurações de websocket personalizadas')
        use_custom_radio.setChecked(self.values['use_custom'])

        form.update({'not_use_custom': not_use_custom_radio})
        form.update({'use_custom': use_custom_radio})

        not_use_custom.addWidget(form.get('not_use_custom'))
        not_use_custom.setAlignment(Qt.AlignmentFlag.AlignTop)
        not_use_custom.setContentsMargins(0, 0, 0, 0)

        use_custom_row.addWidget(form.get('use_custom'))
        use_custom_row.addWidget(self.renderCustomWebsocket())
        use_custom_row.setAlignment(Qt.AlignmentFlag.AlignTop)
        use_custom_row.setContentsMargins(0, 0, 0, 0)

        layout.addLayout(not_use_custom)
        layout.addLayout(use_custom_row)

        form.get('use_custom').toggled.connect(lambda x: self.setDisabledCustomWebsocket(not x))

        form_content_widget.setLayout(layout)
        self.setDisabledCustomWebsocket(not self.values['use_custom'])

        self.formObserver()

        return form_content_widget

    def renderCustomWebsocket(self) -> QWidget:
        form: {QWidget} = self.websocket_form
        labels: {Label} = self.websocket_labels
        fixed_label_width: int = 50

        host_label = Label('Host: ')
        host_label.setFixedWidth(fixed_label_width)
        host_label.setContentsMargins(0, 0, 5, 0)

        port_label = Label('Porta: ')
        port_label.setFixedWidth(fixed_label_width)
        port_label.setContentsMargins(0, 0, 5, 0)

        labels.update({'host_name': host_label})
        labels.update({'port_number': port_label})

        form.update({'websocket_host': Input(placeholder='0.0.0.0', value=self.values['host'])})
        form.update({'websocket_port': SpinBox(value=self.values['port'])})

        row = Row()
        row.addWidget(labels.get('host_name'))
        row.addWidget(form.get('websocket_host'))
        row.setContentsMargins(23, 0, 0, 0)

        row_port = Row()
        row_port.addWidget(labels.get('port_number'))
        row_port.addWidget(form.get('websocket_port'))
        row_port.setContentsMargins(23, 0, 0, 0)

        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(row)
        vertical_layout.addLayout(row_port)

        use_custom_widget_1 = QWidget()
        use_custom_widget_1.setLayout(vertical_layout)

        return use_custom_widget_1

    def formObserver(self):
        for field_name in self.websocket_form.keys():
            item = self.websocket_form.get(field_name)

            if isinstance(item, Input):
                item.textChanged.connect(functools.partial(self._changedEvent, field_name, item))
            elif isinstance(item, SpinBox):
                item.valueChanged.connect(functools.partial(self._changedEvent, field_name, item))
            elif isinstance(item, RadioButton) and field_name == 'use_custom':
                item.toggled.connect(functools.partial(self._changedEvent, field_name, item))

    def _changedEvent(self, field_name, item):
        key: str = ''

        try:
            if field_name == 'websocket_host':
                key = self._host_key
            elif field_name == 'websocket_port':
                key = self._port_key
            elif field_name == 'use_custom' or field_name == 'not_use_custom':
                key = self._use_custom_key

            if isinstance(item, RadioButton):
                value = item.isChecked()

                if item.isChecked():
                    self.savePropertyInTemporaryFile(self._port_key, self.websocket_form.get('websocket_port').text())
                    self.savePropertyInTemporaryFile(self._host_key, self.websocket_form.get('websocket_host').text())
            elif isinstance(item, Input):
                value = item.text()
            else:
                value = item.value()

            self.savePropertyInTemporaryFile(key, value)
        except Exception as err:
            logging.error('Internal error to identify the aciton to be saved in the settings temporary file.', err)

    def setDisabledCustomWebsocket(self, disabled: bool):
        labels: {Label} = self.websocket_labels
        form: {QWidget} = self.websocket_form

        labels.get('host_name').setDisabled(disabled)
        form.get('websocket_host').setDisabled(disabled)

        labels.get('port_number').setDisabled(disabled)
        form.get('websocket_port').setDisabled(disabled)
