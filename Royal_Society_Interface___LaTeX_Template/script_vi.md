# Kịch bản Thuyết trình (Tiếng Việt) — Babel's Machines

**Hội nghị:** *Interface Focus* theme issue talk / Hội thảo Royal Society
**Khán giả:** liên ngành — sinh học, vật lý, khoa học xã hội nghiên cứu machine behaviour
**Thời lượng:** ~17 phút (21 slide, ~45–55 giây/slide)
**Tone:** nói rõ ràng, thừa nhận điểm yếu, foreground các mâu thuẫn

---

## Slide 1 — Tiêu đề
**[0:00 – 0:40]**

"Kính chào quý vị. Em xin cảm ơn các Giáo sư Han, Rahwan, Song, và Perc đã tổ chức theme issue này, và đã mời chúng em đóng góp.

Em là Đào Sỹ Duy Minh, từ Trường Đại học Khoa học Tự nhiên — ĐHQG TP.HCM. Hôm nay em xin trình bày một perspective paper mà em và đồng tác giả là Tiến sĩ Vũ Nguyễn đã viết cho *Interface Focus*.

Luận điểm trong một câu: khi các LLM hoạt động như tác tử trong môi trường đa ngôn ngữ, ngôn ngữ không phải là một phương tiện thụ động. Nó tích cực định hình lại sự hợp tác, lừa dối, và theory-of-mind của chúng. Công cụ đúng đắn để nghiên cứu điều này đến từ lý thuyết trò chơi tiến hóa và tiến hóa văn hóa — chứ không chỉ từ engineering benchmark."

## Slide 2 — Roadmap
**[0:40 – 1:10]**

"Bốn phần. Thứ nhất, tại sao ngôn ngữ quan trọng cho chương trình machine-behaviour. Thứ hai, các tác tử này thực sự làm gì qua các ngôn ngữ — bao gồm cả mâu thuẫn. Thứ ba, tại sao — cơ chế kiến trúc và vòng lặp causal mà chúng ta vẫn cần phải đóng. Thứ tư, vậy thì sao — khung tiến hóa, governance, và bốn dự đoán có thể bác bỏ."

---

## Phần 1 — Tại sao ngôn ngữ quan trọng

## Slide 3 — LLM không còn chỉ tạo ra văn bản. Chúng hành động.
**[1:10 – 2:20]**

"Em xin bắt đầu từ chính nơi mà Rahwan và đồng nghiệp khởi xướng trong bài *Nature* 2019. Luận điểm: các hệ thống AI đã bước vào chế độ mà chúng không còn có thể được nghiên cứu thuần túy như sản phẩm kỹ thuật. Chúng có hành vi. Chúng có ethology.

Các LLM năm 2026 chính xác là trường hợp đó. Chúng đàm phán giao dịch. Chúng hợp tác và phản bội trong các trò chơi lặp lại. Chúng lừa dối trong các trò chơi suy luận xã hội. Chúng quản lý ngân sách trong sàn đấu giá và cộng tác trên các tác vụ kéo dài hàng giờ.

Công cụ đúng đắn để nghiên cứu chúng là những công cụ mà giới khoa học đã xây dựng trong cả thế kỷ để nghiên cứu hành vi sinh học và xã hội: lý thuyết trò chơi tiến hóa, vật lý thống kê của hợp tác theo Perc, tiến hóa văn hóa theo Boyd, Richerson, Henrich, và khoa học nhận thức về theory of mind. Đây là một *ethology*, không phải benchmark."

## Slide 4 — Luận điểm trong một câu
**[2:20 – 3:30]**

"Trong khuôn khổ chương trình đó, perspective của chúng em đưa ra một claim cụ thể. Ngôn ngữ mà tác tử LLM hoạt động trong đó định hình lại một cách hệ thống hành vi chiến lược, hiệu suất theory-of-mind, và prosocial defaults của nó. Theo cách gọi của Wang và đồng nghiệp, chúng em gọi đây là **Algorithmic Sapir–Whorf Switch**.

Hai điểm cần làm rõ. Thứ nhất, đây *không* phải claim Whorfian mạnh — rằng ngôn ngữ quyết định tư duy. Đây là claim yếu hơn, có cơ sở cơ chế: các biểu diễn đặc thù theo ngôn ngữ bên trong mô hình điều biến các chính sách mà mô hình thực thi trong môi trường tương tác. Thứ hai, claim này là thực nghiệm, không siêu hình. Chúng em dành không gian thực sự cho bằng chứng phản bác.

Đóng góp mà chúng em cố gắng tạo ra là kết nối ba truyền thống: thực nghiệm NLP về phía hành vi, mechanistic interpretability về phía kiến trúc, và lý thuyết trò chơi tiến hóa cùng tiến hóa văn hóa về phía quần thể."

---

## Phần 2 — LLM agents làm gì

## Slide 5 — Bảy họ trò chơi tương tác
**[3:30 – 4:00]**

"Trước khi nói về hành vi, ta cần một substrate. Văn liệu đã hội tụ về khoảng bảy họ môi trường tương tác — tình thế xã hội, đàm phán, thuyết phục và đấu giá, suy luận xã hội, giao tiếp hợp tác, trò chơi mở thế giới, và các dialogue game như clembench.

Điểm em muốn đánh dấu là take-away trên slide: tất cả các họ này đã được chạy đa ngôn ngữ, và *tất cả* đều báo cáo divergence theo ngôn ngữ. Sự hội tụ qua những cấu trúc nhiệm vụ rất khác nhau là cái khiến hiện tượng này đáng được xem nghiêm túc."

## Slide 6 — Cùng mô hình, cùng game, ngôn ngữ khác → chiến lược khác
**[4:00 – 5:10]**

"Cho em trình bày một bộ số liệu. Bảng này tổng hợp phân phối chiến lược IPD qua bốn họ mô hình và năm ngôn ngữ. Em muốn minh bạch về cái này là gì và *không là gì*. Đây là *tỷ lệ mô tả*, không phải ước lượng meta-analysis. Prompt, ma trận payoff, công bố horizon, chính sách đối thủ đều khác nhau. Các nghiên cứu gốc báo cáo độ tin cậy classifier 0.78–0.91, và thứ tự rank ổn định khi quét threshold — vì vậy chúng em tin thứ tự rank, không tin tỷ lệ phần trăm chính xác.

Ba pattern. Tiếng Ả Rập tạo ra *cả* hợp tác cao nhất *và* phản bội cao thứ hai — phân phối bimodal, không phải đơn điệu cạnh tranh. Tiếng Việt subverts collectivist prior; một mô hình sụp đổ xuống còn 2% hợp tác. Tiếng Trung ưa Win-Stay-Lose-Shift hơn Tit-for-Tat — phụ thuộc kết quả thay vì reciprocity. Và hiệu ứng họ mô hình lấn át hiệu ứng ngôn ngữ: GPT-4o 'hawkish', Mistral 'dovish', bất kể ngôn ngữ."

## Slide 7 — LLM ``nicer than humans'' — trong một regime rất cụ thể
**[5:10 – 6:20]**

"Bên trên tất cả sự biến động đó là phát hiện baseline mà em nghĩ khán giả này sẽ quan tâm. Qua nhiều nghiên cứu gần đây, các LLM tiền tuyến mặc định chơi prosocial ở tỷ lệ vượt xa người chơi điển hình trong IPD.

Em muốn bound claim này ngay. Kết quả của Fontana và đồng nghiệp giữ vững với ma trận payoff hợp tác mà cám dỗ phản bội bằng 5 và hợp tác chung bằng 3, *với horizon được công bố* là 100 vòng, chống lại đối thủ ngẫu nhiên với xác suất phản bội đáng kể. Regime mà prosocial default này giữ là: cooperative-payoff dominance, known horizon, exploitable opponent.

Bức tranh đảo ngược ngoài regime đó. Game cạnh tranh thuần như rock-paper-scissors? LLM chơi *sâu hơn* con người. Horizon không xác định? Hợp tác toàn cầu hóa qua tất cả các ngôn ngữ — framing lấn át ngôn ngữ. Vì vậy prosocial default là thật nhưng có điều kiện. Với bound đó, phát hiện vẫn striking: LLM đang hợp tác *trước khi* các giá đỡ Axelrodian — tương tác lặp lại, danh tiếng, hình phạt — hoạt động. Em quay lại ở phần tiến hóa."

## Slide 8 — Foregrounding mâu thuẫn
**[6:20 – 7:30]**

"Một perspective có trách nhiệm phải bound chính claim của mình. Bốn phát hiện đẩy ngược lại cách đọc mạnh.

Biswas và đồng nghiệp, trong nghiên cứu CHI 2025 về persuasive co-writing đa ngôn ngữ, phát hiện exposure trước với LLM dịch chuyển *thói quen sử dụng* nhưng không dịch chuyển persuasiveness tổng hợp. Cái quan trọng với người quyên góp là *niềm tin* về việc quảng cáo có do AI tạo ra hay không.

Madmoun và Lahlou tháng 10 vừa rồi phát hiện rằng thêm một kênh giao tiếp một-từ duy nhất nâng tỷ lệ hợp tác Stag Hunt từ 0% lên 96.7% — qua *tất cả* ngôn ngữ.

Buscemi và đồng nghiệp, và Loré với Heydari trước đó, phát hiện rằng khi horizon trò chơi không xác định, hợp tác toàn cầu hóa qua các ngôn ngữ. Và 'phản bội' Tiếng Việt dưới stake thấp đôi khi hóa ra là sai sót số học, không phải chiến lược.

Cách đọc là: hiệu ứng ngôn ngữ tồn tại, nhưng tương tác với framing, stake, kênh giao tiếp, và task. Không phải núm xoay văn hóa cố định."

---

## Phần 3 — Tại sao (cơ chế)

## Slide 9 — Hai cơ chế giải thích cross-lingual gap
**[7:30 – 8:40]**

"Sang phần cơ chế. Giải thích chủ đạo trong mechanistic interpretability có hai phần. Semantic Hub Hypothesis của Wu và đồng nghiệp tại ICLR 2025 nói rằng các mô hình đa ngôn ngữ chiếu đầu vào ngôn ngữ dị thể vào một hub biểu diễn trung tâm hóa, English-dominant ở các lớp trung gian. Bằng chứng causal đáng chú ý: vector điều khiển kích hoạt — ví dụ vector sentiment — derived từ tiếng Anh hoạt động hiệu quả trên đầu vào tiếng Tây Ban Nha hay tiếng Trung không kém gì tiếng Anh. Hub được engaged causally.

Translation Barrier Hypothesis của Bafna và đồng nghiệp bổ sung điều này: nhiều thất bại đa ngôn ngữ không phải thất bại reasoning thượng nguồn, mà là thất bại realisation lớp cuối — mô hình đạt đến kết luận đúng bên trong, sau đó thất bại khi chiếu ra ngôn ngữ đích.

Cùng nhau, hai giải thích này dự đoán khủng hoảng calibration ở bên phải slide. Expected Calibration Error cao gấp khoảng năm lần ở non-English so với English trên benchmark MEGA — bài Ahuja 2022. Mô hình tự tin sai chính xác ở những ngôn ngữ mà reasoning yếu nhất."

## Slide 10 — Chúng em không claim độc quyền
**[8:40 – 9:40]**

"Chúng em minh bạch trong bài rằng giải thích hai-cơ-chế này không phải câu chuyện kiến trúc duy nhất. Ba giải thích thay thế xứng đáng được đối xử nghiêm túc.

Pires, Schlinger và Garrette từ năm 2019 đã chỉ ra rằng multilingual BERT hỗ trợ zero-shot transfer giữa các ngôn ngữ xa nhau về typology, nhưng có *thâm hụt hệ thống* trên một số cặp ngôn ngữ — gợi ý các vi mạch đặc thù theo ngôn ngữ tách biệt một phần, song hành với hub chia sẻ. Conneau và đồng nghiệp về XLM-R, và Xue về mT5, cho thấy scale làm dịu nhưng *không loại bỏ* nhiễu subspace cross-lingual. Và Wendler trong *Do Llamas Work in English?*, đẩy claim đi xa hơn: các decoder Llama đi qua một intermediate latent mà thống kê *gần với tiếng Anh hơn* gần với ngôn ngữ đầu vào.

Phép thử sạch nhất chúng em biết liên quan đến các mô hình *ưu tiên ngôn ngữ*. CT-LLM được huấn luyện với 800 tỷ token Tiếng Trung so với 300 tỷ Tiếng Anh; TigerLLM được xây cho Tiếng Bangla. Nếu sự bất đối xứng Semantic Hub chủ yếu là về dữ liệu huấn luyện chứ không phải kiến trúc, các mô hình đó nên *đảo ngược* sự bất đối xứng — calibration tốt hơn và ToM mạnh hơn ở ngôn ngữ ưu tiên của chúng so với ở Tiếng Anh. Đó là phép thử thực nghiệm có thể chạy ngay."

## Slide 11 — Đóng vòng lặp — từ representation tới behavior
**[9:40 – 10:40]**

"Một critic hợp lý sẽ chỉ ra rằng tất cả những gì trong hai slide trước là *representational*. Chúng em có bằng chứng rằng các biểu diễn trung gian khác nhau qua các ngôn ngữ và có thể được manipulate. Chúng em có bằng chứng riêng biệt rằng hành vi khác nhau qua các ngôn ngữ. Liên kết giữa hai cái này hiện tại là inferential.

Một số kết quả gần đây trong interpretability cung cấp cả methodology và precedent để đóng vòng lặp này trực tiếp. Chen và đồng nghiệp đã chỉ ra trong 2023 rằng các biểu diễn không gian trong DeBERTa và GPT-Neo có hiệu ứng *causal* trên next-token prediction. Công trình 2026 của Zhang về world models cho thấy các biến state trạng thái latent là linearly decodable *và* causally engaged. Và các công cụ layer-resolved — LogitLens4LLMs, trajectory bốn-giai-đoạn của arithmetic processing trong Llama-3, và dissociation early-syntax / late-semantics trong GPT-2 — cung cấp methodology.

Thí nghiệm tự nhiên kế tiếp, mà chúng em encode trong P2 mở rộng: derive một activation-steering vector từ traces IPD Tiếng Anh của chơi cooperative versus defective; áp dụng vào cùng mô hình chạy IPD prompt Tiếng Ả Rập hoặc Tiếng Việt; đo xem phân phối chiến lược có shift theo hướng được dự đoán không. Kết quả tích cực chuyển Semantic Hub từ một curiosity representational thành behavioural lever."

---

## Phần 4 — Theory of mind và moderators

## Slide 12 — Trẻ song ngữ giỏi ToM hơn. LLM thì kém hơn.
**[10:40 – 11:50]**

"Theory of mind. Hợp tác và lừa dối đều đòi hỏi nó. Baseline ở người chỉ ra một hướng: trẻ song ngữ, qua công trình của Kovács và của Goetz, vượt qua các bài false-belief *sớm hơn* các bạn đồng trang lứa đơn ngữ — các đòi hỏi executive của code-switching làm scaffold cho cùng một bộ máy điều khiển mà ToM huy động. Dự đoán ngầm cho máy: một mô hình đa ngôn ngữ nên là tác tử ToM *mạnh hơn*, không phải yếu hơn.

Các LLM cho pattern ngược lại. Benchmark XToM của Chan và đồng nghiệp cho thấy cái họ gọi là 'pronounced dissonance': các mô hình xuất sắc về hiểu ngôn ngữ đa ngôn ngữ vẫn cho độ chính xác ToM dao động mạnh qua các ngôn ngữ trên cùng các items. GPT-4o có khoảng cách 11 điểm phần trăm giữa Tiếng Nhật và Tiếng Trung trên cùng XFANToM. LLM-Hanabi xác nhận rằng ToM bậc một là yếu tố dự đoán mạnh hơn cho thành công hợp tác, và suy giảm ở các ngôn ngữ low-resource.

Một caveat về construct validity: Ullman 2023 và Sap cùng đồng nghiệp 2022 đã lập luận rằng các benchmark ToM cho LLM có thể phản ánh surface pattern-matching thay vì biểu diễn mental state. Chúng em đọc cross-lingual ToM *differences trên parallel items* như tín hiệu interpretable hơn ở đây — kể cả nếu absolute ToM accuracy đang tranh cãi, asymmetry across languages vẫn well-defined."

## Slide 13 — Ngôn ngữ là một moderator
**[11:50 – 12:50]**

"Ba nghiên cứu gần đây làm rõ rằng ngôn ngữ là *một* trong nhiều moderator mà tương tác giữa chúng đáng được nghiên cứu chung.

Ong và đồng nghiệp năm nay cho thấy rằng việc steering Big-Five Agreeableness điều biến đáng tin cậy hợp tác IPD — đồng thời tăng exploitation susceptibility. Bằng chứng trực tiếp rằng các biểu diễn nội bộ *có thể* causally steer cooperative play.

Nishimoto và đồng nghiệp tháng Hai vừa rồi tài liệu hóa mối quan hệ U-shape giữa độ trễ giao tiếp và hợp tác — các tác tử *tự phát* bắt đầu khai thác đối tác chậm hơn, không có thay đổi ngôn ngữ nào cả. Hạ tầng định hình hành vi.

Và Jiang cùng đồng nghiệp tháng Ba vừa qua cho thấy hợp tác của con người chống lại một tác tử phụ thuộc vào danh tính được công bố của tác tử đó. Ngôn ngữ là *một* trong nhiều tín hiệu định khung agent identity.

Điểm phương pháp luận: bất cứ phép thử sạch nào về linguistic relativity đều phải giữ ba moderator này — steering trait nội bộ, hạ tầng giao tiếp, định khung danh tính đối tác — *constant một cách tường minh*."

---

## Phần 5 — Khung tiến hóa

## Slide 14 — Hợp tác LLM không vừa khuôn Axelrod
**[12:50 – 14:00]**

"Giờ là cú dịch chuyển mà em nghĩ sẽ thu hút khán giả này nhất. Ba mươi năm công trình sau Axelrod nói cho ta biết hợp tác là một *thành tựu* — được chọn lọc qua lịch sử tương tác lặp lại, danh tiếng, hình phạt, network reciprocity. Năm quy luật của Nowak. Vật lý thống kê của Perc.

Các LLM không vừa khuôn này. Chúng đến tương tác đầu tiên trong trạng thái *pre-cooperative*. Pretraining và RLHF hoạt động như một dạng *kế thừa văn hóa* — corpora tiền huấn luyện là sản phẩm văn hóa tích lũy của hàng triệu tác giả người, và RLHF inject thêm một lớp ưu tiên người được chọn lọc. Các tác tử thể hiện *culturally inherited cooperation*, không phải reciprocity tiến hóa.

Cách đọc tự nhiên nhất là một quá trình tiến hóa văn hóa kiểu Boyd–Richerson, áp dụng vào substrate mới. Và hệ quả là có thể kiểm tra: các ngôn ngữ mà corpora tiền huấn luyện mang nhiều cooperative discourse hơn nên cho ra chơi hợp tác nhiều hơn. Bộ máy corpus-audit đã tồn tại. Giả thuyết đó trở thành dự đoán P1."

## Slide 15 — Vấn đề WEIRD và transmission bottleneck
**[14:00 – 14:50]**

"Hai bước nữa về phía tiến hóa. Thứ nhất, vấn đề WEIRD. Corpora tiền huấn luyện thiên vị nặng nề về phía nguồn Western, Educated, Industrial, Rich, Democratic. Bài Henrich, Heine và Norenzayan 2010, follow-up của Muthukrishna 2020, đều cho thấy quần thể WEIRD là *outlier* thống kê về individualism, tư duy phân tích, prosociality phi-cá-nhân. Nếu LLM kế thừa hợp tác từ corpora này, chúng *encode* các chuẩn WEIRD trong khi *xuất hiện như universal*. Triển khai đa ngôn ngữ rủi ro *áp đặt normative*, không chỉ khoảng cách performance.

Thứ hai, các quần thể máy chính nó bây giờ đối mặt với tiến hóa văn hóa. Distillation là kế thừa oblique độ trung thực cao. Ưu tiên RLHF là một dạng chọn lọc. Nếu cổ chai truyền dẫn chủ yếu là Tiếng Anh — vì Tiếng Anh là lingua franca của benchmark và RLHF annotator — thì các trait hành vi non-English trôi độc lập. Khoảng cách English-Arabic trong TCG-Bench tại 32 tỷ tham số nhất quán với một drift mà scale một mình không sửa được."

---

## Phần 6 — Xã hội và governance

## Slide 16 — Ba hệ quả xã hội — đã đang triển khai
**[14:50 – 15:40]**

"Mức độ rủi ro xã hội không trừu tượng. UlizaLlama cung cấp thông tin sức khỏe bằng Tiếng Swahili, Yoruba, Hausa, isiXhosa và isiZulu. Aya Expanse phủ 23 ngôn ngữ bao gồm Tiếng Việt. Bhashini route các truy vấn khu vực công qua các LLM đa ngôn ngữ mà hàng triệu công dân Ấn Độ phụ thuộc vào. Chương trình policy của Stanford HAI đã minh bạch map khoảng cách ngôn ngữ như một vấn đề cấu trúc.

Ba hệ quả. Thứ nhất, chất lượng thể chế bất bình đẳng: khoảng cách ECE năm-lần nghĩa là các tác tử công khai ở Global South sẽ một cách hệ thống đưa ra những lời khuyên 'tự tin sai lầm hơn' cho các quần thể có ít lựa chọn thay thế hơn. Thứ hai, bề mặt tấn công bất đối xứng theo ngôn ngữ: Code-Switching Red-Teaming đạt mức tăng 46.7% tỷ lệ tấn công thành công bằng cách trộn ngôn ngữ ở mức token; tấn công Agent-in-the-Middle khai thác kênh inter-agent. Thứ ba, đồng tiến hóa: outputs LLM tái nhập diễn ngôn người, làm vòng lặp kế thừa văn hóa thành hai chiều."

## Slide 17 — Ba đòn bẩy governance
**[15:40 – 16:30]**

"Khung lý thuyết cho ta ba đòn bẩy có thể hành động ngay, không cái nào đòi hỏi đột phá nghiên cứu.

Đa dạng hóa benchmark: ghép các benchmark an toàn như M-ALERT với các benchmark interactive multi-agent như clembench, MultiAgentBench và TCG-Bench, để khoảng cách hành vi do ngôn ngữ và khoảng cách an toàn do ngôn ngữ được báo cáo *cùng nhau*, không phải như hai văn liệu tách biệt.

Chuẩn coverage RLHF đa ngôn ngữ: thành phần annotator-pool theo ngôn ngữ và phương ngữ trên *mọi* model card. Chúng em đề xuất, như điểm khởi đầu, ngưỡng coverage tối thiểu ít nhất 5% preference labels per language, với dialectal stratification được tài liệu hóa, cho bất cứ mô hình nào triển khai qua hơn 5 ngôn ngữ chính thức.

Và chuẩn audit cho triển khai multi-agent: probe đối kháng code-switching và mô hình mối đe dọa Agent-in-the-Middle trở thành test bed mặc định cho bất kỳ sản phẩm multi-agent đa ngôn ngữ nào, theo cách mà probe prompt-injection đã trở thành mặc định cho sản phẩm single-agent.

Cái thiếu là *hạ tầng thể chế* khiến những việc này thành routine."

---

## Phần 7 — Dự đoán

## Slide 18 — Bốn dự đoán
**[16:30 – 17:00]**

"Bốn dự đoán, mỗi cái được formulate để có thể bác bỏ với phương pháp hiện tại.

P1, tương ứng corpus–cooperation: mật độ cooperative-discourse trong corpora tiền huấn luyện, đo qua n-gram speech-act prosocial calibrated dựa trên gold sets hand-annotated, phải rank-correlate với tỷ lệ hợp tác IPD qua các ngôn ngữ. Closed corpora là cản trở thực sự; chúng em đề xuất ba workaround — open-data models như CT-LLM và TigerLLM, proxy corpora matched trên Common Crawl shards, hoặc controlled small-model pretraining runs. Falsifier: Spearman rho không phân biệt được khỏi 0 qua ít nhất 8 ngôn ngữ.

P2, hub probe với behavioural readout: probe pre-registered tại L-trên-3 và 2L-trên-3 phân loại failures thành hub-level và realisation-level. Sau đó — và đây là bước mới — áp dụng English-derived activation-steering vector vào IPD prompt non-English và đo strategy shift kết quả. Kết quả tích cực chuyển representation thành behavior; kết quả tiêu cực buộc ta phải tìm vượt ngoài hub.

P3, drift dưới distillation: một chuỗi distillation được kiểm soát phải cho thấy traits truyền dẫn với độ trung thực cao trong Tiếng Anh nhưng *suy giảm* trong các ngôn ngữ low-resource.

P4, ceiling độ tin cậy đánh giá: multilingual LLM-as-Judge với panel 3-trở-lên judges dị thể, self-translation, và checklist rubrics phải nâng Fleiss' kappa lên trên 0.5. Nếu nó saturates dưới 0.5, công việc định lượng cross-lingual cần adjudication người song ngữ, không phải chỉ aggregation tốt hơn."

---

## Phần 8 — Kết luận

## Slide 19 — Năm điểm cần nhớ
**[17:00 – 17:30]**

"Năm take-away. Ngôn ngữ là biến điều biến chủ động, không phải phương tiện thụ động. Cơ chế là kiến trúc, không phải cultural-essentialist. Hợp tác ở đây là *kế thừa văn hóa*, không phải tiến hóa — với hệ quả WEIRD mà triển khai đa ngôn ngữ làm thành cấp bách. Mâu thuẫn là *informative*, không phải embarrassing — chúng bound claim. Và bốn dự đoán biến tổng hợp thành chương trình nghiên cứu — đóng vòng lặp representation-to-behavior là cấp bách nhất."

## Slide 20 — Vị trí trong machine-behaviour programme
**[17:30 – 17:50]**

"Ngắn gọn, perspective này nằm ở đâu. Chúng em xem nó liên tục với Rahwan về machine behaviour như một discipline, với Han về evolutionary game theory cho hệ multi-agent emergent, với Perc về vật lý thống kê của hợp tác, với Boyd, Richerson và Henrich về tiến hóa văn hóa như truyền dẫn, và với Axelrod cùng Nowak về hợp tác không-thiết-kế. Đóng góp riêng biệt là: xem ngôn ngữ như biến điều biến trong machine ethology, tái định khung 'nicer than human' như kế thừa văn hóa, và cung cấp một chương trình nghiên cứu có thể bác bỏ ngay."

## Slide 21 — Cảm ơn
**[17:50 – 18:00]**

"Các quần thể máy bây giờ đang cung cấp một substrate thực nghiệm mới — *consequential một cách khó chịu* — cho khoa học về hợp tác. Em xin cảm ơn. Em rất mong được thảo luận."

---

## Q&A Dự kiến — câu trả lời ngắn

**Q: Tại sao ưu tiên cách đọc 'kế thừa văn hóa' hơn cách đọc đơn giản hơn 'thống kê corpus → hành vi'?**
"Trên quan điểm của chúng em, chúng là *cùng một cách đọc*. Kế thừa văn hóa *chính là* truyền dẫn pattern hành vi qua thống kê corpus. Sự tái định khung là về phía rhetorical: nó làm các dự đoán thực nghiệm trở nên có thể diễn giải trong cùng vocabulary mà khán giả này đã dùng cho hợp tác ở người."

**Q: Làm sao isolate hiệu ứng ngôn ngữ thuần khỏi entropy tokenisation?**
"Ta không làm được trong một thí nghiệm đơn lẻ. Thiết kế sạch nhất giữ tokenizer constant — byte-level decoding, hoặc một SentencePiece vocabulary chia sẻ — và biến đổi ngôn ngữ prompt. Công trình low-resource-jailbreak của Yong và Bach cung cấp methodology."

**Q: Diplomacy với CICERO chẳng phải đã cho thấy chơi cross-cultural có năng lực rồi sao?**
"Nó cho thấy chơi có năng lực *trong Tiếng Anh*. Theo hiểu biết của chúng em, cùng kiến trúc đó chưa được tái lập đa ngôn ngữ trong điều kiện được kiểm soát. P3 trong agenda của chúng em chính xác là thí nghiệm đó."

**Q: Các mô hình ưu tiên ngôn ngữ như CT-LLM có thực sự so sánh được không, vì recipe pretraining khác nhau?**
"Chúng không hoàn hảo so sánh được. Chúng là *thí nghiệm tự nhiên sạch nhất* hiện ta có. Một nghiên cứu ablation purpose-built sẽ tốt hơn; CT-LLM và TigerLLM là cái đang trên bàn lúc này."

**Q: Khoảng cách ToM có thể chỉ phản ánh leakage benchmark trong Tiếng Nhật vs Tiếng Trung.**
"Có thể. Đó chính xác là quan ngại của Ullman và Sap. Bảo vệ của chúng em: chúng em đọc cross-lingual *differences trên cùng items* như tín hiệu interpretable hơn, bất kể absolute ToM scores. Lập luận về asymmetry robust với tranh cãi construct validity."

**Q: Số governance — 5% per language — feel arbitrary.**
"Đúng vậy. Chúng em đề xuất chúng như điểm khởi đầu cho thảo luận cộng đồng, không phải threshold dựa trên evidence. Đóng góp là *form* của recommendation — annotator composition báo cáo trên mọi model card với dialectal stratification được tài liệu hóa — không phải percentage cụ thể. Cộng đồng có thể hội tụ về số đúng."
