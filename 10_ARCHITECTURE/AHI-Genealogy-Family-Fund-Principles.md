# Nguyên tắc Gia phả AHI-P và Quỹ Tài chính Dòng họ (AHI-O Gia tộc)

> **Người biên soạn & phê duyệt:** Lê Minh Công — Người sáng lập dự án AHI (AHI-F)
> **Phiên bản:** 1.0 — khởi tạo.
> Tài liệu này chuẩn hóa nguyên tắc xây dựng gia phả bằng AHI-P và nguyên tắc tài chính quỹ dòng họ, dựa trên đối chiếu trực tiếp với tài liệu quy ước gia tộc truyền thống (*Kỷ yếu Di sản và Quy ước Gia tộc Lê Tổ Miếu*, mục VIII và IX) và kiến trúc AHI-P/AHI-O đã có tại *AHI-WS-Thiet-Ke-Kien-Truc.md*. Nguyên tắc cốt lõi: **không phát minh cơ chế mới** — mọi nội dung dưới đây là bản dịch trực tiếp truyền thống gia tộc sang cơ chế số hóa của AHI.

---

## 1. Nguyên tắc nền tảng: một dòng họ = một AHI-O đặc biệt

Thay vì tạo một thực thể hoàn toàn mới cho "dòng họ", tài liệu này dùng lại đúng cấu trúc **AHI-O (AHI-Organization)** đã định nghĩa tại mục 3.4, *AHI-WS-Thiet-Ke-Kien-Truc.md*, với các đặc điểm riêng của một "AHI-O gia tộc":

| Đặc điểm AHI-O chuẩn | Áp dụng cho AHI-O gia tộc |
|---|---|
| Hình thành từ nhiều AHI-P theo tỷ lệ % | Hình thành từ các AHI-P là thành viên dòng họ, tỷ lệ tính theo trọng số thế hệ (mục 10.5, *AHI-WS-Thiet-Ke-Kien-Truc.md*, công thức 1/2ⁿ) thay vì tỷ lệ vốn góp thông thường |
| Mọi cá nhân thuộc tổ chức phải có AHI-P đã xác thực | Thành viên còn sống cần AHI-P xác thực; tổ tiên đã mất được lưu dưới dạng **hồ sơ lịch sử/tham chiếu** (mục 3 dưới đây), không bắt buộc có AHI-P đầy đủ nếu không còn dữ liệu |
| Quản trị theo đồng thuận quá bán (mục 11) | Do **Hội đồng Gia tộc** quyết định — đối chiếu trực tiếp "Ban Quản trị Từ đường" trong quy ước gốc |
| Một AHI-O có thể chứa AHI-O con | Nhánh/chi trong dòng họ = AHI-O con, mỗi Trưởng chi ngành quản lý một AHI-O con |

---

## 2. Hội đồng Gia tộc — đối chiếu Ban Quản trị Từ đường

Theo quy ước gốc: *"Ban Quản trị Từ đường (Hội đồng Gia tộc): Thành phần bao gồm Trưởng tộc, các Trưởng chi ngành và những thành viên có uy tín, tâm huyết được con cháu tín nhiệm bầu ra."*

Đối chiếu vào cơ chế AHI đã có:

- **Hội đồng Gia tộc** đóng vai trò tương đương **Đại hội đồng AHI** ở quy mô một AHI-O (mục 9.3, *AHI-WS-Thiet-Ke-Kien-Truc.md*) — có quyền phê duyệt các quyết định cần quá bán trong phạm vi dòng họ (ví dụ: nội dung bản dịch câu đối, phân bổ quỹ, quyết định vĩ mô của Robot AHI-Successor theo mục 10.5).
- Nhiệm vụ: trông nom di sản, điều hành lễ tiết, hòa giải nội bộ, đại diện giao lưu — các nhiệm vụ này **không đổi**, chỉ bổ sung thêm vai trò công nghệ: xác nhận nội dung trước khi AHI-V nâng trạng thái từ `draft` lên `official` trong DBG.

---

## 3. Nguyên tắc xây dựng gia phả bằng AHI-P

| Bước | Nội dung | Cơ chế AHI-P tương ứng |
|---|---|---|
| **1. Khởi tạo gốc** | Xác định thủy tổ dòng họ làm node gốc của cây phả hệ | Node gốc trong Knowledge Graph (*AHI-Knowledge-OS-Data-Model.md* mục 5) |
| **2. Gắn AHI-P theo từng thế hệ** | Thành viên còn sống có AHI-P đã xác thực; thành viên đã mất có AHI-P đóng băng (nếu từng được số hóa khi còn sống) hoặc hồ sơ lịch sử thuần túy (nếu là tổ tiên xa, chưa từng có AHI-P) | Nguyên tắc "mỗi người một AHI-P duy nhất" (mục 3.1.2); với tổ tiên xa, dùng entry DBG dạng tư liệu lịch sử, `knowledge_level: biết`, không gán AHI-P giả |
| **3. Liên kết phả hệ và trọng số biểu quyết** | Dùng đúng công thức 1/2ⁿ đã có (mục 10.5) để tính trọng số biểu quyết trong các quyết định liên quan quỹ dòng họ | Không tạo công thức mới |
| **4. Số hóa tư liệu gốc** | Văn tế, câu đối, ảnh, bản dịch nghĩa Hán cổ — đưa vào DBG dạng `context_scope: gia tộc` | Trạng thái `official` chỉ đạt được sau khi Hội đồng Gia tộc xác nhận (mục 2 ở trên) |
| **5. Xử lý dị bản/tranh cãi** | Nếu có nhiều bản dịch câu đối khác nhau (đúng thách thức đã nêu trong quy ước gốc: *"đọc sai, hiểu nhầm, dẫn đến những suy diễn lệch lạc"*) | Dùng cơ chế **Luật án lệ** (mục 9.3, *AHI-WS-Thiet-Ke-Kien-Truc.md*) — bản dịch được Hội đồng Gia tộc phê duyệt trở thành án lệ chính thức, các bản dịch cũ **không bị xóa**, giữ làm tư liệu đối sánh lịch sử (đúng nguyên tắc "không xóa, chỉ tiến hóa") |
| **6. Từ đường vật lý ↔ AHI-Successor** | Nhà từ đường là **node tham chiếu cố định** của cả dòng họ; mỗi AHI-Successor cá nhân (mục 10.1–10.5, *AHI-WS-Thiet-Ke-Kien-Truc.md*) liên kết ngược về node này | Không thay thế vai trò tâm linh/văn hóa của từ đường vật lý — AHI chỉ số hóa và hỗ trợ, không can thiệp nghi lễ |

---

## 4. Nguyên tắc tài chính — Quỹ Trường tồn Dòng họ (Tộc quỹ số hóa)

Đối chiếu trực tiếp mục VIII của quy ước gốc:

> *"Nguồn quỹ được xây dựng từ sự đóng góp tự nguyện, tùy tâm của con cháu và sự phát tâm công đức của các doanh nhân, những người thành đạt trong họ... Thu chi phải được ghi chép sổ sách rõ ràng, có thủ quỹ và kế toán theo dõi, báo cáo công khai minh bạch trước toàn thể dòng họ vào ngày giỗ Tổ hằng năm."*

| Nguyên tắc gốc | Cơ chế số hóa tương ứng |
|---|---|
| Đóng góp tự nguyện, tùy tâm | Đúng mô hình kinh tế hai dòng lợi nhuận (mục 10.4, *AHI-WS-Thiet-Ke-Kien-Truc.md*) — "nuôi cây phả hệ" từ phần thặng dư của Robot AHI-Successor, không ép buộc; thành viên còn sống có thể đóng góp thêm bằng AHI-Coin |
| Mục đích: hương khói, bảo trì, hiếu hỷ, khuyến học | Chuẩn hóa thành các hạng mục chi tiêu cố định trong `context_scope: gia tộc`, mỗi hạng mục là một loại entry DBG riêng để dễ tổng hợp báo cáo |
| Ghi chép sổ sách rõ ràng, có thủ quỹ + kế toán | Mỗi khoản thu/chi là một entry DBG **bất biến, chỉ nối thêm** (mục 8.4) — vai trò "thủ quỹ/kế toán" được thực hiện tự động bởi AHI-V, không cần con người ghi chép thủ công, nhưng Hội đồng Gia tộc vẫn có quyền xem toàn bộ lịch sử `version_chain` |
| Báo cáo công khai minh bạch vào ngày giỗ Tổ hằng năm | Robot AHI-Successor **tự động sinh báo cáo thu-chi hằng năm**, gửi tới toàn bộ cây phả hệ còn sống vào đúng ngày giỗ/ngày tưởng niệm — đã bổ sung chính thức vào mục 10.4, *AHI-WS-Thiet-Ke-Kien-Truc.md* (v2.8) |

### 4.1 Quỹ Khuyến học — mô-đun con của Tộc quỹ

Quy ước gốc duy trì **Quỹ Khuyến học** riêng, vinh danh con cháu có thành tích xuất sắc, gắn với tinh thần *"Tự đắc ý thành công"*. Đề xuất giữ nguyên như một hạng mục con trong Tộc quỹ số hóa, với chỉ số theo dõi riêng trên ESG Dashboard nếu dòng họ có tham gia hoạt động môi trường/xã hội (đối chiếu *AHI-NetZeroLoop-Spec.md* mục 3, ESG Dashboard) — không bắt buộc, chỉ là điểm kết nối tùy chọn giữa hai tài liệu.

---

## 5. Việc còn để ngỏ

- Ngưỡng cụ thể để một bản dịch câu đối/tư liệu Hán Nôm được coi là "đã vượt qua" tranh cãi (đối chiếu `dialectical_state`, *AHI-Ung-Dung-Triet-Hoc.md* mục 2).
- Cơ chế xác thực danh tính cho tổ tiên xa không còn giấy tờ/ADN — cần nguyên tắc riêng, khác với xác thực AHI-P đương đại (mục 5, *AHI-WS-Thiet-Ke-Kien-Truc.md*).
- Các mục này phù hợp xử lý dần qua cơ chế Luật án lệ khi phát sinh tình huống thực tế của từng dòng họ cụ thể.

---

## 6. Nhật ký cập nhật (Changelog)

| Phiên bản | Ngày | Mục thay đổi | Phạm vi / Giới hạn |
|---|---|---|---|
| v1.0 | 2026-07-15 | Toàn bộ tài liệu | Khởi tạo: nguyên tắc "một dòng họ = một AHI-O đặc biệt", đối chiếu Hội đồng Gia tộc với Đại hội đồng AHI, quy trình 6 bước xây dựng gia phả bằng AHI-P, nguyên tắc tài chính Tộc quỹ số hóa dựa trên đối chiếu trực tiếp *Kỷ yếu Di sản và Quy ước Gia tộc Lê Tổ Miếu* mục VIII–IX |
