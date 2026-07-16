# 070. AHI Skill Validation

| Item | Value |
|------|-------|
| Document ID | AHI-SC-070 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế kiểm tra (Validation) của AHI Skill trước, trong và sau khi được sử dụng trong hệ sinh thái AHI.

AHI Skill Validation bảo đảm rằng mọi Skill đều tuân thủ Hiến pháp AHI, có thể truy vết, có khả năng kế thừa và không làm suy giảm chất lượng tri thức của hệ sinh thái.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- 010_AHI_SKILL_ARCHITECTURE.md.
- 020_AHI_SKILL_COMPILATION.md.
- 030_AHI_SKILL_FORMAT.md.
- 040_AHI_SKILL_EXECUTION.md.
- 050_AHI_SKILL_EVOLUTION.md.
- 060_AHI_SKILL_LIBRARY.md.

---

# 3. Validation Principles

Mọi Skill phải được kiểm tra theo các nguyên tắc:

- Tuân thủ Hiến pháp AHI.
- Có nguồn gốc rõ ràng (Lineage).
- Có khả năng truy vết.
- Không mâu thuẫn với các tài liệu kế thừa.
- Không làm mất lịch sử tiến hóa.
- Không chứa nội dung chưa được phê duyệt.

Nếu thiếu thông tin cần thiết, AHI không được suy diễn hoặc tự bổ sung mà phải yêu cầu làm rõ theo Hiến pháp AHI.

---

# 4. Validation Scope

Việc kiểm tra bao gồm:

- Cấu trúc Skill.
- Metadata.
- Lineage.
- Dependencies.
- Nội dung.
- Phiên bản.
- Trạng thái phê duyệt.
- Khả năng kế thừa.
- Tính nhất quán với các đặc tả liên quan.

---

# 5. Validation Workflow

```text
Skill Package
      │
      ▼
Structure Validation
      │
      ▼
Lineage Validation
      │
      ▼
Dependency Validation
      │
      ▼
Constitution Validation
      │
      ▼
AHI-V Review
      │
      ▼
Validation Result
```

---

# 6. Validation Result

Kết quả kiểm tra có thể thuộc một trong các trạng thái:

| Status | Ý nghĩa |
|---------|----------|
| Approved | Đạt yêu cầu, có thể sử dụng. |
| Approved with Notes | Được sử dụng nhưng có khuyến nghị cải tiến. |
| Pending | Chưa đủ thông tin để đánh giá. |
| Rejected | Không đạt yêu cầu theo Hiến pháp hoặc đặc tả. |

---

# 7. Relationship with AHI-V

AHI-V là thành phần chịu trách nhiệm thực hiện Validation.

AHI-V không sửa nội dung Skill.

AHI-V chỉ:

- Phát hiện vấn đề.
- Đối chiếu với Hiến pháp.
- Đưa ra kết quả kiểm tra.
- Đề xuất các điểm cần hoàn thiện.

Quyết định cuối cùng thuộc về chủ sở hữu AHI-P.

---

# 8. Relationship with AHI-SuBiet

AHI-SuBiet sử dụng kết quả Validation như một đầu vào trong quá trình đánh giá mức độ tiến hóa của Skill.

Validation không thay thế việc đánh giá "Sự biết"; nó chỉ bảo đảm Skill đáp ứng các điều kiện cần trước khi được đánh giá theo AHI-SuBiet.

---

# 9. Notes

Tài liệu này đặc tả cơ chế Validation ở mức kiến trúc.

Các bộ quy tắc kiểm tra tự động, tiêu chí đánh giá chi tiết và công cụ hỗ trợ sẽ được đặc tả trong các tài liệu kỹ thuật tương ứng.

---

**End of Document**
