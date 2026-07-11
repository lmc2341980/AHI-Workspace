# AHI Service API
(**Đặc tả API Dịch vụ AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-SERVICE-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Services (Dịch vụ) within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn để mọi Dịch vụ trong AHI Workspace có thể đăng ký, khám phá, gọi, giám sát và tiến hóa theo cùng một chuẩn.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Application (Ứng dụng) shall expose capabilities as standardized Services.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Ứng dụng đều công bố khả năng của mình dưới dạng Dịch vụ chuẩn.)

---

# Vision (Tầm nhìn)

Everything is a Service.

(Mọi thành phần đều là Dịch vụ.)

Every Service is discoverable.

(Mọi Dịch vụ đều có thể được khám phá.)

Every Service is replaceable.

(Mọi Dịch vụ đều có thể thay thế.)

---

# Service Model (Mô hình Dịch vụ)

Every Service shall include:

(Mọi Dịch vụ phải bao gồm:)

- Service ID (Mã Dịch vụ)
- Service Name (Tên Dịch vụ)
- Service Version (Phiên bản Dịch vụ)
- Service Type (Loại Dịch vụ)
- Provider (Nhà cung cấp)
- Endpoint (Điểm truy cập)
- Supported Operations (Các thao tác hỗ trợ)
- Input Schema (Lược đồ Đầu vào)
- Output Schema (Lược đồ Đầu ra)
- Security Policy (Chính sách Bảo mật)
- Context Requirements (Yêu cầu Ngữ cảnh)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- RegisterService() (Đăng ký Dịch vụ)
- DiscoverService() (Khám phá Dịch vụ)
- GetService() (Lấy thông tin Dịch vụ)
- InvokeService() (Gọi Dịch vụ)
- UpdateService() (Cập nhật Dịch vụ)
- DisableService() (Vô hiệu hóa Dịch vụ)
- RemoveService() (Gỡ Dịch vụ)
- MonitorService() (Giám sát Dịch vụ)

---

# Service Lifecycle (Vòng đời Dịch vụ)

```text
Develop
    │
    ▼
Register
    │
    ▼
Validate
    │
    ▼
Publish
    │
    ▼
Discover
    │
    ▼
Invoke
    │
    ▼
Monitor
    │
    ▼
Upgrade
    │
    ▼
Retire
```

---

# Service Types (Các loại Dịch vụ)

The Service API shall support:

(API Dịch vụ phải hỗ trợ:)

- Runtime Service (Dịch vụ Runtime)
- AI Service (Dịch vụ AI)
- Memory Service (Dịch vụ Bộ nhớ)
- Context Service (Dịch vụ Ngữ cảnh)
- Workflow Service (Dịch vụ Quy trình)
- Task Service (Dịch vụ Nhiệm vụ)
- Device Service (Dịch vụ Thiết bị)
- Integration Service (Dịch vụ Tích hợp)
- External Service (Dịch vụ Bên ngoài)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Service API shall support:

(API Dịch vụ phải hỗ trợ:)

- Service Discovery (Khám phá Dịch vụ)
- Load Balancing (Cân bằng Tải)
- Service Versioning (Quản lý Phiên bản)
- High Availability (Sẵn sàng Cao)
- Distributed Invocation (Gọi Dịch vụ Phân tán)
- Health Monitoring (Giám sát Sức khỏe)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Everything is exposed as a Service.

(Mọi khả năng đều được công bố dưới dạng Dịch vụ.)

---

## Principle 002

Services are loosely coupled.

(Các Dịch vụ được liên kết lỏng.)

---

## Principle 003

Services communicate semantically.

(Các Dịch vụ giao tiếp bằng ngữ nghĩa.)

---

## Principle 004

Services evolve independently.

(Các Dịch vụ tiến hóa độc lập.)

---

## Principle 005

Every Service is governed by security and policy.

(Mọi Dịch vụ đều chịu sự quản trị của chính sách và bảo mật.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Service Traits
- Rust Service Registry
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Service Manifest Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-RESOURCE-API
- AHI-PLUGIN-API
- AHI-EVENT-API
- AHI-SERVICE-MESH
- AHI-CORE-KERNEL
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-11 | Initial version. |
