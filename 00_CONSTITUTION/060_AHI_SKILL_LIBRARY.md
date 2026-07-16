# 060. AHI Skill Library

| Item | Value |
|------|-------|
| Document ID | AHI-SC-060 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả mô hình quản lý thư viện Skill (AHI Skill Library) trong hệ sinh thái AHI.

AHI Skill Library là nơi tổ chức, quản lý, truy xuất và tái sử dụng các Skill đã được biên dịch theo AHI Skill Compiler.

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

---

# 3. Design Principles

AHI Skill Library được xây dựng theo các nguyên tắc:

- Có khả năng truy xuất.
- Có khả năng kế thừa.
- Có khả năng tiến hóa.
- Không trùng lặp không cần thiết.
- Có thể kiểm chứng nguồn gốc.

---

# 4. Skill Categories

Skill có thể được tổ chức theo nhiều chiều, ví dụ:

- Domain.
- Chức năng.
- Chủ sở hữu AHI-P.
- Mức AHI-S.
- Phiên bản.
- Mức AHI-SuBiet.
- Trạng thái phê duyệt.

Việc phân loại cụ thể sẽ được đặc tả trong các repository chuyên biệt.

---

# 5. Skill Metadata

Mỗi Skill trong Library tối thiểu phải có:

- Skill ID.
- Tên Skill.
- Phiên bản.
- Trạng thái.
- Chủ sở hữu.
- Lineage.
- Tài liệu kế thừa.
- AES liên quan.
- Ngày tạo.
- Ngày cập nhật.

---

# 6. Skill Retrieval

Việc truy xuất Skill có thể dựa trên:

- Định danh.
- Chủ đề.
- Thực thể liên quan.
- Từ khóa.
- Lineage.
- Mức AHI-SuBiet.
- Phiên bản.

Cơ chế truy xuất cụ thể sẽ do các thành phần tìm kiếm của AHI thực hiện.

---

# 7. Relationship with AHI Knowledge

AHI Skill Library không thay thế kho tri thức.

Skill là kết quả đóng gói từ tri thức đã được phê duyệt để phục vụ tái sử dụng.

Tri thức gốc vẫn được quản lý theo các đặc tả Knowledge và Memory của AHI.

---

# 8. Relationship with AHI-Om

Các Skill được chia sẻ theo quy định của Hiến pháp có thể được tham chiếu trong AHI-Om.

Việc lưu trữ trong AHI Skill Library và việc chia sẻ lên AHI-Om là hai cơ chế độc lập.

---

# 9. Notes

Tài liệu này mô tả mô hình thư viện Skill ở mức kiến trúc.

Các cơ chế lập chỉ mục, tìm kiếm ngữ nghĩa, xếp hạng và quản trị vòng đời sẽ được đặc tả trong các tài liệu kỹ thuật tương ứng.

---

**End of Document**
