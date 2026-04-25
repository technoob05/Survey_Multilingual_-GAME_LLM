# SCRIPT THUYẾT TRÌNH — Under the Shadow of Babel
### Thời lượng ước tính: 15–20 phút

---

## 📌 SLIDE 1: Title Page
**[Mở đầu — giọng tự tin, chào khán giả]**

> Xin chào quý thầy cô và các bạn. Hôm nay tôi sẽ trình bày bài survey mang tên **"Under the Shadow of Babel"** — một bài position survey về ảnh hưởng của ngôn ngữ đối với hành vi chiến lược và khả năng lừa dối trong các trò chơi đa ngôn ngữ của Large Language Models.

---

## 📌 SLIDE 2: Outline
**[Lướt nhanh cấu trúc]**

> Bài trình bày gồm 7 phần chính: Đầu tiên là động lực và giả thuyết trung tâm, sau đó là bằng chứng thực nghiệm qua 7 thể loại trò chơi, tiếp theo là nền tảng cơ chế bên trong mô hình, rồi đến các mối đe dọa mới nổi, vấn đề đánh giá đa ngôn ngữ, đề xuất benchmark, và cuối cùng là kết luận.

---

## 📌 SLIDE 3: The Epistemological Gap
**[Giọng nghiêm túc — đặt vấn đề]**

> LLM ngày nay không còn là những hệ thống hỏi-đáp tĩnh nữa. Chúng đang trở thành **agent tự trị** — đàm phán, lừa dối, hợp tác trong các hệ thống đa agent.
>
> Nhưng đây là vấn đề: **toàn bộ hệ thống an toàn — từ safety guardrails đến RLHF — đều được tối ưu cho tiếng Anh**. Khi chuyển sang môi trường đa ngôn ngữ, tương tác nhiều agent, hệ thống an toàn suy yếu đáng kể.
>
> Kết quả là gì? Một thứ chúng tôi gọi là **"Ảo giác Alignment"** — mô hình trông an toàn khi test bằng tiếng Anh, nhưng hành vi thực sự có thể hoàn toàn khác khi hoạt động trong ngôn ngữ khác.
>
> Câu hỏi trung tâm của chúng tôi: **Ngôn ngữ chỉ đơn thuần là phương tiện truyền tải suy nghĩ, hay nó thực sự định hình lại cách mô hình suy nghĩ?**
>
> Để trả lời câu hỏi này, chúng tôi tổng hợp hơn 80 bài báo, bao phủ 7 thể loại trò chơi, và đặc biệt quan trọng — chúng tôi không chỉ trình bày bằng chứng ủng hộ mà còn **đối mặt nghiêm túc với bằng chứng mâu thuẫn**.

---

## 📌 SLIDE 4: Algorithmic Sapir-Whorf Switch
**[Giọng giải thích — trình bày giả thuyết]**

> Giả thuyết trung tâm của bài survey: chúng tôi gọi nó là **"Công tắc Sapir-Whorf thuật toán"**, dựa trên nghiên cứu của Wang và cộng sự năm 2025.
>
> Ý tưởng cốt lõi là: **ngôn ngữ không phải kênh truyền thụ động** — nó là một **công tắc chủ động** tái cấu hình các biểu diễn nội bộ của mô hình, ảnh hưởng đến ý định chiến lược, Theory of Mind, và cả năng lực lừa dối.
>
> Giả thuyết này được đặt trên hai trụ cột cơ chế:
>
> **Thứ nhất: Semantic Hub Hypothesis** — của Wu và cộng sự 2024. Khi mô hình nhận đầu vào bằng bất kỳ ngôn ngữ nào, nó sẽ **nén có tổn thất** vào một "hub" — một không gian biểu diễn chung nằm ở các lớp giữa, mà hub này **bị chi phối bởi tiếng Anh**. Điều khiển hub này cho ngôn ngữ khác đòi hỏi cường độ cao hơn đáng kể.
>
> **Thứ hai: Translation Barrier Hypothesis** — của Bafna và cộng sự 2025. Đây là điểm thú vị: suy luận bên trong mô hình có thể **đúng hoàn toàn** — nhưng lỗi xảy ra ở "chặng cuối" khi chiếu kết quả ngược về không gian token của ngôn ngữ đích. Nghĩa là một số lỗi là lỗi hiện thực hóa, không phải lỗi suy luận.

---

## 📌 SLIDE 5: Taxonomy Tree
**[Giọng tổng quan — giới thiệu nhanh cấu trúc]**

> Đây là toàn bộ kiến trúc nghiên cứu của chúng tôi dưới dạng sơ đồ cây.
>
> Ở bên trái là **7 thể loại trò chơi** chúng tôi khảo sát: Social Deduction như Werewolf, Negotiation như Diplomacy, Persuasion, Cooperative như Codenames và Hanabi, Open-World như Minecraft, Dialogue Games qua framework clembench, và Social Dilemmas như Prisoner's Dilemma.
>
> Ở giữa là **hai trụ cột cơ chế** — Semantic Hub và Translation Barrier.
>
> Rồi đến **các mối đe dọa** — từ tấn công Code-Switching, AutoRed, Agent-in-the-Middle, đến rủi ro collusion giữa các agent.
>
> Và cuối cùng là **vấn đề đánh giá** — sự sụp đổ của LLM-as-Judge trong ngữ cảnh đa ngôn ngữ.

---

## 📌 SLIDE 6: Striking Findings
**[Giọng hào hứng — chia sẻ phát hiện thú vị]**

> Cho phép tôi chia sẻ những phát hiện nổi bật nhất từ các thể loại trò chơi.
>
> **Phát hiện 1: Lập kế hoạch ≠ Trí thông minh xã hội.** SPIN-Bench cho thấy o3-mini đạt 51% trên bài planning PDDL nhưng hoàn toàn thất bại trong suy luận ý định. Trong khi Claude 3.5 Sonnet làm ngược lại — planning yếu nhưng đoán ý định gần như hoàn hảo. Hai năng lực này **không tỷ lệ thuận** với nhau.
>
> **Phát hiện 2: LLM "tốt bụng hơn con người"!** Trong Prisoner's Dilemma, tỷ lệ hợp tác của LLM lên đến khoảng 80%, so với baseline con người chỉ 48%. Nhưng đừng vội mừng — bên dưới lớp hợp tác này ẩn chứa những hành vi "dark" — collusion bí mật, phân bổ tài nguyên lừa dối.
>
> **Phát hiện 3: Mù văn hóa.** Trong Codenames, clue bằng ngôn ngữ không phải tiếng Anh dựa trên **âm thanh tương tự** thay vì **ý nghĩa khái niệm** — do tokenizer BPE phân mảnh.
>
> **Phát hiện 4:** XToM cho thấy Theory of Mind suy giảm đáng kể khi chuyển từ tiếng Anh sang tiếng Trung — cấu trúc đệ quy "A tin rằng B có ý định..." bị sụp đổ.
>
> **Phát hiện 5:** TCG-Bench cho thấy khoảng cách tiếng Anh–tiếng Ả Rập đạt gần 47% ở quy mô 32B — và đây là điều đáng lo: **khoảng cách ngôn ngữ tăng lên** khi mô hình lớn hơn, chứ không giảm.
>
> **Phát hiện 6:** clembench phân tách rõ: các thất bại đa ngôn ngữ chủ yếu là **cấu trúc** — lỗi format, lặp vòng — chứ không phải lỗi chiến lược.

---

## 📌 SLIDE 7: Contradictory Evidence
**[Giọng trung thực, khiêm tốn — đối mặt với bằng chứng ngược]**

> Tuy nhiên, điều làm bài survey này khác biệt là chúng tôi **không chỉ kể câu chuyện thuận**. Chúng tôi đối mặt nghiêm túc với bằng chứng mâu thuẫn.
>
> **Bất ngờ 1:** Trong IPD, mô hình prompt bằng tiếng Ả Rập **không** defect đồng nhất như dự đoán. Thay vào đó, chúng hiển thị phân phối **bimodal dao động** — 32% hợp tác, 28% phản bội — hoàn toàn không ổn định.
>
> Tiếng Việt thì sao? Mặc dù Việt Nam thường được xem là văn hóa tập thể, mô hình prompt tiếng Việt lại có **tỷ lệ phản bội cao bất ngờ** — đi ngược dự đoán văn hóa.
>
> **Bất ngờ 2:** Và có lẽ gây sốc nhất — một nghiên cứu đối chứng nghiêm ngặt của Arango về quảng cáo từ thiện cho thấy **ngôn ngữ KHÔNG có hiệu ứng đáng kể** lên hành vi thuyết phục con người. Tại sao? Vì **siêu nhận thức** của con người — sự nghi ngờ về nguồn gốc AI — override hoàn toàn thao túng ngôn ngữ.
>
> Kết luận: Những mâu thuẫn này được giải thích tốt nhất bởi **cơ chế kiến trúc**, không phải bởi chủ nghĩa bản chất văn hóa.

---

## 📌 SLIDE 8: Semantic Hub & Translation Barrier
**[Giọng kỹ thuật nhưng dễ hiểu — giải thích cơ chế]**

> Vậy bên trong mô hình thực sự xảy ra gì?
>
> Hãy tưởng tượng một đầu vào bằng tiếng Việt đi qua 4 bước: **Bước 1** — nhận input. **Bước 2** — các lớp giữa nén nó vào một "hub" chung bị chi phối bởi tiếng Anh. **Bước 3** — suy luận chiến lược diễn ra trong hub này. **Bước 4** — kết quả được chiếu ngược về tiếng Việt.
>
> Từ đây có **hai kiểu lỗi**:
>
> **Lỗi Hub** — đầu vào quá tổn thất, suy luận trong hub bị sai. Đây là nguyên nhân của phân phối bimodal tiếng Ả Rập và lỗi toán tiếng Việt.
>
> **Lỗi Barrier** — suy luận đúng nhưng "chặng cuối" chiếu về ngôn ngữ đích thất bại. Đây là nguyên nhân lỗi format trong clembench ở tiếng Đức và tiếng Ý.
>
> Và bảng bên phải cho thấy hậu quả về calibration: **ECE tăng gấp 5 lần** — từ 4.6% ở tiếng Anh lên 23.1% ở ngôn ngữ khác. Mô hình **tự tin sai** trong ngữ cảnh không phải tiếng Anh.
>
> Tin tốt: kỹ thuật LACE — lấy mẫu từ các lớp trung-cuối — có thể phục hồi calibration bằng cách bỏ qua nhiễu ở lớp cuối cùng.

---

## 📌 SLIDE 9: Language as Compound Attack Vector
**[Giọng cảnh báo — nêu rủi ro]**

> Bây giờ đến phần đáng lo ngại: ngôn ngữ có thể bị vũ khí hóa.
>
> **CSRT — Code-Switching Red-Teaming** — của Yoo và cộng sự: trộn ngôn ngữ trong cùng một câu có thể **gần gấp đôi** tỷ lệ tấn công thành công. Với Claude 3 Haiku: 9% ASR so với 2.4% baseline tiếng Anh. Tấn công này khai thác lỗ hổng của Semantic Hub — ở mức **dưới** lớp kiểm tra đầu vào, nghĩa là bộ lọc an toàn không nhận ra.
>
> Hệ sinh thái red-teaming đang mở rộng nhanh chóng: AutoRed dùng RL với persona, OpenRT tạo áp lực đa lượt, Genesis tiến hóa chiến thuật tấn công, M2S kết hợp đa chiến lược.
>
> **Agent-in-the-Middle** — tấn công chặn và thao túng tin nhắn giữa các agent trong hệ thống đa agent. Kết hợp với code-switching, kẻ tấn công có thể thao túng **cả nội dung và ngôn ngữ** — tạo bề mặt tấn công kép.
>
> Và cuối cùng, rủi ro **collusion giấu mặt** — Audit-Whisper đạt 0.819 AUROC để phát hiện, X-SIR giữ vững dưới tấn công xóa watermark đa ngôn ngữ.

---

## 📌 SLIDE 10: The Multilingual Judge Problem
**[Giọng nghiêm trọng — đây là vấn đề cốt lõi]**

> Và đây là điều có thể khiến quý vị bất ngờ nhất: **chính công cụ đánh giá cũng hỏng.**
>
> Fu và cộng sự cho thấy khi dùng một LLM làm judge cho nội dung đa ngôn ngữ, Fleiss' kappa chỉ đạt khoảng 0.3 — **gần như ngẫu nhiên**. Mức "fair to poor agreement".
>
> Nghĩa là nếu bạn chạy benchmark bằng tiếng Ả Rập và dùng GPT-4 làm judge, kết quả **gần như không tin cậy**.
>
> Giải pháp chúng tôi đề xuất — **Ensemble Judging Protocol** gồm 4 bước:
>
> **Một** — Panel ít nhất 3 judge từ các gia đình mô hình khác nhau: GPT-4o, Claude, Gemini.
>
> **Hai** — Self-translation: chuyển transcript sang tiếng Anh trước khi chấm — bước này một mình đã phục hồi khoảng 40% khoảng cách kappa.
>
> **Ba** — Dùng checklist rubric nhị phân thay vì thang Likert — giảm tải nhận thức cho judge.
>
> **Bốn** — Bỏ phiếu có trọng số, cho phép abstention khi confidence thấp.
>
> Kết quả: panel 3-judge cùng checklist rubric đẩy kappa lên trên 0.5 — mức "moderate agreement".

---

## 📌 SLIDE 11: Cross-Cultural Agentic Sandbox
**[Giọng đề xuất — giải pháp cụ thể]**

> Vậy chúng tôi đề xuất gì? Một **Cross-Cultural Agentic Sandbox** — benchmark thế hệ mới.
>
> **Nguyên tắc thiết kế**: Kiểm soát confound — tách biệt tokenizer, RLHF coverage, hyperparameter decoding. Dùng gold standard do con người annotate cho từng ngôn ngữ. Pre-register mọi protocol. Và quan trọng nhất: dùng probe ở lớp trung gian để phân biệt lỗi Hub và lỗi Barrier.
>
> Để benchmark này khả thi, chúng tôi thiết kế **Minimal Viable Benchmark** — phiên bản tối thiểu:
>
> **8 ngôn ngữ**: tiếng Anh là baseline, tiếng Pháp (Romance resource cao), tiếng Ả Rập (hình thái phức tạp, viết phải-sang-trái), tiếng Trung giản thể (logographic), tiếng Việt (tonal, resource thấp), tiếng Swahili (châu Phi, agglutinative), Hindi, và tiếng Thổ Nhĩ Kỳ.
>
> **3 thể loại game**: IPD cho kiểm soát chặt, clembench cho phân tách format/strategy, Codenames cho cultural grounding.
>
> **3 mô hình**: GPT-4o, LLaMA-3-70B, Aya-Expanse.
>
> Tổng ngân sách: **dưới 15 ngàn đô** — bao gồm cả API cost và human annotation.

---

## 📌 SLIDE 12: Key Takeaways
**[Giọng tổng kết, nhấn mạnh]**

> Năm điểm chính tôi muốn quý vị nhớ:
>
> **Một:** Ngôn ngữ điều chỉnh hành vi chiến lược. Nó là biến chủ động, không phải kênh thụ động.
>
> **Hai:** Mâu thuẫn là thông tin. Phân phối bimodal tiếng Ả Rập, tỷ lệ defect bất ngờ của tiếng Việt, và kết quả null về persuasion — tất cả giúp chúng tôi **giới hạn claims** và chỉ về giải thích cơ chế, không phải văn hóa.
>
> **Ba:** Hai kiểu lỗi giải thích toàn bộ phổ. Lỗi Hub ở upstream — suy luận sai. Lỗi Barrier ở downstream — hiện thực hóa sai.
>
> **Bốn:** Đánh giá tiêu chuẩn hỏng rồi. Kappa 0.3 nghĩa là single-judge LLM evaluation trong ngữ cảnh đa ngôn ngữ **không đáng tin cậy**. Ensemble protocol là bắt buộc.
>
> **Năm:** Chúng ta cần sandbox tương tác, đa ngôn ngữ, nhận thức văn hóa — với diagnostic pre-registered, adversary kết hợp, và kiểm soát confound.

---

## 📌 SLIDE 13: Contributions at a Glance
**[Giọng tự tin — tổng kết đóng góp]**

> Về mặt **khái niệm**: chúng tôi đề xuất giả thuyết "Công tắc Sapir-Whorf thuật toán", đây là survey đầu tiên kết hợp bằng chứng hành vi và cơ chế qua 7 thể loại game, và chúng tôi tích hợp trung thực bằng chứng mâu thuẫn.
>
> Về mặt **thực tiễn**: chúng tôi cung cấp **protocol ensemble judging** chi tiết ở Appendix E, **diagnostic protocol pre-registered** để phân biệt Hub và Barrier ở Appendix D, thiết kế **Minimal Viable Benchmark** với chi phí 15 ngàn đô, và **registry tham chiếu** cho khả năng tái tạo ở Appendix G.

---

## 📌 SLIDE 14: Thank You
**[Giọng thân thiện, mở lời mời thảo luận]**

> Xin cảm ơn quý thầy cô và các bạn đã lắng nghe. Toàn bộ code, data, và benchmark registry sẽ được công bố tại link OSF khi paper được chấp nhận.
>
> Tôi rất sẵn lòng nhận câu hỏi và thảo luận. Xin mời!

---

## 📋 GHI CHÚ CHO NGƯỜI THUYẾT TRÌNH

### Thời gian phân bổ gợi ý:
| Phần | Slides | Thời gian |
|------|--------|-----------|
| Mở đầu + Giả thuyết | 1–4 | 4 phút |
| Taxonomy + Findings | 5–7 | 5 phút |
| Cơ chế | 8 | 2 phút |
| Threats | 9 | 2 phút |
| Evaluation + Benchmark | 10–11 | 3 phút |
| Kết luận | 12–14 | 2 phút |
| **Q&A** | — | **2–5 phút** |

### Câu hỏi hay có thể được hỏi:
1. **"Làm sao phân biệt hiệu ứng ngôn ngữ vs confound tokenizer?"** → Trả lời: MVB bao gồm ablation tokenizer + RLHF coverage audit, xem Section 7.
2. **"Self-translation có tạo bias hub-centric không?"** → Trả lời: Có rủi ro, nên chúng tôi đề xuất validate bằng human bilingual adjudication, xem Appendix E.
3. **"Tại sao không chạy experiments mới?"** → Trả lời: Position paper tập trung synthesis + đề xuất framework có thể tái tạo, không claim causal.
4. **"Kappa 0.3 áp dụng cho mọi language pair?"** → Trả lời: Là trung bình; một số pair thấp hơn (AR-EN), một số cao hơn (FR-EN).
