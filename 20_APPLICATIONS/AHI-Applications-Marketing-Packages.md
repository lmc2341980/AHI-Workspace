# AHI Applications — AHI AI Journey Framework™ & NetZeroLoop

> **Người biên soạn & phê duyệt:** Lê Minh Công — Người sáng lập dự án AHI (AHI-F)
> **Phiên bản:** 1.0 — khởi tạo.
> Tài liệu này trình bày mô hình thương mại hóa AHI dành cho đối tác/khách hàng doanh nghiệp, dựa trên **AHI AI Journey Framework™**. Đây là tài liệu **hướng thương mại**, tách riêng khỏi các tài liệu Hiến pháp/Kiến trúc kỹ thuật để phù hợp đối tượng đọc (nhà đầu tư, đối tác kinh doanh). Mọi thuật ngữ kỹ thuật dùng trong tài liệu này đều đối chiếu về đúng định nghĩa gốc tại *AHI-WS-Thiet-Ke-Kien-Truc.md*.

---

## 1. Hai trục độc lập — nguyên tắc nền tảng của Framework

AHI AI Journey Framework™ tách rõ hai câu hỏi khác nhau, không gộp làm một:

1. **Khách hàng đang ở Mức AI nào?** → Trục **AI Maturity Levels** (mục 2)
2. **AHI sẽ triển khai theo quy trình nào?** → Trục **Implementation Process** (mục 3)

---

## 2. Trục 1 — 6 Mức trưởng thành AI (AI Adoption Levels)

| Mức | AI phổ thông | Tên AHI | Đối chiếu thực thể/kiến trúc AHI đã có |
|---|---|---|---|
| 1 | Sử dụng AI miễn phí | AI Assistant | Chưa có AHI-P, tương tác trực tiếp AHI-Old (mục 8.2, *AHI-WS-Thiet-Ke-Kien-Truc.md*) |
| 2 | AI trả phí | AI Productivity | AHI-P ở mức xác thực thấp nhất (mục 5) |
| 3 | AI tích hợp API | AI Business | Bắt đầu dùng mô hình kết nối **API** (mục 8.9) |
| 4 | AI mã nguồn mở | AI Enterprise | Tích hợp qua **MCP**, thuê AHI-WS dạng SaaS (mục 1) |
| 5 | AI tự phát triển | AI Core Technology | Tự vận hành lớp **AHI-Cache** riêng (mục 3.2) |
| 6 | AI + phần cứng + hệ sinh thái | AHI Ecosystem | Đầy đủ **AHI-CP** + AHI-Successor + tham gia **AHI-Om** |

**Thông điệp cốt lõi:** *"Doanh nghiệp không cần bắt đầu từ Mức 6. AHI giúp doanh nghiệp đi từng bước."*

---

## 3. Trục 2 — Quy trình triển khai AHI chuẩn (6 bước)

### Bước 1 — Khảo sát
Thu thập hiện trạng: dữ liệu, ERP, CRM, Excel, camera, sensor, nhân sự, pain point.
**Kết quả:** AI Readiness Report.

### Bước 2 — Phân tích
Đánh giá ROI, Quick Wins, AI Maturity (đối chiếu Trục 1). Lựa chọn 3–10 Use Case.

### Bước 3 — Thiết kế
Đề xuất kiến trúc — chính là **AHI-Or + adapter AHI-Old** (mục 8.2, *AHI-WS-Thiet-Ke-Kien-Truc.md*) áp dụng cho khách hàng cụ thể:

```
ERP
  ↓
AHI Gateway (= AHI-Or)
  ↓
GPT / Claude / Gemini (= AHI-Old, mục 8.2) / OCR / RAG / IoT / Camera / Dashboard
```

Xây dựng Business Case, ROI, Timeline, Chi phí.

### Bước 4 — Thử nghiệm (PoC/Pilot)
Triển khai thật ở quy mô nhỏ (AI Sales, AI QC, AI Camera, AI ERP...). Đo ROI, Accuracy, KPI. Đối chiếu trực tiếp đề xuất PoC đã có tại mục 17, *AHI-WS-Thiet-Ke-Kien-Truc.md*.

### Bước 5 — Triển khai
Scale và tích hợp đầy đủ (ERP, CRM, MES, IoT, Camera, HRM). Đào tạo, Change Management. Đây chính là vai trò **SaaS đối ngoại** của AHI-WS (mục 1).

### Bước 6 — Đồng hành
AHI không dừng ở triển khai — tiếp tục tối ưu, nâng cấp, mở rộng, huấn luyện AI, cập nhật tri thức, phát triển Agent mới, giúp khách hàng chuyển dần từ Mức 2 → 6. Đây là giai đoạn tạo doanh thu dịch vụ định kỳ (AI-as-a-Service), vận hành đúng bản chất **AHI-CP** (mục 8.9) — ngữ cảnh liên tục, không ngắt theo dự án.

---

## 4. Ghép hai trục

```
                 AI LEVEL
Level 6 ─────────────────────────────
Level 5 ─────────────────────────────
Level 4 ─────────────────────────────
Level 3 ─────────────────────────────
Level 2 ─────────────────────────────
Level 1 ─────────────────────────────
            ↑
    AHI khảo sát → thiết kế → triển khai → đồng hành
    để nâng khách hàng lên Level tiếp theo
```

---

## 5. So sánh định vị

| Tiêu chí | Đơn vị AI thông thường | AHI |
|---|---|---|
| Mục tiêu | Bán phần mềm AI | Xây dựng năng lực AI dài hạn |
| Khảo sát | Có | Có, đánh giá AI Maturity và ROI |
| Triển khai | Theo dự án | Theo lộ trình nhiều giai đoạn |
| Công nghệ | Một mô hình AI | Đa mô hình (qua AHI-Or, mục 8.2) |
| Dữ liệu | Phục vụ dự án | Trở thành tài sản tri thức doanh nghiệp (ghi vào DBG) |
| Sau triển khai | Bảo hành | Đồng hành, huấn luyện, mở rộng (AHI-CP) |
| Đích đến | Hoàn thành dự án | Nâng doanh nghiệp từ Level 1 lên Level 6 |

**Thông điệp bán hàng:** *"Chúng tôi không hỏi 'Doanh nghiệp muốn mua AI gì?', mà hỏi 'Doanh nghiệp đang ở Mức AI nào, và làm thế nào để tiến lên mức tiếp theo với chi phí và rủi ro thấp nhất?'"*

---

## 6. NetZeroLoop — tích hợp với AHI-Energy

**NetZeroLoop** là vòng lặp khép kín hướng tới phát thải ròng bằng 0, thuộc nhóm nhiệm vụ **AHI-Energy** đã có (*AHI-Cong-Bo-Du-An.md* mục 10). Vòng lặp dùng đúng cơ chế draft→official đã có (mục 8.4, *AHI-WS-Thiet-Ke-Kien-Truc.md*), không tạo trạng thái mới:

```
[Đo tiêu hao thực]  ──▶  [AHI-Energy tính điểm phát thải ròng]
        │                              │
        │                              ▼
        │                    [Ghi vào DBG, context_scope: môi trường]
        │                              │
        ▼                              ▼
[AHI-Cache tối ưu lại cấu hình]  ◀──  [So sánh với ngưỡng NetZero]
        │
        └──▶ Đạt ngưỡng → cấp điểm ESG, cộng vào điểm đóng góp (mục 12)
             Chưa đạt → giữ trạng thái "thảo luận", lặp lại vòng tối ưu
```

NetZeroLoop được gắn vào **Bước 6 (Đồng hành)** của quy trình triển khai — là một trong các hạng mục "tối ưu liên tục" mà AHI cung cấp cho khách hàng ở Mức 4 trở lên (nơi đã đủ dữ liệu vận hành để đo phát thải).

**Đối chiếu ESG/COP:**

| Trụ cột ESG | Cơ chế AHI tương ứng |
|---|---|
| Environmental (Môi trường) | NetZeroLoop qua AHI-Energy |
| Social (Xã hội) | Nguyên tắc "con người làm trung tâm" (mục 9, *AHI-WS-Thiet-Ke-Kien-Truc.md*) |
| Governance (Quản trị) | Cơ chế quá bán và Luật án lệ (mục 9.3) |

**Lưu ý về tính hợp lệ pháp lý:** việc một gói dịch vụ có "đạt chuẩn ESG" hay "phù hợp cam kết COP của một quốc gia cụ thể" hay không cần thẩm định pháp lý/kỹ thuật riêng khi thương mại hóa thật — tài liệu này chỉ trình bày khung đối chiếu khái niệm, không phải xác nhận đạt chuẩn.

---

## 7. Nhật ký cập nhật (Changelog)

| Phiên bản | Ngày | Mục thay đổi | Phạm vi / Giới hạn |
|---|---|---|---|
| v1.0 | 2026-07-14 | Toàn bộ tài liệu | Khởi tạo AHI AI Journey Framework™: tách 2 trục độc lập (6 mức trưởng thành AI, quy trình triển khai 6 bước), bảng so sánh định vị, tích hợp NetZeroLoop với AHI-Energy và đối chiếu ESG/COP |
