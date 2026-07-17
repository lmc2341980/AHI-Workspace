# 010. AHI Protocol Architecture

| Item | Value |
|------|-------|
| Document ID | AHI-PS-010 |
| Parent | 002_AHI_PROTOCOL_SPECIFICATION.md |
| Related | 006_AHI_LANG_SPECIFICATION.md |
| Related | 007_AHI_SERVICE_PROTOCOL_SPECIFICATION.md |
| Version | 2.0.0 |
| Status | Artifact |


# 1. Purpose

Đặc tả kiến trúc tổng thể của AHI Protocol (AHI-PS).

Tài liệu này mô tả các thành phần chính, trách nhiệm và quan hệ giữa các lớp trong hệ sinh thái AHI.

AHI Protocol Architecture không mô tả implementation cụ thể.

Kiến trúc này định nghĩa nguyên tắc để các thành phần AHI có thể:

- kế thừa;
- giao tiếp;
- phối hợp;
- kiểm tra;
- tiến hóa.


# 2. Inheritance

Kế thừa từ:

- Hiến pháp AHI.
- 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md.
- 002_AHI_PROTOCOL_SPECIFICATION.md.


# 3. Design Principles

Kiến trúc AHI được xây dựng theo các nguyên tắc:

- Human-Centered Hybrid Intelligence.
- Constitution First.
- Inheritance First.
- One Meaning, Many Representations.
- Tiến hóa liên tục.
- Không sử dụng mô hình Client–Server truyền thống làm kiến trúc nền.
- Quyết định cuối cùng thuộc về Con người.
- Mọi thành phần phải tuân thủ Hiến pháp AHI.


# 4. Core Components

Các thành phần chính:

- Human
- Environment
- AHI-P
- AHI-S
- AHI-Or
- AHI-V
- AHI-Factory
- AHI-SuBiet
- AHI-Old
- AHI-Lang
- AHI-SP
- AHI-Om
- AHI-Successor

Chi tiết của từng thành phần được đặc tả trong các tài liệu chuyên biệt.


# 5. Architecture Responsibilities


## Human

- Chủ thể quyết định cuối cùng.
- Chủ sở hữu AHI-P.
- Phê duyệt tri thức.
- Kiểm soát quyền sử dụng AHI.


---

## AHI-P

- Đại diện Hybrid Intelligence cá nhân của một con người.
- Quản lý Identity.
- Quản lý Personal Memory.
- Quản lý Personal Knowledge.
- Quản lý Personal Skills.

Nguyên tắc:
