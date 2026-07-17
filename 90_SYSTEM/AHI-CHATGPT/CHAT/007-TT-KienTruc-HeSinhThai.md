# AHI-Workspace – Nội dung đã cung cấp và đã thống nhất (Checkpoint)

> **Mục đích**
>
> Tài liệu này ghi lại các nguyên tắc làm việc đã được thống nhất để tránh mất ngữ cảnh, suy diễn hoặc làm sai chuỗi khi chuyển sang cửa sổ CHAT mới.

---

# I. Nội dung người dùng đã cung cấp

## 1. Định hướng AHI

* AHI đi theo hướng **Artificial Hybrid Intelligence (Trí tuệ nhân lai)**.
* GitHub là **Source of Truth**.
* Mọi cuộc hội thoại chỉ là nơi tiến hóa tri thức trước khi chuẩn hóa thành Artifact và đưa lên GitHub.
* Không suy diễn.
* Không bịa dữ liệu.
* Không coi Proposal là Fact.
* Thiếu dữ liệu phải nói rõ và hỏi.
* Ưu tiên tính đúng đắn hơn sự đồng thuận.

---

## 2. Quy trình phát triển

Quy trình làm việc được thống nhất:

```text
Conversation
        ↓
Workflow
        ↓
Skill
        ↓
Specification
        ↓
Artifact
        ↓
GitHub
        ↓
Evolution
```

GitHub là phiên bản chính thức (Current Best Version).

---

## 3. Chuẩn GitHub

Mọi phản hồi GitHub theo đúng thứ tự:

```text
CM (Commit Message)
        ↓
PATH
        ↓
CONTENT
```

Không dùng Patch nếu không được yêu cầu.

Không dùng Diff nếu không được yêu cầu.

Ưu tiên để người dùng chỉ cần copy một lần.

---

## 4. Quy trình tạo Artifact

Mỗi Artifact được tạo theo đúng trình tự:

```text
CM
        ↓
PATH
        ↓
CONTENT
        ↓
DONE
```

---

## 5. Tín hiệu hoàn thành

Đã thống nhất:

* `DONE` là tín hiệu hoàn thành.
* **CM của file trước hoặc thư mục trước đã hoàn thành cũng được xem là tín hiệu hoàn thành và là lệnh để thực hiện bước kế tiếp.**

Điều này tương đương:

```text
DONE
        =
Commit Message Completed
        =
Execute Next Step
```

---

## 6. Tiếp tục khi sang cửa sổ CHAT mới

Đã thống nhất:

Không được:

* tự suy diễn checkpoint;
* tự quay lại bước cũ;
* tự dựng lại roadmap;
* tự đổi phase;
* tự tạo file tiếp theo khi chưa xác định đúng checkpoint.

Phải kiểm tra theo thứ tự:

```text
Project
        ↓
Folder hiện tại
        ↓
File cuối
        ↓
CM cuối
        ↓
DONE
        ↓
Tiếp tục bước kế tiếp
```

Nếu không xác định được checkpoint thì phải yêu cầu dữ liệu gốc, không được đoán.

---

## 7. Trạng thái tri thức

Phân biệt rõ:

```text
Proposal
        ↓
Discussing
        ↓
Approved
        ↓
Artifact
        ↓
Implemented
        ↓
Deprecated
```

Không coi Proposal là Fact.

---

# II. Nội dung đã thống nhất

## 1. GitHub là Source of Truth

Mọi Artifact chính thức đều nằm trên GitHub.

Chat không phải nguồn chính thức.

---

## 2. Không suy diễn

Khi thiếu dữ liệu:

* không tự tạo nội dung;
* không tự đoán checkpoint;
* không tự dựng cấu trúc.

---

## 3. Kế thừa trước khi tạo mới

Nếu Artifact đã tồn tại:

* đọc trước;
* kế thừa;
* tiến hóa;
* không viết lại từ đầu.

---

## 4. Kiến trúc đã khóa (Architecture Lock)

Những phần đã thống nhất không được tự ý thay đổi nếu không có yêu cầu rõ ràng.

---

## 5. CM là tín hiệu điều khiển

Sau khi người dùng gửi lại Commit Message của bước vừa hoàn thành:

AI phải hiểu:

```text
DONE
        ↓
Thực hiện Artifact tiếp theo
```

Không hỏi lại bước trước.

Không quay lại nội dung cũ.

---

## 6. Quy tắc khi chuyển CHAT

Checkpoint phải được xác định bằng:

```text
Folder
        ↓
File cuối
        ↓
CM cuối
        ↓
DONE
```

Không sử dụng suy luận để xác định tiến độ.

---

## 7. Quy tắc chống Hallucination

Nếu thiếu dữ liệu:

Đúng:

```text
Chưa đủ dữ liệu để xác định checkpoint.
Vui lòng cung cấp CM hoặc PATH cuối.
```

Sai:

```text
Tôi đoán...
```

---

# III. Nội dung cần bổ sung vào nguyên tắc chuẩn

Qua quá trình làm việc đã phát hiện cần bổ sung:

## 1.

Checkpoint không chỉ là DONE.

Checkpoint còn bao gồm:

* CM cuối.
* PATH cuối.
* File cuối.
* Thư mục hiện tại.

---

## 2.

CM hoàn thành có giá trị tương đương DONE và đồng thời là tín hiệu chuyển sang bước tiếp theo.

---

## 3.

Khi chuyển sang cửa sổ CHAT mới:

Không được phục hồi tiến độ bằng trí nhớ hoặc suy luận.

Chỉ được phục hồi bằng checkpoint đã được xác nhận.

---

## 4.

Nếu không có checkpoint:

Phải yêu cầu người dùng cung cấp.

Không được tự tạo.

---

# IV. Vấn đề đã phát hiện

Trong quá trình làm việc đã xảy ra lỗi:

* Tự suy diễn checkpoint.
* Quay lại file cũ.
* Tạo sai chuỗi Specification.
* Trộn lẫn tư tưởng AHI với AHI-Workspace.
* Mô tả AHI-Workspace theo hiểu biết chung thay vì theo tư tưởng thiết kế gốc.
* Không phân biệt giữa:

  * AHI.
  * AHI-Workspace.
  * Module/API/SPEC.

Các lỗi này đã được xác định là không được phép lặp lại.

---

# V. Nội dung còn thiếu (chưa được xác nhận)

Hiện **chưa đủ dữ liệu** để xác định chính xác tư tưởng thiết kế gốc của **AHI-Workspace** từ cửa sổ CHAT **"Thiết kế AHI-Workspace"**.

Do đó:

* Không được tự diễn giải.
* Không được tự bổ sung.
* Chỉ được hoàn thiện sau khi đọc lại nội dung gốc của cửa sổ CHAT đó.
