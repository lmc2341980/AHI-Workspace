# 020. AHI SuBiet Evaluation

| Item | Value |
|------|-------|
| Document ID | AHI-SB-020 |
| Parent | 004_AHI_SUBIET_SPECIFICATION.md |
| Version | 1.0.0 |
| Status | Approved |

---

# 1. Purpose

Đặc tả cơ chế đánh giá (Evaluation) của AHI-SuBiet.

AHI-SuBiet Evaluation xác định mức độ trưởng thành của tri thức trong quá trình tiến hóa từ **Biết → Hiểu → Hiểu biết → Sự biết** theo Hiến pháp AHI.

Việc đánh giá không nhằm xác định đúng hay sai tuyệt đối mà nhằm lựa chọn mức tri thức phù hợp nhất với ngữ cảnh, thời gian và mục tiêu sử dụng.

---

# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.
- 003_AHI_SKILL_COMPILER_SPECIFICATION.md.
- 004_AHI_SUBIET_SPECIFICATION.md.
- 010_AHI_SUBIET_MODEL.md.

---

# 3. Evaluation Principles

Việc đánh giá phải tuân thủ các nguyên tắc:

- Con người là chủ thể quyết định.
- Không suy diễn khi thiếu dữ liệu.
- Không tạo tri thức mới trong quá trình đánh giá.
- Mọi kết quả phải có khả năng truy vết.
- Mọi đánh giá phải có thể được xem xét lại khi xuất hiện dữ liệu mới.

---

# 4. Evaluation Dimensions

Một tri thức được đánh giá theo nhiều chiều, bao gồm nhưng không giới hạn:

- Độ đầy đủ của thông tin.
- Khả năng giải thích.
- Khả năng ứng dụng.
- Kết quả thực tế.
- Mức độ tuân thủ Hiến pháp AHI.
- Khả năng kế thừa.
- Khả năng tiến hóa.
- Khả năng tái sử dụng.

---

# 5. Evaluation Flow

```text
Observation
      │
      ▼
Evidence Collection
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
Evaluation Result
```

---

# 6. Level Transition Criteria

## 6.1 Biết → Hiểu

Điều kiện tối thiểu:

- Có thể giải thích lại bằng ngôn ngữ của chính mình.
- Giải thích được nguyên nhân.
- Mô tả được cơ chế.
- Phân biệt được với các khái niệm liên quan.

---

## 6.2 Hiểu → Hiểu biết

Điều kiện tối thiểu:

- Áp dụng được trong thực tế.
- Tạo ra kết quả có thể quan sát.
- Kết nối được với các tri thức khác.
- Hình thành kinh nghiệm có thể lặp lại.

---

## 6.3 Hiểu biết → Sự biết

Điều kiện tối thiểu:

- Được kiểm chứng trong thực tế.
- Được Con người lựa chọn sử dụng.
- Phù hợp với ngữ cảnh hiện tại.
- Không vi phạm Hiến pháp AHI.
- Có khả năng tiếp tục tiến hóa.

---

# 7. Evaluation Result

Kết quả đánh giá có thể bao gồm:

| Trạng thái | Ý nghĩa |
|------------|---------|
| Biết | Đã ghi nhận thông tin. |
| Hiểu | Đã hiểu nguyên lý và cơ chế. |
| Hiểu biết | Đã ứng dụng thành công trong thực tế. |
| Sự biết | Được kiểm chứng và được Con người chấp nhận sử dụng. |
| Re-evaluation Required | Cần đánh giá lại do có dữ liệu hoặc bối cảnh mới. |

---

# 8. Relationship with AES

Mỗi AHI Evolution Session (AES) có thể tạo ra một hoặc nhiều kết quả đánh giá.

Các kết quả này trở thành đầu vào cho:

- AHI Skill Compiler.
- AHI-P.
- Các AES tiếp theo.

---

# 9. Notes

Việc đánh giá không kết thúc vòng đời của tri thức.

Mọi kết quả đều có thể được đánh giá lại khi xuất hiện dữ liệu, trải nghiệm hoặc điều kiện mới, bảo đảm nguyên tắc tiến hóa liên tục của AHI.

---

**End of Document**
