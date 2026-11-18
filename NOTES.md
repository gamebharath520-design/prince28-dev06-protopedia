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
