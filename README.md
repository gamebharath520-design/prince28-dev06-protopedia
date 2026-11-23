# ProtoPedia

Answers 'what does the RFC actually say' for core internet protocols (HTTP, TLS, DNS, TCP, QUIC), citing section numbers and following obsoleted RFCs to the current one.

**Status:** Day 1 foundation (FastAPI skeleton, quality gates). Live URL from Day 5.

[![CI](https://github.com/gamebharath520-design/prince28-dev06-protopedia/actions/workflows/ci.yml/badge.svg)](https://github.com/gamebharath520-design/prince28-dev06-protopedia/actions/workflows/ci.yml)
[![Live](https://img.shields.io/website?url=https%3A%2F%2Fprotopedia.onrender.com%2Fhealth&label=live)](https://protopedia.onrender.com/docs)
[![Uptime (30 days)](https://img.shields.io/uptimerobot/ratio/YOUR-MONITOR-KEY)](https://protopedia.onrender.com/health)

**Live:** https://protopedia.onrender.com · [API docs](https://protopedia.onrender.com/docs) · [health](https://protopedia.onrender.com/health)


## Who it's for

Junior network engineer at a Chennai telecom equipment company who must answer protocol questions from test teams.

## The problem

1)RFCs are long and often obsoleted or updated by later RFCs. People quote RFC 2616 for HTTP when RFC 9110-9112 replaced it.

2)Developers often use outdated HTTP documentation and misunderstand the differences between HTTP/1.1, HTTP/2, and HTTP/3. This leads to incorrect assumptions about connection handling, multiplexing, and performance.

3)TLS 1.2 and TLS 1.3 have significant differences in handshake mechanisms and security. Developers sometimes follow outdated TLS documentation, resulting in insecure configurations and compatibility issues.

4)TCP specifications have evolved over time, and developers often rely on outdated RFCs when implementing connection establishment, termination, retransmission, and congestion control.

5)Developers sometimes misunderstand HTTP status codes because they rely on incomplete or outdated documentation, leading to incorrect error handling and API responses.

## Data sources

About 400 core RFCs (HTTP 9110-9114, TLS 8446, DNS 1034/1035 and updates, TCP 9293, QUIC 9000-9002) plus errata and the RFC index metadata.

- https://www.rfc-editor.org/
- https://www.rfc-editor.org/rfc-index.xml
- Terms: RFCs may be copied and reproduced with attribution (IETF Trust legal provisions).

## Hardest problem (my interview story)

Obsoletes/updates graph: RFC 2616 was replaced by 7230-7235 and then by 9110-9112. Answers must follow the 'obsoleted by' chain to the current RFC, mention updates, and quote requirement words (MUST/SHOULD) exactly.

## Signature feature

RFC lineage graph: for any answer, see the RFC family tree and which document is current.

## Target metric

Current-RFC citation correct for 95%+ of 50 questions.

## Run it locally

```bash
uv sync
cp .env.example .env   # Windows: copy .env.example .env
uv run uvicorn protopedia.api.main:create_app --factory --reload
```

Then open http://localhost:8000/docs

## Checks

```bash
uv run pytest
uv run ruff check .
```

## Run locally in one command

You need Docker Desktop running. From a fresh clone:

```bash
docker compose up --build
```

This starts Postgres (with pgvector), Redis, runs the migrations and loads the sample data once, then starts the API.

- API docs: http://localhost:8000/docs
- Liveness: http://localhost:8000/health
- Readiness (checks the database): http://localhost:8000/ready

Stop with `Ctrl+C`, then `docker compose down`. Add `-v` to also delete the database volume.

## Develop and test

| Task | Mac / Linux | Windows |
|---|---|---|
| Run the API with reload | `make dev` | `uv run poe dev` |
| Unit tests (no network) | `make test` | `uv run poe test` |
| Integration tests (needs `docker compose up`) | `make test-integration` | `uv run poe test-integration` |
| Coverage report | `make cov` | `uv run poe cov` |
| Lint and format check | `make lint` | `uv run poe lint` |
