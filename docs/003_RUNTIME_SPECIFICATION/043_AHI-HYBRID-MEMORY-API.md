# AHI Hybrid Memory API
(**Đặc tả API Bộ nhớ Lai AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-HYBRID-MEMORY-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for the Hybrid Memory (Bộ nhớ Lai) of Artificial Hybrid Intelligence (AHI - Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn cho Bộ nhớ Lai của AHI.)

Every Runtime, Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), AHI-P (Artificial Hybrid Intelligence Person - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng) and Application (Ứng dụng) shall access memory only through this API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng và Ứng dụng chỉ được truy cập bộ nhớ thông qua API này.)

---

# Vision (Tầm nhìn)

One Memory API.

(Một API Bộ nhớ.)

Unlimited storage implementations.

(Vô số cách hiện thực lưu trữ.)

Identical semantic behavior.

(Hành vi ngữ nghĩa thống nhất.)

---

# Memory Layers (Các tầng Bộ nhớ)

```text
Working Memory
        │
        ▼
Context Memory
        │
        ▼
Session Memory
        │
        ▼
Semantic Memory
        │
        ▼
Knowledge Graph
        │
        ▼
Long-Term Memory
        │
        ▼
Archive Memory
```

---

# Core Interfaces (Các giao diện lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- Create Memory Object (Tạo Đối tượng Bộ nhớ)
- Read Memory Object (Đọc Đối tượng Bộ nhớ)
- Update Memory Object (Cập nhật Đối tượng Bộ nhớ)
- Delete Memory Object (Xóa Đối tượng Bộ nhớ)
- Search Memory (Tìm kiếm Bộ nhớ)
- Semantic Search (Tìm kiếm Ngữ nghĩa)
- Context Search (Tìm kiếm theo Ngữ cảnh)
- Version History (Lịch sử Phiên bản)
- Synchronization (Đồng bộ)
- Backup & Recovery (Sao lưu & Phục hồi)

---

# Standard API

## Create

```text
CreateMemory()
```

Creates a new semantic memory object.

(Tạo một đối tượng bộ nhớ ngữ nghĩa mới.)

---

## Read

```text
GetMemory()
```

Returns one memory object.

(Trả về một đối tượng bộ nhớ.)

---

## Update

```text
UpdateMemory()
```

Updates semantic information.

(Cập nhật thông tin ngữ nghĩa.)

---

## Delete

```text
DeleteMemory()
```

Marks memory as retired without permanent removal.

(Đánh dấu bộ nhớ ngừng sử dụng mà không xóa vĩnh viễn.)

---

## Search

```text
SearchMemory()
```

Performs semantic retrieval.

(Thực hiện truy xuất ngữ nghĩa.)

---

## Synchronize

```text
SynchronizeMemory()
```

Synchronizes Hybrid Memory across all Runtime nodes.

(Đồng bộ Bộ nhớ Lai trên toàn bộ các Runtime.)

---

# Memory Object Schema (Lược đồ Đối tượng Bộ nhớ)

Every Memory Object shall include:

(Mọi Đối tượng Bộ nhớ phải bao gồm:)

- Memory ID (Mã Bộ nhớ)
- Semantic ID (Mã Ngữ nghĩa)
- Context ID (Mã Ngữ cảnh)
- Owner (Chủ sở hữu)
- Created Time (Thời gian tạo)
- Updated Time (Thời gian cập nhật)
- Version (Phiên bản)
- Trust Level (Mức Tin cậy)
- Source (Nguồn)
- Tags (Nhãn)
- Relationships (Quan hệ)

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The API shall support:

(API phải hỗ trợ:)

- High Availability (Sẵn sàng Cao)
- Distributed Storage (Lưu trữ Phân tán)
- Event Consistency (Nhất quán Sự kiện)
- Horizontal Scaling (Mở rộng Ngang)
- Encryption at Rest (Mã hóa khi Lưu trữ)
- Encryption in Transit (Mã hóa khi Truyền)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Memory is semantic.

(Bộ nhớ mang ngữ nghĩa.)

---

## Principle 002

Memory never truly disappears.

(Bộ nhớ không thực sự biến mất.)

---

## Principle 003

Memory is versioned.

(Bộ nhớ được quản lý phiên bản.)

---

## Principle 004

Memory follows context.

(Bộ nhớ đi theo ngữ cảnh.)

---

## Principle 005

Hybrid Memory is the single source of truth.

(Bộ nhớ Lai là nguồn dữ liệu chuẩn duy nhất.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

(Đặc tả này phải sinh:)

- Rust Traits
- Rust Storage Engine
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-CORE-KERNEL
- AHI-RUNTIME-SPECIFICATION
- AHI-HYBRID-MEMORY-MANAGER
- AHI-KNOWLEDGE-GRAPH
- AHI-CONTEXT-RUNTIME
- AHI-SEMANTIC-RUNTIME

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
