# 070. AHI SuBiet Validation

| Item | Value |
|------|-------|
| Document ID | AHI-SB-070 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế kiểm tra (Validation) của AHI-SuBiet.

AHI-SuBiet Validation bảo đảm rằng mọi kết quả đánh giá "Sự biết" đều:

- tuân thủ Hiến pháp AHI;
- có đầy đủ nguồn gốc (Lineage);
- có khả năng truy vết;
- không mâu thuẫn với các tài liệu kế thừa;
- đủ điều kiện để tiếp tục tiến hóa.

Validation không tạo ra tri thức mới và không thay thế quyết định của Con người.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- 004_AHI_SUBIET_SPECIFICATION.md.
- 010_AHI_SUBIET_MODEL.md.
- 020_AHI_SUBIET_EVALUATION.md.
- 030_AHI_SUBIET_EVOLUTION.md.
- 040_AHI_SUBIET_APPROVAL.md.
- 050_AHI_SUBIET_LIBRARY.md.
- 060_AHI_SUBIET_SHARING.md.

---

# 3. Validation Principles

Việc Validation phải tuân thủ các nguyên tắc:

- Tuân thủ Hiến pháp AHI.
- Không suy diễn khi thiếu dữ liệu.
- Không tự bổ sung thông tin chưa được xác nhận.
- Giữ nguyên lịch sử tiến hóa.
- Bảo toàn Lineage.
- Có khả năng truy vết toàn bộ quá trình.

Nếu thiếu dữ liệu, AHI phải yêu cầu làm rõ thay vì tự đưa ra kết luận.

---

# 4. Validation Scope

Các nội dung được kiểm tra bao gồm:

- Cấu trúc "Sự biết".
- Metadata.
- Version.
- Lineage.
- Evolution History.
- Approval Information.
- Quan hệ với Skill.
- Quan hệ với AES.
- Quan hệ với các tài liệu kế thừa.
- Tính nhất quán với Hiến pháp AHI.

---

# 5. Validation Workflow

```text
SuBiet Package
        │
        ▼
Metadata Validation
        │
        ▼
Lineage Validation
        │
        ▼
Constitution Validation
        │
        ▼
Relationship Validation
        │
        ▼
AHI-V Review
        │
        ▼
Validation Result
```

---

# 6. Validation Result

| Trạng thái | Ý nghĩa |
|------------|---------|
| Approved | Đạt yêu cầu theo đặc tả. |
| Approved with Notes | Được chấp nhận nhưng có khuyến nghị cải tiến. |
| Pending | Thiếu dữ liệu hoặc cần làm rõ. |
| Rejected | Không đạt yêu cầu hoặc vi phạm Hiến pháp AHI. |

---

# 7. Relationship with AHI-V

AHI-V là thành phần chịu trách nhiệm thực hiện Validation.

AHI-V có trách nhiệm:

- phát hiện vấn đề;
- đối chiếu với Hiến pháp;
- kiểm tra Lineage;
- kiểm tra khả năng kế thừa;
- đưa ra kết quả Validation.

AHI-V không được phép tự sửa nội dung hoặc tự tạo "Sự biết" mới.

---

# 8. Relationship with AHI-SuBiet

Validation là điều kiện cần trước khi một kết quả được xem xét trong quá trình đánh giá hoặc phê duyệt của AHI-SuBiet.

Validation bảo đảm chất lượng dữ liệu; AHI-SuBiet đánh giá mức độ trưởng thành của tri thức.

---

# 9. Notes

AHI-SuBiet Validation là lớp bảo đảm chất lượng của toàn bộ hệ thống đánh giá tri thức.

Mọi kết quả Validation đều phải được lưu lại như một phần của Evolution History để phục vụ truy vết và các AHI Evolution Session (AES) trong tương lai.

---

**End of Document**
