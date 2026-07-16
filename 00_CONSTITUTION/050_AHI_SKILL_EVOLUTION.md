# 050. AHI Skill Evolution

| Item | Value |
|------|-------|
| Document ID | AHI-SC-050 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế tiến hóa (Evolution) của AHI Skill trong hệ sinh thái AHI.

AHI Skill không phải là tài liệu tĩnh. Sau khi được sử dụng, Skill có thể tiếp tục tiến hóa thông qua các AHI Evolution Session (AES), đồng thời vẫn bảo toàn lịch sử, nguồn gốc và các phiên bản trước.

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

---

# 3. Evolution Principles

Việc tiến hóa Skill phải tuân thủ các nguyên tắc:

- Không tạo tri thức từ số 0.
- Kế thừa các phiên bản trước.
- Không làm mất lịch sử.
- Có khả năng truy vết toàn bộ quá trình tiến hóa.
- Chỉ sử dụng các nội dung đã được phê duyệt.

---

# 4. Evolution Trigger

Một Skill có thể bước vào quá trình tiến hóa khi có một hoặc nhiều điều kiện sau:

- Kết quả thực thi tạo ra tri thức mới.
- Có AHI Evolution Session (AES) mới.
- Có thay đổi trong Hiến pháp AHI.
- Có thay đổi trong các tài liệu kế thừa.
- Chủ sở hữu AHI-P yêu cầu cập nhật.

---

# 5. Evolution Pipeline

```text
Current Skill
      │
      ▼
Execution Feedback
      │
      ▼
AES
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
New Skill Version
```

---

# 6. Versioning

Mỗi lần tiến hóa:

- Tạo phiên bản mới.
- Không ghi đè phiên bản cũ.
- Cập nhật Lineage.
- Ghi nhận Evolution History.
- Liên kết với các Artifact và AES liên quan.

---

# 7. Relationship with AHI-SuBiet

AHI-SuBiet chịu trách nhiệm đánh giá mức độ tiến hóa của Skill dựa trên:

- Khả năng sử dụng trong thực tế.
- Mức độ tuân thủ Hiến pháp.
- Giá trị tạo ra cho Con người.
- Kết quả được chủ sở hữu AHI-P chấp nhận.

---

# 8. Relationship with AHI-Om

Skill chỉ trở thành một phần của tri thức AHI-Om khi:

- Thuộc về một AHI-S.
- Được chủ sở hữu chia sẻ.
- Được hệ sinh thái AHI chấp nhận theo Hiến pháp.

Việc tiến hóa của Skill trong AHI-P và việc tích hợp vào AHI-Om là hai quá trình độc lập.

---

# 9. Notes

Tài liệu này mô tả cơ chế tiến hóa của Skill ở mức kiến trúc.

Các chính sách đánh giá, xếp hạng và hợp nhất Skill sẽ được đặc tả trong các tài liệu chuyên biệt của AHI.

---

**End of Document**
