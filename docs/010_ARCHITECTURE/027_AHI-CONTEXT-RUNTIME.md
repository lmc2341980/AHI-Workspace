# AHI Context Runtime
(**Môi trường Thực thi Ngữ cảnh AHI**)

---

## Document Information (Thông tin tài liệu)

| Item | Value |
|------|------|
| Document ID | AHI-CONTEXT-RUNTIME |
| Version | R001 |
| Status | Draft |
| Repository | AHI-Workspace |
| Author | Lê Minh Công (Thomas Le) & ChatGPT |
| Language | English / Tiếng Việt |

---

# Purpose (Mục đích)

This document defines the Context Runtime (Môi trường Thực thi Ngữ cảnh) of the Artificial Hybrid Intelligence Workspace (AHI-Workspace - Không gian làm việc Trí tuệ Nhân tạo Lai).

(Tài liệu này định nghĩa Môi trường Thực thi Ngữ cảnh của Không gian làm việc Trí tuệ Nhân tạo Lai.)

Unlike traditional Artificial Intelligence systems that rely on short conversation windows, the Context Runtime manages unlimited, persistent and evolving contexts across the entire lifetime of an Artificial Hybrid Intelligence Person (AHI-P - Cá nhân Trí tuệ Nhân tạo Lai).

(Khác với các hệ thống Trí tuệ Nhân tạo truyền thống chỉ dựa trên cửa sổ hội thoại ngắn, Môi trường Thực thi Ngữ cảnh quản lý các ngữ cảnh không giới hạn, tồn tại lâu dài và liên tục tiến hóa trong toàn bộ vòng đời của một Cá nhân Trí tuệ Nhân tạo Lai.)

---

# Vision (Tầm nhìn)

Context never disappears.

(Ngữ cảnh không bao giờ biến mất.)

Only its priority changes.

(Chỉ mức độ ưu tiên của nó thay đổi.)

Every experience contributes to future understanding.

(Mọi trải nghiệm đều đóng góp vào sự thấu hiểu trong tương lai.)

---

# Position inside AHI (Vị trí trong AHI)

```text
Human
      │
      ▼
Semantic Runtime
      │
      ▼
Context Runtime
      │
      ├── Context Manager
      ├── Context Cache
      ├── Context Index
      ├── Context Ranking
      ├── Context Linking
      ├── Context Snapshot
      ├── Context Recovery
      ├── Memory Connector
      └── Knowledge Graph Connector
      │
      ▼
Reasoning Engine
```

---

# Responsibilities (Trách nhiệm)

The Context Runtime shall:

(Môi trường Thực thi Ngữ cảnh phải:)

- Maintain unlimited contexts.

(Duy trì số lượng ngữ cảnh không giới hạn.)

- Automatically organize contexts.

(Tự động tổ chức các ngữ cảnh.)

- Link related contexts together.

(Liên kết các ngữ cảnh có liên quan.)

- Recover historical contexts when needed.

(Khôi phục các ngữ cảnh lịch sử khi cần.)

- Continuously evolve contextual understanding.

(Liên tục phát triển khả năng hiểu ngữ cảnh.)

---

# Context Lifecycle (Vòng đời Ngữ cảnh)

```text
Create Context
      │
      ▼
Collect Information
      │
      ▼
Semantic Linking
      │
      ▼
Context Ranking
      │
      ▼
Memory Classification
      │
      ▼
Reasoning
      │
      ▼
Evolution
      │
      ▼
Archive (Never Delete)
```

---

# Context Layers (Các Tầng Ngữ cảnh)

## Layer 001 — Active Context (Ngữ cảnh Hoạt động)

The context currently used by the user.

(Ngữ cảnh đang được người dùng sử dụng.)

---

## Layer 002 — Working Context (Ngữ cảnh Làm việc)

Recently used contexts with high relevance.

(Các ngữ cảnh vừa sử dụng và có mức liên quan cao.)

---

## Layer 003 — Long-Term Context (Ngữ cảnh Dài hạn)

Stable knowledge accumulated over time.

(Tri thức ổn định được tích lũy theo thời gian.)

---

## Layer 004 — Archived Context (Ngữ cảnh Lưu trữ)

Historical contexts retained permanently.

(Các ngữ cảnh lịch sử được lưu giữ vĩnh viễn.)

---

# Context Ranking (Xếp hạng Ngữ cảnh)

Context priority shall be dynamically calculated using:

(Mức ưu tiên ngữ cảnh được tính động dựa trên:)

- Usage Frequency (Tần suất Sử dụng)
- Recency (Độ Gần về Thời gian)
- Semantic Similarity (Độ Tương đồng Ngữ nghĩa)
- User Preference (Sở thích Người dùng)
- Task Importance (Mức Quan trọng của Nhiệm vụ)
- Evolution Score (Điểm Tiến hóa)

Higher ranked contexts remain readily available.

(Các ngữ cảnh có thứ hạng cao luôn sẵn sàng để sử dụng.)

---

# Context Recovery (Khôi phục Ngữ cảnh)

The Context Runtime shall reconstruct previous working states by combining:

(Môi trường Thực thi Ngữ cảnh phải tái tạo trạng thái làm việc trước đó bằng cách kết hợp:)

- Conversation History (Lịch sử Hội thoại)
- Semantic Objects (Đối tượng Ngữ nghĩa)
- Knowledge Graph (Đồ thị Tri thức)
- Hybrid Memory (Bộ nhớ Lai)
- Related Documents (Tài liệu Liên quan)
- Device Data (Dữ liệu Thiết bị)

---

# Design Principles (Nguyên tắc Thiết kế)

## Principle 001 (Nguyên tắc 001)

Contexts are never deleted.

(Ngữ cảnh không bao giờ bị xóa.)

---

## Principle 002 (Nguyên tắc 002)

Only relevance changes.

(Chỉ mức độ liên quan thay đổi.)

---

## Principle 003 (Nguyên tắc 003)

Every context has semantic meaning.

(Mọi ngữ cảnh đều mang ngữ nghĩa.)

---

## Principle 004 (Nguyên tắc 004)

Contexts continuously enrich Hybrid Memory (Bộ nhớ Lai).

(Các ngữ cảnh liên tục làm giàu Bộ nhớ Lai.)

---

## Principle 005 (Nguyên tắc 005)

The Context Runtime continuously evolves through experience.

(Môi trường Thực thi Ngữ cảnh liên tục tiến hóa thông qua trải nghiệm.)

---

# Related Documents (Tài liệu liên quan)

- AHI-SEMANTIC-RUNTIME
- AHI-CONTEXT-ENGINE
- AHI-HYBRID-MEMORY-ARCHITECTURE
- AHI-KNOWLEDGE-GRAPH
- AHI-REASONING-ENGINE
- AHI-EVOLUTIONARY-WORKSPACE

---

# Revision History (Lịch sử Phiên bản)

| Version | Date | Description |
|---------|------|-------------|
| R001 | 2026-07-10 | Initial version. |
