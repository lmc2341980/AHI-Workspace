# 003. AHI Skill Compiler Specification (AHI-SC)

| Item | Value |
|------|-------|
| Document ID | AHI-SC-003 |
| Version | 1.0.0 |
| Status | Approved |
| Repository | AHI-Workspace |
| Path | `00_CONSTITUTION/003_AHI_SKILL_COMPILER_SPECIFICATION.md` |

---

# 1. Purpose

AHI Skill Compiler Specification (AHI-SC) là tài liệu gốc đặc tả cơ chế chuyển đổi tri thức đã được thống nhất thành Skill có thể sử dụng trong hệ sinh thái AHI.

AHI-SC là một thành phần của AHI Protocol Specification (AHI-PS).

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.

---

# 3. Scope

AHI-SC quy định:

- Quy trình đóng gói tri thức thành Skill.
- Quy trình kế thừa và tiến hóa Skill.
- Quan hệ giữa AES, AHI-SB, Artifact và Skill.
- Cấu trúc chuẩn của Skill.
- Quy trình nạp Skill vào AHI-CHATGPT trong giai đoạn AHI-Workspace chưa hoàn thiện.

---

# 4. Document Structure

AHI-SC được tổ chức thành các tài liệu con.

```text
003_AHI_SKILL_COMPILER_SPECIFICATION.md

010_AHI_SKILL_ARCHITECTURE.md

020_AHI_SKILL_COMPILATION.md

030_AHI_SKILL_FORMAT.md

040_AHI_SKILL_EXECUTION.md

050_AHI_SKILL_EVOLUTION.md

060_AHI_SKILL_LIBRARY.md

070_AHI_SKILL_VALIDATION.md

080_AHI_SKILL_EXAMPLES.md

090_AHI_SKILL_APPENDIX.md
```

---

# 5. Evolution Rule

Các tài liệu con:

- kế thừa Hiến pháp AHI;
- kế thừa tài liệu gốc này;
- chỉ tiến hóa trong phạm vi của mình;
- không được mâu thuẫn với AHI-PS.

---

# 6. Notes

Tài liệu này chỉ định nghĩa phạm vi và cấu trúc của AHI Skill Compiler.

Các cơ chế chi tiết được đặc tả trong các tài liệu con.

---

**End of Document**
