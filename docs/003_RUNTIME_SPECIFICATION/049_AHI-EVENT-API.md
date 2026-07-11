# AHI Event API
(**Đặc tả API Sự kiện AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-EVENT-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for event management within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn cho việc quản lý Sự kiện trong AHI Workspace.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng), Workflow (Quy trình) and Application (Ứng dụng) shall communicate through the Event API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng, Quy trình và Ứng dụng đều giao tiếp thông qua API Sự kiện.)

---

# Vision (Tầm nhìn)

Everything is an event.

(Mọi thứ đều là sự kiện.)

Every event is observable.

(Mọi sự kiện đều có thể quan sát.)

Every event contributes knowledge.

(Mọi sự kiện đều đóng góp tri thức.)

---

# Event Model (Mô hình Sự kiện)

Every event shall include:

(Mọi Sự kiện phải bao gồm:)

- Event ID (Mã Sự kiện)
- Event Type (Loại Sự kiện)
- Event Source (Nguồn Sự kiện)
- Event Timestamp (Thời gian Sự kiện)
- Producer (Bên phát)
- Consumer(s) (Bên nhận)
- Context ID (Mã Ngữ cảnh)
- Workflow ID (Mã Quy trình)
- Task ID (Mã Nhiệm vụ)
- Semantic Object References (Tham chiếu Đối tượng Ngữ nghĩa)
- Payload (Dữ liệu)
- Priority (Độ ưu tiên)
- Security Level (Mức An toàn)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- PublishEvent() (Phát Sự kiện)
- SubscribeEvent() (Đăng ký Sự kiện)
- UnsubscribeEvent() (Hủy Đăng ký)
- ReplayEvent() (Phát lại Sự kiện)
- AcknowledgeEvent() (Xác nhận Sự kiện)
- SearchEvent() (Tìm kiếm Sự kiện)
- ArchiveEvent() (Lưu trữ Sự kiện)
- MonitorEvent() (Giám sát Sự kiện)

---

# Event Lifecycle (Vòng đời Sự kiện)

```text
Create
    │
    ▼
Validate
    │
    ▼
Publish
    │
    ▼
Route
    │
    ▼
Consume
    │
    ▼
Acknowledge
    │
    ▼
Archive
```

---

# Event Delivery Modes (Các chế độ Phân phối)

The Event API shall support:

(API Sự kiện phải hỗ trợ:)

- Point-to-Point Delivery (Điểm tới Điểm)
- Publish/Subscribe (Xuất bản/Đăng ký)
- Broadcast (Phát quảng bá)
- Multicast (Phát đa hướng)
- Event Streaming (Luồng Sự kiện)
- Distributed Event Bus (Bus Sự kiện Phân tán)

---

# Reliability Requirements (Yêu cầu Độ tin cậy)

The Event API shall support:

(API Sự kiện phải hỗ trợ:)

- At-most-once Delivery (Giao tối đa một lần)
- At-least-once Delivery (Giao ít nhất một lần)
- Exactly-once Delivery (Giao chính xác một lần)
- Retry Policy (Chính sách Thử lại)
- Dead Letter Queue (Hàng đợi Thư lỗi)
- Event Ordering (Sắp xếp Thứ tự Sự kiện)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Everything communicates through events.

(Mọi thành phần giao tiếp thông qua sự kiện.)

---

## Principle 002

Every event is immutable.

(Mọi sự kiện là bất biến.)

---

## Principle 003

Events are traceable.

(Sự kiện luôn có thể truy vết.)

---

## Principle 004

Events enrich Hybrid Memory.

(Sự kiện làm giàu Bộ nhớ Lai.)

---

## Principle 005

Events enable distributed intelligence.

(Sự kiện tạo nền tảng cho trí tuệ phân tán.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Event Traits
- Rust Event Bus
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- Async Event Interfaces
- OpenAPI Specification
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-TASK-API
- AHI-WORKFLOW-API
- AHI-CONTEXT-API
- AHI-HYBRID-MEMORY-API
- AHI-EVENT-BUS
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
