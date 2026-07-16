# 040. AHI SuBiet Approval

| Item | Value |
|------|-------|
| Document ID | AHI-SB-040 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế phê duyệt (Approval) của AHI-SuBiet.

AHI-SuBiet Approval quy định cách một kết quả đánh giá được xác nhận để trở thành "Sự biết" của AHI-P và điều kiện để tiếp tục tiến hóa hoặc được chia sẻ sang AHI-Om.

Việc phê duyệt luôn đặt **Con người là chủ thể quyết định cuối cùng**, AI chỉ đóng vai trò hỗ trợ, phân tích và đề xuất.

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

---

# 3. Approval Principles

Việc phê duyệt phải tuân thủ các nguyên tắc:

- Con người là chủ thể quyết định.
- AI không tự động phê duyệt.
- Không phê duyệt khi thiếu thông tin.
- Không suy diễn hoặc tự bổ sung dữ liệu.
- Mọi quyết định đều phải có khả năng truy vết.
- Mọi thay đổi phải được ghi nhận theo Lineage.

---

# 4. Approval Workflow

```text
Observation
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
Human Review
      │
      ▼
Approval Decision
      │
      ├────────► Rejected
      │
      ├────────► Pending
      │
      └────────► Approved
                     │
                     ▼
             AHI-P Knowledge
                     │
                     ▼
             Skill Compilation (Optional)
                     │
                     ▼
            AHI-Om Sharing (Optional)
```

---

# 5. Approval States

| Trạng thái | Ý nghĩa |
|------------|---------|
| Draft | Đang hình thành trong quá trình tiến hóa. |
| Pending | Chờ chủ sở hữu xem xét. |
| Approved | Được chủ sở hữu AHI-P phê duyệt. |
| Rejected | Không được phê duyệt. |
| Archived | Lưu lịch sử, không còn sử dụng mặc định nhưng vẫn có thể truy xuất. |

---

# 6. Human Approval

Một "Sự biết" chỉ được coi là chính thức khi:

- Đã trải qua AHI-V Validation.
- Đã được AHI-SuBiet đánh giá.
- Được chủ sở hữu AHI-P phê duyệt.
- Tuân thủ Hiến pháp AHI.

Nếu thiếu bất kỳ điều kiện nào ở trên, kết quả vẫn chỉ là tri thức đang tiến hóa.

---

# 7. Relationship with Skill

Sau khi được phê duyệt:

- Có thể được đóng gói thành AHI Skill.
- Có thể tiếp tục tiến hóa qua các AES mới.
- Không làm thay đổi hoặc mất phiên bản đã phê duyệt trước đó.

---

# 8. Relationship with AHI-Om

Việc được phê duyệt trong AHI-P **không đồng nghĩa** với việc trở thành tri thức của AHI-Om.

Một "Sự biết" chỉ được tích hợp vào AHI-Om khi:

- Chủ sở hữu tự nguyện chia sẻ.
- Tuân thủ Hiến pháp AHI.
- Được hệ sinh thái AHI tiếp nhận theo quy trình quản trị.

---

# 9. Notes

AHI-SuBiet Approval là điểm chuyển đổi từ tri thức đang tiến hóa sang tri thức đã được xác nhận trong phạm vi AHI-P.

Việc phê duyệt không kết thúc quá trình tiến hóa mà mở ra các chu kỳ tiến hóa tiếp theo thông qua AHI Evolution Session (AES).

---

**End of Document**
