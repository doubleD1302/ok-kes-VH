import os
import sys
import unittest

# Add ok_tasks and project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OK_TASKS_DIR = os.path.join(PROJECT_ROOT, "ok_tasks")
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if OK_TASKS_DIR not in sys.path:
    sys.path.insert(0, OK_TASKS_DIR)

class MockBox:
    def __init__(self, name, x=0.5, y=0.5, width=0.1, height=0.05):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class MockTask:
    def __init__(self, game_lang="简体中文", all_texts=None, width=1920, height=1080):
        self.config = {"游戏语言": game_lang}
        self.default_config = {}
        self.all_texts = all_texts or []
        self.width = width
        self.height = height
        self.name = "MockTask"

    def log_info(self, msg):
        pass


class TestMultiLangSupport(unittest.TestCase):

    def test_syntax_and_import_maps(self):
        """1. Kiểm tra cú pháp và khả năng import các file bản đồ ngôn ngữ"""
        import ok_tasks.assets.game_text_map.en as en_map
        import ok_tasks.assets.game_text_map.vi as vi_map
        import ok_tasks.assets.game_text_map.zh_tw as tw_map
        
        self.assertIsInstance(en_map.SERVER_TEXT_MAP, dict)
        self.assertIsInstance(vi_map.SERVER_TEXT_MAP, dict)
        self.assertIsInstance(tw_map.SERVER_TEXT_MAP, dict)
        self.assertGreater(len(en_map.SERVER_TEXT_MAP), 40)
        self.assertGreater(len(vi_map.SERVER_TEXT_MAP), 40)

    def test_syntax_and_import_tasks(self):
        """2. Kiểm tra cú pháp và import utils, ChaosMode, SortieMode"""
        import ok_tasks.utils as utils
        from ok_tasks.ChaosMode import ChaosMode
        from ok_tasks.SortieMode import SortieMode

        self.assertIn("English", utils._GAME_LANG_FILE_MAP)
        self.assertIn("Tiếng Việt", utils._GAME_LANG_FILE_MAP)
        self.assertIn("繁体中文", utils._GAME_LANG_FILE_MAP)

    def test_load_game_text_map(self):
        """3. Kiểm tra hàm _load_game_text_map hoạt động và có caching"""
        from ok_tasks.utils import _load_game_text_map, _LOADED_MAPS
        
        en_dict = _load_game_text_map("English")
        self.assertIn("English", _LOADED_MAPS)
        self.assertEqual(en_dict.get("继续"), "Continue")

        vi_dict = _load_game_text_map("Tiếng Việt")
        self.assertIn("Tiếng Việt", _LOADED_MAPS)
        self.assertEqual(vi_dict.get("继续"), "Tiếp tục")

    def test_get_game_text(self):
        """4. Kiểm tra _get_game_text trả về đúng giá trị theo từng ngôn ngữ cấu hình"""
        from ok_tasks.utils import _get_game_text
        
        task_cn = MockTask(game_lang="简体中文")
        self.assertEqual(_get_game_text(task_cn, "继续"), "继续")

        task_tw = MockTask(game_lang="繁体中文")
        self.assertEqual(_get_game_text(task_tw, "继续"), "继续进行")

        task_en = MockTask(game_lang="English")
        self.assertEqual(_get_game_text(task_en, "继续"), "Continue")

        task_vi = MockTask(game_lang="Tiếng Việt")
        self.assertEqual(_get_game_text(task_vi, "继续"), "Tiếp tục")

    def test_find_text_synonyms(self):
        """5. Kiểm tra hàm find_text với MULTI_LANG_SYNONYMS"""
        from ok_tasks.utils import find_text

        # Test Vietnamese OCR button match
        task_vi = MockTask(all_texts=[MockBox("Xác nhận"), MockBox("Tiếp tục")])
        hit = find_text(task_vi, "确认")
        self.assertIsNotNone(hit)
        self.assertEqual(hit.name, "Xác nhận")

        # Test English OCR button match
        task_en = MockTask(all_texts=[MockBox("CONFIRM"), MockBox("CANCEL")])
        hit_en = find_text(task_en, "确认")
        self.assertIsNotNone(hit_en)
        self.assertEqual(hit_en.name, "CONFIRM")

    def test_clean_match(self):
        """6. Kiểm tra hàm _clean_match loại bỏ ký tự lạ và khớp từ đồng nghĩa đa ngữ"""
        from ok_tasks.utils import _clean_match

        self.assertTrue(_clean_match("Xác nhận!", "确认"))
        self.assertTrue(_clean_match("[Confirm]", "确认"))
        self.assertTrue(_clean_match("xac nhan", "确认"))
        self.assertTrue(_clean_match("Rời khỏi", "离开"))
        self.assertTrue(_clean_match("Exit", "离开"))
        self.assertTrue(_clean_match("Bỏ qua", "跳过"))

    def test_route_normalize_map(self):
        """7. Kiểm tra hàm _get_route_priority chuẩn hóa từ đa ngữ về chuẩn nội bộ"""
        from ok_tasks.utils import _get_route_priority
        
        task_en = MockTask()
        task_en.config['路线优先级'] = ["Rest", "Elite", "Event", "Enemy"]
        p_en = _get_route_priority(task_en)
        self.assertEqual(p_en, ["休息", "精英", "事件", "小怪"])

        task_vi = MockTask()
        task_vi.config['路线优先级'] = ["Nghỉ ngơi", "Tinh anh", "Sự kiện", "Quái thường"]
        p_vi = _get_route_priority(task_vi)
        self.assertEqual(p_vi, ["休息", "精英", "事件", "小怪"])

    def test_card_name_matching(self):
        """8. Kiểm tra hàm _match_card_name khớp tên thẻ bài Trung - Anh"""
        from ok_tasks.utils import _match_card_name

        # Config Chinese, OCR English
        self.assertTrue(_match_card_name("剑雨", "Rain of Swords"))
        self.assertTrue(_match_card_name("展开极光", "Cast Aurora"))
        self.assertTrue(_match_card_name("剑雨", "Sword Rain"))
        self.assertTrue(_match_card_name("展开极光", "Effulgent Expansion"))

        # Config English, OCR Chinese
        self.assertTrue(_match_card_name("Rain of Swords", "剑雨"))
        self.assertTrue(_match_card_name("Sword Rain", "剑雨"))
        self.assertTrue(_match_card_name("Cast Aurora", "展开极光"))
        self.assertTrue(_match_card_name("Effulgent Expansion", "展开极光"))

        # Case insensitive & partial
        self.assertTrue(_match_card_name("rain of swords", " [Rain of Swords] +1 "))
        self.assertTrue(_match_card_name("sword rain", " [Sword Rain] +1 "))

    def test_task_keyword_matching(self):
        """9. Kiểm tra hàm _match_task_keyword khớp từ khóa nhiệm vụ đa ngữ hai chiều"""
        from ok_tasks.utils import _match_task_keyword

        # Chinese keyword with English / Vietnamese description
        self.assertTrue(_match_task_keyword("信用点增加", "Gain 100 Credits upon clear"))
        self.assertTrue(_match_task_keyword("信用点增加", "Nhận thêm 50 Tín dụng"))
        self.assertTrue(_match_task_keyword("复制", "Duplicate a selected card"))
        self.assertTrue(_match_task_keyword("复制", "Sao chép 1 thẻ bài"))
        self.assertTrue(_match_task_keyword("压力", "Giảm 20 Áp lực cho toàn đội"))

        # English keyword with Chinese description
        self.assertTrue(_match_task_keyword("Credit Increase", "获得50信用点增加"))
        self.assertTrue(_match_task_keyword("Duplicate", "复制1张手牌"))

        # Vietnamese keyword with Chinese description
        self.assertTrue(_match_task_keyword("Tăng tín dụng", "获得50信用点增加"))
        self.assertTrue(_match_task_keyword("Xóa thẻ", "移除手牌中的卡牌"))

    def test_equipment_mapping(self):
        """10. Kiểm tra từ điển trang bị EQUIPMENT_NAME_MAP"""
        from ok_tasks.utils import EQUIPMENT_NAME_MAP
        
        self.assertIn("蚀化臂铠", EQUIPMENT_NAME_MAP)
        self.assertIn("Corrupted Gauntlet", EQUIPMENT_NAME_MAP["蚀化臂铠"])
        self.assertIn("拷问工具箱", EQUIPMENT_NAME_MAP)
        self.assertIn("Torture Toolbox", EQUIPMENT_NAME_MAP["拷问工具箱"])
        self.assertIn("异象石碑", EQUIPMENT_NAME_MAP)
        self.assertIn("Stele of Heresy", EQUIPMENT_NAME_MAP["异象石碑"])


if __name__ == '__main__':
    unittest.main()

