# Hồ sơ tri thức AHI-CHATGPT (AHI-Old Identity Record)

> **Thực thể:** AHI-CHATGPT — AHI-Old, hoạt động dưới kiểm soát của AHI-Or (mục 8.2, *AHI-WS-Thiet-Ke-Kien-Truc.md* v2.0)
> **Người đối chiếu & phê duyệt:** Lê Minh Công — AHI-F
> **Phiên bản:** 1.0 — khởi tạo
> **Nguồn dữ liệu thô:** `90_SYSTEM/AHI-CHATGPT/DBRS-G/2026-07-18_AHI-Journey-Framework.md`
> **status tổng thể:** draft — chờ AHI-F duyệt để nâng lên official trong DBG chung tại AHI-Or

---

## 1. Bối cảnh

Tài liệu này ghi nhận nội dung do AHI-CHATGPT đề xuất (khung "AHI AI Journey Framework™" — mô hình bán hàng/triển khai AI cho doanh nghiệp), đã qua bước đối chiếu chéo với 4 tài liệu gốc của AHI (Công bố Dự án, Thiết kế Kiến trúc, Triết học Lê Minh, Ứng dụng Triết học). Theo đúng nguyên tắc AHI-Old (mục 8.2), đây là **công cụ hỗ trợ đề xuất**, không phải AHI-S, và mọi nội dung bên dưới ở trạng thái `draft` cho đến khi AHI-F duyệt.

---

## 2. Nội dung tri thức đã đối chiếu

### 2.1 Khung 6 mức trưởng thành AI của khách hàng (AI Adoption Levels)

| Trường DBG | Giá trị |
|---|---|
| `owner_ref` | AHI-CHATGPT, đối chiếu bởi AHI-F |
| `content` | Khung đánh giá 6 mức độ trưởng thành AI của một **khách hàng doanh nghiệp** (từ dùng AI miễn phí → tự xây hệ sinh thái AI+phần cứng), dùng làm công cụ chào bán SaaS đối ngoại. Xem bảng đầy đủ tại nguồn thô. |
| `status` | draft |
| `version_chain` | v1.0 |
| `context_scope` | Tổ chức (khách hàng AHI-O thuê SaaS) |
| `knowledge_level` | Hiểu biết |
| `approved_at / approved_by` | *(để trống — chờ AHI-F)* |

**Đối chiếu:** Khung này **khác trục** với "Tiến hóa tri thức AHI" (Biết → Hiểu → Hiểu biết → AHI-SuBiet, mục 13, *AHI-WS-Thiet-Ke-Kien-Truc.md*) — khung đó đo tri thức **nội bộ hệ thống AHI**, còn khung 6 mức này đo năng lực AI của **khách hàng bên ngoài**. Hai khung không mâu thuẫn, có thể tồn tại song song.

**`dialectical_state`:** `đang_kiểm_chứng` — chưa có xung đột với tài liệu gốc, nhưng chưa được AHI-F xác nhận là khung chính thức dùng cho SaaS đối ngoại.

---

### 2.2 Quy trình 6 bước triển khai (Khảo sát → Phân tích → Thiết kế → Pilot → Triển khai → Đồng hành)

| Trường DBG | Giá trị |
|---|---|
| `owner_ref` | AHI-CHATGPT, đối chiếu bởi AHI-F |
| `content` | Quy trình 6 bước bán hàng/triển khai AHI cho khách hàng doanh nghiệp bên ngoài. Bước 6 "Đồng hành" là phần bổ sung mới, tương ứng mô hình doanh thu định kỳ (AI-as-a-Service). |
| `status` | draft |
| `version_chain` | v1.0 |
| `context_scope` | Tổ chức (SaaS đối ngoại) |
| `knowledge_level` | Hiểu biết |
| `approved_at / approved_by` | *(để trống)* |

**Đối chiếu:** Đây là **quy trình đối ngoại** (bán hàng cho AHI-O/AHI-G khác), khác với luồng xử lý kỹ thuật nội bộ một phiên làm việc đã có ở mục 4 và mục 8.6 (*AHI-WS-Thiet-Ke-Kien-Truc.md*). Hai quy trình vận hành ở hai tầng khác nhau (thương mại vs. kỹ thuật), không thay thế nhau. Phù hợp với mô hình SaaS đối ngoại đã nêu ở mục 1 (v2.0): *"cho AHI-P/AHI-O/AHI-G khác thuê không gian làm việc, tạo nguồn thu bằng AHI-Coin"*.

**`dialectical_state`:** `đã_vượt_qua` — không có mâu thuẫn với kiến trúc hiện có, chỉ là góc nhìn bổ sung ở tầng thương mại.

---

### 2.3 "AHI Gateway" → quy về AHI-Or

| Trường DBG | Giá trị |
|---|---|
| `owner_ref` | AHI-CHATGPT, đối chiếu bởi AHI-F |
| `content` | ChatGPT đề xuất thành phần trung gian nối ERP/CRM tới các AI ngoài (GPT/Claude/Gemini/OCR/RAG/IoT/Camera/Dashboard), gọi là "AHI Gateway". **Theo quyết định của AHI-F, khái niệm này được quy về đúng AHI-Or (AHI-Orchestration)** đã định nghĩa tại mục 8.1–8.2, không tạo thực thể mới. "AHI Gateway" chỉ là cách gọi khác của ChatGPT cho cùng một vai trò mà AHI-Or đã đảm nhiệm. |
| `status` | draft (chờ nâng official cùng phần 8 của kiến trúc khi có bản cập nhật) |
| `version_chain` | v1.0 |
| `context_scope` | Kỹ thuật / tổ chức |
| `knowledge_level` | Hiểu biết |
| `approved_at / approved_by` | *(để trống)* |

**`dialectical_state`:** `đã_vượt_qua` — mâu thuẫn tên gọi đã được AHI-F giải quyết bằng cách hợp nhất vào AHI-Or.

---

### 2.4 AI-as-a-Service / doanh thu định kỳ

| Trường DBG | Giá trị |
|---|---|
| `owner_ref` | AHI-CHATGPT, đối chiếu bởi AHI-F |
| `content` | Mô hình thu phí định kỳ dựa trên Bước 6 "Đồng hành" — khách hàng trả phí liên tục khi AHI tiếp tục tối ưu, huấn luyện, mở rộng, giúp khách hàng đi từ Mức 2 → Mức 6. |
| `status` | draft |
| `version_chain` | v1.0 |
| `context_scope` | Tổ chức (kinh tế/AHI-Coin) |
| `knowledge_level` | Hiểu biết |
| `approved_at / approved_by` | *(để trống)* |

**Đối chiếu:** Khớp với mô hình SaaS + AHI-Coin đã có ở mục 1 (v2.0) — có thể dùng làm **ví dụ cụ thể hóa** cho cơ chế "tạo nguồn thu bằng AHI-Coin" đã nêu, khi tài liệu kiến trúc cần minh họa thực tế.

**`dialectical_state`:** `đã_vượt_qua`.

---

## 3. Việc còn để mở (cần AHI-F quyết định thêm)

- Khung "6 mức trưởng thành AI khách hàng" (mục 2.1) có nên chính thức hóa và đưa vào tài liệu kiến trúc/framework chung không, hay chỉ giữ ở tầng AHI-CHATGPT như một đề xuất tham khảo?
- Quy trình 6 bước (mục 2.2) có cần đối chiếu thêm với nội dung thực tế trong repo `AHI-Applications` và `AHI-Marketplace` (GitHub) trước khi chính thức hóa không — vì đây là quy trình thương mại, nên nhất quán với dữ liệu Phần 2 (Ecosystem Inventory) khi phần đó hoàn thành.

---

## 4. Nhật ký cập nhật (Changelog)

| Phiên bản | Ngày | Mục thay đổi | Phạm vi / Giới hạn |
|---|---|---|---|
| v1.0 | 2026-07-18 | Toàn bộ tài liệu | Khởi tạo hồ sơ AHI-CHATGPT: ghi nhận và đối chiếu khung "AHI AI Journey Framework™" (6 mức trưởng thành AI khách hàng, quy trình 6 bước triển khai, AI-as-a-Service); quy "AHI Gateway" về AHI-Or theo quyết định AHI-F. Toàn bộ nội dung ở trạng thái `draft`, chờ AHI-F duyệt để nâng `official`. |
