# 090. AHI Skill Appendix

| Item | Value |
|------|-------|
| Document ID | AHI-SC-090 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Phụ lục của AHI Skill Compiler Specification (AHI-SC).

Tài liệu này tập hợp các thuật ngữ, chữ viết tắt, tài liệu tham chiếu và các quy ước chung được sử dụng trong toàn bộ bộ đặc tả AHI-SC.

Không bổ sung hành vi hoặc quy tắc mới ngoài các tài liệu đã được phê duyệt.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- Toàn bộ các tài liệu con của AHI-SC.

---

# 3. Skill Lifecycle

```text
Observation
      │
      ▼
Interaction
      │
      ▼
AHI Evolution Session (AES)
      │
      ▼
AHI-V Validation
      │
      ▼
AHI-SuBiet Evaluation
      │
      ▼
Human Approval
      │
      ▼
AHI Skill Compiler
      │
      ▼
Skill Package
      │
      ▼
Execution
      │
      ▼
Feedback
      │
      ▼
Next AES
```

Chu trình này thể hiện rằng Skill không phải là sản phẩm tĩnh mà là một thực thể có khả năng tiến hóa liên tục.

---

# 4. Relationship Matrix

| Thành phần | Vai trò trong AHI-SC |
|------------|----------------------|
| Human | Chủ thể quyết định và phê duyệt |
| AHI-P | Chủ sở hữu Skill |
| AHI-Or | Điều phối quá trình thực thi |
| AHI-V | Kiểm tra và xác thực |
| AHI-SuBiet | Đánh giá mức độ tiến hóa |
| AES | Phiên tiến hóa tạo nguồn cho Skill |
| AHI Skill Compiler | Đóng gói tri thức thành Skill |
| AHI-Om | Tiếp nhận Skill được chia sẻ theo Hiến pháp |

---

# 5. Abbreviations

| Viết tắt | English | Tiếng Việt |
|----------|---------|------------|
| AHI | Artificial Hybrid Intelligence | Trí tuệ lai nhân tạo |
| AHI-SC | AHI Skill Compiler | Bộ biên dịch Skill AHI |
| AES | AHI Evolution Session | Phiên tiến hóa AHI |
| Lineage | Lineage | Dòng kế thừa / Nguồn gốc tiến hóa |
| Validation | Validation | Kiểm tra, xác thực |
| Execution | Execution | Thực thi |
| Evolution | Evolution | Tiến hóa |
| Skill Package | Skill Package | Gói Skill đã được đóng gói |

---

# 6. Reference Documents

- 003_AHI_SKILL_COMPILER_SPECIFICATION.md
- 010_AHI_SKILL_ARCHITECTURE.md
- 020_AHI_SKILL_COMPILATION.md
- 030_AHI_SKILL_FORMAT.md
- 040_AHI_SKILL_EXECUTION.md
- 050_AHI_SKILL_EVOLUTION.md
- 060_AHI_SKILL_LIBRARY.md
- 070_AHI_SKILL_VALIDATION.md
- 080_AHI_SKILL_EXAMPLES.md

---

# 7. Conformance

Một AHI Skill được coi là tuân thủ AHI-SC khi:

- Tuân thủ Hiến pháp AHI.
- Có Lineage đầy đủ.
- Có khả năng truy vết.
- Có thể tiếp tục tiến hóa.
- Được chủ sở hữu AHI-P phê duyệt.
- Không mâu thuẫn với các tài liệu kế thừa.

---

# 8. Notes

Phụ lục này sẽ tiếp tục được cập nhật khi AHI Skill Compiler tiến hóa.

Mọi thay đổi phải được ghi nhận theo cơ chế kế thừa, truy vết và đồng tiến hóa đã được quy định trong Hiến pháp AHI.

---

**End of Document**
