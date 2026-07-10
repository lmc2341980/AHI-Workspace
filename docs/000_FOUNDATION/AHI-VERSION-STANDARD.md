# AHI Version Standard
(**Tiêu chuẩn Phiên bản AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-VERSION-STANDARD |
| Version | R001 |
| Status | Active |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This document defines the mandatory versioning standard for repositories, documents, applications and components within the Artificial Hybrid Intelligence (AHI - Trí tuệ Nhân tạo Lai) ecosystem.

(Tài liệu này quy định tiêu chuẩn đánh phiên bản cho Repository, tài liệu, ứng dụng và các thành phần trong hệ sinh thái Trí tuệ Nhân tạo Lai.)

---

# Rule 001 (Quy tắc 001)

Every repository shall have its own independent version.

(Mỗi Repository có phiên bản độc lập.)

Example (Ví dụ)

```text
AHI-Workspace R001
AHI-Core R001
AHI-Language R001
```

---

# Rule 002 (Quy tắc 002)

Documents shall use Revision (Bản sửa đổi) numbers.

(Tài liệu sử dụng số Revision.)

Format (Định dạng)

```text
R001
R002
...
R999
```

---

# Rule 003 (Quy tắc 003)

Applications shall use Semantic Versioning (Đánh phiên bản ngữ nghĩa).

Format (Định dạng)

```text
Major.Minor.Patch

1.0.0
1.1.0
1.1.1
2.0.0
```

---

# Rule 004 (Quy tắc 004)

Repository releases shall use Git Tags (Thẻ Git).

Format (Định dạng)

```text
v1.0.0
v1.1.0
v2.0.0
```

---

# Rule 005 (Quy tắc 005)

Every document shall contain its current Revision.

(Mọi tài liệu phải ghi rõ Revision hiện tại.)

---

# Rule 006 (Quy tắc 006)

Every revision shall be recorded in Revision History.

(Mọi lần sửa đổi phải được ghi trong Lịch sử phiên bản.)

---

# Rule 007 (Quy tắc 007)

Previous revisions shall not be deleted without documented justification.

(Không được xóa lịch sử phiên bản nếu không có lý do được ghi nhận.)

---

# Rule 008 (Quy tắc 008)

Breaking changes shall increase the Major version.

(Thay đổi không tương thích phải tăng Major.)

---

# Rule 009 (Quy tắc 009)

New features shall increase the Minor version.

(Tính năng mới tăng Minor.)

Bug fixes shall increase the Patch version.

(Sửa lỗi tăng Patch.)

---

# Rule 010 (Quy tắc 010)

Versioning shall support long-term evolutionary development.

(Hệ thống phiên bản phải hỗ trợ quá trình phát triển và tiến hóa lâu dài.)

---

# Revision History (Lịch sử phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
