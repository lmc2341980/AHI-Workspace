# AHI Commit Standard
(**Tiêu chuẩn Commit AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-COMMIT-STANDARD |
| Version | R001 |
| Status | Active |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This document defines the mandatory Commit Message standard for all repositories in the Artificial Hybrid Intelligence (AHI - Trí tuệ Nhân tạo Lai) ecosystem.

(Tài liệu này quy định tiêu chuẩn bắt buộc về Commit Message cho toàn bộ Repository trong hệ sinh thái Trí tuệ Nhân tạo Lai.)

---

# Rule 001 (Quy tắc 001)

Every Commit Message shall begin with the prefix **AHI**.

(Mọi Commit Message phải bắt đầu bằng tiền tố **AHI**.)

---

# Rule 002 (Quy tắc 002)

The Commit Message format shall be:

(Định dạng Commit Message là:)

```text
AHI <TYPE>: <Short Description>
```

Example (Ví dụ)

```text
AHI DOC: Create AHI Commit Standard
AHI ARCH: Add Workspace Architecture
AHI CORE: Add Memory Manager
AHI FIX: Correct Translation Error
```

---

# Rule 003 (Quy tắc 003)

The Commit Message shall be written in English.

(Commit Message phải được viết bằng tiếng Anh.)

---

# Rule 004 (Quy tắc 004)

The description shall start with a verb.

(Mô tả phải bắt đầu bằng một động từ.)

Examples (Ví dụ)

- Add
- Create
- Update
- Remove
- Refactor
- Improve
- Fix
- Rename
- Move
- Standardize
- Initialize

---

# Rule 005 (Quy tắc 005)

Each commit shall represent one logical work unit.

(Mỗi Commit chỉ đại diện cho một đơn vị công việc logic.)

---

# Rule 006 (Quy tắc 006)

Do not mix unrelated changes in the same commit.

(Không gộp các thay đổi không liên quan trong cùng một Commit.)

---

# Rule 007 (Quy tắc 007)

Commit types shall use the following standard.

(Các loại Commit sử dụng tiêu chuẩn sau.)

| Type | Meaning | Ý nghĩa |
|------|---------|---------|
| DOC | Documentation | Tài liệu |
| ARCH | Architecture | Kiến trúc |
| CORE | Core | Lõi |
| MEM | Memory | Bộ nhớ |
| LANG | Language | Ngôn ngữ |
| API | Application Programming Interface | Giao diện lập trình ứng dụng |
| UI | User Interface | Giao diện người dùng |
| TEST | Testing | Kiểm thử |
| FIX | Bug Fix | Sửa lỗi |
| REF | Refactor | Tái cấu trúc |
| PERF | Performance | Hiệu năng |
| BUILD | Build System | Hệ thống Build |
| DEVOPS | Development Operations | Vận hành phát triển |
| SECURITY | Security | Bảo mật |
| RELEASE | Release | Phát hành |

---

# Rule 008 (Quy tắc 008)

Commit Messages should be concise.

(Commit Message nên ngắn gọn.)

Recommended length (Độ dài khuyến nghị):

Less than 72 characters.

(Dưới 72 ký tự.)

---

# Rule 009 (Quy tắc 009)

Every repository within the AHI ecosystem shall follow this Commit Message standard.

(Mọi Repository trong hệ sinh thái AHI phải tuân thủ tiêu chuẩn Commit Message này.)

---

# Rule 010 (Quy tắc 010)

ChatGPT shall always generate the Commit Message before generating file contents.

(ChatGPT luôn phải sinh Commit Message trước khi sinh nội dung tệp.)

---

# Revision History (Lịch sử phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
