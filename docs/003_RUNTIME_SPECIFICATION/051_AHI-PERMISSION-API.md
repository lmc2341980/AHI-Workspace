# AHI Permission API
(**Đặc tả API Phân quyền AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-PERMISSION-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for authorization and permission management within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn để quản lý phân quyền và ủy quyền trong AHI Workspace.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng), Service (Dịch vụ) and Application (Ứng dụng) shall perform authorization through this API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng, Dịch vụ và Ứng dụng đều phải thực hiện phân quyền thông qua API này.)

---

# Vision (Tầm nhìn)

One Permission API.

(Một API Phân quyền.)

Centralized governance.

(Quản trị tập trung.)

Distributed enforcement.

(Thực thi phân tán.)

Human authority always prevails.

(Con người luôn có quyền quyết định cuối cùng.)

---

# Permission Model (Mô hình Phân quyền)

Every permission shall include:

(Mọi quyền phải bao gồm:)

- Permission ID (Mã Quyền)
- Permission Name (Tên Quyền)
- Resource ID (Mã Tài nguyên)
- Subject ID (Mã Chủ thể)
- Action (Hành động)
- Scope (Phạm vi)
- Conditions (Điều kiện)
- Grant Type (Loại Cấp quyền)
- Expiration (Thời hạn)
- Audit Metadata (Siêu dữ liệu Kiểm toán)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- GrantPermission() (Cấp quyền)
- RevokePermission() (Thu hồi quyền)
- CheckPermission() (Kiểm tra quyền)
- ListPermissions() (Liệt kê quyền)
- UpdatePermission() (Cập nhật quyền)
- DelegatePermission() (Ủy quyền)
- ValidatePermission() (Xác thực quyền)
- AuditPermission() (Kiểm toán quyền)

---

# Authorization Flow (Luồng Phân quyền)

```text
Request
    │
    ▼
Authenticate
    │
    ▼
Identify Subject
    │
    ▼
Load Context
    │
    ▼
Evaluate Policy
    │
    ▼
Check Permission
    │
    ▼
Authorize / Deny
    │
    ▼
Audit
```

---

# Supported Authorization Models (Các mô hình Phân quyền)

The Permission API shall support:

(API Phân quyền phải hỗ trợ:)

- Role-Based Access Control (RBAC - Kiểm soát Truy cập theo Vai trò)
- Attribute-Based Access Control (ABAC - Kiểm soát Truy cập theo Thuộc tính)
- Policy-Based Access Control (PBAC - Kiểm soát Truy cập theo Chính sách)
- Context-Based Access Control (CBAC - Kiểm soát Truy cập theo Ngữ cảnh)
- Hybrid Authorization (Phân quyền Lai)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Permission API shall support:

(API Phân quyền phải hỗ trợ:)

- Distributed Authorization (Phân quyền Phân tán)
- High Availability (Sẵn sàng Cao)
- Audit Logging (Nhật ký Kiểm toán)
- Versioned Policies (Phiên bản Chính sách)
- Fine-grained Authorization (Phân quyền Chi tiết)
- Real-time Policy Evaluation (Đánh giá Chính sách Thời gian thực)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Security by default.

(An toàn theo mặc định.)

---

## Principle 002

Least privilege.

(Đặc quyền tối thiểu.)

---

## Principle 003

Every decision is auditable.

(Mọi quyết định đều có thể kiểm toán.)

---

## Principle 004

Permissions follow governance.

(Phân quyền tuân theo quản trị.)

---

## Principle 005

Authorization is semantic and context-aware.

(Phân quyền mang ngữ nghĩa và nhận biết ngữ cảnh.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Authorization Traits
- Rust Permission Service
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Policy Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-PLUGIN-API
- AHI-CORE-KERNEL
- AHI-CONTEXT-API
- AHI-EVENT-API
- AHI-PERMISSION-ENGINE
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-11 | Initial version. |
