# 040. AHI Skill Execution

| Item | Value |
|------|-------|
| Document ID | AHI-SC-040 |
| Parent | 003_AHI_SKILL_COMPILER_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế thực thi (Execution) của AHI Skill trong hệ sinh thái AHI.

AHI Skill Execution quy định cách một Skill đã được biên dịch và phê duyệt được nạp, thực thi, theo dõi và tiếp tục tiến hóa mà vẫn tuân thủ Hiến pháp AHI.

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

---

# 3. Execution Principles

Việc thực thi Skill phải tuân thủ các nguyên tắc:

- Không vi phạm Hiến pháp AHI.
- Không thay đổi nội dung Skill đã được phê duyệt trong quá trình thực thi.
- Có khả năng ghi nhận kết quả để phục vụ tiến hóa.
- Có khả năng tạm dừng, tiếp tục hoặc thay thế bằng phiên bản mới khi được phê duyệt.

---

# 4. Execution Flow

```text
Skill Package
      │
      ▼
AHI-Or
      │
      ▼
Execution Context
      │
      ▼
Skill Runtime
      │
      ▼
Execution Result
      │
      ▼
AHI-V
      │
      ▼
AHI-SuBiet
      │
      ▼
AES
      │
      ▼
Next Skill Version (Optional)
```

---

# 5. Execution Context

Một Skill được thực thi trong ngữ cảnh xác định, có thể bao gồm:

- Chủ sở hữu AHI-P.
- Phiên làm việc hiện tại.
- Dữ liệu đầu vào.
- Các tài nguyên được cấp quyền.
- Các Skill phụ thuộc.
- Các quy định của Hiến pháp AHI.

---

# 6. Execution Result

Kết quả thực thi phải có khả năng ghi nhận:

- Kết quả đầu ra.
- Nhật ký thực thi.
- Các quyết định của Con người.
- Các đề xuất của AI.
- Các điểm cần cải tiến.
- Dữ liệu phục vụ AES tiếp theo.

---

# 7. Evolution after Execution

Việc thực thi không kết thúc vòng đời của Skill.

Nếu có tri thức mới được hình thành và được chủ sở hữu phê duyệt, kết quả sẽ trở thành đầu vào của một AHI Evolution Session (AES) mới để tiếp tục tiến hóa.

---

# 8. Relationship with AHI-Or and AHI-V

- AHI-Or chịu trách nhiệm điều phối việc thực thi.
- AHI-V kiểm tra sự tuân thủ Hiến pháp và tính nhất quán.
- AHI-SuBiet đánh giá kết quả tiến hóa.
- Con người quyết định việc chấp nhận hay từ chối kết quả.

---

# 9. Notes

Tài liệu này đặc tả cơ chế thực thi ở mức kiến trúc.

Các Runtime Engine, Execution Engine và cơ chế triển khai cụ thể sẽ được đặc tả trong các repository kỹ thuật tương ứng.

---

**End of Document**
