from qfluentwidgets import DoubleSpinBox

import ok.gui.widget.SpinBoxPatch
from ok.gui.common.design_system import DesignToken
from ok.gui.tasks.ConfigLabelAndWidget import ConfigLabelAndWidget


class LabelAndDoubleSpinBox(ConfigLabelAndWidget):

    def __init__(self, config_desc, config, key: str, config_type=None):
        super().__init__(config_desc, config, key)
        self.key = key
        self.spin_box = DoubleSpinBox()
        range_min = config_type.get('min', -99999999.0) if isinstance(config_type, dict) else -99999999.0
        range_max = config_type.get('max', 99999999.0) if isinstance(config_type, dict) else 99999999.0
        self.spin_box.setRange(range_min, range_max)
        self.update_value()
        self.spin_box.valueChanged.connect(self.value_changed)
        self.spin_box.setFixedWidth(DesignToken.CONTROL_WIDTH)
        self.add_widget(self.spin_box)

    def update_value(self):
        val = self.config.get(self.key)
        if val is not None:
            try:
                self.spin_box.setValue(float(val))
            except (ValueError, TypeError):
                pass

    def value_changed(self, value):
        self.update_config(value)
