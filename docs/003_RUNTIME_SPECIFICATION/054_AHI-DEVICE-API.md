# AHI Device API
(**Đặc tả API Thiết bị AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-DEVICE-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Devices (Thiết bị) connected to the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn để kết nối, quản lý và điều khiển mọi Thiết bị trong hệ sinh thái AHI.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Service (Dịch vụ) shall communicate with physical devices through this API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Dịch vụ đều giao tiếp với Thiết bị thông qua API này.)

---

# Vision (Tầm nhìn)

One Device API.

(Một API Thiết bị.)

Every physical device becomes a semantic object.

(Mọi thiết bị vật lý đều trở thành một Đối tượng Ngữ nghĩa.)

Unified communication across all hardware.

(Giao tiếp thống nhất trên mọi phần cứng.)

---

# Device Model (Mô hình Thiết bị)

Every Device shall include:

(Mọi Thiết bị phải bao gồm:)

- Device ID (Mã Thiết bị)
- Device Name (Tên Thiết bị)
- Device Type (Loại Thiết bị)
- Manufacturer (Nhà sản xuất)
- Model (Mẫu)
- Firmware Version (Phiên bản Firmware)
- Runtime Compatibility (Khả năng tương thích Runtime)
- Supported Capabilities (Khả năng hỗ trợ)
- Connection Status (Trạng thái Kết nối)
- Security Profile (Hồ sơ Bảo mật)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- RegisterDevice() (Đăng ký Thiết bị)
- DiscoverDevice() (Khám phá Thiết bị)
- ConnectDevice() (Kết nối Thiết bị)
- DisconnectDevice() (Ngắt kết nối)
- ReadDeviceState() (Đọc Trạng thái)
- WriteDeviceState() (Ghi Trạng thái)
- MonitorDevice() (Giám sát Thiết bị)
- UpdateFirmware() (Cập nhật Firmware)

---

# Device Lifecycle (Vòng đời Thiết bị)

```text
Discover
    │
    ▼
Register
    │
    ▼
Authenticate
    │
    ▼
Connect
    │
    ▼
Operate
    │
    ▼
Monitor
    │
    ▼
Update
    │
    ▼
Disconnect
    │
    ▼
Retire
```

---

# Supported Device Categories (Các loại Thiết bị)

The Device API shall support:

(API Thiết bị phải hỗ trợ:)

- Sensors (Cảm biến)
- Cameras (Camera)
- Microphones (Micro)
- Displays (Màn hình)
- Robots (Robot)
- Wearables (Thiết bị đeo)
- Industrial Controllers (Bộ điều khiển Công nghiệp)
- IoT Devices (Thiết bị IoT)
- Mobile Devices (Thiết bị Di động)
- Embedded Systems (Hệ thống Nhúng)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Device API shall support:

(API Thiết bị phải hỗ trợ:)

- Real-time Communication (Giao tiếp Thời gian thực)
- Secure Communication (Giao tiếp An toàn)
- Device Discovery (Khám phá Thiết bị)
- Hot Plug Support (Kết nối Nóng)
- Remote Management (Quản lý Từ xa)
- Device Health Monitoring (Giám sát Sức khỏe Thiết bị)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Every device is uniquely identifiable.

(Mọi Thiết bị đều có định danh duy nhất.)

---

## Principle 002

Hardware differences are abstracted.

(Khác biệt phần cứng được trừu tượng hóa.)

---

## Principle 003

Every interaction is event-driven.

(Mọi tương tác đều dựa trên sự kiện.)

---

## Principle 004

Devices operate within contextual awareness.

(Thiết bị hoạt động dựa trên ngữ cảnh.)

---

## Principle 005

Security is mandatory for every connection.

(Bảo mật là bắt buộc đối với mọi kết nối.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

- Rust Device Traits
- Rust Device Manager
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Device Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-SERVICE-API
- AHI-RESOURCE-API
- AHI-PHYSICAL-WORLD-INTERFACE
- AHI-WEARABLE-INTERFACE
- AHI-DEVICE-RUNTIME
- AHI-RUNTIME-SPECIFICATION

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-11 | Initial version. |
