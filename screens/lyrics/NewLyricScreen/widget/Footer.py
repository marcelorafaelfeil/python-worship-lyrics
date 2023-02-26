from PyQt6.QtWidgets import QDialogButtonBox


class Footer(QDialogButtonBox):

    def __init__(self, on_save, on_cancel):
        super().__init__()

        save_button = QDialogButtonBox.StandardButton.Save
        cancel_button = QDialogButtonBox.StandardButton.Cancel

        self.setStandardButtons(save_button | cancel_button)
        self.accepted.connect(on_save)
        self.rejected.connect(on_cancel)
