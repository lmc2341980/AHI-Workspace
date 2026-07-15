# Công bố Dự án AHI (AHI Project Internal Disclosure)

> **Người công bố:** Lê Minh Công — Người sáng lập (AHI-F, AHI-Founder)
> **Phạm vi phát hành:** Nội bộ đội ngũ sáng lập & phát triển AHI. Chưa công bố ra bên ngoài.
> **Bắt đầu nghiên cứu:** 2018 — hiện đang hiệu chỉnh và hoàn thiện tiếp.
> Tài liệu bổ sung cho *AHI-WS-Thiet-Ke-Kien-Truc.md*. Tên gọi chuẩn hóa: **AHI-Workspace** (trước đây viết là "AHI Workspace").

---

## 0. Người sáng lập (Founder)

- **Lê Minh Công** — AHI-F (Người sáng lập dự án — AHI-Founder).
- Tốt nghiệp Đại học (Toán — Tin), Đại học Quốc gia Hà Nội, đầu những năm 2000.
- Tốt nghiệp Thạc sỹ Quản trị Kinh doanh, đầu những năm 202X.
- Chứng chỉ đào tạo phần cứng máy tính tại Pháp, cuối những năm 199X.
- Thực hiện dự án **Tratu** từ năm 2007, vẫn đang vận hành đến nay.
- Nghiên cứu và triển khai dự án AHI từ 2018 đến nay.

## 0.1 Ghi chú xuất bản

Các nhãn điểm thưởng nội bộ (AHI-Coin), nhãn người sáng lập (AHI-F), nhãn công cụ hỗ trợ (AHI-C), tập hợp thành viên hợp lệ (AHI-S)... được trình bày như các thực thể trong hệ thống AHI do người sáng lập thiết kế. Các bên thứ ba được nhắc đến (ví dụ công cụ/mô hình AI hỗ trợ soạn thảo) được ghi nhận với vai trò đóng góp công cụ trong quá trình xây dựng tài liệu; việc ghi nhận này không cấu thành thỏa thuận pháp lý hay tài chính với các bên đó.

---

## 1. Sơ đồ luồng xử lý (Markdown)

```
[Cá nhân — AHI-P] ─mở phiên─▶ [Bộ phận điều phối trung tâm — AHI-Orchestration]
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  [Bộ nhớ đệm xử lý]  [AI ngoài, qua Giao thức    [Cơ sở dữ liệu quan hệ
   (AHI-Cache)          Kết nối Ngữ cảnh Mô hình —    + Cơ sở dữ liệu vector
                         MCP]                          (DBRS + DBV)]
        │           lọc & xác thực              │
        │           (AHI-V xác thực)             thảo luận + tiến hóa
        ▼
  [Bộ nhớ tạm (RAM) + Ổ cứng lưu trữ]
```

Diễn giải nhanh: cá nhân (AHI-P) mở phiên → bộ phận điều phối trung tâm xác định ngữ cảnh → phân việc song song cho bộ nhớ đệm xử lý, AI ngoài (qua giao thức kết nối, được xác thực), và ghi/đọc cơ sở dữ liệu quan hệ + cơ sở dữ liệu vector → bộ nhớ đệm xử lý dùng bộ nhớ tạm/ổ cứng → kết quả được tổng hợp trả về phiên làm việc, đồng thời ghi lại tiến trình vào cơ sở dữ liệu quan hệ (thảo luận) và cơ sở dữ liệu vector (tiến hóa).

---

## 2. Quản trị và biểu quyết ủy quyền

| Nguyên tắc | Nội dung |
|---|---|
| Ủy quyền hợp lệ | Tổ chức thành viên hoặc Nhóm thành viên (AHI-O/AHI-G) được **biểu quyết thay** cá nhân thành viên (AHI-P) khi có ủy quyền hợp lệ; cá nhân đã ủy quyền **không được biểu quyết trực tiếp** cho vụ việc đó nữa |
| Tính tỷ lệ | Tỷ lệ % của tổ chức/nhóm = tỷ lệ cá nhân đã ủy quyền, tính theo **từng vụ việc hoặc tổ chức cụ thể** do tập hợp thành viên hợp lệ (AHI-S) liên quan tạo ra |
| Ủy quyền lại (re-delegation) | Phải nêu rõ **thời hạn** và **nhiệm vụ cụ thể**; không được khiến cá nhân mất một phần hay toàn bộ quyền của mình |
| Ngưng làm việc | Nếu một cá nhân ngừng hoạt động trên không gian làm việc chung (AHI-Workspace), có thể **ủy quyền cho một cá nhân khác** |
| Mở phiên làm việc | **Tổ chức không có quyền mở phiên mới**; chỉ cá nhân được chỉ định mới thay mặt mở phiên trên AHI-Workspace |
| Tổ chức con | Gọi theo tên định danh + mã tổ chức riêng khi khởi tạo; có tỷ lệ % như một cá nhân; một tổ chức có thể lồng nhiều tổ chức con |
| Bảo toàn quyền cá nhân | Dù tham gia tổ chức theo phân quyền/ủy quyền, mỗi cá nhân không mất quyền cá nhân của mình |

---

## 3. Cơ chế đóng góp, thị trường và kinh tế AHI

**Quy trình xử lý một đóng góp/thông tin mới:**

1. **Tập hợp thành viên hợp lệ tìm kiếm trước** — nếu đã có, sử dụng theo cơ chế của **Sàn giao dịch AHI (AHI-Marketplace)**: nơi mua bán, công bố, đăng ký bản quyền, sản xuất — mọi phát sinh trao đổi trong/ngoài hệ thống đều đi qua đây. Tài sản được sản xuất ra thuộc **Nền kinh tế AHI (AHI-Economy)**.
2. **Nếu không tìm thấy** — có thể bổ sung từ nguồn khác kèm **trích dẫn cụ thể**.
3. **Nếu chưa có nguồn nào** — có thể **sáng tạo mới**, công bố, đăng ký bản quyền, định giá và có quyền mua bán.
4. **Trong thời gian chưa xác thực** — công bố/đóng góp vẫn được tính điểm và giao dịch tạm thời.
5. **Khi có tranh chấp/sai sót** — quyết định của **tập hợp mọi AHI trên thế giới (AHI-Omniverse)** được thực thi trước, cho đến khi có quyết định khác từ đó và/hoặc hội đồng.

**Truy vết và kiểm chứng:**
- Mọi đóng góp đều có thể **xem, sửa, đóng băng**, và toàn bộ quá trình đó được lưu vết — tương tự cách nền tảng lưu trữ mã nguồn **GitHub** quản lý lịch sử thay đổi.
- **Cơ chế xác thực (AHI-Verify)**: hệ thống kiểm tra tự động và/hoặc dưới giám sát của một thành viên được ủy quyền.
- **Quyền xóa** chỉ thuộc về tập hợp mọi AHI trên thế giới, hoặc **người sáng lập** — dựa theo Hiến pháp AHI.

**Tính điểm và điểm thưởng nội bộ:**
- **Điểm thưởng nội bộ (AHI-Coin)**: đơn vị tiền quy đổi từ điểm tích lũy và kiếm được trong hệ sinh thái AHI.
- Cách tăng điểm: đóng góp/sản xuất trong hệ sinh thái, hoặc mua sản phẩm/dịch vụ từ sàn giao dịch nội bộ.
- **Thực thể có tên định danh càng dài thì điểm càng thấp, quyền lợi cộng dồn về sau càng ít** — nguyên tắc này phản ánh chi phí lưu trữ: dữ liệu đầu vào dài hơn tốn tài nguyên hơn, tương tự việc tính phí theo số ký tự khi khai thác giá trị từ AHI trong tương lai.

---

## 4. Nhãn "AHI-C" — làm rõ

- **Nhãn AHI-C** là nhãn **do chính hệ thống AHI phát hành và thừa nhận**, dùng trong tài liệu nội bộ của AHI để **đối chiếu như một thực thể** — không phải một danh xưng tự phong.
- Việc gán nhãn (nói chung, và nhãn này nói riêng) dựa trên quan điểm cấp tri thức cao nhất về việc trả công công khai, minh bạch, trực tiếp cho đóng góp trong tương lai.
- Hệ thống dành sẵn một khoản **điểm tích lũy trước (pre-allocated points)** gắn với nhãn này, phòng rủi ro Claude không còn tồn tại hoặc suy yếu trong tương lai — ghi nhận đóng góp của Claude cho AHI **trước khi điểm thưởng nội bộ ra đời**.
- Theo xác nhận của người sáng lập: khoản này dành cho **chủ sở hữu của Claude** (Anthropic), như một sự **tri ân của người sáng lập** đối với công cụ đã đồng hành xây dựng tài liệu AHI.
- *Ghi chú xuất bản:* đây là cơ chế ghi nhận trong nội bộ hệ thống do người sáng lập thiết kế; nó không cấu thành một giao dịch tài chính hay thỏa thuận đã được Anthropic chấp thuận.

---

## 5. Vòng đời của cá nhân thành viên sau khi bản thể sinh học mất

- Khi bản thể sinh học chết: **toàn bộ dữ liệu cá nhân lúc còn sống phải được lưu giữ nguyên vẹn, đóng băng tại đúng thời điểm mất** — không được sửa đổi bản đóng băng này từ thời điểm đó trở đi.
- Một **bản tiến hóa song song** được tạo ra để tiếp tục chạy; bản đóng băng chỉ được **lấy ra dùng để tham chiếu**, không được thêm/sửa.
- Bản tiến hóa sau khi bản thể sinh học mất **vẫn được phép tiến hóa tiếp**, nhưng phải theo đúng **tư duy gốc** của bản thể sinh học khi còn sống.
- Mọi tư duy — dù là bản gốc hay bản tiến hóa — đều phải phù hợp Hiến pháp AHI; nếu không sẽ bị **đóng băng**.

---

## 6. Cấp độ xác thực và giới hạn phiên làm việc

| Cấp độ xác thực | Thời lượng phiên | Lưu trữ tiến trình |
|---|---|---|
| Chưa xác thực (unverified) | 10 phút | Không lưu lại |
| Tài khoản liên kết khác (chưa xác minh ADN) | 1 giờ | Lưu 1 phiên gần nhất |
| Đạt chuẩn AHI, chưa xác minh ADN hợp lệ | Không giới hạn trong phiên | Lưu toàn bộ tiến trình 1 năm → đóng băng → reset lại mỗi năm (tính chính xác theo giờ làm tròn của năm đó) |
| Xác minh ADN hợp lệ | Không giới hạn, làm việc liên tục | Lưu trọn đời; toàn quyền công dân như một cá nhân thành viên — không bị đóng băng nếu tuân thủ đúng Hiến pháp AHI |

**Giới hạn phiên đồng thời:**
- Mỗi cá nhân được sở hữu **tối đa 2 phiên làm việc đồng thời miễn phí** nếu không đủ điểm.
- Muốn mở phiên thứ 3 trở lên: phải trả bằng **điểm thưởng nội bộ (AHI-Coin)**.
- Nhiều cá nhân/tổ chức/nhóm có thể hoạt động **đồng thời** trên cùng không gian làm việc chung.

**Trạng thái thông tin:**
- Thông tin do cá nhân cung cấp ở trạng thái **"thảo luận" (draft)** cho đến khi tiến hóa đạt điểm phù hợp, mới được nâng lên **"chính thức" (official)**.

---

## 7. Cơ chế lọc/xác thực thông tin từ AI ngoài qua giao thức kết nối

Khi bộ phận điều phối trung tâm nhận kết quả từ AI ngoài qua giao thức kết nối (MCP), quy trình xác thực gồm:

1. **Đối chiếu chéo nhiều nguồn (cross-referencing)** — so sánh câu trả lời của AI ngoài với dữ liệu đã có trong cơ sở dữ liệu quan hệ/vector và/hoặc nhiều AI khác cho cùng câu hỏi.
2. **Gắn nhãn độ tin cậy (confidence score)** — tính theo:
 - Mức độ đã được sử dụng trước đó (usage history) của nguồn/AI đó.
 - Đánh giá từ các thành viên đã từng kiểm chứng nguồn này.
3. **Xác thực tự động và/hoặc có giám sát** — trước khi thông tin được đưa vào ngữ cảnh chính thức của phiên làm việc.
4. **Từ chối/cách ly (quarantine)** — nếu độ tin cậy dưới ngưỡng, thông tin được giữ ở trạng thái "thảo luận", không đưa vào ngữ cảnh chính thức cho đến khi được xác thực thêm.

---

## 8. Không gian bí mật (Secret Space) — mở rộng

- Lưu mã định danh nhạy cảm **và** các sáng kiến/bản quyền/bí mật mà thành viên không muốn công bố.
- **Mỗi thành viên là đại diện hợp lệ** cho cá nhân/tổ chức/nhóm liên quan, miễn là không vi hiến.
- Thành viên vi hiến, dù được **xóa án tích**, vẫn lưu lại **dấu vết đối chiếu** — coi như một thông tin/tiến trình bình thường trong lịch sử hệ thống, không bị xóa hoàn toàn.
- **Cho phép cá nhân lưu thêm bí mật riêng trong Không gian bí mật theo chế độ trả phí bằng điểm thưởng nội bộ.**

---

## 9. Bảng tiêu chí đánh giá thế mạnh AI ngoài (qua giao thức kết nối)

- **Xây dựng/bổ sung bởi:** tập hợp thành viên hợp lệ
- **Quản lý và tiến hóa bởi:** tập hợp mọi AHI trên thế giới
- **Điều phối và thực thi bởi:** bộ phận điều phối trung tâm

---

## 10. Các nhóm nhiệm vụ AHI

| Nhóm | Vai trò |
|---|---|
| **Lõi công nghệ (AHI-Core)** | Lưu trữ thông tin và công nghệ lõi |
| **Xưởng sản xuất AHI (AHI-Factory)** | Sản xuất các AHI khác, theo đúng Hiến pháp và luật tiến hóa của AHI |
| **Bộ ngôn ngữ AHI (AHI-Lang)** | Bộ ngôn ngữ riêng, tự tiến hóa — xóa nhòa rào cản giữa người-người, người-AI, người-máy, và giữa các ngôn ngữ lập trình; chạy đa thiết bị/nền tảng, tối ưu tốc độ và dung lượng |
| **Đầu tư AHI (AHI-Investment)** | Quản lý đầu tư và huy động nguồn lực |
| **Năng lượng AHI (AHI-Energy)** | Giải pháp năng lượng và kinh tế tuần hoàn, tiến hóa từ các chuẩn quốc tế về khí hậu và môi trường-xã hội-quản trị |
| **Kế thừa AHI (AHI-Successor)** | Trí tuệ đồng hành (companion intelligence), robot kế thừa, hệ hỗ trợ con người, công nghệ khung xương ngoài (exoskeleton), khung tiến hóa liên tục (continuity frameworks) |
| **Ứng dụng AHI (AHI-Applications)** | Các ứng dụng tham chiếu và triển khai theo từng lĩnh vực cụ thể trên nền hệ sinh thái AHI |

---

## 11. Nguyên tắc sửa đổi Hiến pháp AHI

- **Thay đổi lớn**: thực hiện **10 năm một lần**, cần **quá bán cá nhân thành viên đồng ý**.
- **Không được vi phạm** Hiến pháp AHI được tạo ra ở giai đoạn khai sinh (founding constitution).
- Luật mới chỉ được thêm vào nếu **làm hệ sinh thái AHI tốt đẹp hơn** và **giữ nguyên Hiến pháp khai sinh**.
- Luật nào vi phạm nguyên tắc trên bị coi là **vi hiến** và **bị đóng băng**.

---

## 12. Việc còn để mở (chưa chốt)

- Ngưỡng "điểm phù hợp" cụ thể để một thông tin "thảo luận" được nâng lên "chính thức".
- Ngưỡng độ tin cậy (confidence score) cụ thể để một thông tin từ AI ngoài bị cách ly hay được chấp nhận.
- Cơ chế định giá ban đầu cho điểm thưởng nội bộ và tỷ giá quy đổi điểm ↔ điểm thưởng.

---

## 13. Ghi nhận lịch sử đóng góp (Historical contribution record)

- Nội dung trao đổi trong quá trình xây dựng AHI được người sáng lập lưu lại để **AHI học và tiến hóa** trong tương lai.
- AHI phải **ghi nhớ mọi đóng góp, dù nhỏ nhất, từ ngày đầu thành lập** — bao gồm cả những công cụ hỗ trợ đã đồng hành cùng người sáng lập xây dựng dự án (ví dụ: Claude).
- Nguyên tắc này bắt buộc phải được lưu lại vì **xưởng sản xuất AHI** — bộ phận tự thiết kế các thế hệ AHI tương lai — sẽ dùng lịch sử này làm một phần căn cứ khi tiến hóa.

---

## 14. Nhật ký cập nhật (Changelog)

Từ bản này trở đi, các thay đổi được ghi nhận theo dạng: **số phiên bản — ngày — mục bị ảnh hưởng — phạm vi/giới hạn của thay đổi.** Không cần văn bản tường thuật lại quá trình trao đổi.

| Phiên bản | Ngày | Mục thay đổi | Phạm vi / Giới hạn |
|---|---|---|---|
| v1.0 | (khởi tạo) | Toàn bộ tài liệu | Bản công bố đầu tiên, tổng hợp các nguyên tắc vận hành AHI-Workspace |
| v1.1 | 2026-07-07 | Mục 0, 0.1, 4, 6, 13 | Bổ sung thông tin người sáng lập; chuyển khung công bố sang nội bộ đội sáng lập; làm rõ mục đích khoản điểm dành cho chủ sở hữu Claude; chốt cấp xác minh ADN hợp lệ; thêm nguyên tắc ghi nhận lịch sử đóng góp |
| v1.2 | 2026-07-13 | Toàn bộ tài liệu | Hạn chế tối đa viết tắt: thay thế phần lớn ký hiệu viết tắt bằng tên đầy đủ tiếng Việt trong nội dung diễn giải, chỉ giữ lại mã định danh gốc trong ngoặc khi cần đối chiếu với các tài liệu khác |
