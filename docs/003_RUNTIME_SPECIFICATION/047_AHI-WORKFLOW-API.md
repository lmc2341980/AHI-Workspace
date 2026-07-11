# AHI Workflow API
(**Đặc tả API Quy trình AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-WORKFLOW-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for the Workflow Engine (Bộ máy Quy trình) of the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn cho Bộ máy Quy trình của AHI Workspace.)

The Workflow API enables every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Application (Ứng dụng) to create, execute, monitor and evolve workflows using a unified semantic interface.

(API Quy trình cho phép mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Ứng dụng tạo, thực thi, giám sát và tiến hóa quy trình thông qua một giao diện ngữ nghĩa thống nhất.)

---

# Vision (Tầm nhìn)

One Workflow API.

(Một API Quy trình.)

Unlimited workflow implementations.

(Vô số cách hiện thực quy trình.)

Every workflow follows semantic execution.

(Mọi quy trình đều thực thi theo ngữ nghĩa.)

---

# Workflow Model (Mô hình Quy trình)

Every workflow shall include:

(Mọi quy trình phải bao gồm:)

- Workflow ID (Mã Quy trình)
- Workflow Name (Tên Quy trình)
- Workflow Version (Phiên bản Quy trình)
- Owner (Chủ sở hữu)
- Semantic Goal (Mục tiêu Ngữ nghĩa)
- Input Parameters (Tham số Đầu vào)
- Output Parameters (Tham số Đầu ra)
- Tasks (Các Nhiệm vụ)
- Dependencies (Các Phụ thuộc)
- Participants (Các Thành phần Tham gia)
- Context Reference (Tham chiếu Ngữ cảnh)
- Status (Trạng thái)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- CreateWorkflow() (Tạo Quy trình)
- GetWorkflow() (Lấy Quy trình)
- UpdateWorkflow() (Cập nhật Quy trình)
- ExecuteWorkflow() (Thực thi Quy trình)
- PauseWorkflow() (Tạm dừng Quy trình)
- ResumeWorkflow() (Tiếp tục Quy trình)
- CancelWorkflow() (Hủy Quy trình)
- MonitorWorkflow() (Giám sát Quy trình)
- OptimizeWorkflow() (Tối ưu Quy trình)
- ArchiveWorkflow() (Lưu trữ Quy trình)

---

# Workflow Lifecycle (Vòng đời Quy trình)

```text
Create
    │
    ▼
Validate
    │
    ▼
Plan
    │
    ▼
Execute
    │
    ▼
Monitor
    │
    ▼
Optimize
    │
    ▼
Version
    │
    ▼
Archive
```

---

# Workflow Execution Modes (Các chế độ Thực thi)

The Workflow API shall support:

(API Quy trình phải hỗ trợ:)

- Sequential Execution (Thực thi Tuần tự)
- Parallel Execution (Thực thi Song song)
- Distributed Execution (Thực thi Phân tán)
- Event-Driven Execution (Thực thi theo Sự kiện)
- Scheduled Execution (Thực thi theo Lịch)
- Human-in-the-Loop Execution (Thực thi có Con người tham gia)
- AI Autonomous Execution (Thực thi Tự động bởi AI)
- Hybrid Execution (Thực thi Lai)

---

# Workflow State Model (Mô hình Trạng thái Quy trình)

Possible states include:

(Bao gồm:)

- Created (Đã tạo)
- Validated (Đã kiểm tra)
- Ready (Sẵn sàng)
- Running (Đang chạy)
- Waiting (Đang chờ)
- Suspended (Tạm dừng)
- Completed (Hoàn thành)
- Failed (Thất bại)
- Cancelled (Đã hủy)
- Archived (Đã lưu trữ)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Workflow API shall support:

(API Quy trình phải hỗ trợ:)

- High Availability (Sẵn sàng Cao)
- Horizontal Scaling (Mở rộng Ngang)
- Fault Recovery (Khôi phục Lỗi)
- Workflow Versioning (Quản lý Phiên bản Quy trình)
- Semantic Validation (Kiểm tra Ngữ nghĩa)
- Runtime Monitoring (Giám sát Runtime)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Every workflow begins with semantic intent.

(Mọi quy trình bắt đầu từ ý định ngữ nghĩa.)

---

## Principle 002

Every execution is observable.

(Mọi quá trình thực thi đều có thể quan sát.)

---

## Principle 003

Every workflow is evolvable.

(Mọi quy trình đều có thể tiến hóa.)

---

## Principle 004

Every workflow contributes knowledge.

(Mọi quy trình đều đóng góp tri thức.)

---

## Principle 005

Human governance remains authoritative.

(Quản trị của con người luôn là thẩm quyền cao nhất.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Traits
- Rust Workflow Engine
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Workflow Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-REASONING-API
- AHI-CONTEXT-API
- AHI-HYBRID-MEMORY-API
- AHI-WORKFLOW-ENGINE
- AHI-TASK-SCHEDULER
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
