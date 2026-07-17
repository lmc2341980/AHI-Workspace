# AHI-WORKSPACE — TỔNG HỢP NỘI DUNG ĐÃ CUNG CẤP VÀ ĐÃ THỐNG NHẤT

**Version:** Proposal Consolidation V1
**Status:** Discussing → Approved (tùy từng mục)

---

# 1. TẦM NHÌN AHI

AHI (Artificial Hybrid Intelligence) là hệ thống Trí tuệ Nhân Lai, kết hợp giữa:

* Con người
* AI
* Tri thức
* Quy trình
* Dữ liệu
* Thiết bị
* Phần mềm
* Phần cứng

Mục tiêu cuối cùng:

* Tích lũy
* Kế thừa
* Tiến hóa

thay vì chỉ tạo ra câu trả lời tốt nhất tại thời điểm hiện tại.

---

# 2. TRIẾT LÝ

Đã thống nhất:

* Constitution First
* Inheritance First
* Artifact First
* Copy First
* Think Twice, Write Once
* Evolution First
* Human Ownership
* One Meaning, Many Representations
* Current Best Version

Nguyên tắc:

* Không bịa dữ liệu.
* Không suy diễn.
* Thiếu dữ liệu phải hỏi.
* Proposal không phải Fact.
* GitHub là Source of Truth.

---

# 3. KIẾN TRÚC TRI THỨC

Đã thống nhất:

Conversation

↓

Workflow

↓

Skill

↓

Specification

↓

Artifact

↓

GitHub

↓

Evolution

---

# 4. TRẠNG THÁI TRI THỨC

Proposal

↓

Discussing

↓

Approved

↓

Artifact

↓

Implemented

↓

Deprecated

---

# 5. AHI-WORKSPACE LÀ REPOSITORY TRUNG TÂM

Đã thống nhất:

AHI-Workspace là trung tâm điều phối toàn bộ hệ sinh thái AHI.

Vai trò:

* Constitution
* Specification
* Skill
* Runtime
* Prompt
* Memory
* AI Adapter
* Documentation
* Standards

---

# 6. GITHUB

Đã thống nhất:

GitHub là Source of Truth.

Conversation chỉ là nơi tiến hóa tri thức.

Mọi tri thức cuối cùng phải trở thành Artifact trên GitHub.

---

# 7. CHUẨN GITHUB

Đã thống nhất:

Mọi phản hồi GitHub theo đúng thứ tự:

1. Commit Message

2. File

3. Toàn bộ nội dung

Không dùng Patch nếu không yêu cầu.

Không dùng Diff.

Ưu tiên mỗi nội dung chỉ cần copy một lần.

---

# 8. THIẾT KẾ ARTIFACT

Đã thống nhất:

Artifact phải:

* đọc được sau nhiều năm
* AI đọc được
* con người đọc được
* có thể kế thừa
* có thể mở rộng
* có thể sinh tự động
* có thể kiểm tra tự động

---

# 9. AHI+

Đã thống nhất:

AHI+

là tín hiệu kích hoạt

AHI Working Mode.

---

# 10. AHI+ NEXT

Đã thống nhất:

AHI+ NEXT

nghĩa là:

tiếp tục Dependency tiếp theo

không lặp lại nội dung cũ.

---

# 11. AHI-CHATGPT

Đã thống nhất:

ChatGPT trong AHI:

* không chỉ là chatbot
* là AHI-CHATGPT
* đồng hành cùng AHI
* hỗ trợ tiến hóa tri thức
* không thay thế con người

---

# 12. GITHUB LÀ SOURCE OF TRUTH

Đã thống nhất:

Nếu Artifact tồn tại:

* đọc trước
* kế thừa
* tiến hóa

Không viết lại từ đầu.

---

# 13. KIẾN TRÚC AHI

Đã thống nhất các thành phần:

* Constitution
* Specification
* Skill
* Runtime
* Memory
* AI Provider
* Agent
* Context Engine
* Semantic Search
* GitHub API
* MCP
* Workspace Runtime

---

# 14. AHI RUNTIME

Đã thống nhất Runtime gồm:

* GitHub API
* AI Provider
* Embedding
* Semantic Search
* Context Engine
* MCP
* Conversation Runtime
* Agent Runtime

---

# 15. AHI-GITHUB API

Đã thống nhất:

Chức năng:

* Clone
* Pull
* Push
* Commit
* Read Tree
* Read File
* Search
* Webhook

---

# 16. AHI-MCP

Đã thống nhất:

AHI đóng vai trò MCP Server.

Cung cấp Tool:

* read_file()
* search()
* commit()
* create_issue()
* list_repository()

---

# 17. AHI-AI PROVIDER

Đã thống nhất:

Adapter chung cho:

* OpenAI
* Gemini
* Claude
* Ollama
* DeepSeek

Interface:

* Generate()
* Chat()
* Embedding()
* Vision()
* Speech()

---

# 18. AHI-EMBEDDING

Đã thống nhất:

Markdown

↓

Chunk

↓

Embedding

↓

Vector

↓

Qdrant

---

# 19. AHI-SEMANTIC SEARCH

Đã thống nhất:

Question

↓

Embedding

↓

Vector Search

↓

Top K

↓

Markdown

↓

Context

---

# 20. AHI-CONTEXT ENGINE

Đã thống nhất:

Question

↓

GitHub

↓

Semantic Search

↓

Memory

↓

Skill

↓

Prompt

↓

AI Provider

---

# 21. AHI-CONVERSATION RUNTIME

Đã thống nhất:

Quản lý:

* Conversation
* History
* Prompt
* Summary
* Memory

---

# 22. AHI-AGENT RUNTIME

Đã thống nhất:

Các Agent:

* Architect
* Programmer
* Reviewer
* Researcher
* Translator
* Tester

Dùng chung Context Engine.

---

# 23. CÔNG NGHỆ ĐỀ XUẤT

Đã thống nhất:

* Python
* FastAPI
* Docker
* Docker Compose
* PostgreSQL
* Redis
* Qdrant
* GitHub Actions
* JWT
* MCP Python SDK

---

# 24. KIẾN TRÚC TRIỂN KHAI

GitHub

↓

AHI Runtime

↓

GitHub API

↓

Embedding

↓

Semantic Search

↓

Context Engine

↓

AI Provider

↓

Conversation Runtime

↓

Agent Runtime

---

# 25. MỤC TIÊU CUỐI CÙNG

AHI phải có khả năng:

* đọc GitHub
* hiểu Artifact
* tìm kiếm ngữ nghĩa
* kế thừa tri thức
* sinh Context
* hỗ trợ nhiều AI
* không phụ thuộc một AI duy nhất
* coi GitHub là nguồn tri thức chính thức
* tiến hóa lâu dài theo Human Ownership

---

# 26. CÁC MỤC CẦN TRIỂN KHAI TIẾP

1. Chuẩn hóa cấu trúc AHI-Workspace.
2. Hoàn thiện Specification cho từng Runtime.
3. Xây dựng AHI-GitHub API.
4. Xây dựng AHI-MCP.
5. Xây dựng AHI-AI Provider.
6. Xây dựng Embedding + Semantic Search.
7. Xây dựng Context Engine.
8. Xây dựng Conversation Runtime.
9. Xây dựng Agent Runtime.
10. Tích hợp toàn bộ vào AHI-Workspace và triển khai CI/CD.

---

# KẾT LUẬN

Đến thời điểm hiện tại, AHI đã thống nhất định hướng kiến trúc theo mô hình Hybrid Intelligence với GitHub là Source of Truth. Toàn bộ quá trình phát triển sẽ ưu tiên kế thừa Artifact, chuẩn hóa thành Skill và Specification, sau đó triển khai Runtime có khả năng đọc GitHub, tìm kiếm ngữ nghĩa, quản lý ngữ cảnh và hỗ trợ nhiều AI thông qua một lớp điều phối thống nhất.
