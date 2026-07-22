# NetZeroLoop Energy™
## Một ứng dụng của AHI Industry™ — Kiến trúc Kỹ thuật Nhà máy

*Hệ thống năng lượng tuần hoàn tích hợp AI vận hành thời gian thực, áp dụng tại nhà máy xử lý chất thải Khe Giang, Quảng Ninh*

Phiên bản 1.0 — Tháng 7/2026

---

## 1. Vị trí trong kiến trúc AHI

NetZeroLoop Energy™ là lớp ứng dụng công nghiệp cụ thể của **AHI Industry™** — lớp thứ tư trong kiến trúc bốn lớp của AHI (Human Layer™, AI Core™, Hybrid Intelligence™, AHI Industry™). Trong khi tài liệu "AHI — Nguyên lý Nền tảng" trình bày cơ sở lý luận tổng quát cho toàn bộ kiến trúc, tài liệu này tập trung vào thiết kế kỹ thuật cụ thể cho lĩnh vực năng lượng tuần hoàn và xử lý chất thải công nghiệp.

Về mặt lý luận, NetZeroLoop Energy™ là minh chứng thực tiễn cho **Nguyên lý 3 — Entropy Tri thức**: hệ thống tạo ra vòng phản hồi thời gian thực giữa AI Core™ và dữ liệu vận hành vật lý của nhà máy, qua đó giảm độ lệch giữa mô hình dự báo và thực tế vận hành theo thời gian.

---

## 2. Kiến trúc hệ thống NetZeroLoop Energy™

### 2.1. Chu trình Brayton sCO₂ (Supercritical CO₂ Brayton Cycle)
Chu trình nhiệt động sử dụng CO₂ siêu tới hạn làm môi chất công tác, thay thế hơi nước truyền thống trong các chu trình Rankine kinh điển. Ưu điểm chính là mật độ năng lượng cao hơn trên một đơn vị thể tích thiết bị, hiệu suất chuyển đổi nhiệt – điện cao hơn ở dải nhiệt độ trung bình đến cao, và footprint thiết bị nhỏ gọn hơn — phù hợp với các nhà máy có diện tích hạn chế như cơ sở xử lý chất thải.

### 2.2. Chu trình ORC/Rankine hữu cơ (Organic Rankine Cycle)
Chu trình bổ sung, tận dụng nhiệt thải ở dải nhiệt độ thấp hơn (waste heat recovery) mà chu trình Brayton sCO₂ không khai thác hết, sử dụng môi chất hữu cơ có điểm sôi thấp. Kết hợp Brayton sCO₂ và ORC tạo thành hệ thống thu hồi năng lượng đa tầng nhiệt độ (cascaded thermal recovery), tối đa hoá tỷ lệ chuyển đổi nhiệt thải thành điện năng hữu ích.

### 2.3. Carbon Recovery Loop™
Vòng thu hồi các-bon khép kín, thiết kế để thu giữ CO₂ phát sinh trong quá trình đốt/xử lý chất thải và tái sử dụng một phần làm môi chất công tác cho chính chu trình Brayton sCO₂, đồng thời xử lý phần CO₂ dư theo hướng thu giữ – lưu trữ hoặc thương mại hoá (ví dụ cung cấp cho công nghiệp thực phẩm, nông nghiệp), giảm phát thải ròng của toàn hệ thống.

### 2.4. AI Energy Brain™
Lớp điều phối thông minh, đóng vai trò AI Core™ chuyên biệt cho vận hành năng lượng: dự báo tải nhiệt/điện theo thời gian thực, tối ưu hoá phân bổ giữa các chu trình Brayton sCO₂ và ORC, điều tiết Carbon Recovery Loop™, và phát hiện bất thường vận hành sớm. AI Energy Brain™ vận hành trong khuôn khổ giám sát của Human Layer™ theo đúng nguyên lý an toàn phân tầng của kiến trúc AHI — không có quyền quyết định độc lập tại các nút trọng yếu (an toàn thiết bị, ngắt khẩn cấp, ngưỡng phát thải).

### Bảng tổng hợp bốn phân hệ kỹ thuật

| Phân hệ | Vai trò kỹ thuật | Chức năng trong vòng lặp AHI |
|---|---|---|
| Brayton sCO₂ | Chuyển đổi nhiệt độ cao – điện, hiệu suất cao, gọn | Nguồn dữ liệu vận hành thời gian thực cho AI Energy Brain™ |
| ORC/Rankine | Thu hồi nhiệt thải nhiệt độ thấp | Tối ưu hoá tỷ lệ thu hồi năng lượng tổng thể |
| Carbon Recovery Loop™ | Thu giữ và tái sử dụng CO₂ | Giảm phát thải ròng, tạo dòng doanh thu phụ |
| AI Energy Brain™ | Điều phối, dự báo, phát hiện bất thường | Thực thi Nguyên lý 3 (Entropy Tri thức) qua phản hồi thực địa |

---

## 3. Ứng dụng thực tế: Nhà máy Khe Giang, Quảng Ninh

Đối tác triển khai: **Công ty CP Việt Long**, chủ đầu tư cơ sở xử lý chất thải Khe Giang. Đề xuất hợp tác chiến lược bao gồm thành lập liên doanh **VietLong–AHI NetZero Technology JSC**, với lộ trình niêm yết (IPO) hướng tới giai đoạn 2029–2030.

Mục tiêu triển khai tại Khe Giang gồm ba trụ cột:

1. Nâng cấp hiệu suất năng lượng của cơ sở xử lý chất thải hiện hữu thông qua tích hợp chu trình Brayton sCO₂ và ORC, giảm chi phí vận hành và tăng sản lượng điện thương phẩm.
2. Giảm phát thải ròng thông qua Carbon Recovery Loop™, hướng tới các tiêu chí ESG và khả năng tiếp cận nguồn vốn xanh, bao gồm nguồn tài trợ tiềm năng từ Sở Khoa học và Công nghệ Quảng Ninh.
3. Thiết lập vòng phản hồi dữ liệu vận hành thực tế đầu tiên cho AI Energy Brain™, làm cơ sở dữ liệu thực nghiệm để kiểm chứng Nguyên lý 3 trong tài liệu AHI — Nguyên lý Nền tảng, phục vụ lộ trình nâng cấp Nguyên lý này thành Định lý.

Định hướng mở rộng quốc tế sau giai đoạn thí điểm tại Khe Giang bao gồm tiếp cận nhà đầu tư Nhật Bản và thị trường ASEAN, dựa trên kết quả vận hành thực chứng thay vì chỉ dựa trên mô hình lý thuyết.

---

## 4. Liên kết ngược với Nguyên lý AHI

Dữ liệu vận hành thu thập từ nhà máy Khe Giang sẽ được sử dụng làm bằng chứng thực nghiệm cho **Giai đoạn 2** của "Lộ trình từ Nguyên lý đến Định lý" nêu trong tài liệu AHI — Nguyên lý Nền tảng, cụ thể là chỉ số sai lệch dự báo (forecast deviation) của AI Energy Brain™ theo chu kỳ hàng quý, và tỷ lệ can thiệp của Human Layer™ tại các nút quyết định an toàn thiết bị và ngưỡng phát thải.
