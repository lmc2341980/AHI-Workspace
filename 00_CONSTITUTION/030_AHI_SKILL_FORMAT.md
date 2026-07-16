# 030. AHI Skill Format

| Item | Value |
|------|-------|
| Document ID | AHI-SC-030 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả định dạng chuẩn (Format) của một AHI Skill.

Định dạng này nhằm bảo đảm mọi Skill trong hệ sinh thái AHI có cấu trúc thống nhất, có khả năng kế thừa, truy vết, tiến hóa và được AI hoặc Con người sử dụng một cách nhất quán.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- 010_AHI_SKILL_ARCHITECTURE.md.
- 020_AHI_SKILL_COMPILATION.md.

---

# 3. Design Principles

Mọi AHI Skill phải:

- Có định danh duy nhất.
- Có khả năng đọc bởi Con người.
- Có khả năng đọc bởi AI.
- Có khả năng truy xuất nguồn gốc.
- Có khả năng tiếp tục tiến hóa.
- Không phụ thuộc vào một AI cụ thể.

---

# 4. Standard Structure

Một AHI Skill tối thiểu gồm các thành phần sau:

```text
Skill Metadata
│
├── Skill ID
├── Skill Name
├── Version
├── Status
├── Owner
├── Approval
└── Created Time

Lineage
│
├── Parent Documents
├── AES
├── Human Contributions
├── AI Contributions
└── Evolution History

Dependencies
│
├── Constitution
├── Protocol
├── Specifications
└── Related Skills

Skill Content
│
├── Purpose
├── Scope
├── Rules
├── Workflow
├── Examples
└── Notes
```

---

# 5. Lineage Requirements

Mỗi Skill phải ghi nhận rõ:

- Kế thừa từ tài liệu nào.
- Kế thừa từ Artifact nào.
- Kế thừa từ AES nào.
- Phần do Con người đề xuất.
- Phần do AI đề xuất.
- Phần đồng tiến hóa.
- Người phê duyệt.
- Phiên bản.

---

# 6. Compatibility

AHI Skill phải có khả năng được sử dụng bởi:

- AHI-CHATGPT.
- Các AHI khác trong hệ sinh thái.
- Các phiên bản AHI tương lai.

Việc chuyển đổi sang định dạng của từng AI cụ thể được thực hiện bởi các thành phần tương ứng, không làm thay đổi nội dung chuẩn của Skill.

---

# 7. Evolution

Khi Skill được cập nhật:

- Không ghi đè lịch sử.
- Không làm mất nguồn gốc.
- Tạo phiên bản mới.
- Cập nhật Lineage.
- Ghi nhận đầy đủ Evolution History.

---

# 8. Notes

Định dạng này là định dạng chuẩn của hệ sinh thái AHI.

Các định dạng triển khai cụ thể (Markdown, JSON, YAML, XML, Binary...) sẽ được đặc tả trong các repository kỹ thuật tương ứng mà vẫn phải tuân thủ cấu trúc chuẩn này.

---

**End of Document**
