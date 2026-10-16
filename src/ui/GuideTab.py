from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QTextBrowser,
)
from qfluentwidgets import (
    FluentIcon,
    NavigationItemPosition,
    Pivot,
    TitleLabel,
    SubtitleLabel,
    BodyLabel,
    CardWidget,
    isDarkTheme,
)

from ok.gui.widget.CustomTab import CustomTab


GUIDE_PAGES = [
    {
        "title": "Khởi đầu & Cài đặt Game",
        "icon": FluentIcon.PLAY,
        "content": """
        <h3>1. Thiết lập Game bắt buộc (Rất quan trọng)</h3>
        <p>Để bot có thể nhận diện hình ảnh và điều khiển chính xác 100%, bạn cần cài đặt trong game như sau:</p>
        <ul>
            <li><b>Độ phân giải:</b> Chạy game ở chế độ <b>Cửa sổ (Windowed)</b> với chuẩn tỉ lệ <b>16:9</b> (khuyên dùng <code>1920x1080</code>, <code>1600x900</code> hoặc <code>1280x720</code>).</li>
            <li><b>Bật hiển thị phím tắt (Shortcut Display = ON):</b> Trong Cài đặt Game bản PC, hãy bật hiển thị phím tắt bàn phím (ON). Tính năng này giúp bot nhận diện phím bấm chính xác khi ra bài trong trận.</li>
            <li><b>Bật tự động đối thoại (Auto Dialogue = ON):</b> Nhấp vào biểu tượng tự động tua hội thoại ở góc trên màn hình game.</li>
            <li><b>Tắt lớp phủ (Overlay) & Filter:</b> Tắt các bộ lọc làm nét của card màn hình (NVIDIA Game Filter, AMD Image Sharpening) và tắt các phần mềm hiển thị overlay che màn hình game.</li>
            <li><b>Nếu dùng giả lập MuMu:</b> Xóa bỏ các phím số gán tự động ở khu vực thẻ bài trên tay để không che mất chữ của lá bài.</li>
        </ul>

        <h3>2. Kết nối Tool với Game</h3>
        <ol>
            <li>Mở game <i>Chaos Zero Nightmare</i> lên trước.</li>
            <li>Khởi động <b>ok-kes.exe</b> (hoặc <b>KhoiDong.exe</b>).</li>
            <li>Tại tab <b>Bắt đầu & Kết nối (Capture)</b>:
                <ul>
                    <li><b>Chọn cửa sổ:</b> Chọn đúng cửa sổ game <code>Chaos Zero Nightmare</code> hoặc giả lập của bạn.</li>
                    <li><b>Phương thức thao tác:</b> Chọn <code>WindowsInteraction</code> hoặc <code>PostMessage</code> (hỗ trợ thao tác ngầm ngay cả khi cửa sổ game bị che khuất hoặc thu nhỏ).</li>
                    <li>Bấm nút <b>Bắt đầu</b>. Khi thấy trạng thái báo <b>Đã kết nối</b> màu xanh lá là thành công!</li>
                </ul>
            </li>
        </ol>
        """,
    },
    {
        "title": "Chế độ Tự động Xuất kích",
        "icon": FluentIcon.GAME,
        "content": """
        <h3>1. Mục đích sử dụng</h3>
        <p>Tự động hóa hoàn toàn việc cày ải Xuất kích hàng ngày, farm nguyên liệu, tiêu hao thể lực (Ether) và diệt Boss tầng 1 để nhận phần thưởng.</p>

        <h3>2. Cách kích hoạt chuẩn</h3>
        <ol>
            <li>Trong game, tự điều khiển nhân vật vào giao diện có nút <b>Vào ải (Xuất kích)</b> hoặc đã bước vào trong ải.</li>
            <li>Mở tool, vào tab <b>Nhiệm vụ Tự động (Triggers)</b> -> Gạt công tắc bật <b>Tự động Xuất kích</b>.</li>
            <li><i>Lưu ý:</i> Không bật khi đang đứng ở sảnh chính (Lobby). Tool sẽ tự tắt công tắc nếu phát hiện chưa vào đúng ải để tránh thao tác nhầm.</li>
        </ol>

        <h3>3. Các tính năng nổi bật</h3>
        <ul>
            <li><b>Tự động chọn Đặc vụ:</b> Tự chọn nhân vật dẫn đầu theo danh sách ưu tiên cấu hình.</li>
            <li><b>Lộ trình thông minh:</b> Tự động chọn nhánh đường tối ưu (Nghỉ ngơi -> Sự kiện -> Quái thường -> Tinh anh).</li>
            <li><b>Chiến đấu thông minh:</b> Tự động nhận diện bài trên tay và xuất chiêu theo thứ tự ưu tiên combo bài.</li>
            <li><b>Quản lý thẻ bài & Cửa hàng:</b> Tự nhặt thẻ bài mới, vào cửa hàng Delang để xóa thẻ bài rác, tự động thoát sau khi đánh xong Boss tầng 1 và nhận quà.</li>
        </ul>

        <h3>4. Sử dụng Cấu hình Phổ biến (Khuyên dùng)</h3>
        <p>Tại thẻ nhiệm vụ Xuất kích, bấm nút <b>Cấu hình phổ biến</b> -> Chọn cấu hình của người chơi có tỉ lệ thắng cao (95% - 100%) phù hợp với nhân vật bạn có -> Bấm <b>Áp dụng</b> để nạp toàn bộ danh sách ưu tiên bài chỉ với 1 cú click!</p>
        """,
    },
    {
        "title": "Chế độ Tự động Kaos",
        "icon": FluentIcon.SYNC,
        "content": """
        <h3>1. Mục đích sử dụng</h3>
        <p>Vượt ải Kaos mùa giải, Hệ thống Zero, tẩy và cày bản lưu (Save Data) dung lượng cao, farm thẻ bài Flash và thần thiểm.</p>

        <h3>2. Cách kích hoạt chuẩn</h3>
        <ol>
            <li>Trong game, hãy <b>tự xếp đội hình 3 người</b> của bạn trước.</li>
            <li>Vào giao diện ải Kaos hoặc Hệ thống Zero.</li>
            <li>Trong cấu hình tool, điền tên nhân vật chủ lực của bạn vào ô <b>Đặc vụ cày file lưu</b> (phải là 1 trong 3 người trong đội hình).</li>
            <li>Gạt công tắc bật <b>Tự động Khiêu chiến Chaos</b>.</li>
        </ol>

        <h3>3. Quy trình bot tự xử lý</h3>
        <ul>
            <li><b>Tự động quản lý bài:</b> Xóa bài cơ bản, sao chép bài mạnh, làm sáng (Flash), chuyển hóa thẻ bài.</li>
            <li><b>Trị liệu sụp đổ tinh thần:</b> Tự động di chuyển đến trung tâm chấn thương để phục hồi khi nhân vật gặp sang chấn tâm lý.</li>
            <li><b>Xử lý dữ liệu bản lưu (Save Data):</b> Tự động xóa/bán các file lưu dưới mức TB bạn cài đặt để đổi lấy vàng, chỉ giữ lại file lưu đạt chuẩn.</li>
            <li><b>Sự kiện & Boss:</b> Tự đưa ra lựa chọn sự kiện tối ưu theo danh sách ưu tiên.</li>
        </ul>
        """,
    },
    {
        "title": "Cốt truyện & Phụ trợ",
        "icon": FluentIcon.DOCUMENT,
        "content": """
        <h3>1. Chế độ Bán tự động Cốt truyện (Story Mode)</h3>
        <ul>
            <li>Tự động bỏ qua (skip) các đoạn hội thoại dài khi làm nhiệm vụ chính tuyến.</li>
            <li>Khi gặp ải đánh nhau, bạn chỉ cần chọn người rồi bật chế độ Xuất kích để tool tự đánh. Gặp ải Kaos thì bật chế độ Kaos.</li>
        </ul>

        <h3>2. Nhập & Xuất Cấu hình qua mã Base64</h3>
        <ul>
            <li><b>Xuất mã cấu hình:</b> Bấm nút <i>Xuất mã cấu hình</i> để mã hóa toàn bộ cài đặt của bạn thành chuỗi ký tự và tự động copy vào bộ nhớ tạm (clipboard) để gửi cho bạn bè.</li>
            <li><b>Nhập mã cấu hình:</b> Khi được người khác chia sẻ mã, chỉ cần copy mã đó rồi bấm nút <i>Nhập mã cấu hình</i> -> Tool sẽ tự động áp dụng.</li>
            <li><b>Lưu & Đổi cấu hình cục bộ:</b> Bạn có thể lưu nhiều bộ cấu hình khác nhau cho từng nhân vật (ví dụ: bộ cho Hyde Mary, bộ cho Mika) và chuyển đổi qua lại nhanh chóng.</li>
        </ul>

        <h3>3. Đồng bộ đám mây (Supabase)</h3>
        <p>Mỗi 5 phút tool sẽ tự động gửi thống kê cấu hình ẩn danh và tỉ lệ thắng lên máy chủ để tính điểm bảng xếp hạng <i>Cấu hình phổ biến</i>. Cam kết không thu thập bất kỳ thông tin cá nhân hay hình ảnh nào của bạn.</p>
        """,
    },
    {
        "title": "Câu hỏi thường gặp (FAQ)",
        "icon": FluentIcon.QUESTION,
        "content": """
        <h3>Hỏi: Tôi chơi máy chủ Quốc tế (Global) thì cần lưu ý gì?</h3>
        <p><b>Đáp:</b> Trong cấu hình của chế độ bạn dùng, hãy đổi mục <b>Ngôn ngữ game</b> thành <code>繁体中文</code> (Phồn thể). Vì server Quốc tế dùng tiếng Trung phồn thể, bot cần đối chiếu đúng font chữ này.</p>

        <h3>Hỏi: Làm sao để bot ra bài chuẩn và thắng nhiều hơn?</h3>
        <p><b>Đáp:</b> Hãy chắc chắn bạn đã <b>bật hiển thị phím tắt</b> trong game. Ngoài ra, hãy sử dụng nút <b>Cấu hình phổ biến</b> để lấy danh sách thứ tự đánh bài của các cao thủ có winrate trên 90%.</p>

        <h3>Hỏi: Tại sao bot báo lỗi đường dẫn không hợp lệ?</h3>
        <p><b>Đáp:</b> Thư viện nhận diện chữ OCR của C++ yêu cầu đường dẫn thư mục cài đặt không chứa dấu tiếng Việt hoặc khoảng trắng lạ. Bản cập nhật đã tự động hỗ trợ đường dẫn 8.3 Short Path, tuy nhiên tốt nhất bạn nên đặt thư mục tool tại ổ đĩa như <code>D:\\ok-kes</code> để đảm bảo độ mượt mà cao nhất.</p>

        <h3>Hỏi: Backend OCR nên chọn ONNX Runtime hay OpenVINO?</h3>
        <p><b>Đáp:</b> Mặc định để <b>Tự động</b>. Nếu máy bạn dùng CPU Intel và RAM từ 12 GB trở lên, OpenVINO sẽ chạy nhanh và mượt hơn. Với các máy khác, ONNX Runtime sẽ nhẹ RAM hơn (chỉ tốn ~1.5 GB RAM).</p>
        """,
    },
]


class GuideTab(CustomTab):
    def __init__(self):
        super().__init__()
        GuideTab.instance = self
        self.setObjectName("GuideTab")

        # Header Title
        title_box = QVBoxLayout()
        title_box.setSpacing(4)
        title = TitleLabel("📖 Hướng dẫn Sử dụng Chi tiết", self.view)
        subtitle = BodyLabel(
            "Cẩm nang vận hành, thiết lập tối ưu và giải đáp thắc mắc cho công cụ tự động hóa ok-kes.",
            self.view,
        )
        title_box.addWidget(title)
        title_box.addWidget(subtitle)
        self.addLayout(title_box)

        # Pivot Navigation
        self.pivot = Pivot(self.view)
        self.stacked_widget = QStackedWidget(self.view)
        self.stacked_widget.setMinimumHeight(480)

        for i, page in enumerate(GUIDE_PAGES):
            tab_name = page["title"]
            self.pivot.addItem(
                routeKey=f"page_{i}",
                text=tab_name,
                onClick=lambda _, idx=i: self.stacked_widget.setCurrentIndex(idx),
                icon=page.get("icon"),
            )

            # Page container
            card = CardWidget(self.stacked_widget)
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(20, 16, 20, 20)
            card_layout.setSpacing(12)

            page_title = SubtitleLabel(page["title"], card)
            card_layout.addWidget(page_title)

            browser = QTextBrowser(card)
            browser.setOpenExternalLinks(True)
            browser.setReadOnly(True)
            self._apply_browser_style(browser)
            browser.setHtml(self._wrap_html(page["content"]))
            card_layout.addWidget(browser)

            self.stacked_widget.addWidget(card)

        self.pivot.setCurrentItem("page_0")
        self.add_widget(self.pivot)
        self.add_widget(self.stacked_widget)

    @property
    def name(self):
        return "Hướng dẫn"

    @property
    def icon(self):
        return FluentIcon.HELP

    @property
    def position(self):
        return NavigationItemPosition.SCROLL

    @property
    def add_after_default_tabs(self):
        return True

    def _apply_browser_style(self, browser: QTextBrowser):
        is_dark = isDarkTheme()
        bg_color = "transparent"
        text_color = "#f0f0f0" if is_dark else "#222222"
        link_color = "#4cc2ff" if is_dark else "#0066cc"

        browser.setStyleSheet(
            f"""
            QTextBrowser {{
                background-color: {bg_color};
                color: {text_color};
                border: none;
                font-size: 14px;
                line-height: 1.6;
            }}
            QTextBrowser a {{
                color: {link_color};
                text-decoration: none;
            }}
            """
        )

    def _wrap_html(self, body_html: str) -> str:
        is_dark = isDarkTheme()
        code_bg = "#2d2d2d" if is_dark else "#f0f0f0"
        code_color = "#ff99aa" if is_dark else "#c7254e"
        return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 0;
                    padding: 0;
                }}
                h3 {{
                    margin-top: 16px;
                    margin-bottom: 8px;
                    font-size: 16px;
                }}
                p {{
                    margin: 6px 0;
                }}
                ul, ol {{
                    margin: 6px 0 12px 20px;
                    padding-left: 0;
                }}
                li {{
                    margin-bottom: 6px;
                }}
                code {{
                    background-color: {code_bg};
                    color: {code_color};
                    padding: 2px 5px;
                    border-radius: 4px;
                    font-family: Consolas, monospace;
                    font-size: 13px;
                }}
            </style>
        </head>
        <body>
            {body_html}
        </body>
        </html>
        """


GuideTab.instance = None


def install_guide_handler():
    from ok.gui.about.LinksBar import LinksBar
    if getattr(LinksBar, "_ok_kes_guide_installed", False):
        return

    original_open_url = LinksBar.open_url

    def open_url(links_bar, url_name):
        if url_name in ("faq", "guide"):
            from ok import og
            guide = getattr(GuideTab, "instance", None)
            main_window = getattr(og, "main_window", None)
            if guide is not None and main_window is not None:
                main_window.switchTo(guide)
                return
        original_open_url(links_bar, url_name)

    LinksBar.open_url = open_url
    LinksBar._ok_kes_guide_installed = True

