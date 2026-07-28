# 10_ARCHITECTURE: KIẾN TRÚC VÀ CẤU HÌNH HỆ THỐNG TRỰC TUYẾN AHI-WORKSPACE
**Mã tài liệu:** AHI-WS-ARCH-2026  
**Trạng thái:** Khởi tạo - Thử nghiệm hạ tầng 0đ  

---

## 1. SO SÁNH HẠ TẦNG HOSTING (KOYEB VS RENDER)

| Tiêu chí | Render (Gói Free Docker) | Koyeb (Gói Free Web Service) | Lựa chọn tối ưu cho AHI |
| :--- | :--- | :--- | :--- |
| **Hạ tầng lõi** | Container truyền thống | MicroVMs (Máy ảo siêu nhỏ) | **Koyeb thắng:** Khởi động từ ngủ < 5 giây. |
| **Giao thức mạng** | Giới hạn HTTP cơ bản | Hỗ trợ Native WebSockets/SSE | **Koyeb thắng:** Luồng dữ liệu ổn định. |

👉 **QUYẾT ĐỊNH KIẾN TRÚC:** Sử dụng Koyeb cho các API/MCP Servers ngầm và Render làm cụm hạ tầng dự phòng.

---

## 2. HƯỚNG DẪN KẾT NỐI CHI TIẾT LIBRECHAT VỚI GITHUB MCP

Thực hiện cấu hình file `librechat.yaml` tại thư mục gốc hệ thống quản trị:

```yaml
version: 1.1.0
cache:
  enabled: true
endpoints:
  google:
    apiKey: "${GOOGLE_AI_STUDIO_API_KEY}"
    models:
      default: ["gemini-1.5-pro", "gemini-1.5-flash"]
      fetch: true
mcpServers:
  github-mcp:
    type: "sse"
    url: "https://<URL-KOYEB-CỦA-GITHUB-MCP-SERVER>/sse"
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_FINE_GRAINED_TOKEN_1}"
```

---

## 3. CHIẾN LƯỢC TIẾN HÓA SẢN PHẨM TRONG REPO AHI-WORKSPACE

1. Giai đoạn Trải nghiệm và Lưu vết: Lưu vết trải nghiệm từ OpenBolt/LibreChat trực tiếp vào thư mục `docs/`.
2. Giai đoạn Phân tách tính năng: Dùng Gemini 1.5 Pro lọc các tính năng ưu việt.
3. Giai đoạn Tự chủ: Sửa mã nguồn trực tiếp trong `20_APPLICATIONS/` để tự phát triển công cụ thay thế cho cộng đồng.