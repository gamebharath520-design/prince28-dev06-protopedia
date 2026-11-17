# Real user questions: ProtoPedia

Written the way my user types them. User: Junior network engineer at a Chennai telecom equipment company who must answer protocol questions from test teams.

These 10 questions become my first evaluation set in Week 3. Question 6 is not answerable from my documents: the product must say "I don't know".

| # | Question | Type | Where the answer is (document, page) | More than one page? |
|---|---|---|---|---|
| 1 | What does the TLS 1.3 handshake look like according to RFC 8446? | simple | RFC 8446, Section 2 | No |


| 2 | Which RFC defines HTTP semantics today? | simple | RFC 9110, Sections 1.2–1.4 | No |


| 3 | What does RFC 2119 say MUST and SHOULD mean? | simple | RFC 2119, Sections 1 and 3 | No |


| 4 | A device sends an HTTP/1.1 request with both Content-Length and Transfer-Encoding headers. What do the current RFCs say the server must do, and why is it a security risk? | multi-step (several pages) | RFC 9112, Sections 6.2, 6.3 and 11.2 | Yes |


| 5 | Compare connection setup in TCP (RFC 9293) and QUIC (RFC 9000). | comparison | RFC 9293, Section 3.5; RFC 9000, Section 7 | Yes |


| 6 | Why is our office internet slow today? | unanswerable: must reply "I don't know" | none: not in any document | - |


| 7 | If a PUT request times out and I don't receive a response, can I safely send the same request again? | practical / multi-step | RFC 9110, Section 9.2.2 | No |


| 8 | Does HTTP/1.1 open a new TCP connection for every request, or can it reuse the same connection? | simple | RFC 9112, Section 9.3 | No |


| 9 | If a mobile device switches from Wi-Fi to mobile data during a QUIC connection, does the connection have to restart? | practical / multi-step | RFC 9000, Sections 5.1 and 9 | Yes |


| 10 | Can an HTTP/1.1 server process multiple pipelined requests at the same time? What order should it send the responses in? | practical / multi-step | RFC 9112, Section 9.3.2 | No |
