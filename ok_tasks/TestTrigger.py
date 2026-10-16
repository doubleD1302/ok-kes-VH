from ok import TriggerTask

from utils_sortie import handle_secret_enemy


class TestTrigger(TriggerTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "测试trigger"
        self.description = "测试trigger"
        self.trigger_interval = 2
        self.instructions = """<b>Nhiệm vụ Xử lý Kẻ địch bí mật:</b><br><br>
Tự động phát hiện và xử lý tương tác khi chạm trán Kẻ địch bí mật trong ải."""

    def run(self):
        self.all_texts = self.ocr()
        handle_secret_enemy(self)
