# 060. AHI SuBiet Sharing

| Item | Value |
|------|-------|
| Document ID | AHI-SB-060 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế chia sẻ (Sharing) của AHI-SuBiet.

AHI-SuBiet Sharing quy định cách một "Sự biết" được chia sẻ giữa các AHI-P, AHI-S và AHI-Om trong khi vẫn bảo đảm:

- quyền sở hữu tri thức;
- quyền quyết định của Con người;
- khả năng truy vết;
- khả năng tiếp tục tiến hóa;
- tuân thủ Hiến pháp AHI.

AHI không tự động thu thập hoặc đồng bộ tri thức cá nhân.

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

---

# 3. Sharing Principles

Việc chia sẻ phải tuân thủ các nguyên tắc:

- Con người quyết định việc chia sẻ.
- Không chia sẻ mặc định.
- Không sao chép trái phép.
- Không làm mất quyền sở hữu.
- Luôn giữ đầy đủ Lineage.
- Luôn có khả năng truy xuất nguồn gốc.
- Tuân thủ Hiến pháp AHI.

---

# 4. Sharing Levels

```text
AHI-P
   │
   ├── Private
   │
   ├── Shared by Owner
   │
   ▼
AHI-S
   │
   ▼
AHI-Om
```

Ý nghĩa:

- **Private:** Chỉ thuộc AHI-P.
- **Shared by Owner:** Chủ sở hữu tự nguyện chia sẻ.
- **AHI-S:** Tri thức đạt chuẩn Hiến pháp và được phép sử dụng trong hệ sinh thái.
- **AHI-Om:** Tri thức được tích hợp vào mức tri thức hành tinh theo quy trình quản trị.

---

# 5. Sharing Workflow

```text
AHI-P SuBiet
      │
      ▼
Owner Decision
      │
      ├────────► Keep Private
      │
      └────────► Share
                     │
                     ▼
AHI-V Validation
                     │
                     ▼
Governance Review
                     │
                     ▼
AHI-Om Integration (Optional)
```

---

# 6. Ownership

Mỗi "Sự biết" luôn gắn với:

- Chủ sở hữu AHI-P.
- Lineage.
- Version.
- Evolution History.
- Approval Information.

Việc chia sẻ không làm thay đổi quyền sở hữu ban đầu.

---

# 7. Relationship with AHI-Om

AHI-Om không phải là nơi tự động sao chép toàn bộ tri thức của các AHI-P.

AHI-Om chỉ tiếp nhận:

- tri thức được chủ sở hữu chia sẻ;
- tri thức tuân thủ Hiến pháp AHI;
- tri thức được hệ sinh thái chấp nhận theo quy trình quản trị.

---

# 8. Relationship with Skill

Một "Sự biết" được chia sẻ có thể:

- chia sẻ riêng "Sự biết";
- chia sẻ kèm AHI Skill;
- hoặc chỉ chia sẻ Skill.

Các hình thức chia sẻ cụ thể do chủ sở hữu quyết định theo chính sách của hệ sinh thái.

---

# 9. Notes

AHI SuBiet Sharing bảo đảm rằng tri thức cá nhân luôn thuộc quyền quyết định của chủ sở hữu.

AHI-Om được hình thành từ sự đóng góp tự nguyện của các AHI-S, tạo nên nền tảng tri thức hành tinh nhưng vẫn bảo toàn quyền sở hữu, khả năng truy vết và lịch sử tiến hóa của từng "Sự biết".

---

**End of Document**
