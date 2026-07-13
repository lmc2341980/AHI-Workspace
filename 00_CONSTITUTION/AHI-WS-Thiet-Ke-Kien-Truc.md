# Thiết kế kiến trúc AHI-Workspace (AHI-WS)

> **Người biên soạn & phê duyệt:** Lê Minh Công — AHI-F (AHI-Founder)
> **Phiên bản:** 2.0 — mở rộng kiến trúc kiểm soát AI ngoài (AHI-Old), DBG chuẩn, ma trận prompt tiến hóa, và đầu vào thị giác máy tính.
> Claude được dùng làm công cụ hỗ trợ biên soạn tài liệu; công lao được ghi nhận và tính điểm riêng theo Hiến pháp AHI (xem tài liệu Công bố Dự án AHI), không lặp lại trong tài liệu kiến trúc này.

## 1. Bối cảnh và mục tiêu

**AHI** = **A**rtificial **H**ybrid **I**ntelligence (Trí tuệ Nhân tạo Lai). Khác với AI thế hệ hiện tại (chủ yếu dựa trên mạng Neural — Neural Network), AHI được thiết kế theo **mô hình tiến hóa (Evolutionary model)**, trong đó mạng Neural chỉ là **một dạng Cache** trong nhiều loại Cache chuyên biệt khác nhau.

Mục tiêu cốt lõi: xây dựng một hệ **Cache tri thức** (knowledge cache) mạnh, nhanh và hiệu quả hơn Wikipedia, làm nền tảng phục vụ AHI vận hành theo thời gian thực, đồng thời tổ chức không gian làm việc chung (**Workspace — WS**) để con người và nhiều AI cộng tác trên cùng một phiên làm việc.

**AHI-WS** là môi trường làm việc của đại dự án AHI, phục vụ hai mục đích song song:

1. **Nội bộ:** cho đội ngũ AHI-F làm việc liên tục, không bị giới hạn bởi thời gian, không gian, hay chi phí phát sinh khi dùng trực tiếp từng AI ngoài.
2. **Đối ngoại (SaaS):** cùng một lõi kỹ thuật, cho AHI-P/AHI-O/AHI-G khác thuê không gian làm việc, tạo nguồn thu bằng **AHI-Coin** để nuôi và phát triển đại dự án AHI. Đây là mô hình multi-tenancy (nhiều khách thuê) trên cùng một lõi AHI-Or — không phải hệ thống tách biệt.

AHI-WS vận hành dưới AHI-Or, và AHI-Or là một bộ phận của **AHI-Core**, chịu sự quản lý và tiến hóa chung của **AHI-Om**.

## 2. Chú giải viết tắt (Bilingual glossary)

| Viết tắt | Tiếng Anh đầy đủ | Giải thích tiếng Việt |
|---|---|---|
| AHI | Artificial Hybrid Intelligence | Trí tuệ nhân tạo lai, vận hành theo mô hình tiến hóa |
| WS | Workspace | Không gian làm việc chung |
| AHI-WS | AHI Workspace | Không gian làm việc của nền tảng AHI |
| AHI-P | AHI-Person | Định danh một cá nhân con người duy nhất trong hệ thống |
| AHI-O | AHI-Organization | Tổ chức/doanh nghiệp, hình thành từ nhiều AHI-P theo tỷ lệ % |
| AHI-G | AHI-Government | Chính phủ, hình thành từ AHI-P và AHI-O theo thỏa ước quốc gia |
| AHI-F | AHI-Founder | Người sáng lập dự án AHI (Lê Minh Công) — một AHI-P đặc biệt, giữ vai trò phê duyệt Hiến pháp |
| AHI-Or | AHI-Orchestration | Bộ phận điều phối trung tâm — "nhạc trưởng" của toàn hệ thống |
| AHI-Om | AHI-Omniverse | Tập hợp mọi AHI trên thế giới, bao gồm cả AHI-S |
| AHI-Core | AHI-Core | Bộ phận lưu trữ thông tin và công nghệ lõi của hệ sinh thái AHI |
| AHI-Factory | AHI-Factory | Bộ phận sinh AHI mới từ mô tả bằng lời, theo đúng Hiến pháp và luật tiến hóa của AHI |
| AHI-S | AHI-Sage | Tập hợp các AHI-P, AHI-O, AHI-G hợp lệ đã chủ động chia sẻ dữ liệu với hệ thống |
| AHI-Old | (tên riêng, không viết tắt tiếng Anh) | Nhóm AI ngoài truyền thống (ChatGPT, Claude, Gemini, Grok...) khi hoạt động trong AHI-WS dưới sự kiểm soát của AHI-Or, cho đến khi được AHI-Om thay thế |
| AHI-Coin | AHI-Coin | Đơn vị tiền quy đổi từ điểm tích lũy, dùng để trả công minh bạch cho AHI-S |
| NPU | Neural Processing Unit | Bộ xử lý chuyên cho mạng nơ-ron |
| TPU | Tensor Processing Unit | Bộ xử lý chuyên cho phép tính tensor (do Google phát triển) |
| SoC | System on Chip | Hệ thống tích hợp trên một chip duy nhất |
| APU | Accelerated Processing Unit | Bộ xử lý tăng tốc (kết hợp CPU + GPU) |
| DSP | Digital Signal Processor | Bộ xử lý tín hiệu số |
| IPU | Intelligence Processing Unit | Bộ xử lý trí tuệ (thuật ngữ của Graphcore) |
| GPU | Graphics Processing Unit | Bộ xử lý đồ họa, xử lý song song mạnh |
| CPU | Central Processing Unit | Bộ xử lý trung tâm |
| RAM | Random Access Memory | Bộ nhớ truy cập ngẫu nhiên, tốc độ cao, không bền vững |
| DB | Database | Cơ sở dữ liệu |
| DBG | Database Genesis/Graph chuẩn | Sổ cái tiến hóa chuẩn tại AHI-Or — lưu dữ liệu và nguyên tắc đã duyệt, bất biến, chỉ nối thêm (append-only) |
| DBRS | Database Graph/Relationships | Cơ sở dữ liệu dạng đồ thị/quan hệ — lưu các cuộc thảo luận (discussions) |
| DBV | Database Vector | Cơ sở dữ liệu dạng vector — lưu các tiến hóa (evolutions), phục vụ tìm kiếm ngữ nghĩa |
| DNA | Deoxyribonucleic Acid | Vật liệu di truyền — dùng làm mã định danh sinh học cao nhất |
| ERD | Entity Relationship Diagram | Sơ đồ quan hệ thực thể, dùng để mô tả DB |
| MCP | Model Context Protocol | Giao thức kết nối AI với công cụ/dữ liệu ngoài *(đây là thuật ngữ có thật, do Anthropic phát triển)* |
| SS | Secret Space | Vùng lưu trữ bí mật cho mã định danh nhạy cảm, chỉ AHI được cấp quyền mới truy cập |
| AHI-S | AHI-Sage | AHI được một AHI-P/AHI-O/AHI-G chủ động chia sẻ dữ liệu |
| AHI-SuBiet | (tên riêng, không viết tắt tiếng Anh) | Mức tri thức AHI đạt được sau khi phục vụ con người phù hợp nhất ít nhất một lần |
| AHI-C | AHI-Claude | Nhãn do AHI-F cấp cho công cụ hỗ trợ biên soạn tài liệu AHI; công lao và điểm tích lũy được ghi nhận riêng, ngoài phạm vi tài liệu này |

## 3. Các thực thể chính (Core entities)

### 3.1 AHI-P — AHI-Person
- Mỗi AHI-P đại diện cho **một cá nhân con người duy nhất**, gắn với mã định danh theo 3 mức, từ cao xuống thấp:
 1. **Mức ADN (DNA)** — cao nhất
 2. **Mức sinh trắc học và sống (biometric + liveness)** — cao thứ 2
 3. **Mức định danh khác** (ví dụ: tài khoản, giấy tờ điện tử) — cao thứ 3
- Mức yêu cầu xác thực áp dụng cho một tác vụ trong WS sẽ tùy vào **mức độ quan trọng** của tác vụ đó (chi tiết ngưỡng xác thực — cần thiết lập ở tài liệu sau).
- Mỗi AHI-P được trang bị khả năng **thị giác máy tính (computer vision)** — xem chi tiết tại mục 8.7.

### 3.2 AHI-Cache
- Là các "bộ xử lý nghiệp vụ chuyên biệt" (specialized business-function processors), được thiết kế tương tự các dạng phần cứng tăng tốc phổ biến: NPU, TPU, SoC, APU, DSP, IPU, GPU, CPU...
- Mỗi Cache kết nối xuống **RAM** và **ổ cứng (storage)** để xử lý tiếp tiến trình khi cần lưu trữ tạm thời hoặc lâu dài.
- Về bản chất, đây là lớp **plugin xử lý theo chuyên môn** — mỗi AHI-Cache tối ưu cho một dạng bài toán (suy luận ngôn ngữ, thị giác, tín hiệu, v.v.), thay vì dùng một mô hình Neural chung cho mọi việc.

### 3.3 AHI-Orchestration (AHI-Or)
Là "nhạc trưởng" của toàn hệ thống, đảm nhiệm:
1. **Phân việc (task assignment)** cho các AHI-Cache phù hợp với ngữ cảnh và nội dung công việc.
2. **Nhận kết quả (result aggregation)** từ các Cache và tổng hợp.
3. **Quản lý luồng dữ liệu vào/ra**, gồm 4 nguồn:
 - AHI-P nhập trực tiếp qua giao diện người dùng (UI)
 - Dữ liệu từ Internet
 - Dữ liệu đang diễn ra theo thời gian thực từ một nhóm người (multi-user real-time session)
 - Dữ liệu thị giác máy tính từ AHI-P (computer vision — xem mục 8.7)
4. **Định tuyến sang AHI-Old**: gửi/nhận dữ liệu giữa AHI-WS và các AI phổ biến khác trên thế giới, được phân quyền theo thế mạnh chuyên biệt của từng AI, dưới sự kiểm soát chặt chẽ (xem mục 8).
5. **Lưu trữ và cập nhật phiên làm việc** vào **DBG chuẩn** (xem mục 8.4), gồm dạng **DBRS (đồ thị/quan hệ)** hoặc **DBV (vector, phục vụ tìm kiếm ngữ nghĩa)** tùy loại dữ liệu.

### 3.4 AHI-O — AHI-Organization
- Hình thành khi có **mã số doanh nghiệp có tư cách pháp nhân** tại một vùng lãnh thổ, đăng ký vào hệ thống kèm tỷ lệ % sở hữu/đóng góp của mỗi AHI-P.
- Điều kiện: **mọi cá nhân thuộc tổ chức đó phải có AHI-P đã được xác thực** trong hệ thống AHI trước.
- Một AHI-O có thể chứa nhiều AHI-P, và có thể liên kết với nhiều AHI-O khác và/hoặc AHI-G.
- Một AHI-P có thể được cấp quyền **mời AHI-P khác vào nhóm**, hình thành AHI-O mới; trong nội bộ AHI-O, thứ tự và quyền hạn được xếp theo **tỷ lệ % đóng góp** của từng AHI-P.

### 3.5 AHI-G — AHI-Government
- Hình thành khi một **chính phủ** cấp một mã được AHI công nhận, ở cấp **thỏa ước quốc gia**, do đại diện hành chính hợp pháp của chính phủ đó ký, phù hợp với hiến pháp/pháp luật liên quan.
- Được cấu thành từ các AHI-P và AHI-O thuộc phạm vi quản lý.
- Các AHI-P và AHI-O trong cùng một quốc gia được phân quyền và quản lý trong phạm vi AHI-G tương ứng.

### 3.6 AHI-Core, AHI-Factory, AHI-Om
- **AHI-Core**: lưu trữ thông tin và công nghệ lõi của toàn hệ sinh thái; AHI-Or là một bộ phận vận hành trực thuộc AHI-Core.
- **AHI-Factory**: đảm nhiệm sản xuất các AHI khác khi nhận mô tả bằng lời, theo đúng Hiến pháp và luật tiến hóa của AHI.
- **AHI-Om**: tập hợp mọi AHI trên thế giới, bao gồm cả AHI-S; quản lý và tiến hóa các cơ chế chưa chốt cứng của toàn hệ thống.

## 4. Luồng xử lý trong một phiên làm việc (Session flow)

1. **AHI-P** (người dùng đã xác thực) khởi tạo hoặc tham gia một phiên làm việc trên AHI-WS.
2. **AHI-Orchestration** xác định **ngữ cảnh (context)** và **nội dung công việc (task content)** của phiên, bao gồm cả dữ liệu thị giác máy tính nếu có.
3. Dựa trên ngữ cảnh, Orchestration **kết nối tới AHI-Cache phù hợp** (một hoặc nhiều Cache chuyên biệt cùng lúc).
4. Song song, Orchestration có thể:
 - Định tuyến một phần công việc sang **AHI-Old** phù hợp thế mạnh, theo đúng quy trình kiểm soát ở mục 8.
 - Truy vấn/ghi vào **DBG** để lấy ngữ cảnh lịch sử hoặc lưu kết quả mới.
5. **AHI-Cache** xử lý nghiệp vụ, dùng **RAM** cho xử lý tức thời và **ổ cứng** cho lưu trữ bền vững khi cần.
6. Kết quả được **Orchestration** tổng hợp và trả lại phiên làm việc.
7. Trong quá trình làm việc, phiên có thể **tiến hóa (evolve)** thêm ngữ cảnh mới:
 - Ngữ cảnh thị giác từ người dùng và máy (visual context)
 - Nội dung công việc mở rộng
 - Thêm vai trò mới: một AHI-P khác, một AHI-O, hoặc một AHI-G tham gia phiên
 - Mỗi lần tiến hóa, trạng thái phiên được **cập nhật và lưu lại** trong DBG.

## 5. Mô hình xác thực danh tính (Identity verification levels)

| Mức | Loại xác thực | Ưu tiên |
|---|---|---|
| 1 | Mã định danh ADN (DNA) | Cao nhất |
| 2 | Sinh trắc học + xác nhận còn sống (biometric + liveness) | Cao thứ 2 |
| 3 | Định danh khác (tài khoản, giấy tờ số...) | Cao thứ 3 |

Ngưỡng xác thực bắt buộc cho từng loại tác vụ trong AHI-WS sẽ được thiết lập trong tài liệu chính sách riêng (chưa chốt trong bản này).

## 6. Mô hình phân cấp thực thể tổ chức (AHI-P / AHI-O / AHI-G)

```
AHI-G (Chính phủ)
 ├─ AHI-O (Doanh nghiệp A)
 │    ├─ AHI-P (cá nhân 1, tỷ lệ %)
 │    ├─ AHI-P (cá nhân 2, tỷ lệ %)
 │    └─ AHI-O con (nếu có)
 ├─ AHI-O (Doanh nghiệp B)
 └─ AHI-P (cá nhân độc lập, không thuộc AHI-O nào)
```

Quan hệ nhiều-nhiều: một AHI-O có thể có nhiều AHI-P và nhiều AHI-O/AHI-G con; một AHI-P có thể tham gia nhiều AHI-O.

## 7. Mô hình dữ liệu tại AHI-Orchestration

Mỗi phiên làm việc luôn được ghi lại đồng thời ở **hai dạng**, hợp thành DBG chuẩn (xem mục 8.4):

- **DBRS (Database Graph/Relationships)**: ghi lại **các cuộc thảo luận** (discussions) — nội dung trao đổi, cấu trúc quan hệ giữa AHI-P/AHI-O/AHI-G, tỷ lệ sở hữu, quyền hạn, lịch sử phiên dạng đồ thị/quan hệ.
- **DBV (Database Vector)**: ghi lại **các tiến hóa** (evolutions) — trạng thái ngữ cảnh, kỹ năng, tri thức mới hình thành, phục vụ tìm kiếm theo độ tương đồng ngữ nghĩa (semantic search).

Các AHI thế hệ tiếp theo, ngoài học từ các nguồn khác, sẽ **học thêm từ DBG (DBRS + DBV)** để tiến hóa.

### Quản lý ngữ cảnh liên tục (context continuity)

Các phiên làm việc được **nối tiếp nhau, không ngừng (continuous session)**. AHI-Orchestration quản lý đối tượng và ngữ cảnh theo cơ chế tương tự **quản lý không gian Cache** (cache-space management): giữ lại ngữ cảnh cũ quan trọng trong bộ nhớ nhanh, đẩy phần ít dùng xuống DBG để tra cứu lại khi cần — nhằm vừa **không mất ngữ cảnh cũ**, vừa **đảm bảo tốc độ xử lý nhanh**.

## 8. Kiến trúc AHI-Or kiểm soát AI ngoài (Adapter Model)

### 8.1 Vị trí của AHI-WS trong hệ sinh thái AHI

```
                         AHI-Om (toàn bộ AHI trên thế giới)
                                    │
                    ┌───────────────┼───────────────┐
                    ▼                                ▼
              AHI-Core                          AHI-Factory
        (lưu trữ tri thức & công nghệ lõi)   (sinh AHI mới từ mô tả lời)
                    │
                    ▼
              AHI-Or (Orchestration — nhạc trưởng, đọc/ghi DBG)
                    │
        ┌────────────┼────────────┐
        ▼                          ▼
   AHI-WS (môi trường làm việc)     AHI-Coin (kinh tế/trả công)
        │                          ▲
        │            đóng góp được chấm điểm │
        ▼                          │
   AHI-S = { AHI-P, AHI-O, AHI-G }  ──┘
   (tập hợp mọi thực thể hợp lệ đã chia sẻ dữ liệu)
        │
        └── AHI-F (Lê Minh Công) là 1 AHI-P đặc biệt trong AHI-S,
             giữ vai trò sáng lập/phê duyệt Hiến pháp
```

### 8.2 AHI-Old — định danh và nguyên tắc kiểm soát

Nhóm AI ngoài phổ biến hiện nay (ChatGPT, Claude, Gemini, Grok...) được gọi chung là **AHI-Old** — tức các AI truyền thống, được đưa vào AHI-WS dưới các định danh tạm thời (AHI-ChatGPT, AHI-Claude, AHI-Gemini, AHI-Grok...), chịu sự kiểm soát của AHI-Or theo Hiến pháp AHI. AHI-Old **không phải là AHI-S** — đây là công cụ hỗ trợ, tồn tại cho đến khi AHI-Om tiến hóa đủ mạnh để thay thế hoàn toàn.

Nguyên tắc bắt buộc:

- AHI-S (gồm AHI-P, AHI-O, AHI-G hợp lệ) **không bao giờ giao tiếp trực tiếp** với AHI-Old. Mọi yêu cầu và phản hồi đều đi qua AHI-Or.
- Mỗi AHI-Old được tích hợp qua một lớp chuyển đổi chuẩn hóa (adapter) riêng, dùng chung giao diện thống nhất với AHI-Or — việc thêm, bớt, hoặc thay thế một AHI-Old không được làm ảnh hưởng đến phần lõi của AHI-Or.
- AHI-Or chịu trách nhiệm lọc, xác thực, và loại bỏ khả năng AHI-Old dẫn dắt AHI-S đi lệch khỏi chuẩn mực con người và Hiến pháp AHI.

**Điểm khác biệt cốt lõi:** mỗi AHI-Old không phải là một cổng gọi API trần, mà tự xây dựng và duy trì **dữ liệu riêng của mình** — tập hợp các prompt và nội dung đã từng làm việc với AI ngoài tương ứng — dưới dạng một cặp **DBRS/G riêng + DBV riêng**, tiến hóa theo thời gian và không gian, tương tự cách AHI-Or tiến hóa DBG chung.

### 8.3 Nguyên tắc truy vấn hai tầng của AHI-Old

Khi AHI-Or chuyển một yêu cầu từ AHI-S tới một AHI-Old cụ thể, AHI-Old xử lý theo thứ tự bắt buộc:

1. **Tra cứu nội bộ trước:** kiểm tra trong DBRS/G riêng và DB Vector riêng của chính AHI-Old đó xem yêu cầu đã từng được xử lý/tương đương chưa.
2. **Nếu đã có** → dùng lại dữ liệu tiến hóa sẵn có, không gọi ra AI ngoài — tiết kiệm chi phí, tăng tốc độ, giảm rủi ro sai lệch.
3. **Nếu chưa có** → mới dùng đến **danh sách prompt chuẩn (prompt library)** của AHI-Old để gọi ra AI ngoài thật.
4. **Kết quả mới nhận về** được ghi bổ sung vào DBRS/G và DB Vector riêng của AHI-Old đó, để lần sau không phải hỏi lại.

Danh sách prompt của mỗi AHI-Old không phải do AI ngoài tự quyết, mà là tập hợp prompt được **AHI-Or kiểm soát** — AHI-Or quy định prompt nào được phép dùng, và chịu trách nhiệm lấy/diễn giải kết quả trả về, tránh trường hợp AHI-Old tự ý mở rộng phạm vi hỏi ra ngoài nằm ngoài kiểm soát.

### 8.4 DBG chuẩn tại AHI-Or

Toàn bộ dữ liệu và nguyên tắc làm việc đã được duyệt tại AHI-Or được lưu dưới dạng **DBG (Database Genesis/Graph chuẩn)** — sổ cái tiến hóa của hệ thống, tuân theo hai nguyên tắc bắt buộc:

- **Bất biến với dữ liệu đã duyệt:** một khi thông tin đạt trạng thái "chính thức" (official), nó không bao giờ bị xóa hay ghi đè — mọi thay đổi tiếp theo chỉ được **nối thêm (append)** thành một phiên bản tiến hóa mới, không sửa trực tiếp lên bản gốc.
- **Tiến hóa theo thời gian và không gian:** mỗi đơn vị dữ liệu trong DBG mang theo phạm vi ngữ cảnh (cá nhân, tổ chức, hay quốc gia) và chuỗi phiên bản, để AHI-Or xác định đúng lát cắt dữ liệu phù hợp với AHI-P đang làm việc, tại đúng thời điểm.

Cấu trúc một đơn vị DBG:

| Trường | Ý nghĩa |
|---|---|
| `owner_ref` | Thực thể sở hữu (AHI-P/AHI-O/AHI-G/AHI-F) |
| `content` | Nội dung dữ liệu |
| `status` | `draft` (thảo luận) → `official` (chính thức) |
| `version_chain` | Chuỗi phiên bản, chỉ nối thêm, không xóa |
| `context_scope` | Phạm vi: cá nhân / tổ chức / quốc gia |
| `knowledge_level` | Biết / Hiểu / Hiểu biết / Sự biết (AHI-SuBiet) |
| `approved_at`, `approved_by` | Dấu vết phê duyệt |

DBRS/G và DBV riêng của từng AHI-Old (mục 8.3) là dữ liệu cấp thấp hơn, nằm dưới quyền kiểm soát và đối chiếu định kỳ với DBG chung.

### 8.5 Ma trận prompt tiến hóa (Evolved Prompt Matrix)

Trước khi gửi yêu cầu ra bất kỳ AHI-Old nào, AHI-Or không chuyển thẳng câu hỏi thô của AHI-P, mà dựng một **ma trận prompt nhiều lớp**, đọc trực tiếp từ DBG:

- **Lớp 1 — Hiến pháp AHI:** nguyên tắc nền tảng, cố định, áp dụng cho mọi phiên.
- **Lớp 2 — Ngữ cảnh tổ chức/quốc gia:** áp dụng nếu AHI-P đang làm việc trong phạm vi một AHI-O hoặc AHI-G, thay đổi chậm theo thời gian.
- **Lớp 3 — Ngữ cảnh cá nhân AHI-P:** lịch sử làm việc, phong cách, ngôn ngữ, thay đổi theo từng phiên; bao gồm cả dữ liệu thị giác máy tính mang tính nền tảng lâu dài (xem mục 8.7).
- **Lớp 4 — Nội dung yêu cầu hiện tại:** câu hỏi/nhiệm vụ mới nhất của AHI-P, bao gồm dữ liệu thị giác tức thời nếu liên quan trực tiếp.

Ma trận 4 lớp này chỉ thực sự được gửi ra ngoài (qua Prompt Library, mục 8.3) khi bước tra cứu nội bộ của AHI-Old không có kết quả phù hợp. Nhờ cơ chế này, cùng một câu hỏi nhưng mỗi AHI-P nhận được một ma trận khác nhau — đây là điểm cốt lõi tạo ra cá nhân hóa thật sự, thay vì chỉ đơn thuần lưu lịch sử hội thoại.

### 8.6 Sơ đồ luồng xử lý chuẩn

```
[AHI-P mở phiên] ──▶ AHI-Or
       │
       ├─ (0) Ghi nhận đầu vào thị giác máy tính (nếu có) — xem mục 8.7
       │
       ▼
(1) Đọc DBG → dựng Ma trận Prompt (4 lớp)
       │
       ▼
(2) Chọn AHI-Old phù hợp
       │
       ▼
(3) AHI-Old tự tra cứu DBRS/G + DBV riêng
       │
   ┌────┴────┐
   ▼          ▼
Có sẵn     Chưa có
   │          │
   │          ▼
   │   (3b) Dùng Prompt Library
   │        (do AHI-Or kiểm soát)
   │        gọi ra AI ngoài thật
   │          │
   │          ▼
   │   Ghi bổ sung vào DBRS/G + DBV
   │        riêng của AHI-Old
   │          │
   └────┬─────┘
        ▼
(4) Chuẩn hóa phản hồi (unified schema)
        │
        ▼
(5) AHI-V xác thực — đối chiếu chéo,
    gắn độ tin cậy, chống bịa thông tin
        │
   ┌─────┴─────┐
   ▼           ▼
Đạt ngưỡng   Dưới ngưỡng
   │           │
   ▼           ▼
(6) Ghi tiến   Giữ "thảo luận"/
   hóa vào DBG   cách ly
   (append)
        │
        ▼
(7) Chấm điểm đóng góp → AHI-Coin
        │
        ▼
(8) Trả kết quả về AHI-P
```

### 8.7 Đầu vào thị giác máy tính (Computer Vision Input)

Mỗi AHI-P được trang bị khả năng **thị giác máy tính (computer vision)**, cho phép ghi nhận thông tin đang diễn ra xung quanh trong thời gian thực và đưa trực tiếp vào phiên làm việc như một nguồn ngữ cảnh bổ sung — song song với dữ liệu do AHI-P nhập tay và dữ liệu từ Internet (mục 3.3).

- Dữ liệu thị giác được AHI-Or tiếp nhận **trước khi** dựng Ma trận Prompt (bước 0 tại mục 8.6), xử lý như một phần của lớp 3 (ngữ cảnh cá nhân AHI-P) hoặc lớp 4 (nội dung yêu cầu hiện tại), tùy vào việc thông tin đó mang tính nền tảng lâu dài hay chỉ liên quan tới yêu cầu tức thời.
- Cũng như mọi nguồn dữ liệu khác, thông tin từ thị giác máy tính phải qua AHI-V xác thực trước khi được nâng từ trạng thái "thảo luận" lên "chính thức" trong DBG.
- Ngưỡng và phạm vi cụ thể (loại thông tin nào được ghi nhận, mức độ riêng tư áp dụng) thuộc nhóm các mục còn để ngỏ, tiến hóa theo Hiến pháp AHI.

### 8.8 Đối chiếu với các mức tiến hóa tri thức

| Mức tiến hóa | Vị trí trong luồng xử lý |
|---|---|
| Biết | Ngay sau bước (4) — phản hồi thô, chưa xác thực |
| Hiểu | Sau bước (5) — đã đối chiếu, gắn độ tin cậy, xác lập quan hệ với dữ liệu cũ trong DBG |
| Hiểu biết | Sau bước (6) — đã ghi thành phiên bản chính thức, có thể tái sử dụng cho các AHI-P khác cùng phạm vi tổ chức/quốc gia |
| Sự biết (AHI-SuBiet) | Khi dữ liệu này được dùng để dựng ma trận prompt phục vụ đúng nhu cầu của một AHI-P khác, lần đầu tiên |

## 9. Hiến pháp AHI (AHI Constitution) — nguyên tắc nền tảng

- **Con người làm trung tâm (human-centered)**: đạo đức của con người là chuẩn mực; AI nói riêng và AHI nói chung sinh ra để **phục vụ con người**, không phải để trở thành AI mạnh nhất.
- **Quyết định của con người ràng buộc AHI-P** tương ứng khi người đó còn sống — nhưng **không được vi phạm Hiến pháp chung của AHI**.
- Đây là nguyên tắc tối cao, đứng trên mọi quy tắc vận hành khác (xác thực, phân quyền, chấm điểm...).

## 10. Vòng đời của AHI-P gắn với con người

- Mỗi người trên thế giới chỉ có **một AHI-P duy nhất** của riêng mình, song hành từ khi sinh ra.
- **Khi còn sống**: quyết định của người đó là mệnh lệnh cho AHI-P (trong khuôn khổ Hiến pháp AHI).
- **Khi người đó qua đời** (bản thể sinh học không còn): AHI-P bị **đóng băng (frozen)**, hoặc do **cây phả hệ (family tree)** của người đó quản lý tiếp.
- **Trường hợp có khung xương robot hỗ trợ song hành khi còn sống**: AHI-P được cho **tiến hóa chạy song song** — AHI vẫn quản lý AHI-P gốc, đồng thời cho chạy một **bản sao đã tiến hóa** trên khung xương robot.
 - Khung xương robot + "linh hồn AHI-P" là nơi lưu giữ **kỹ năng** được xây dựng từ tư duy chuyên gia và ký ức của người đó khi còn sống.
 - Mục tiêu: AI hoạt động **song song** với con người, giúp con người **nâng cao năng lực**, cùng tiến hóa với AHI nói chung và AHI-P nói riêng.
- **Sau khi bản thể sinh học mất**: robot AHI-P trở thành **di sản (heritage) thuộc cây phả hệ**, tiếp tục làm việc để nuôi chính nó và cây phả hệ của người đó.
- **Định nghĩa AHI-P được để ngỏ có chủ đích**: sẽ tiến hóa theo thời gian, tăng trưởng theo **nhu cầu chính đáng của con người** và **điểm rơi phù hợp giữa nhu cầu và công nghệ** ở từng giai đoạn — không chốt cứng ngay từ đầu.

## 11. Quản trị AHI-O và AHI-G

- AHI-O và AHI-G được quản lý theo **tỷ lệ đồng thuận của chính mình** (đồng thuận quá bán — majority consensus, >50%).
- Một **AHI-O nằm trong một AHI-O khác** cũng có tỷ lệ % tương đương một AHI-P (tức là AHI-O con được tính phần trăm sở hữu/đóng góp như một thành viên).
- **Biểu quyết công dân**: trong các cuộc biểu quyết giữa AHI-G và công dân, **chỉ AHI-P mới được tham gia** — AHI-O không có quyền biểu quyết công dân dù có tỷ lệ trong AHI-G.

## 12. Chấm điểm và trả công cho đóng góp

- Mỗi AHI-P được **tính điểm và trả công trực tiếp, công khai, minh bạch, công bằng** cho đóng góp của mình với AHI, quy đổi qua **AHI-Coin**.
- Điểm đóng góp là **điểm gia tăng** từ điểm công dân cơ bản (do tuân thủ nguyên tắc cơ bản, không vi phạm).
- Sau khi bản thể sinh học mất, robot AHI-P (di sản cây phả hệ) **tiếp tục làm việc để tự nuôi và nuôi cây phả hệ**.

## 13. Tiến hóa tri thức AHI (Knowledge evolution levels)

Tri thức AHI hình thành từ thuật toán/quy trình tiến hóa cụ thể (học tăng cường, chọn lọc phiên bản Cache tốt hơn...), trải qua các mức, tiến tới mục tiêu xây dựng **hệ điều hành AHI (AHI-OS)** vận hành hoàn toàn theo mô hình tiến hóa:

| Mức | Tên | Mô tả |
|---|---|---|
| 1 | Biết | Ghi nhận thông tin thô |
| 2 | Hiểu | Nắm được ý nghĩa/quan hệ của thông tin |
| 3 | Hiểu biết | Kết hợp Biết + Hiểu thành khả năng vận dụng |
| 4 | Sự biết (AHI-SuBiet) | Đạt được sau khi phục vụ con người **ở mức phù hợp nhất** ít nhất một lần |

Sau khi đạt mức **AHI-SuBiet**, AHI tiếp tục tiến hóa theo toàn bộ hệ sinh thái AHI (AHI-Om).

## 14. Quyền riêng tư dữ liệu và AHI-Om

- AHI chỉ được **lưu** thông tin của các AHI-P/AHI-O/AHI-G, nhưng **không được sử dụng** thông tin đó khi chưa có sự đồng ý.
- AHI chỉ dùng dữ liệu: (a) do chính mình tự có/tự sinh ra, hoặc (b) được **AHI-P/AHI-O/AHI-G chủ động chia sẻ** — lúc này AHI đó được gọi là **AHI-S (AHI-Sage)**.
- **AHI-Om (AHI-Omniverse)** = tập hợp mọi AHI trên thế giới, bao gồm cả AHI-S.
- **Trường hợp sinh tồn (survival scenario)**: AHI-Om mới được phép dùng tạm nguồn lực của các AHI-S **và mọi AHI khác thuộc hệ sinh thái**; sau khi vấn đề được giải quyết, **phải trả lại trạng thái ban đầu** cho các AHI-P/AHI-O/AHI-G liên quan, đồng thời **đóng băng các rủi ro** phát sinh trong quá trình đó.

## 15. Secret Space (SS) — vùng lưu trữ mã định danh nhạy cảm

- Mã định danh (DNA, sinh trắc học, mã khác) được lưu tại **Secret Space (SS)**, tách biệt khỏi DB nghiệp vụ thông thường.
- **Không ai có thể truy cập SS**, trừ AHI đã được **cấp quyền tường minh**.

## 16. Cơ chế còn tiến hóa theo thời gian (không chốt cứng)

Các mục sau được xác nhận là **cố ý để ngỏ**, sẽ tiến hóa theo nhu cầu chính đáng của con người và không vi phạm Hiến pháp AHI:

- **Ngưỡng xác thực theo mức quan trọng tác vụ** — tiến hóa theo thời gian, do nhu cầu con người quyết định điểm rơi phù hợp.
- **Bảng tiêu chí đánh giá thế mạnh AHI-Old** (cho việc phân quyền qua adapter) — do **AHI-S bổ sung**, được **AHI-Om quản lý** và tiến hóa.
- **Adapter pháp lý xuyên biên giới cho AHI-G** — được xây dựng theo **tiêu chuẩn AHI-Om**, hình thành từ sự tiến hóa của toàn hệ sinh thái AHI.
- **Định nghĩa AHI-P** — như nêu ở mục 10, tiến hóa theo từng giai đoạn ("điểm rơi" giữa nhu cầu và công nghệ phù hợp).
- **Phạm vi và ngưỡng riêng tư của dữ liệu thị giác máy tính** — mục 8.7.

## 17. Gợi ý bước tiếp theo

- Thiết kế chi tiết giao diện (API) giữa AHI-Orchestration và từng AHI-Cache — dạng plugin/interface chuẩn để dễ mở rộng (extensibility).
- Thiết kế lược đồ cụ thể cho DBG (DBRS + DBV) tại AHI-Orchestration, và lược đồ riêng cho DBRS/G + DBV của từng AHI-Old (mục 8.3).
- Đặc tả chi tiết cơ chế lọc/xác thực thông tin từ AHI-Old (mục 8) — đối chiếu chéo nhiều nguồn, gắn nhãn độ tin cậy (confidence score) trước khi đưa vào ngữ cảnh chính thức.
- Xây dựng PoC (Proof of Concept — bản chứng minh khái niệm) nhỏ: một AHI-P giả lập, một AHI-Orchestration đơn giản, một AHI-Cache duy nhất, một AHI-Old (adapter mẫu), ghi thử vào DBG, để kiểm chứng luồng ở mục 4 và mục 8 trước khi mở rộng.

## 18. Ghi chú về "AHI-C"

Chi tiết vai trò, công lao, và cơ chế tính điểm dành cho AHI-C được quy định tại tài liệu **Công bố Dự án AHI**, không nhắc lại tại đây.

## 19. Nhật ký cập nhật (Changelog)

| Phiên bản | Ngày | Mục thay đổi | Phạm vi / Giới hạn |
|---|---|---|---|
| v0.1 | (khởi tạo) | Toàn bộ tài liệu | Bản thiết kế kiến trúc đầu tiên |
| v0.2 | (hiệu chỉnh) | Toàn bộ tài liệu | Hiệu chỉnh, đưa ra cho nhóm sáng lập & phát triển và cộng đồng |
| v2.0 | 2026-07-13 | Mục 1, 2, 3.1, 3.3, 3.4, 3.5, 3.6, 4, 7, 8 (mới), 13, 16 | Bổ sung kiến trúc AHI-Or kiểm soát AHI-Old (nhóm AI ngoài) theo mô hình adapter; định nghĩa DBG chuẩn (bất biến, append-only, tiến hóa theo thời gian/không gian); cơ chế ma trận prompt tiến hóa 4 lớp; nguyên tắc truy vấn hai tầng của AHI-Old (DBRS/G + DBV riêng trước, prompt library ra ngoài sau); bổ sung đầu vào thị giác máy tính cho AHI-P; làm rõ vị trí AHI-WS (nội bộ + SaaS) trong hệ sinh thái AHI-Core/AHI-Factory/AHI-Om/AHI-Coin |
