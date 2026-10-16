from PySide6.QtWidgets import QSizePolicy
from qfluentwidgets import PushButton, BodyLabel

from ok import og
from ok.gui.tasks.ConfigLabelAndWidget import ConfigLabelAndWidget
from ok.gui.tasks.ModifyListDialog import ModifyListDialog
from ok.gui.widget.UpdateConfigWidgetItem import value_to_string


MAX_LIST_DISPLAY_LENGTH = 100


class ModifyListItem(ConfigLabelAndWidget):

    def __init__(self, config_desc, config, key: str, options_available=None, allow_duplication=False):
        super().__init__(config_desc, config, key)
        self.options_available = options_available
        self.allow_duplication = allow_duplication
        self.switch_button = PushButton(self.tr('Modify'))
        self.switch_button.clicked.connect(self.clicked)
        self.list_text = BodyLabel("")
        self.list_text.setWordWrap(False)
        self.list_text.setMaximumWidth(550)
        self.list_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.update_value()
        self.add_widget(self.list_text, stretch=0)
        self.add_widget(self.switch_button, stretch=0)

    def update_value(self):
        items = self.config.get(self.key) or []
        display_items = [og.app.tr(item) for item in items]
        full_text = value_to_string(display_items)
        display_text = full_text
        if len(display_text) > MAX_LIST_DISPLAY_LENGTH:
            display_text = f'{display_text[:MAX_LIST_DISPLAY_LENGTH - 3]}...'
        self.list_text.setText(display_text)
        self.list_text.setToolTip(full_text if display_text != full_text else '')

    def clicked(self):
        dialog = ModifyListDialog(
            self.config.get(self.key) or [], self.window(), options_available=self.options_available,
            allow_duplication=self.allow_duplication, title_text=self.key
        )
        dialog.list_modified.connect(self.list_modified)
        dialog.exec()

    def list_modified(self, the_list):
        self.update_config(the_list)
        self.update_value()

