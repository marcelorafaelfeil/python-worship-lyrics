from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from widgets.form import Input, Row, RadioButton, SpinBox
from widgets import Label
from .FormHeader import FormHeader


class WebSocketForm(QWidget):
    def __init__(self):
        super(WebSocketForm, self).__init__()

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

        use_custom_radio = RadioButton('Não usar configurações personalizadas')
        use_custom_radio.setChecked(True)

        form.update({'not_use_custom': use_custom_radio})
        form.update({'use_custom': RadioButton('Usar configurações de websocket personalizadas')})

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
        self.setDisabledCustomWebsocket(True)

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

        form.update({'websocket_host': Input(placeholder='0.0.0.0')})
        form.update({'websocket_port': SpinBox(value=4041)})

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

    def setDisabledCustomWebsocket(self, disabled: bool):
        labels: {Label} = self.websocket_labels
        form: {QWidget} = self.websocket_form

        labels.get('host_name').setDisabled(disabled)
        form.get('websocket_host').setDisabled(disabled)

        labels.get('port_number').setDisabled(disabled)
        form.get('websocket_port').setDisabled(disabled)
