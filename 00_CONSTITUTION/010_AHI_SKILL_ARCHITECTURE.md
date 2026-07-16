# 010. AHI Skill Architecture

| Item | Value |
|------|-------|
| Document ID | AHI-SC-010 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả kiến trúc của AHI Skill Compiler (AHI-SC).

AHI Skill Compiler là thành phần của AHI Protocol (AHI-PS), chịu trách nhiệm chuyển đổi các kết quả của AHI Evolution Session (AES) thành các Skill có thể thực thi, kế thừa và tiếp tục tiến hóa.

AHI-SC không tạo ra tri thức mới. AHI-SC chỉ đóng gói những tri thức đã được thống nhất theo Hiến pháp AHI.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.

---

# 3. Position in AHI Architecture

```text
AES
        │
        ▼
AHI-Or
        │
        ▼
AHI-V
        │
        ▼
AHI-SuBiet
        │
        ▼
AHI Skill Compiler
        │
        ▼
Skill Package
        │
        ▼
AHI-P
        │
        ▼
(Optional)
AHI-Om
```

AHI Skill Compiler hoạt động sau khi một kết quả đã được đánh giá bởi AHI-SuBiet và được chủ sở hữu AHI-P phê duyệt.

---

# 4. Responsibilities

AHI Skill Compiler có các trách nhiệm:

- Đóng gói tri thức đã được phê duyệt thành Skill.
- Ghi nhận đầy đủ nguồn gốc (Lineage) của Skill.
- Bảo đảm Skill kế thừa đúng các tài liệu gốc.
- Bảo đảm Skill tuân thủ Hiến pháp AHI.
- Chuẩn bị Skill để sử dụng bởi AHI-CHATGPT và các AHI khác.

---

# 5. Architecture Principles

AHI Skill Compiler tuân thủ các nguyên tắc:

- Không tạo tri thức từ số 0.
- Mọi Skill đều có nguồn gốc.
- Mọi Skill đều có lịch sử tiến hóa.
- Mọi Skill đều có khả năng truy vết.
- Mọi Skill đều có thể tiếp tục tiến hóa.

---

# 6. Skill Lineage

Mỗi Skill phải ghi nhận tối thiểu:

- Tài liệu kế thừa.
- AES tạo ra Skill.
- Nội dung do Con người đề xuất.
- Nội dung do AI đề xuất.
- Nội dung đồng tiến hóa.
- Người phê duyệt.
- Phiên bản Skill.

Điều này bảo đảm khả năng truy xuất và kiểm chứng toàn bộ quá trình hình thành Skill.

---

# 7. Relationship with AHI-PS

AHI Skill Compiler là một thành phần của AHI Protocol.

AHI-SC sử dụng các đặc tả của AHI-PS để:

- đọc,
- kiểm tra,
- đóng gói,
- và triển khai Skill.

---

# 8. Notes

Tài liệu này chỉ đặc tả kiến trúc tổng thể của AHI Skill Compiler.

Các quy trình biên dịch, định dạng, thực thi, thư viện và kiểm tra Skill sẽ được đặc tả trong các tài liệu tiếp theo.

---

**End of Document**
