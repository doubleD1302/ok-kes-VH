# coding:utf-8
import sys
import unittest
from PySide6.QtWidgets import QApplication
from qfluentwidgets import SpinBox, DoubleSpinBox, CompactSpinBox, setTheme, Theme

import ok.gui.widget.SpinBoxPatch


class TestSpinBoxGui(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not QApplication.instance():
            cls.app = QApplication(sys.argv)
        else:
            cls.app = QApplication.instance()

    def test_spin_box_not_collapsed_dark(self):
        setTheme(Theme.DARK)
        sb = SpinBox()
        sb.resize(180, 33)
        sb.show()
        QApplication.processEvents()
        self.assertGreater(sb.lineEdit().width(), 30, f"SpinBox lineEdit collapsed: {sb.lineEdit().geometry()}")

    def test_spin_box_not_collapsed_light(self):
        setTheme(Theme.LIGHT)
        sb = SpinBox()
        sb.resize(180, 33)
        sb.show()
        QApplication.processEvents()
        self.assertGreater(sb.lineEdit().width(), 30, f"SpinBox lineEdit collapsed: {sb.lineEdit().geometry()}")

    def test_double_spin_box_not_collapsed(self):
        setTheme(Theme.DARK)
        dsb = DoubleSpinBox()
        dsb.resize(180, 33)
        dsb.show()
        QApplication.processEvents()
        self.assertGreater(dsb.lineEdit().width(), 30, f"DoubleSpinBox lineEdit collapsed: {dsb.lineEdit().geometry()}")

    def test_compact_spin_box_not_collapsed(self):
        setTheme(Theme.DARK)
        csb = CompactSpinBox()
        csb.resize(180, 33)
        csb.show()
        QApplication.processEvents()
        self.assertGreater(csb.lineEdit().width(), 30, f"CompactSpinBox lineEdit collapsed: {csb.lineEdit().geometry()}")

    def test_spin_box_value_interactions(self):
        setTheme(Theme.DARK)
        sb = SpinBox()
        sb.setRange(0, 999999)
        sb.setValue(62000)
        sb.resize(180, 33)
        sb.show()
        QApplication.processEvents()

        self.assertEqual(sb.value(), 62000)
        self.assertEqual(sb.lineEdit().text(), "62000")

        sb.stepUp()
        self.assertEqual(sb.value(), 62001)

        sb.stepDown()
        self.assertEqual(sb.value(), 62000)

        sb.setReadOnly(True)
        QApplication.processEvents()
        self.assertGreater(sb.lineEdit().width(), 30)

        sb.setReadOnly(False)
        QApplication.processEvents()
        self.assertGreater(sb.lineEdit().width(), 30)


if __name__ == '__main__':
    unittest.main()
