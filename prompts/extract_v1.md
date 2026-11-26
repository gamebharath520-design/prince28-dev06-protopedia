You read one document from ProtoPedia's collection and fill in a small record about it.

What ProtoPedia does: Answers 'what does the RFC actually say' for core internet protocols (HTTP, TLS, DNS, TCP, QUIC), citing section numbers and following obsoleted RFCs to the current one.

Rules:
- Reply with one JSON object and nothing else: no explanation, no Markdown fences.
- Use only what the document says. If it does not say, use null for the year and [] for a list.
- summary: one or two plain sentences, at most 300 characters.
- topics: 1 to 6 short topics.
- Every list holds short values copied from the document, at most 8.

What each field means:
- doc_kind: what kind of document this is.
- year: the year it was published or came into force.
- language: the main language of the text (en, ta, hi or other).
- rfc_number: every "rfc number" this document is mainly about.
- status: every "status" this document is mainly about.
- obsoletes: every "obsoletes" this document is mainly about.
- obsoleted_by: every "obsoleted by" this document is mainly about.
- updates: every "updates" this document is mainly about.
- section: every "section" this document is mainly about.
