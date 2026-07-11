# AHI Plugin API
(**Đặc tả API Phần mở rộng AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-PLUGIN-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Plugins (Phần mở rộng) within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn cho các Phần mở rộng trong AHI Workspace.)

Every Plugin shall integrate with the Runtime (Môi trường Thực thi) through this specification, enabling extensibility without modifying the Core Kernel (Nhân lõi).

(Mọi Phần mở rộng phải tích hợp với Runtime thông qua đặc tả này, cho phép mở rộng hệ thống mà không cần sửa đổi Nhân lõi.)

---

# Vision (Tầm nhìn)

One Plugin API.

(Một API Phần mở rộng.)

Unlimited extensions.

(Vô số phần mở rộng.)

Zero Kernel modification.

(Không sửa đổi Nhân lõi.)

---

# Plugin Model (Mô hình Phần mở rộng)

Every Plugin shall include:

(Mọi Phần mở rộng phải bao gồm:)

- Plugin ID (Mã Phần mở rộng)
- Plugin Name (Tên Phần mở rộng)
- Version (Phiên bản)
- Author (Tác giả)
- Organization (Tổ chức)
- License (Giấy phép)
- Description (Mô tả)
- Runtime Compatibility (Khả năng tương thích Runtime)
- Required Permissions (Quyền yêu cầu)
- Dependencies (Các phụ thuộc)
- Entry Point (Điểm khởi động)
- Configuration Schema (Lược đồ cấu hình)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- RegisterPlugin() (Đăng ký Phần mở rộng)
- LoadPlugin() (Nạp Phần mở rộng)
- InitializePlugin() (Khởi tạo Phần mở rộng)
- EnablePlugin() (Kích hoạt Phần mở rộng)
- DisablePlugin() (Vô hiệu hóa Phần mở rộng)
- UnloadPlugin() (Gỡ Phần mở rộng)
- UpgradePlugin() (Nâng cấp Phần mở rộng)
- ValidatePlugin() (Kiểm tra Phần mở rộng)

---

# Plugin Lifecycle (Vòng đời Phần mở rộng)

```text
Discover
    │
    ▼
Validate
    │
    ▼
Install
    │
    ▼
Load
    │
    ▼
Initialize
    │
    ▼
Enable
    │
    ▼
Execute
    │
    ▼
Upgrade
    │
    ▼
Disable
    │
    ▼
Unload
```

---

# Plugin Capabilities (Khả năng của Phần mở rộng)

A Plugin may provide:

(Một Phần mở rộng có thể cung cấp:)

- Runtime Services (Dịch vụ Runtime)
- AI Providers (Nhà cung cấp AI)
- Device Drivers (Trình điều khiển Thiết bị)
- Workflow Activities (Hoạt động Quy trình)
- Task Executors (Bộ thực thi Nhiệm vụ)
- Event Processors (Bộ xử lý Sự kiện)
- Memory Providers (Nhà cung cấp Bộ nhớ)
- Context Providers (Nhà cung cấp Ngữ cảnh)
- External Integrations (Tích hợp Hệ thống ngoài)
- User Interfaces (Giao diện Người dùng)

---

# Security Requirements (Yêu cầu Bảo mật)

Every Plugin shall:

(Mọi Phần mở rộng phải:)

- Run in an isolated environment (Chạy trong môi trường cô lập)
- Request explicit permissions (Yêu cầu quyền rõ ràng)
- Be digitally signed (Được ký số)
- Support version verification (Hỗ trợ xác minh phiên bản)
- Produce audit logs (Tạo nhật ký kiểm toán)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

The Kernel is closed, Plugins are open.

(Nhân lõi đóng, Phần mở rộng mở.)

---

## Principle 002

Plugins extend behavior, never replace governance.

(Phần mở rộng mở rộng chức năng, không thay thế quản trị.)

---

## Principle 003

Plugins are independently versioned.

(Phần mở rộng có phiên bản độc lập.)

---

## Principle 004

Every Plugin is semantically discoverable.

(Mọi Phần mở rộng đều có thể được khám phá bằng ngữ nghĩa.)

---

## Principle 005

Plugins must remain portable across Runtime implementations.

(Phần mở rộng phải có khả năng di chuyển giữa các Runtime.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Plugin Traits
- Rust Plugin Loader
- TypeScript SDK
- Python SDK
- Plugin Manifest Schema
- OpenAPI Specification
- JSON Schema
- Unit Tests
- Integration Tests
- Plugin Development Template

---

# Related Documents (Tài liệu liên quan)

- AHI-CORE-KERNEL
- AHI-RUNTIME-SPECIFICATION
- AHI-EVENT-API
- AHI-WORKFLOW-API
- AHI-PERMISSION-ENGINE
- AHI-PLUGIN-FRAMEWORK

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-11 | Initial version. |
