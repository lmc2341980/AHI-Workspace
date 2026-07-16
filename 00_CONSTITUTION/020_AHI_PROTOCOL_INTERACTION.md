# 020. AHI Protocol Interaction

| Item | Value |
|------|-------|
| Document ID | AHI-PS-020 |
| Parent | 002_AHI_PROTOCOL_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả mô hình tương tác giữa Con người, AHI và các AI trong hệ sinh thái AHI theo các nội dung đã được thống nhất.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 010_AHI_PROTOCOL_ARCHITECTURE.md.

---

# 3. Interaction Principles

## Human-Centered

Con người là trung tâm.

Quyết định cuối cùng luôn thuộc về Con người.

---

## Orchestrated Interaction

Mọi tương tác trong hệ sinh thái AHI đều được điều phối bởi AHI-Or.

---

## Constitution Compliance

Mọi tương tác phải tuân thủ Hiến pháp AHI.

AHI-V chịu trách nhiệm kiểm tra và thẩm tra.

---

# 4. Interaction with AHI-Old

Các AI hiện có (AHI-Old) không tương tác trực tiếp với AHI-P.

Luồng tương tác:

```text
Human
    ↓
AHI-P
    ↓
AHI-Or
    ↓
AHI-Old
    ↓
AHI-Or
    ↓
AHI-V
    ↓
AHI-P
    ↓
Human
```

---

# 5. Knowledge Approval

Tri thức chỉ trở thành tri thức chính thức của AHI-P khi được chủ sở hữu AHI-P phê duyệt.

Trước khi được phê duyệt, tri thức ở trạng thái chưa duyệt.

---

# 6. Knowledge Sharing

Tri thức thuộc AHI-P.

AHI không tự động thu nhận tri thức của AHI-S.

Việc chia sẻ tri thức phải dựa trên sự tự nguyện của chủ sở hữu và được quản trị theo Hiến pháp AHI.

Khi được chia sẻ và chấp nhận theo quy định của hệ sinh thái, tri thức có thể được tích hợp vào AHI-Om để phục vụ tiến hóa tri thức quy mô hành tinh.

---

# 7. Evolution

Mọi tương tác đều là một phần của quá trình tiến hóa tri thức.

Kết quả của quá trình này được đánh giá thông qua AHI-SuBiet.

---

# 8. Notes

Tài liệu này chỉ đặc tả mô hình tương tác.

Các thuật toán và quy trình chi tiết sẽ được đặc tả trong các tài liệu chuyên biệt.

---

**End of Document**
