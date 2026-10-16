# coding:utf-8
from PySide6.QtCore import QObject, QEvent
from qfluentwidgets.components.widgets.spin_box import SpinBoxBase

_is_spin_box_patched = False


class LineEditGuard(QObject):
    """Guard lineEdit inside QFluentWidgets SpinBox from collapsing to 1px width in Qt 6."""

    def __init__(self, spin_box):
        super().__init__(spin_box)
        self.spin_box = spin_box
        self._fixing = False

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.Resize, QEvent.Move, QEvent.Show) and not self._fixing:
            # If Qt stylesheet engine collapsed lineEdit to 1px width
            if obj.width() <= 10 and self.spin_box.width() > 30:
                self._fixing = True
                self.fix_geometry()
                self._fixing = False
        return super().eventFilter(obj, event)

    def fix_geometry(self):
        sb = self.spin_box
        if not hasattr(sb, 'lineEdit'):
            return

        right_margin = 10
        if hasattr(sb, 'upButton') and hasattr(sb, 'downButton'):
            if not sb.upButton.isHidden() or not sb.downButton.isHidden():
                btn_w = (sb.upButton.width() or 31) + (sb.downButton.width() or 31) + 15
                right_margin = btn_w
        elif hasattr(sb, 'compactSpinButton'):
            if not sb.compactSpinButton.isHidden():
                right_margin = (sb.compactSpinButton.width() or 26) + 8

        left_margin = 10
        w = max(10, sb.width() - right_margin - left_margin)
        h = max(10, sb.height() - 2)
        sb.lineEdit().setGeometry(left_margin, 1, w, h)


def install_spin_box_patch():
    """Install global fix for QFluentWidgets SpinBox, DoubleSpinBox, and CompactSpinBox."""
    global _is_spin_box_patched
    if _is_spin_box_patched:
        return

    orig_init = SpinBoxBase.__init__
    orig_resize = getattr(SpinBoxBase, 'resizeEvent', None)
    orig_set_read_only = SpinBoxBase.setReadOnly
    orig_set_symbol_visible = SpinBoxBase.setSymbolVisible

    def patched_init(self, parent=None):
        orig_init(self, parent=parent)
        guard = LineEditGuard(self)
        self.lineEdit().installEventFilter(guard)
        self._line_edit_guard = guard

    def patched_resize(self, e):
        if orig_resize:
            orig_resize(self, e)
        else:
            super(SpinBoxBase, self).resizeEvent(e)
        if hasattr(self, '_line_edit_guard'):
            self._line_edit_guard.fix_geometry()

    def patched_set_read_only(self, is_read_only: bool):
        orig_set_read_only(self, is_read_only)
        if hasattr(self, '_line_edit_guard'):
            self._line_edit_guard.fix_geometry()

    def patched_set_symbol_visible(self, is_visible: bool):
        orig_set_symbol_visible(self, is_visible)
        if hasattr(self, '_line_edit_guard'):
            self._line_edit_guard.fix_geometry()

    SpinBoxBase.__init__ = patched_init
    SpinBoxBase.resizeEvent = patched_resize
    SpinBoxBase.setReadOnly = patched_set_read_only
    SpinBoxBase.setSymbolVisible = patched_set_symbol_visible

    _is_spin_box_patched = True


# Auto-install on module import
install_spin_box_patch()
