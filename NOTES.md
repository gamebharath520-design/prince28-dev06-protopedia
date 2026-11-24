# Engineering notes: ProtoPedia

## D03 · PostgreSQL

### Migrations (upgrade, downgrade, upgrade)

```text
paste the output of:
uv run alembic downgrade -1
    INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    INFO  [alembic.runtime.migration] Running downgrade 98e811f6823d -> 1c3f3884756f, add gin index on metad

run alembic current
    INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    1c3f3884756f

uv run alembic upgrade head
    INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade 1c3f3884756f -> 98e811f6823d, add gin index on metadat

uv run alembic history
    1c3f3884756f -> 98e811f6823d (head), add gin index on metadata
    <base> -> 1c3f3884756f, create documents and pages
```

### The loader is idempotent

```text
run 1: records=20 inserted=20 updated=0 unchanged=0
run 2: records=20 inserted=0 updated=0 unchanged=20
run 3 (after editing one record): records=20 inserted=0 updated=1 unchanged=19
```

### EXPLAIN for ?rfc_number=VALUE

```text
paste the output of: uv run python scripts/explain.py rfc_number VALUE

-- 1) What the planner chooses on its own:
Seq Scan on documents  (cost=0.00..11.00 rows=1 width=36) (actual time=0.019..0.019 rows=0.00 loops=1)
  Filter: (metadata @> '{"rfc_number": "VALUE"}'::jsonb)
  Rows Removed by Filter: 21
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=147 read=2
Planning Time: 1.787 ms
Execution Time: 0.046 ms

-- 2) Seq scan switched off, to prove the index can be used:
Bitmap Heap Scan on documents  (cost=12.81..16.82 rows=1 width=36) (actual time=1.879..1.880 rows=0.00 loops=1)
  Recheck Cond: (metadata @> '{"rfc_number": "VALUE"}'::jsonb)
  Buffers: shared hit=1 read=2
  ->  Bitmap Index Scan on ix_documents_metadata_gin  (cost=0.00..12.81 rows=1 width=0) (actual time=1.851..1.851 rows=0.00 loops=1)
        Index Cond: (metadata @> '{"rfc_number": "VALUE"}'::jsonb)
        Index Searches: 1
        Buffers: shared hit=1 read=2
Planning:
  Buffers: shared hit=1
Planning Time: 0.076 ms
Execution Time: 1.932 ms

```

Why did the planner choose a Seq Scan on my table? (2 lines, your own words)

    The planner chose a Seq Scan because my table has only 21 records, making it faster to check all rows directly.
    Using the GIN index would add extra overhead, so PostgreSQL estimated that a full table scan was cheaper.


When would it switch to the GIN index? (1 line)

    PostgreSQL may switch to the GIN index when the table grows and the query matches fewer rows, making an index scan cheaper than a full table scan.


## D04 · Docker, Compose and tests

### The image

```text
paste the output of: docker images protopedia:dev

    IMAGE            ID             DISK USAGE   CONTENT SIZE   EXTRA
    protopedia:dev   b4a7e070ec93        300MB           70MB

paste the output of: docker run --rm protopedia:dev id

    uid=999(app) gid=999(app) groups=999(app)

```

- Size: 378 MB (target: under 400 MB)
- First build: 110 s. After changing one line of code: 30.3 s.
- Which step said CACHED, and why? (1 line, your own words)
    The uv sync --locked --no-install-project step was cached because changing only application code doesn't change uv.lock or dependencies.

### The stack

```text
paste the output of: docker compose ps -a

    NAME                   IMAGE                    COMMAND                  SERVICE   CREATED          STATUS      PORTS
    protopedia-api-1       protopedia-api           "sh -c 'exec uvicorn…"   api       47 minutes ago   Up 47 minutes (healthy)     0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp
    protopedia-db-1        pgvector/pgvector:pg17   "docker-entrypoint.s…"   db        47 minutes ago   Up 47 minutes (healthy)     0.0.0.0:5433->5432/tcp, [::]:5433->5432/tcp
    protopedia-migrate-1   protopedia-migrate       "sh -c 'alembic upgr…"   migrate   47 minutes ago   Exited (0) 29 minutesago
    protopedia-redis-1     redis:7-alpine           "docker-entrypoint.s…"   redis     47 minutes ago   Up 47 minutes (healthy)     0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp

paste the last line of: docker compose logs migrate   (first up, then after down + up)

migrate-1  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
migrate-1  | records=20 inserted=0 updated=0 unchanged=20

migrate-1  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
migrate-1  | records=20 inserted=0 updated=0 unchanged=20
```

### Breaking the database on purpose

```text
db stopped:  /health → paste {"status":"ok","app":"protopedia","env":"local"}
db stopped:  /ready  → paste {"status":"not_ready","checks":{"database":false}}
db started:  /ready  → paste {"status":"ready","checks":{"database":true}}
```

Why should a load balancer stop sending traffic here but not restart the app? (2 lines)

    A load balancer should stop sending traffic because the app cannot serve requests when the database is unavailable.
    It shouldn't restart the app because the app itself is healthy; only its database dependency is temporarily unavailable.

### Tests and coverage

```text
uv run poe test              → paste the last line      16 passed in 0.30s
uv run poe test-integration  → paste the last line      7 passed in 2.90s
coverage TOTAL, unit only    → paste                    83%
coverage TOTAL, with integration tests → paste          92%
```

Two files or lines my coverage report says are never run, and whether they matter: (2 lines)
    Two examples are scripts/explain.py and scripts/load_db.py, which may have some lines that are not covered by tests.
    They are not necessarily problems because some lines are utility or command-line code that may not be exercised by unit tests.


## D05 · CI/CD and going live

- Live URL: (https://protopedia.onrender.com)
- CI run for pull request 1: https://github.com/gamebharath520-design/prince28-dev06-protopedia/actions ((https://github.com/gamebharath520-design/prince28-dev06-protopedia/actions/runs/44707428857))
- First deploy that ran by itself: (https://github.com/gamebharath520-design/prince28-dev06-protopedia/actions/runs/44699608427)
- Merge clicked at 10:46 → "Smoke test passed" at 10:48 → lead time:  1m 18s


### Smoke test output from that CD run

```text
ok   /health -> 200
ok   /ready -> 200 {'status': 'ready', 'checks': {'database': True}}
ok   /v1/documents?limit=1 -> 200
Smoke test passed
```

### Rollback drill

- Rolled back to sha 524dca931fbf5ad482ea554db046c38d348b5898: started 15.6s, smoke passed 15.8s ([calculate] min)
- Rolled forward to sha 524dca931fbf5ad482ea554db046c38d348b5898 15.8s
- During rollback, the database stayed on the newer schema because the rollback redeployed an older application image without reversing database migrations. This is safe as long as the older application remains compatible with the newer database schema.

### Where my secrets live

- Neon string: GitHub Secret `DATABASE_URL` + Render environment. Not in Git, not in the image.
- Render deploy hook: GitHub Secret `RENDER_DEPLOY_HOOK` only.

### Monitoring

- UptimeRobot checks `/health` every 5 minutes; alerts go to my email.
- One thing that would make my live app faster on its first request: Keeping the Render service warm with regular health checks helps avoid cold-start delays on the free instance.



## D06 · Collecting the corpus

- **Start target:** 50 RFCs (HTTP + TLS + DNS)
- **Collected today:** 1,707 files, 3,881 pages, 16.8 MB
- **Doors used:** URL list / Git repository / sitemap

### Licence check

| Source | Licence or terms, in my words | May I show full text in answers? |
|---|---|---|
| IETF RFC Editor | IETF Trust Legal Provisions allow RFC reproduction with attribution, subject to their terms. | Yes, where permitted by the applicable IETF terms; include attribution and link to the original. |
| FastAPI GitHub repository | MIT License; reuse, modification and distribution are permitted while preserving the copyright and licence notice. | Yes, while complying with the MIT licence and retaining the required notices. |

### robots.txt

- **Site:** `https://www.rfc-editor.org/` and `https://fastapi.tiangolo.com/`
- **Its robots.txt says:** I used the downloader's robots.txt checking, but I did not record the exact robots.txt rules in my terminal log.
- **Was anything blocked for my bot?** No. The final dataset report shows 0 blocked files. I respected the downloader's robots.txt checks.

### Kill and resume

- **Run 1:** I pressed Ctrl+C after 4 files had downloaded.
- **Run 2:** downloaded=5, skipped=5.
- **Run 3:** downloaded=0, skipped=10.

### Capacity (from docs/CAPACITY.md)

- **Tokens per page, measured:** 750 tokens.
- **Full corpus:** 11.25 M tokens, 32,344 chunks, embedding about Rs 184, vectors 99 MB.

### The number that surprised me most, and why

The collected corpus contains 1,707 files and 3,881 pages, but the full target is estimated to need 11.25 million tokens.
Even a relatively small corpus can require significant storage and embedding resources when scaled up.

### One thing that went wrong today, and how I fixed it

Initially, I used placeholder repository and sitemap URLs (`OWNER/REPO` and `SITE`), which caused repository-not-found and DNS errors.
I fixed this by using the actual FastAPI GitHub repository and its sitemap URL. The Git repository added 1,696 files, and the sitemap added one URL that I downloaded successfully.

## D07 · Parser comparison

<!-- parsers:start -->
| File | Parsers (A / B) | Pages | A found | B found | Time (A / B) | Better, why |
|---|---|---|---|---|---|---|
| rfc9110-b1b13a12.html | trafilatura / strip tags | 2 | 5,598 chars, 4 headings, 0 tables | 455,192 chars, 0 headings, 0 tables | 2.71 s / 0.17 s | |
| rfc9000-46f5fb09.html | trafilatura / strip tags | 112 | 312,604 chars, 0 headings, 15 tables | 368,012 chars, 0 headings, 0 tables | 0.97 s / 0.10 s | |
| rfc9293-cf23f6ee.html | trafilatura / strip tags | 48 | 135,005 chars, 0 headings, 17 tables | 203,811 chars, 0 headings, 0 tables | 0.57 s / 0.06 s | |
| rfc9421-a721bf52.html | trafilatura / strip tags | 59 | 160,190 chars, 0 headings, 11 tables | 220,381 chars, 0 headings, 0 tables | 0.51 s / 0.06 s | |
| rfc9113-31239d03.html | trafilatura / strip tags | 48 | 130,304 chars, 0 headings, 1 tables | 177,098 chars, 0 headings, 0 tables | 0.58 s / 0.06 s | |
| rfc8446-e28608fb.html | trafilatura / strip tags | 147 | 275,625 chars, 0 headings, 0 tables | 286,997 chars, 0 headings, 0 tables | 0.26 s / 0.07 s | |
| rfc5280-7e022b9f.html | trafilatura / strip tags | 146 | 287,019 chars, 0 headings, 0 tables | 301,515 chars, 0 headings, 0 tables | 0.42 s / 0.07 s | |
| rfc9114-6e32398e.html | trafilatura / strip tags | 42 | 116,397 chars, 0 headings, 11 tables | 138,216 chars, 0 headings, 0 tables | 0.45 s / 0.04 s | |
| rfc7231-8f8a36c6.html | trafilatura / strip tags | 97 | 201,853 chars, 0 headings, 0 tables | 212,815 chars, 0 headings, 0 tables | 0.19 s / 0.05 s | |
| rfc9112-8ea310bd.html | trafilatura / strip tags | 29 | 80,055 chars, 0 headings, 5 tables | 101,231 chars, 0 headings, 0 tables | 0.29 s / 0.03 s | |
<!-- parsers:end -->

### D07 · Parsing my corpus

- Files in the manifest: 53 · parsed: 53 · failed: 0 · pages in Postgres: 1,099 (confirm total pages in DB if 19 files were already parsed earlier)
- Parsing coverage: 100% of files (53 / 53)

### Failures by reason

| Reason | Files | What I did |
|---|---|---|
| None (0 failures) | 0 | Verified all 53 files parsed and confirmed `uv run python scripts/parse_corpus.py --retry-failed` had no failed rows to retry; noted `0 failures out of 53 files` in NOTES.md. |

- The one I fixed: file N/A (0 failures) , reason N/A , fix: N/A — ran `--retry-failed` to confirm no failed rows remained

### What I saw when I read my parsed pages

- A page where the heading path is right (document, page, path): rfc9110-b1b13a12.html, page 1, [fill exact heading path from DB/output]
- Something that came out wrong (document, page, what): rfc9110-b1b13a12.html — trafilatura extracted 5,598 chars vs. 455,192 chars with plain tag-stripping (or note specific page/heading/text issue found when reading parsed pages)
- A table: Markdown grid or loose text? (document, page): rfc9293-cf23f6ee.html (17 tables detected by trafilatura) — [fill page number and whether Markdown grid or loose text]

### My parser choice

- For PDFs I use PyMuPDF because:
  1. It is the primary PDF parser in our pipeline when comparing against pypdf.
  2. [Add exact page/char count and runtime in seconds from running `compare_parsers.py` on sample PDFs, as the default 10-file run only compared HTML RFCs]
- A kind of document in my corpus that neither parser handles well: Complex multi-column layouts, dense tables, or HTML pages where trafilatura trims aggressively while plain tag-stripping retains boilerplate.

### One thing that went wrong today, and how I fixed it

`uv run poe lint` failed on `ruff format --check .` because `src\protopedia\db\models.py` (around line 82) was unformatted. I ran `uv run ruff format .` to format that file (leaving 43 other files unchanged) and re-ran `uv run poe lint`, which passed with all 52 unit tests and all 44 files formatted.
