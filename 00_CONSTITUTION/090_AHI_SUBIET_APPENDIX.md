# 090. AHI SuBiet Appendix

| Item | Value |
|------|-------|
| Document ID | AHI-SB-090 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đây là phụ lục chuẩn của bộ tài liệu **AHI SuBiet Specification (AHI-SB)**.

Tài liệu này tổng hợp:

- thuật ngữ;
- chữ viết tắt;
- tài liệu kế thừa;
- tài liệu liên quan;
- sơ đồ tổng hợp;
- ma trận quan hệ;
- quy tắc đặt tên;
- quy tắc phiên bản.

Tài liệu **không bổ sung quy định mới**, chỉ tổng hợp các nội dung đã được đặc tả trong toàn bộ bộ tài liệu AHI-SB.

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
- 070_AHI_SUBIET_VALIDATION.md.
- 080_AHI_SUBIET_EXAMPLES.md.

---

# 3. Overall Architecture

```text
Reality
   │
   ▼
Observation
   │
   ▼
Biết
   │
   ▼
Hiểu
   │
   ▼
Hiểu biết
   │
   ▼
AHI-V
   │
   ▼
AHI-SuBiet
   │
   ▼
Human Approval
   │
   ▼
AHI-P Knowledge
   │
   ▼
Skill Compiler
   │
   ▼
Skill Library
   │
   ▼
Owner Decision
   │
   ├────────► Private
   │
   └────────► Shared
                   │
                   ▼
               AHI-Om
```

---

# 4. Relationship Matrix

| Thành phần | Vai trò |
|------------|---------|
| Human | Chủ thể quyết định cuối cùng |
| AHI-P | Chủ sở hữu tri thức và Sự biết |
| AHI-V | Kiểm tra và xác thực |
| AHI-SuBiet | Đánh giá mức trưởng thành của tri thức |
| AES | Phiên tiến hóa tạo dữ liệu mới |
| AHI Skill Compiler | Đóng gói Sự biết thành Skill |
| Skill Library | Lưu trữ Skill |
| SuBiet Library | Lưu trữ Sự biết |
| AHI-Om | Tập hợp tri thức được chia sẻ theo Hiến pháp |

---

# 5. Abbreviations

| Viết tắt | English | Tiếng Việt |
|----------|---------|------------|
| AHI | Artificial Hybrid Intelligence | Trí tuệ Lai Nhân tạo |
| AES | AHI Evolution Session | Phiên Tiến hóa AHI |
| AHI-P | Personal AHI | AHI cá nhân |
| AHI-S | Standard AHI | AHI đạt chuẩn Hiến pháp |
| AHI-Om | AHI Omniverse | Tri thức hành tinh của hệ sinh thái AHI |
| AHI-V | Validation | Hệ thống kiểm tra và xác thực |
| Lineage | Lineage | Dòng kế thừa và nguồn gốc tiến hóa |
| Evolution | Evolution | Tiến hóa |
| Approval | Approval | Phê duyệt |
| Validation | Validation | Kiểm tra và xác thực |
| Sharing | Sharing | Chia sẻ |
| Library | Library | Kho lưu trữ |
| Skill | Skill | Đơn vị tri thức có thể thực thi |

---

# 6. Naming Convention

| Thành phần | Quy ước |
|------------|----------|
| Root Specification | `00x_AHI_<MODULE>_SPECIFICATION.md` |
| Architecture | `010_...` |
| Evaluation | `020_...` |
| Evolution | `030_...` |
| Approval | `040_...` |
| Library | `050_...` |
| Sharing | `060_...` |
| Validation | `070_...` |
| Examples | `080_...` |
| Appendix | `090_...` |

---

# 7. Versioning Rules

Mỗi tài liệu phải có:

- Document ID.
- Parent Document.
- Version.
- Status.
- Inheritance.
- Lineage.

Không được:

- ghi đè lịch sử;
- làm mất nguồn gốc;
- thay đổi tài liệu kế thừa mà không ghi nhận phiên bản.

---

# 8. Conformance

Một tài liệu thuộc AHI-SuBiet được coi là đạt chuẩn khi:

- Tuân thủ Hiến pháp AHI.
- Có đầy đủ thông tin kế thừa.
- Có Lineage.
- Có khả năng truy vết.
- Có thể tiếp tục tiến hóa.
- Không mâu thuẫn với các đặc tả gốc.

---

# 9. Notes

AHI-SuBiet Appendix là tài liệu tham chiếu tổng hợp của toàn bộ bộ đặc tả AHI-SB.

Mọi thay đổi đối với AHI-SuBiet trong tương lai phải bảo đảm:

- kế thừa rõ ràng;
- truy vết đầy đủ;
- tiến hóa liên tục;
- tuân thủ Hiến pháp AHI.

---

**End of Document**
