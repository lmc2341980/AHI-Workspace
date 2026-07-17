# AHI-CHATGPT Principle Reference Skill

| Item | Value |
|------|-------|
| Skill ID | AHI-CHATGPT-SKILL-005 |
| Skill Name | One Principle → One Skill → Many References |
| Version | 1.0.0 |
| Status | Approved |
| Type | Core Skill |

---

# Purpose

Chuẩn hóa việc quản lý các nguyên tắc trong toàn bộ hệ sinh thái AHI.

Một nguyên tắc chỉ được định nghĩa một lần.

Mọi nơi khác chỉ tham chiếu.

---

# Core Principle

One Principle

↓

One Skill

↓

Many References

---

# Rules

Không sao chép cùng một nguyên tắc vào nhiều Artifact.

Nếu một nguyên tắc được sử dụng từ hai nơi trở lên:

1. Chuẩn hóa thành một Skill độc lập.
2. Các Artifact chỉ tham chiếu Skill.
3. Chỉ cập nhật Skill khi nguyên tắc tiến hóa.
4. Artifact tự động kế thừa.

---

# Example

❌ Không đúng

Workflow.md

- Think Twice

Artifact.md

- Think Twice

GitHub.md

- Think Twice

Ba nơi cùng chứa một nội dung.

---

✅ Đúng

Think Twice Skill

↓

Workflow Reference

↓

Artifact Reference

↓

GitHub Reference

---

# Benefits

- Một nguồn sự thật.
- Không trùng lặp.
- Dễ tiến hóa.
- Dễ kiểm tra.
- Dễ tái sử dụng.
- Giảm công bảo trì.

---

# Evolution

Nguyên tắc này áp dụng cho:

- Constitution
- Skill
- Specification
- Workflow
- Artifact
- Runtime
- Documentation

---

End of Skill
