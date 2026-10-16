# coding:utf-8
import sys
from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            OptionsValidator, RangeConfigItem, RangeValidator,
                            ConfigSerializer, Theme)

from ok.util.file import get_relative_path


class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.SimplifiedChineseScript)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.TraditionalChineseScript)
    ENGLISH = QLocale(QLocale.English)
    SPANISH = QLocale(QLocale.Spanish)
    JAPANESE = QLocale(QLocale.Japanese)
    KOREAN = QLocale(QLocale.Korean)
    VIETNAMESE = QLocale(QLocale.Vietnamese)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        if value == "Auto":
            return Language.AUTO
        try:
            return Language(QLocale(value))
        except ValueError:
            loc = QLocale(value)
            for lang in Language:
                if lang != Language.AUTO and lang.value.language() == loc.language():
                    return lang
            return Language.AUTO


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


class AppConfig(QConfig):
    """ Config of application """

    # main window
    micaEnabled = ConfigItem("MainWindow", "MicaEnabled", isWin11(), BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.VIETNAMESE, OptionsValidator(Language), LanguageSerializer(), restart=True)

    # Material
    blurRadius = RangeConfigItem("Material", "AcrylicBlurRadius", 15, RangeValidator(0, 40))

    # software update
    checkUpdateAtStartUp = ConfigItem("Update", "CheckUpdateAtStartUp", True, BoolValidator())


cfg = AppConfig()
_ui_config_path = get_relative_path('configs', "ui_config.json")
cfg.themeMode.value = Theme.AUTO
qconfig.load(_ui_config_path, cfg)

if __name__ == '__main__':
    locale = Language.ENGLISH
    print(locale.name)
    print(locale.value.name())
    print(locale.value.language())
    print(QLocale.languageToString(locale.value.language()))
