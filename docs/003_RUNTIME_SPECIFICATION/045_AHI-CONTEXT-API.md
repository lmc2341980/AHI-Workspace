# AHI Context API
(**Đặc tả API Ngữ cảnh AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-CONTEXT-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Context (Ngữ cảnh) management within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn cho việc quản lý Ngữ cảnh trong AHI Workspace.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Application (Ứng dụng) shall access contextual information only through this API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Ứng dụng chỉ được truy cập thông tin Ngữ cảnh thông qua API này.)

---

# Vision (Tầm nhìn)

One Context API.

(Một API Ngữ cảnh.)

One shared understanding.

(Một sự hiểu biết chung.)

Context follows every interaction.

(Ngữ cảnh đi theo mọi tương tác.)

---

# Context Model (Mô hình Ngữ cảnh)

Every Context shall contain:

(Mọi Ngữ cảnh phải bao gồm:)

- Context ID (Mã Ngữ cảnh)
- Context Type (Kiểu Ngữ cảnh)
- Parent Context (Ngữ cảnh Cha)
- Owner (Chủ sở hữu)
- Participants (Thành phần Tham gia)
- Current Goals (Mục tiêu Hiện tại)
- Semantic Objects (Đối tượng Ngữ nghĩa)
- Related Knowledge (Tri thức Liên quan)
- Hybrid Memory References (Tham chiếu Bộ nhớ Lai)
- Security Level (Mức An toàn)
- Lifecycle State (Trạng thái Vòng đời)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- CreateContext() (Tạo Ngữ cảnh)
- GetContext() (Lấy Ngữ cảnh)
- UpdateContext() (Cập nhật Ngữ cảnh)
- CloseContext() (Đóng Ngữ cảnh)
- SearchContext() (Tìm kiếm Ngữ cảnh)
- MergeContext() (Hợp nhất Ngữ cảnh)
- SplitContext() (Tách Ngữ cảnh)
- SynchronizeContext() (Đồng bộ Ngữ cảnh)

---

# Context Lifecycle (Vòng đời Ngữ cảnh)

```text
Create
    │
    ▼
Initialize
    │
    ▼
Activate
    │
    ▼
Expand
    │
    ▼
Synchronize
    │
    ▼
Share
    │
    ▼
Archive
```

---

# Context Synchronization (Đồng bộ Ngữ cảnh)

The Context API shall synchronize:

(API Ngữ cảnh phải đồng bộ:)

- Human Context (Ngữ cảnh Con người)
- AI Context (Ngữ cảnh AI)
- Workspace Context (Ngữ cảnh Không gian làm việc)
- Runtime Context (Ngữ cảnh Runtime)
- Device Context (Ngữ cảnh Thiết bị)
- Workflow Context (Ngữ cảnh Quy trình)
- Session Context (Ngữ cảnh Phiên làm việc)

Synchronization shall support:

(Đồng bộ phải hỗ trợ:)

- Local Runtime (Runtime Cục bộ)
- Distributed Runtime (Runtime Phân tán)
- Cloud Runtime (Runtime Đám mây)
- Edge Runtime (Runtime Biên)
- Offline Synchronization (Đồng bộ Ngoại tuyến)

---

# Context Resolution Rules (Quy tắc Phân giải Ngữ cảnh)

When multiple contexts are available, the Runtime shall prioritize:

(Khi tồn tại nhiều Ngữ cảnh, Runtime phải ưu tiên:)

1. Active Context (Ngữ cảnh Đang hoạt động)
2. User Intent (Ý định Người dùng)
3. Session Context (Ngữ cảnh Phiên làm việc)
4. Workspace Context (Ngữ cảnh Không gian làm việc)
5. Organizational Context (Ngữ cảnh Tổ chức)
6. Historical Context (Ngữ cảnh Lịch sử)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Context API shall support:

(API Ngữ cảnh phải hỗ trợ:)

- Real-time Updates (Cập nhật Thời gian thực)
- Distributed Synchronization (Đồng bộ Phân tán)
- High Availability (Sẵn sàng Cao)
- Version History (Lịch sử Phiên bản)
- Conflict Resolution (Giải quyết Xung đột)
- Secure Context Isolation (Cô lập Ngữ cảnh An toàn)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Context is dynamic.

(Ngữ cảnh luôn động.)

---

## Principle 002

Context is semantic.

(Ngữ cảnh mang ngữ nghĩa.)

---

## Principle 003

Context is shared when permitted.

(Ngữ cảnh được chia sẻ khi được phép.)

---

## Principle 004

Context drives reasoning.

(Ngữ cảnh dẫn dắt suy luận.)

---

## Principle 005

Context remains synchronized across the entire AHI ecosystem.

(Ngữ cảnh luôn được đồng bộ trên toàn bộ hệ sinh thái AHI.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Traits
- Rust Services
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- JSON Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-SEMANTIC-OBJECT-SPECIFICATION
- AHI-HYBRID-MEMORY-API
- AHI-CONTEXT-RUNTIME
- AHI-RUNTIME-SPECIFICATION
- AHI-CORE-KERNEL
- AHI-REASONING-ENGINE

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
