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
