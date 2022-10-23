from PyQt6.QtWidgets import QHBoxLayout, QDialogButtonBox


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

    def _onClicked(self, button):
        role = self.buttonRole(button)

        if role == QDialogButtonBox.ButtonRole.ApplyRole:
            self.apply()

