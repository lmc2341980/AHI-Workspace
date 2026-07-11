# AHI Semantic Search API
(**Đặc tả API Tìm kiếm Ngữ nghĩa AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-SEMANTIC-SEARCH-API |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Email | ahiprojectteam@gmail.com |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This specification defines the standard Application Programming Interface (API - Giao diện Lập trình Ứng dụng) for Semantic Search (Tìm kiếm Ngữ nghĩa) within the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa API chuẩn để tìm kiếm theo ngữ nghĩa trên toàn bộ hệ sinh thái AHI.)

Every Runtime (Môi trường Thực thi), Artificial Intelligence Engine (Bộ máy Trí tuệ Nhân tạo), Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai), Plugin (Phần mở rộng), Service (Dịch vụ) and Application (Ứng dụng) shall discover information through this API.

(Mọi Runtime, Bộ máy Trí tuệ Nhân tạo, AHI-P, Phần mở rộng, Dịch vụ và Ứng dụng đều tìm kiếm thông tin thông qua API này.)

---

# Vision (Tầm nhìn)

One Semantic Search API.

(Một API Tìm kiếm Ngữ nghĩa.)

Everything is searchable.

(Mọi thứ đều có thể tìm kiếm.)

Meaning before keywords.

(Ngữ nghĩa quan trọng hơn từ khóa.)

---

# Search Model (Mô hình Tìm kiếm)

Every search request shall include:

(Mọi yêu cầu tìm kiếm phải bao gồm:)

- Query ID (Mã Truy vấn)
- Natural Language Query (Truy vấn Ngôn ngữ Tự nhiên)
- Semantic Intent (Ý định Ngữ nghĩa)
- Context Reference (Tham chiếu Ngữ cảnh)
- User Profile (Hồ sơ Người dùng)
- Search Scope (Phạm vi Tìm kiếm)
- Filters (Bộ lọc)
- Ranking Strategy (Chiến lược Xếp hạng)
- Metadata (Siêu dữ liệu)

---

# Core API Interfaces (Các Giao diện API Lõi)

Every implementation shall support:

(Mọi hiện thực phải hỗ trợ:)

- Search() (Tìm kiếm)
- SemanticSearch() (Tìm kiếm Ngữ nghĩa)
- KeywordSearch() (Tìm kiếm Từ khóa)
- HybridSearch() (Tìm kiếm Lai)
- SuggestQuery() (Gợi ý Truy vấn)
- AutoComplete() (Tự động Hoàn thành)
- ExplainResults() (Giải thích Kết quả)
- RankResults() (Xếp hạng Kết quả)

---

# Search Sources (Nguồn Tìm kiếm)

The API shall search across:

(API phải tìm kiếm trên:)

- Hybrid Memory (Bộ nhớ Lai)
- Knowledge Graph (Đồ thị Tri thức)
- Semantic Objects (Đối tượng Ngữ nghĩa)
- Documents (Tài liệu)
- Workflows (Quy trình)
- Tasks (Nhiệm vụ)
- Events (Sự kiện)
- Services (Dịch vụ)
- Plugins (Phần mở rộng)
- External Knowledge Sources (Nguồn Tri thức Bên ngoài)

---

# Search Lifecycle (Vòng đời Tìm kiếm)

```text
Receive Query
      │
      ▼
Understand Intent
      │
      ▼
Build Semantic Query
      │
      ▼
Search
      │
      ▼
Rank Results
      │
      ▼
Explain
      │
      ▼
Return
```

---

# Non-functional Requirements (Yêu cầu Phi chức năng)

The Semantic Search API shall support:

(API phải hỗ trợ:)

- Vector Search (Tìm kiếm Vector)
- Graph Search (Tìm kiếm Đồ thị)
- Hybrid Search (Tìm kiếm Lai)
- Distributed Search (Tìm kiếm Phân tán)
- Real-time Indexing (Lập chỉ mục Thời gian thực)
- Explainable Ranking (Xếp hạng Có thể Giải thích)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001

Search by meaning, not only keywords.

(Tìm kiếm theo ý nghĩa, không chỉ từ khóa.)

---

## Principle 002

Context improves relevance.

(Ngữ cảnh nâng cao độ liên quan.)

---

## Principle 003

Every result is explainable.

(Mọi kết quả đều có thể giải thích.)

---

## Principle 004

Search continuously learns.

(Tìm kiếm liên tục học hỏi.)

---

## Principle 005

Semantic Search is the primary discovery mechanism of AHI.

(Tìm kiếm Ngữ nghĩa là cơ chế khám phá chính của AHI.)

---

# Code Generation Targets (Đích Sinh mã nguồn)

This specification shall generate:

- Rust Search Traits
- Rust Search Engine
- TypeScript SDK
- Python SDK
- REST API
- GraphQL API
- OpenAPI Specification
- Search Schema
- Unit Tests
- Integration Tests

---

# Related Documents (Tài liệu liên quan)

- AHI-KNOWLEDGE-API
- AHI-MEMORY-API
- AHI-KNOWLEDGE-GRAPH
- AHI-SEMANTIC-OBJECT-SPECIFICATION
- AHI-REASONING-API
- AHI-CONTEXT-API

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-11 | Initial version. |
