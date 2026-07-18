# [DBRS-G] Bản ghi thô — AHI Journey Framework (nguồn: ChatGPT)

> **owner_ref:** AHI-CHATGPT (AHI-Old)
> **Nguồn gốc:** Trao đổi trực tiếp với ChatGPT, do AHI-F (Lê Minh Công) dẫn dắt cuộc hội thoại
> **Ngày ghi nhận:** 2026-07-18
> **status:** draft — chưa qua AHI-V xác thực, chưa đối chiếu chéo với DBG chung
> **context_scope:** SaaS đối ngoại / bán hàng-triển khai doanh nghiệp
> **Ghi chú:** Nội dung dưới đây giữ **nguyên văn 100%** theo nguyên tắc "không xóa, không ghi đè" (mục 3, *AHI-Cong-Bo-Du-An-V1.md*). Bản đã đối chiếu và viết lại theo thuật ngữ AHI chính thức nằm tại `90_IDENTITIES/AHI-CHATGPT/AHI-CHATGPT-Identity.md`.

---

Sau khi xem tài liệu, tôi thấy bạn đã có **hai trục độc lập nhưng chưa ghép lại thành một mô hình bán hàng hoàn chỉnh**:

* **Trục 1:** Quy trình triển khai AI/AHI cho doanh nghiệp (4–5 bước: Khảo sát → Lựa chọn → Thiết kế → Pilot → Scale).
* **Trục 2:** 6 mức trưởng thành AI của doanh nghiệp (từ dùng AI miễn phí đến tự xây hệ sinh thái AI).

Theo tôi, khi chào bán sẽ mạnh hơn nếu **tách rõ hai câu hỏi**:

1. **Khách hàng đang ở Mức AI nào?** (AI Maturity)
2. **AHI sẽ triển khai theo quy trình nào?** (Implementation Process)

Đó là hai thứ khác nhau.

---

# AHI AI Journey Framework™

## Phần 1. 6 mức trưởng thành AI (AI Adoption Levels)

| Mức | AI phổ thông                  | AHI                |
| --- | ----------------------------- | ------------------ |
| 1   | Sử dụng AI miễn phí           | AI Assistant       |
| 2   | AI trả phí                    | AI Productivity    |
| 3   | AI tích hợp API               | AI Business        |
| 4   | AI mã nguồn mở                | AI Enterprise      |
| 5   | AI tự phát triển              | AI Core Technology |
| 6   | AI + phần cứng + hệ sinh thái | AHI Ecosystem      |

Thông điệp:

> **Doanh nghiệp không cần bắt đầu từ Mức 6.**
>
> **AHI giúp doanh nghiệp đi từng bước.**

Đây chính là "lộ trình trưởng thành AI".

Nội dung này tương ứng với Phần C của tài liệu.

---

# Phần 2. Quy trình triển khai AHI chuẩn (6 bước)

Đây mới là quy trình bán dịch vụ.

## Bước 1 — KHẢO SÁT

Khách hàng hiện có: dữ liệu gì, ERP, CRM, Excel, camera, sensor, nhân sự, pain point.

Kết quả: AI Readiness Report

## Bước 2 — PHÂN TÍCH

Đánh giá: ROI, Quick Wins, AI Maturity.

Lựa chọn: 3–10 Use Case

## Bước 3 — THIẾT KẾ

Đề xuất kiến trúc, ví dụ:

```
ERP
↓
AHI Gateway
↓
GPT / Claude / Gemini / OCR / RAG / IoT / Camera / Dashboard
```

Xây dựng: Business Case, ROI, Timeline, Chi phí

## Bước 4 — THỬ NGHIỆM (PoC / Pilot)

Làm thật: AI Sales, AI QC, AI Camera, AI ERP

Đo: ROI, Accuracy, KPI

## Bước 5 — TRIỂN KHAI

Scale, tích hợp: ERP, CRM, MES, IoT, Camera, HRM

Đào tạo, Change Management

## Bước 6 — ĐỒNG HÀNH

Đây là phần còn thiếu trong tài liệu hiện tại. AHI không dừng ở triển khai. AHI tiếp tục: tối ưu, nâng cấp, mở rộng, huấn luyện AI, cập nhật tri thức, phát triển Agent mới, xây AI doanh nghiệp, chuyển từ Mức 2 → 3 → 4 → 5 → 6.

Đây là giai đoạn tạo doanh thu dịch vụ định kỳ (AI-as-a-Service).

---

# Ghép hai mô hình

```
                 AI LEVEL
Level 6
──────────────────────────────────
Level 5
──────────────────────────────────
Level 4
──────────────────────────────────
Level 3
──────────────────────────────────
Level 2
──────────────────────────────────
Level 1
──────────────────────────────────
      ↑
AHI khảo sát
AHI thiết kế
AHI triển khai
AHI đồng hành
để nâng khách hàng lên Level tiếp theo.
```

Đây là điểm khác biệt lớn của AHI: không chỉ triển khai dự án mà còn đồng hành nâng cấp năng lực AI của doanh nghiệp.

---

# So sánh để chào bán

| Tiêu chí       | Đơn vị AI thông thường | AHI                                                      |
| -------------- | ----------------------- | --------------------------------------------------------- |
| Mục tiêu       | Bán phần mềm AI         | Xây dựng năng lực AI dài hạn                              |
| Khảo sát       | Có                      | Có, đánh giá AI Maturity và ROI                            |
| Triển khai     | Theo dự án              | Theo lộ trình nhiều giai đoạn                              |
| Công nghệ      | Một mô hình AI          | Đa mô hình (GPT, Claude, Gemini, Open Source...)          |
| Dữ liệu        | Phục vụ dự án           | Trở thành tài sản tri thức doanh nghiệp                    |
| Sau triển khai | Bảo hành                | Đồng hành, huấn luyện và mở rộng AI                        |
| Giá trị        | Tự động hóa             | Tự động hóa + tích lũy tri thức + chuyển đổi năng lực AI  |
| Đích đến       | Hoàn thành dự án        | Nâng doanh nghiệp từ AI Level 1 lên AI Level 6            |

---

## Thông điệp bán hàng đề xuất

> **Đa số đơn vị bán một giải pháp AI. AHI xây dựng một hành trình phát triển AI cho doanh nghiệp.**
>
> **Chúng tôi không hỏi "Doanh nghiệp muốn mua AI gì?", mà hỏi "Doanh nghiệp đang ở Mức AI nào, và làm thế nào để tiến lên mức tiếp theo với chi phí và rủi ro thấp nhất?".**
