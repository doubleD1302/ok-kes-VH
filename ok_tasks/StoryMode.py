from ok import TriggerTask, og

import utils_story
from utils import _simplify_texts

class StoryMode(TriggerTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "半自动剧情模式"
        self.description = "Tự động tua lời thoại cốt truyện và chuyển tiếp các phân cảnh hội thoại"
        self.instructions = """<b>Chế độ Bán tự động Cốt truyện (Story Mode):</b><br><br>
1. <b>Cách bật:</b> Bật khi đang ở các phân cảnh hội thoại hoặc bản đồ cốt truyện để tự động tua nhanh lời thoại.<br>
2. <b>Khi gặp ải chiến đấu:</b> Chọn người thủ công hoặc chuyển sang bật [Tự động Xuất kích] để bot tự đánh.<br>
3. <b>Khi gặp ải Kaos:</b> Chuyển sang bật [Tự động Khiêu chiến Chaos]."""
        self.trigger_interval = 1
        self.all_texts = []
        # 默认关闭，由用户在界面中手动启停，保持 TriggerTask 自己作为主任务运行
        self.default_config['_enabled'] = False

    def enable(self):
        """开启剧情模式时自动禁用出击和卡厄思模式。"""
        from SortieMode import SortieMode
        from ChaosMode import ChaosMode
        sortie = og.executor.get_task_by_class(SortieMode)
        if sortie and sortie.enabled:
            sortie.disable()
        chaos = og.executor.get_task_by_class(ChaosMode)
        if chaos and chaos.enabled:
            chaos.disable()
        super().enable()

    def run(self):
        # 每帧执行一次 OCR 并转简体, 供各页面处理函数复用
        self.all_texts = _simplify_texts(self.ocr())
        # 依次尝试各页面处理函数, 命中(返回 True)即结束本次循环
        for handle_page in utils_story.PAGE_HANDLERS:
            if handle_page(self):
                return
