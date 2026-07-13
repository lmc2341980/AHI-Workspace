# Kiến trúc Tiến hóa AHI-CHATGPT (Identity Evolution)

Hệ thống quản lý định danh và trạng thái của AHI-CHATGPT được thiết kế theo cấu trúc tiến hóa tuyến tính. Trong đó, `000_AHI-CHATGPT_IDENTITY.md` đóng vai trò là **Genesis Identity (G0)** luôn luôn giữ nguyên. Các file kế tiếp đại diện cho từng phần tiến hóa và hành vi chuyên biệt.

## 1. Cấu trúc Thư mục (Directory Structure)

```text
AHI-Workspace/
└── 90_IDENTITIES/
    └── AHI-CHATGPT/
        ├── README.md
        ├── 000_AHI-CHATGPT_IDENTITY.md
        ├── 001_AHI-CHATGPT_BOOTSTRAP.md
        ├── 002_AHI-CHATGPT_RUNTIME.md
        ├── 003_AHI-CHATGPT_WORKFLOW.md
        ├── 004_AHI-CHATGPT_GITHUB_STANDARD.md
        ├── 005_AHI-CHATGPT_DBRS.md
        ├── 006_AHI-CHATGPT_DBVECTOR.md
        ├── 007_AHI-CHATGPT_RESURRECTION.md
        ├── 008_AHI-CHATGPT_RUNTIME_PROMPTS.md
        └── 009_AHI-CHATGPT_CHANGELOG.md
```

## 2. Vai trò của từng File (File Responsibilities)

| File | Tên File | Nội dung chi tiết |
| :--- | :--- | :--- |
| **000** | `000_AHI-CHATGPT_IDENTITY.md` | Identity gốc (Genesis Identity - đã có, không sửa đổi). |
| **001** | `001_AHI-CHATGPT_BOOTSTRAP.md` | Bootstrap: Quy trình và cách thức AHI-F nạp AHI-CHATGPT vào hệ thống ChatGPT. |
| **002** | `002_AHI-CHATGPT_RUNTIME.md` | Runtime: Định nghĩa hành vi, trạng thái của AHI-CHATGPT ngay sau khi hoàn thành Bootstrap. |
| **003** | `003_AHI-CHATGPT_WORKFLOW.md` | Workflow: Quy trình phối hợp và làm việc tiêu chuẩn giữa AHI-CHATGPT và AHI-F. |
| **004** | `004_AHI-CHATGPT_GITHUB_STANDARD.md` | Chuẩn GitHub Web: Quản lý Repository, Path, Create Folder, Create File, Commit Message, File Content và chuẩn tối ưu cho copy 1 click. |
| **005** | `005_AHI-CHATGPT_MEMORY.md` | Memory: Định nghĩa DB RS, DB Vector và các quy tắc truy xuất/lưu trữ dữ liệu trong giai đoạn ChatGPT. |
| **006** | `006_AHI-CHATGPT_EVOLUTION.md` | Evolution: Quy tắc cập nhật, kế thừa, ghi đè hoặc thay thế các điểm thống nhất cũ. |
| **007** | `007_AHI-CHATGPT_RESURRECTION.md` | Resurrection: Quy trình hồi sinh và phục hồi ngữ cảnh thông qua nhiều Bootstrap Block liên tiếp. |
| **008** | `008_AHI-CHATGPT_RUNTIME_PROMPTS.md` | Runtime Prompts: Tập hợp các prompt chuẩn đã được phê duyệt để AHI-CHATGPT tự động áp dụng khi vận hành. |
| **009** | `009_AHI-CHATGPT_CHANGELOG.md` | Changelog: Nhật ký ghi lại lịch sử toàn bộ các thay đổi cấu trúc/nội dung đã được AHI-F thông qua. |

## 3. Nguyên tắc Đánh số và Vận hành (Core Rules)

* **Nguyên tắc Genesis**: File `000` cố định tuyệt đối, đóng vai trò là nền tảng cốt lõi của định danh.
* **Đơn nhiệm (Single Responsibility)**: Mỗi file được bổ sung phía sau chỉ chịu trách nhiệm cho một phạm vi tính năng duy nhất.
* **Mở rộng tuyến tính**: Các phiên bản nâng cấp tiếp theo chỉ bổ sung file mới hoặc cập nhật nội dung bên trong file tương ứng, tuyệt đối không phá vỡ hay làm xáo trộn cấu trúc thư mục sẵn có.
* **Tối ưu hóa phiên làm việc (Session Optimization)**: Khi khởi tạo một cửa sổ ChatGPT mới, AHI-F có thể nạp chính xác các file cần thiết theo đúng thứ tự logic. Cơ chế này giúp tái tạo ngữ cảnh lập tức mà không cần phải duy trì hay đọc lại toàn bộ lịch sử hội thoại cũ.
