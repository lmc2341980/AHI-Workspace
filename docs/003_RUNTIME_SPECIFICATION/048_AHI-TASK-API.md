# AHI Task API
(**Đặc tả API Nhiệm vụ AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-TASK-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Task (Nhiệm vụ) management in the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn để quản lý Nhiệm vụ trong AHI Workspace.)

Every Workflow (Quy trình), Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Application (Ứng dụng) shall create and execute tasks through this API.

(Mọi Quy trình, Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Ứng dụng đều phải tạo và thực thi Nhiệm vụ thông qua API này.)

---

# Vision (Tầm nhìn)

One Task API.

(Một API Nhiệm vụ.)

Every executable action is a task.

(Mọi hành động có thể thực thi đều là một Nhiệm vụ.)

Tasks are semantic, observable and evolvable.

(Nhiệm vụ mang ngữ nghĩa, có thể quan sát và có thể tiến hóa.)

---

# Task Model (Mô hình Nhiệm vụ)

Every task shall include:

(Mọi Nhiệm vụ phải bao gồm:)

- Task ID (Mã Nhiệm vụ)
- Task Name (Tên Nhiệm vụ)
- Task Type (Loại Nhiệm vụ)
- Owner (Chủ sở hữu)
- Assignee (Đối tượng Thực hiện)
- Workflow ID (Mã Quy trình)
- Parent Task (Nhiệm vụ Cha)
- Priority (Độ ưu tiên)
- Status (Trạng thái)
- Context Reference (Tham chiếu Ngữ cảnh)
- Semantic Objects (Đối tượng Ngữ nghĩa)
- Dependencies (Các Phụ thuộc)
- Deadline (Hạn hoàn thành)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- CreateTask() (Tạo Nhiệm vụ)
- GetTask() (Lấy Nhiệm vụ)
- UpdateTask() (Cập nhật Nhiệm vụ)
- AssignTask() (Giao Nhiệm vụ)
- ExecuteTask() (Thực thi Nhiệm vụ)
- PauseTask() (Tạm dừng Nhiệm vụ)
- ResumeTask() (Tiếp tục Nhiệm vụ)
- CancelTask() (Hủy Nhiệm vụ)
- CompleteTask() (Hoàn thành Nhiệm vụ)
- ArchiveTask() (Lưu trữ Nhiệm vụ)

---

# Task Lifecycle (Vòng đời Nhiệm vụ)

```text
Create
    │
    ▼
Validate
    │
    ▼
Assign
    │
    ▼
Schedule
    │
    ▼
Execute
    │
    ▼
Monitor
    │
    ▼
Complete
    │
    ▼
Archive
```

---

# Task Execution Modes (Các chế độ Thực thi)

The Task API shall support:

(API Nhiệm vụ phải hỗ trợ:)

- Human Execution (Con người thực hiện)
- AI Execution (AI thực hiện)
- Hybrid Execution (Con người và AI cùng thực hiện)
- Scheduled Execution (Thực thi theo lịch)
- Event-driven Execution (Thực thi theo sự kiện)
- Distributed Execution (Thực thi phân tán)
- Autonomous Execution (Thực thi tự động)

---

# Task State Model (Mô hình Trạng thái)

Possible states include:

(Bao gồm:)

- Created (Đã tạo)
- Ready (Sẵn sàng)
- Assigned (Đã giao)
- Running (Đang thực hiện)
- Waiting (Đang chờ)
- Blocked (Bị chặn)
- Completed (Hoàn thành)
- Failed (Thất bại)
- Cancelled (Đã hủy)
- Archived (Đã lưu trữ)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Task API shall support:

(API Nhiệm vụ phải hỗ trợ:)

- Distributed Scheduling (Lập lịch Phân tán)
- Retry Policy (Chính sách Thử lại)
- Timeout Control (Kiểm soát Hết thời gian)
- Audit Trail (Nhật ký Kiểm toán)
- Event Notifications (Thông báo Sự kiện)
- High Availability (Sẵn sàng Cao)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Every task has semantic meaning.

(Mọi Nhiệm vụ đều có ngữ nghĩa.)

---

## Principle 002

Every task belongs to a workflow.

(Mọi Nhiệm vụ thuộc một Quy trình.)

---

## Principle 003

Every task is traceable.

(Mọi Nhiệm vụ đều có thể truy vết.)

---

## Principle 004

Every task contributes knowledge.

(Mọi Nhiệm vụ đều đóng góp tri thức.)

---

## Principle 005

Task execution always respects governance and permissions.

(Việc thực thi Nhiệm vụ luôn tuân thủ quản trị và phân quyền.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Traits
- Rust Task Service
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Task Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-WORKFLOW-API
- AHI-TASK-SCHEDULER
- AHI-REASONING-API
- AHI-CONTEXT-API
- AHI-HYBRID-MEMORY-API
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
