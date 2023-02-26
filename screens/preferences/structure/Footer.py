from PyQt6.QtWidgets import QDialogButtonBox


class Footer(QDialogButtonBox):

    def __init__(self, accept, reject, apply):
        super(Footer, self).__init__()

        self.apply = apply

        btn = QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Ok

        self.setStandardButtons(btn)
        self.setFixedWidth(450)

        self.clicked.connect(self._onClicked)
        self.accepted.connect(accept)
        self.rejected.connect(reject)

        self.setContentsMargins(0, 0, 10, 10)

    def disableApplyButton(self):
        self.buttons()[2].setDisabled(True)

    def enableApplyButton(self):
        self.buttons()[2].setDisabled(False)

    def _onClicked(self, button):
        role = self.buttonRole(button)

        if role == QDialogButtonBox.ButtonRole.ApplyRole:
            self.apply()

