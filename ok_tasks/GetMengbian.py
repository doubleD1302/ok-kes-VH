from ok import BaseTask
import re

class GetMengbian(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "刷梦边"
        self.description = "梦边"
        self.instructions = """<b>Nhiệm vụ Cày Biên Giới Giấc Mơ:</b><br><br>
Tự động vào ải Biên giới Giấc mơ (梦之边境) để tìm thẻ bài Truyền thuyết Trung lập, nếu không xuất hiện sẽ tự động đào tẩu và thử lại tối đa 300 lần."""

    def run(self):
        for i in range(300):
            self.log_info("Bắt đầu vòng lặp thứ {}".format(i+1))
            self.log_info("Trang lối vào Biên giới Giấc mơ: chờ và nhấp nút 'Vào' đầu tiên")
            self.wait_click_ocr(match="进入", time_out=60, after_sleep=1)
            self.log_info("Trang lối vào Biên giới Giấc mơ: chờ và nhấp nút 'Vào' thứ hai để xác nhận")
            self.wait_click_ocr(match="进入", time_out=60)
            self.sleep(11)
            if self.ocr(match=re.compile(r".*传说卡牌.*")):
                self.log_info("Thẻ bài Truyền thuyết Trung lập xuất hiện")
                self.log_info("Trang Biên giới Giấc mơ: nhấp chọn thẻ bài Truyền thuyết Trung lập")
                self.click(0.758, 0.853)
                self.sleep(1)
                self.log_info("Trang Biên giới Giấc mơ: nhấp vị trí xác nhận chọn thẻ")
                self.click(0.757, 0.953)
                self.sleep(4)
                if self.ocr(match=re.compile(r"梦之边境")):
                    self.log_info("Biên giới Giấc mơ đã hoàn thành, kết thúc vòng lặp")
                    break
            self.log_info("Chưa xuất hiện thẻ Truyền thuyết Trung lập, tiếp tục vòng lặp")
            self.log_info("Trang Biên giới Giấc mơ: nhấp vị trí thoát")
            self.click(0.959, 0.049)
            self.log_info("Trang thoát Biên giới Giấc mơ: chờ và nhấp 'Đào tẩu'")
            self.wait_click_ocr(match="逃脱", time_out=60)
            self.log_info("Trang thoát Biên giới Giấc mơ: chờ và nhấp 'Xác nhận'")
            self.wait_click_ocr(match="确认",time_out=60,after_sleep=2)


