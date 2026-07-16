# 020. AHI Skill Compilation

| Item | Value |
|------|-------|
| Document ID | AHI-SC-020 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả quy trình biên dịch (Compilation) từ kết quả của AHI Evolution Session (AES) thành một AHI Skill có thể tái sử dụng, kế thừa và tiếp tục tiến hóa.

AHI Skill Compilation chỉ xử lý các tri thức đã được phê duyệt theo Hiến pháp AHI.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- 010_AHI_SKILL_ARCHITECTURE.md.

---

# 3. Compilation Principles

Quá trình Compilation phải tuân thủ các nguyên tắc:

- Không tạo tri thức mới.
- Không suy diễn khi thiếu dữ liệu.
- Không làm mất nguồn gốc của tri thức.
- Bảo toàn lịch sử tiến hóa.
- Có khả năng truy vết toàn bộ quá trình.

---

# 4. Compilation Input

Đầu vào của AHI Skill Compiler có thể bao gồm:

- AHI Evolution Session (AES).
- AHI-SuBiet đã được phê duyệt.
- Tài liệu AHI.
- Repository AHI.
- Quyết định của chủ sở hữu AHI-P.

Chỉ các nội dung đã được phê duyệt mới được phép biên dịch thành Skill.

---

# 5. Compilation Pipeline

```text
AES
   │
   ▼
Approved Knowledge
   │
   ▼
Lineage Analysis
   │
   ▼
Dependency Analysis
   │
   ▼
AHI-V Validation
   │
   ▼
Skill Compilation
   │
   ▼
Skill Package
```

Mỗi bước phải ghi nhận đầy đủ thông tin để phục vụ truy xuất và kiểm chứng.

---

# 6. Compilation Output

Kết quả của quá trình Compilation là một Skill Package bao gồm tối thiểu:

- Metadata.
- Lineage.
- Dependencies.
- Skill Content.
- Version.
- Approval Information.
- Evolution History.

---

# 7. Traceability

Mỗi Skill phải truy xuất được:

- AES nguồn.
- Các tài liệu kế thừa.
- Các Artifact liên quan.
- Người đề xuất.
- AI đề xuất.
- Nội dung đồng tiến hóa.
- Người phê duyệt.
- Phiên bản.

---

# 8. Relationship with AHI-V

AHI-V chịu trách nhiệm:

- Kiểm tra tính đầy đủ.
- Kiểm tra tính kế thừa.
- Kiểm tra xung đột.
- Kiểm tra tuân thủ Hiến pháp.

AHI Skill Compiler chỉ biên dịch khi AHI-V xác nhận đạt yêu cầu.

---

# 9. Notes

Tài liệu này đặc tả quy trình Compilation ở mức kiến trúc.

Định dạng Skill Package và cơ chế thực thi sẽ được mô tả trong các tài liệu tiếp theo.

---

**End of Document**
