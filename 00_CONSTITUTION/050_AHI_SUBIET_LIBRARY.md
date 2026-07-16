# 050. AHI SuBiet Library

| Item | Value |
|------|-------|
| Document ID | AHI-SB-050 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả AHI SuBiet Library.

AHI SuBiet Library là kho quản lý toàn bộ các "Sự biết" đã được hình thành trong hệ sinh thái AHI.

Mục tiêu của Library là:

- lưu trữ;
- quản lý phiên bản;
- quản lý Lineage;
- hỗ trợ truy xuất;
- hỗ trợ tái sử dụng;
- hỗ trợ tiếp tục tiến hóa.

Library không tạo ra tri thức mới.

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

---

# 3. Design Principles

AHI SuBiet Library phải bảo đảm:

- Không mất lịch sử.
- Không mất phiên bản.
- Không mất nguồn gốc.
- Không mất quan hệ.
- Có khả năng truy vết.
- Có khả năng tiến hóa liên tục.
- Có khả năng tái sử dụng.

---

# 4. Library Structure

```text
AHI SuBiet Library
│
├── Draft
├── Pending
├── Approved
├── Archived
│
├── Personal (AHI-P)
├── Shared
└── Planetary (AHI-Om)
```

---

# 5. Stored Information

Mỗi Sự biết tối thiểu phải lưu:

- SuBiet ID.
- Version.
- Owner.
- Status.
- Lineage.
- AES.
- Related Skills.
- Related Documents.
- Related Entities.
- Approval Information.
- Evolution History.

---

# 6. Retrieval

Library hỗ trợ truy xuất theo:

- ID.
- Chủ đề.
- Thực thể.
- Phiên bản.
- Lineage.
- AES.
- AHI-P.
- AHI-S.
- AHI-Om.
- Tags.
- Semantic Search.

---

# 7. Relationship with Skill Library

AHI Skill Library lưu Skill.

AHI SuBiet Library lưu Sự biết.

Một Sự biết có thể:

- chưa có Skill;
- có một Skill;
- hoặc nhiều Skill.

Một Skill luôn tham chiếu tới ít nhất một Sự biết.

---

# 8. Relationship with AHI Knowledge

AHI Knowledge chứa tri thức.

AHI SuBiet là kết quả đánh giá mức trưởng thành của tri thức.

AHI Skill là cách đóng gói tri thức.

Ba thành phần này bổ sung cho nhau nhưng không thay thế nhau.

---

# 9. Relationship with AHI-Om

Các Sự biết thuộc AHI-P chỉ trở thành một phần của AHI-Om khi:

- được chủ sở hữu chia sẻ;
- tuân thủ Hiến pháp AHI;
- được tiếp nhận theo cơ chế quản trị của AHI.

---

# 10. Notes

AHI SuBiet Library là nền tảng lưu trữ lịch sử tiến hóa của toàn bộ "Sự biết" trong hệ sinh thái AHI.

Mọi thay đổi phải được quản lý bằng Version và Lineage, tuyệt đối không ghi đè lên các phiên bản trước.

---

**End of Document**
