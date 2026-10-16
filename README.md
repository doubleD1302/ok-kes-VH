<div align="center">
  <h1 align="center">
    <img src="icons/icon.png" width="200" alt="ok-kes logo"/>
    <br/>
    ok-kes
  </h1> 
  
  <p>
    Một công cụ hỗ trợ tự động hóa Chaos Zero Nightmare (卡厄思梦境) dựa trên nhận diện hình ảnh, hỗ trợ chế độ chạy nền, được phát triển dựa trên <a href="https://github.com/ok-oldking/ok-script">ok-script</a>.
    <br />
    An image-recognition-based automation tool for Chaos Zero Nightmare (卡厄思梦境), with background mode support, developed with <a href="https://github.com/ok-oldking/ok-script">ok-script</a>.
  </p>
  
  <p><i>Mô phỏng thao tác người dùng thông qua giao diện Windows, không đọc bộ nhớ, không chỉnh sửa file game</i></p>
  <p><b>✅ Hỗ trợ server Quốc tế (Tiếng Trung phồn thể), server Trung Quốc PC Client và các phần mềm giả lập Android</b></p>
</div>

<!-- Badges -->
<div align="center">
  
![Nền tảng](https://img.shields.io/badge/platform-Windows-blue)
[![GitHub release](https://img.shields.io/github/v/release/baoxin1100/ok-kes)](https://github.com/baoxin1100/ok-kes/releases)

</div>

### [Tiếng Việt](README.md) | [English Readme](README_en.md) | [中文说明](README_zh.md)

> 📖 **Lần đầu sử dụng? Vui lòng xem: [Tài liệu hướng dẫn đầy đủ](docs/zh-CN/usage-guide.md)**

---

## ⚠️ Tuyên bố miễn trừ trách nhiệm

Phần mềm này là một công cụ hỗ trợ bên ngoài, được thiết kế nhằm tự động hóa một phần quy trình chơi game trong "Chaos Zero Nightmare". Ứng dụng hoàn toàn tương tác với game thông qua việc mô phỏng giao diện người dùng thông thường, tuân thủ các quy định pháp luật liên quan. Dự án này nhằm mục đích đơn giản hóa các thao tác lặp đi lặp lại của người chơi, không can thiệp cân bằng game, không cung cấp lợi thế bất công và tuyệt đối không chỉnh sửa bất kỳ tập tin hoặc dữ liệu nào của game.

Phần mềm này là mã nguồn mở và hoàn toàn miễn phí, chỉ dành cho mục đích học tập và nghiên cứu cá nhân. Nghiêm cấm sử dụng cho bất kỳ mục đích thương mại hoặc trục lợi nào. Nhóm phát triển bảo lưu quyền giải thích cuối cùng cho dự án này. Mọi vấn đề phát sinh do việc sử dụng phần mềm này không liên quan đến dự án và các nhà phát triển.

**Việc sử dụng phần mềm này đồng nghĩa với việc bạn đã đọc, hiểu và đồng ý với toàn bộ tuyên bố trên, đồng thời tự nguyện chịu mọi rủi ro tiềm ẩn.**

## 🚀 Bắt đầu nhanh

Có 3 cách đơn giản để khởi chạy công cụ:

1. **Khởi chạy nhanh 1 chạm (Khuyên dùng)**:
   - Nhấp đúp chuột vào [ok-kes.exe](file:///c:/Users/chann/OneDrive/M%C3%A1y%20t%C3%ADnh/tool%20CN/ok-kes.exe) hoặc [KhoiDong.exe](file:///c:/Users/chann/OneDrive/M%C3%A1y%20t%C3%ADnh/tool%20CN/KhoiDong.exe) ngay tại thư mục gốc. Ứng dụng sẽ tự động mở giao diện Tiếng Việt mà không cần mở dòng lệnh.
2. **Chạy bản Độc lập (Standalone Portable)**:
   - Sử dụng file thực thi độc lập tại `dist/ok-kes-VietHoa.exe` (đã đóng gói sẵn toàn bộ Python, thư viện và mô hình AI OCR, có thể copy mang sang máy khác dùng ngay mà không cần cài Python).
3. **Chạy từ dòng lệnh**:
   - Chạy lệnh `python main.py` (hoặc nhấp đúp vào `KhoiDong.bat`).

## ✨ Các tính năng chính

<img src="docs/images/image_1.png" alt="Giao diện chức năng" />

### Chế độ Tự động Xuất kích (Auto Sortie)
- 🎮 **Tự động chiến đấu**: Đánh bài thông minh dựa trên nhận diện phím tắt, hỗ trợ tùy chỉnh thứ tự ưu tiên xuất bài của người chơi.
- 🃏 **Tự động chọn bài**: Tự động nhận, loại bỏ, sao chép và làm sáng (flash) thẻ bài.
- ⚔️ **Chọn nhân vật chủ chiến**: Tự động chọn nhân vật chủ chiến xuất trận theo thứ tự ưu tiên đã cấu hình.
- 🛣️ **Chọn lộ trình**: Nhận diện thông minh loại nút (node), tự động tiến lên theo mức ưu tiên.
- 🏪 **Xử lý cửa hàng**: Tự động vào cửa hàng Delang để loại bỏ thẻ bài không mong muốn.
- 💊 **Kiểm tra bổ sung thể lực (Ether)**: Tự động thoát khi phát hiện thể lực không đủ.
- Hỗ trợ tùy chỉnh danh sách ưu tiên thẻ bài, danh sách xóa/sao chép/làm sáng thẻ bài.

### Chế độ Tự động Kaos (Auto Chaos)
- 🃏 **Tự động quản lý bài**: Loại bỏ, sao chép, làm sáng, ban phước làm sáng, chuyển hóa thẻ bài, v.v.
- 🛣️ **Chọn lộ trình**: Tự động nhận diện các nút nghỉ ngơi / sự kiện / Boss / quái thường.
- 🏥 **Trị liệu sụp đổ tinh thần**: Tự động di chuyển đến trung tâm chấn thương để hồi phục.
- 📦 **Xử lý dữ liệu lưu trữ**: Tự động xóa các bản lưu dữ liệu (có thể cấu hình giữ lại).
- 🏪 **Xử lý cửa hàng**: Tự động tương tác với cửa hàng Delang.
- 🌀 **Hỗ trợ hệ thống Zero**: Tự động xử lý tìm kiếm pháp điển.
- Các tính năng mới liên tục được phát triển và cập nhật...

### Chế độ Bán tự động Cốt truyện
- 💬 **Tự động đối thoại**: Tự động bỏ qua các đoạn hội thoại cốt truyện.
- ⚠️ Khi gặp các ải chiến đấu hoặc ải Kaos, bạn có thể chuyển thủ công sang chế độ tương ứng.

### Nhập & Xuất Cấu hình
- 📤 **Xuất cấu hình**: Mã hóa cấu hình của chế độ hiện tại thành chuỗi văn bản và sao chép vào bộ nhớ tạm chỉ với một cú nhấp chuột để chia sẻ với người khác.
- 📥 **Nhập cấu hình**: Dán mã cấu hình do người khác chia sẻ để áp dụng ngay lập tức, hỗ trợ nhập cấu hình giữa các phiên bản khác nhau.

### Đồng bộ & Khám phá Cấu hình Phổ biến (v1.3.5+)
- 📡 **Tự động tải lên cấu hình**: Mỗi 5 phút tự động tải thông tin cấu hình ẩn danh và tỉ lệ thắng lên máy chủ đám mây, hỗ trợ thống kê các cấu hình thịnh hành.
- 🌟 **Cấu hình phổ biến**: Nhấp nút "Cấu hình phổ biến" trong trang cấu hình chế độ Kaos / chế độ Xuất kích:
  - Khám phá các cấu hình được chia sẻ bởi những người chơi có tỉ lệ thắng cao (hỗ trợ sắp xếp theo tỉ lệ thắng hoặc số người dùng).
  - Áp dụng cấu hình phổ biến về máy cục bộ chỉ với một cú nhấp chuột.
  - Cần bật tính năng tải lên cấu hình để sử dụng (nhằm khuyến khích tinh thần cộng đồng chia sẻ).
- 🔒 **Chính sách bảo mật**: Tuyệt đối không tải lên bất kỳ thông tin cá nhân, tài khoản game, ảnh chụp màn hình hay địa chỉ IP nào.

### Các tính năng chung
- 🖥️ **Hỗ trợ độ phân giải cao**: Hỗ trợ chuẩn tỉ lệ 16:9 với các độ phân giải 1920x1080 / 1600x900 / 1280x720, v.v.
- 🔄 **Chế độ chạy nền**: Hỗ trợ tiếp tục chạy ổn định dưới nền ngay cả khi cửa sổ game bị thu nhỏ hoặc bị che khuất.
- 🌏 **Hỗ trợ đa ngôn ngữ game**: Tương thích với client tiếng Trung giản thể và phồn thể (cài đặt trong phần "Ngôn ngữ game" ở cấu hình chế độ).

## 🔧 Hướng dẫn sử dụng

1. **Người chơi server Quốc tế lưu ý**: Vui lòng đặt "Ngôn ngữ game" thành Phồn thể (繁体中文) trong cấu hình của chế độ tự động bạn sử dụng.
2. **Tự động chiến đấu**: Tính năng này phụ thuộc vào việc nhận diện phím bấm, vui lòng bật hiển thị phím tắt trong cài đặt game để tăng độ chính xác khi ra bài.
3. **Chế độ Kaos**: Vui lòng chủ động bật tính năng tự động chiến đấu và tự động cốt truyện có sẵn trong game.
4. **Chế độ Cốt truyện**: Đối với các màn chiến đấu, bạn có thể bật chế độ Xuất kích thủ công để gọi tính năng tự động đánh; khi gặp ải Kaos hãy mở chế độ Kaos; đội hình chiến đấu cần được sắp xếp thủ công.

## 🔧 Xử lý sự cố (Troubleshooting)

Nếu gặp sự cố, vui lòng thực hiện kiểm tra theo các bước sau trước khi báo lỗi:

1. **Phần mềm diệt virus**: Thêm thư mục chứa phần mềm vào danh sách loại trừ/tin cậy của phần mềm diệt virus (bao gồm cả Windows Defender) để tránh việc tệp tin bị xóa nhầm hoặc chặn hoạt động.
2. **Cài đặt hiển thị**:
   * Tắt tất cả các bộ lọc card màn hình (ví dụ: NVIDIA Game Filter) và tính năng làm nét (sharpening).
   * Sử dụng cài đặt độ sáng mặc định của game.
   * Tắt các phần mềm hiển thị lớp phủ (overlay) trên màn hình game.
3. **Độ phân giải game**: Đảm bảo tỉ lệ khung hình của game được thiết lập chuẩn 16:9.
4. **Phiên bản phần mềm**: Luôn kiểm tra và cập nhật lên phiên bản mới nhất.
5. **Tìm kiếm sự trợ giúp**: Nếu các bước trên vẫn không giải quyết được vấn đề, vui lòng gửi phản hồi chi tiết qua kênh cộng đồng.

---

## 💖 Ủng hộ nhà phát triển

Nếu bạn yêu thích công cụ này, bạn có thể ủng hộ tác giả gốc để duy trì phát triển dự án~ Xin chân thành cảm ơn!

<p align="center">
  <img src="docs/images/wechat_reward_code.png" alt="Mã ủng hộ WeChat" width="300">
  <img src="docs/images/alipay_reward_code.png" alt="Mã ủng hộ Alipay" width="300">
</p>

---

## 💻 Dành cho nhà phát triển

### Chạy từ mã nguồn (Python)

```bash
# Cài đặt hoặc cập nhật thư viện phụ thuộc
pip install -r requirements.txt --upgrade

# Chạy phiên bản Release
python main.py

# Chạy phiên bản Debug
python main_debug.py
```

## 💬 Kênh cộng đồng

- **Nhóm QQ**: `1040800032` (Đáp án vào nhóm: `烟火焚`)
- **Kênh QQ**: [Bấm để tham gia](https://pd.qq.com/s/eopggnxcu)
- **Trang chủ ok-kes**: [https://ok-script.com/ok-kes](https://ok-script.com/ok-kes)

Dự án này được phát triển dựa trên framework [ok-script](https://github.com/ok-oldking/ok-script), đơn giản và dễ bảo trì. Rất hoan nghênh các nhà phát triển sử dụng [ok-script](https://github.com/ok-oldking/ok-script) để xây dựng các dự án tự động hóa của riêng mình.

## 🔗 Các dự án sử dụng ok-script:

* 卡厄思梦境 (Chaos Zero Nightmare) [https://github.com/baoxin1100/ok-kes](https://github.com/baoxin1100/ok-kes)
* 鸣潮 (Wuthering Waves) [https://github.com/ok-oldking/ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves)
* 少前2 (Girls' Frontline 2) [https://github.com/ok-oldking/ok-gf2](https://github.com/ok-oldking/ok-gf2)
* 星痕共鸣 [https://github.com/Sanheiii/ok-star-resonance](https://github.com/Sanheiii/ok-star-resonance)
* 二重螺旋 (Duet Night Abyss) [https://github.com/BnanZ0/ok-duet-night-abyss](https://github.com/BnanZ0/ok-duet-night-abyss)
* 明日方舟：终末地 (Arknights: Endfield) [https://github.com/AliceJump/ok-end-field](https://github.com/AliceJump/ok-end-field)
* 异环 (NTE) [https://github.com/BnanZ0/ok-nte](https://github.com/BnanZ0/ok-nte)
* 阴阳师 (Onmyoji) [https://ok-script.com/ok-onmyoji](https://ok-script.com/ok-onmyoji)

## ❤️ Lời cảm ơn

* [ok-script](https://github.com/ok-oldking/ok-script)
* [OnnxOCR](https://github.com/ok-oldking/OnnxOCR)
* [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
