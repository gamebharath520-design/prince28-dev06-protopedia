# Dataset: ProtoPedia

Answers 'what does the RFC actually say' for core internet protocols (HTTP, TLS, DNS, TCP, QUIC), citing section numbers and following obsoleted RFCs to the current one.

- **Start target:** 50 RFCs (HTTP + TLS + DNS)
- **Full target:** 400+ RFCs + errata + index metadata (15,000+ pages)
- **Collected by:** `scripts/fetch.py` as `examate-student-bot` (https://github.com/YOUR-GITHUB-USERNAME/prince28-dev06-protopedia): robots.txt respected, at most 4 requests at once, 0.5 s between requests to one site.

## Where the documents come from

- https://www.rfc-editor.org/
- https://www.rfc-editor.org/rfc-index.xml

## Terms I follow

RFCs may be copied and reproduced with attribution (IETF Trust legal provisions).

- Every answer links to the original document.
- No personal data is collected.

<!-- generated:start -->
## Sources (generated 2026-11-23 14:48 UTC by scripts/dataset_report.py)

| Source | Licence / terms | Files | MB | Pages* | How | Fetched | Example URL |
|---|---|---|---|---|---|---|---|
| FastAPI | MIT License | 1697 | 13.2 | 3,333 | git+http @ 05e6df7e90 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/_llm-test.md |
| IETF RFC Editor | IETF Trust Legal Provisions; reproduction with attribution as permitted by the RFC notice | 10 | 3.6 | 548 | http | 2026-11-23 | https://www.rfc-editor.org/rfc/rfc8446.html |

**Total:** 1,707 files, 16.8 MB, 3,881 pages. Not downloaded: 0 blocked by robots.txt, 0 failed.

*Pages = PDF pages, plus one page per 3,000 characters of text or HTML.

## Files (first 200 of 1,707)

The complete list, with a sha256 fingerprint of every file, is `data/manifest.jsonl`.

| # | Title / file | Source | Pages | Fetched | URL |
|---|---|---|---|---|---|
| 1 | docs-e5980895.html | FastAPI | 6 | 2026-11-23 | https://fastapi.tiangolo.com/reference/openapi/docs/ |
| 2 | docs/de/docs/_llm-test.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/_llm-test.md |
| 3 | docs/de/docs/about/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/about/index.md |
| 4 | docs/de/docs/advanced/additional-responses.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/additional-responses.md |
| 5 | docs/de/docs/advanced/additional-status-codes.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/additional-status-codes.md |
| 6 | docs/de/docs/advanced/advanced-dependencies.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/advanced-dependencies.md |
| 7 | docs/de/docs/advanced/advanced-python-types.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/advanced-python-types.md |
| 8 | docs/de/docs/advanced/async-tests.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/async-tests.md |
| 9 | docs/de/docs/advanced/behind-a-proxy.md | FastAPI | 6 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/behind-a-proxy.md |
| 10 | docs/de/docs/advanced/custom-response.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/custom-response.md |
| 11 | docs/de/docs/advanced/dataclasses.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/dataclasses.md |
| 12 | docs/de/docs/advanced/events.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/events.md |
| 13 | docs/de/docs/advanced/generate-clients.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/generate-clients.md |
| 14 | docs/de/docs/advanced/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/index.md |
| 15 | docs/de/docs/advanced/json-base64-bytes.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/json-base64-bytes.md |
| 16 | docs/de/docs/advanced/middleware.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/middleware.md |
| 17 | docs/de/docs/advanced/openapi-callbacks.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/openapi-callbacks.md |
| 18 | docs/de/docs/advanced/openapi-webhooks.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/openapi-webhooks.md |
| 19 | docs/de/docs/advanced/opentelemetry.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/opentelemetry.md |
| 20 | docs/de/docs/advanced/path-operation-advanced-configuration.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/path-operation-advanced-configuration.md |
| 21 | docs/de/docs/advanced/response-change-status-code.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/response-change-status-code.md |
| 22 | docs/de/docs/advanced/response-cookies.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/response-cookies.md |
| 23 | docs/de/docs/advanced/response-directly.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/response-directly.md |
| 24 | docs/de/docs/advanced/response-headers.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/response-headers.md |
| 25 | docs/de/docs/advanced/security/http-basic-auth.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/security/http-basic-auth.md |
| 26 | docs/de/docs/advanced/security/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/security/index.md |
| 27 | docs/de/docs/advanced/security/oauth2-scopes.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/security/oauth2-scopes.md |
| 28 | docs/de/docs/advanced/settings.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/settings.md |
| 29 | docs/de/docs/advanced/stream-data.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/stream-data.md |
| 30 | docs/de/docs/advanced/strict-content-type.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/strict-content-type.md |
| 31 | docs/de/docs/advanced/sub-applications.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/sub-applications.md |
| 32 | docs/de/docs/advanced/templates.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/templates.md |
| 33 | docs/de/docs/advanced/testing-dependencies.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/testing-dependencies.md |
| 34 | docs/de/docs/advanced/testing-events.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/testing-events.md |
| 35 | docs/de/docs/advanced/testing-websockets.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/testing-websockets.md |
| 36 | docs/de/docs/advanced/using-request-directly.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/using-request-directly.md |
| 37 | docs/de/docs/advanced/websockets.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/websockets.md |
| 38 | docs/de/docs/advanced/wsgi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/advanced/wsgi.md |
| 39 | docs/de/docs/agent-banner.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/agent-banner.md |
| 40 | docs/de/docs/ai-development.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/ai-development.md |
| 41 | docs/de/docs/alternatives.md | FastAPI | 9 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/alternatives.md |
| 42 | docs/de/docs/async.md | FastAPI | 9 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/async.md |
| 43 | docs/de/docs/benchmarks.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/benchmarks.md |
| 44 | docs/de/docs/deployment/cloud.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/cloud.md |
| 45 | docs/de/docs/deployment/concepts.md | FastAPI | 7 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/concepts.md |
| 46 | docs/de/docs/deployment/docker.md | FastAPI | 11 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/docker.md |
| 47 | docs/de/docs/deployment/fastapicloud.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/fastapicloud.md |
| 48 | docs/de/docs/deployment/https.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/https.md |
| 49 | docs/de/docs/deployment/index.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/index.md |
| 50 | docs/de/docs/deployment/manually.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/manually.md |
| 51 | docs/de/docs/deployment/server-workers.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/server-workers.md |
| 52 | docs/de/docs/deployment/versions.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/deployment/versions.md |
| 53 | docs/de/docs/editor-support.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/editor-support.md |
| 54 | docs/de/docs/environment-variables.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/environment-variables.md |
| 55 | docs/de/docs/fastapi-cli.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/fastapi-cli.md |
| 56 | docs/de/docs/features.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/features.md |
| 57 | docs/de/docs/help-fastapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/help-fastapi.md |
| 58 | docs/de/docs/history-design-future.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/history-design-future.md |
| 59 | docs/de/docs/how-to/authentication-error-status-code.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/authentication-error-status-code.md |
| 60 | docs/de/docs/how-to/conditional-openapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/conditional-openapi.md |
| 61 | docs/de/docs/how-to/configure-swagger-ui.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/configure-swagger-ui.md |
| 62 | docs/de/docs/how-to/custom-docs-ui-assets.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/custom-docs-ui-assets.md |
| 63 | docs/de/docs/how-to/custom-request-and-route.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/custom-request-and-route.md |
| 64 | docs/de/docs/how-to/extending-openapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/extending-openapi.md |
| 65 | docs/de/docs/how-to/general.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/general.md |
| 66 | docs/de/docs/how-to/graphql.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/graphql.md |
| 67 | docs/de/docs/how-to/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/index.md |
| 68 | docs/de/docs/how-to/migrate-from-pydantic-v1-to-pydantic-v2.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/migrate-from-pydantic-v1-to-pydantic-v2.md |
| 69 | docs/de/docs/how-to/separate-openapi-schemas.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/separate-openapi-schemas.md |
| 70 | docs/de/docs/how-to/testing-database.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/how-to/testing-database.md |
| 71 | docs/de/docs/index.md | FastAPI | 9 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/index.md |
| 72 | docs/de/docs/learn/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/learn/index.md |
| 73 | docs/de/docs/project-generation.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/project-generation.md |
| 74 | docs/de/docs/python-types.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/python-types.md |
| 75 | docs/de/docs/resources/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/resources/index.md |
| 76 | docs/de/docs/translation-banner.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/translation-banner.md |
| 77 | docs/de/docs/tutorial/background-tasks.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/background-tasks.md |
| 78 | docs/de/docs/tutorial/bigger-applications.md | FastAPI | 8 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/bigger-applications.md |
| 79 | docs/de/docs/tutorial/body-fields.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/body-fields.md |
| 80 | docs/de/docs/tutorial/body-multiple-params.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/body-multiple-params.md |
| 81 | docs/de/docs/tutorial/body-nested-models.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/body-nested-models.md |
| 82 | docs/de/docs/tutorial/body-updates.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/body-updates.md |
| 83 | docs/de/docs/tutorial/body.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/body.md |
| 84 | docs/de/docs/tutorial/cookie-param-models.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/cookie-param-models.md |
| 85 | docs/de/docs/tutorial/cookie-params.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/cookie-params.md |
| 86 | docs/de/docs/tutorial/cors.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/cors.md |
| 87 | docs/de/docs/tutorial/debugging.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/debugging.md |
| 88 | docs/de/docs/tutorial/dependencies/classes-as-dependencies.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/classes-as-dependencies.md |
| 89 | docs/de/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md |
| 90 | docs/de/docs/tutorial/dependencies/dependencies-with-yield.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/dependencies-with-yield.md |
| 91 | docs/de/docs/tutorial/dependencies/global-dependencies.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/global-dependencies.md |
| 92 | docs/de/docs/tutorial/dependencies/index.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/index.md |
| 93 | docs/de/docs/tutorial/dependencies/sub-dependencies.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/dependencies/sub-dependencies.md |
| 94 | docs/de/docs/tutorial/encoder.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/encoder.md |
| 95 | docs/de/docs/tutorial/extra-data-types.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/extra-data-types.md |
| 96 | docs/de/docs/tutorial/extra-models.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/extra-models.md |
| 97 | docs/de/docs/tutorial/first-steps.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/first-steps.md |
| 98 | docs/de/docs/tutorial/frontend.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/frontend.md |
| 99 | docs/de/docs/tutorial/handling-errors.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/handling-errors.md |
| 100 | docs/de/docs/tutorial/header-param-models.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/header-param-models.md |
| 101 | docs/de/docs/tutorial/header-params.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/header-params.md |
| 102 | docs/de/docs/tutorial/index.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/index.md |
| 103 | docs/de/docs/tutorial/metadata.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/metadata.md |
| 104 | docs/de/docs/tutorial/middleware.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/middleware.md |
| 105 | docs/de/docs/tutorial/path-operation-configuration.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/path-operation-configuration.md |
| 106 | docs/de/docs/tutorial/path-params-numeric-validations.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/path-params-numeric-validations.md |
| 107 | docs/de/docs/tutorial/path-params.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/path-params.md |
| 108 | docs/de/docs/tutorial/query-param-models.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/query-param-models.md |
| 109 | docs/de/docs/tutorial/query-params-str-validations.md | FastAPI | 6 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/query-params-str-validations.md |
| 110 | docs/de/docs/tutorial/query-params.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/query-params.md |
| 111 | docs/de/docs/tutorial/request-files.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/request-files.md |
| 112 | docs/de/docs/tutorial/request-form-models.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/request-form-models.md |
| 113 | docs/de/docs/tutorial/request-forms-and-files.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/request-forms-and-files.md |
| 114 | docs/de/docs/tutorial/request-forms.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/request-forms.md |
| 115 | docs/de/docs/tutorial/response-model.md | FastAPI | 6 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/response-model.md |
| 116 | docs/de/docs/tutorial/response-status-code.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/response-status-code.md |
| 117 | docs/de/docs/tutorial/schema-extra-example.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/schema-extra-example.md |
| 118 | docs/de/docs/tutorial/security/first-steps.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/security/first-steps.md |
| 119 | docs/de/docs/tutorial/security/get-current-user.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/security/get-current-user.md |
| 120 | docs/de/docs/tutorial/security/index.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/security/index.md |
| 121 | docs/de/docs/tutorial/security/oauth2-jwt.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/security/oauth2-jwt.md |
| 122 | docs/de/docs/tutorial/security/simple-oauth2.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/security/simple-oauth2.md |
| 123 | docs/de/docs/tutorial/server-sent-events.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/server-sent-events.md |
| 124 | docs/de/docs/tutorial/sql-databases.md | FastAPI | 6 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/sql-databases.md |
| 125 | docs/de/docs/tutorial/static-files.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/static-files.md |
| 126 | docs/de/docs/tutorial/stream-json-lines.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/stream-json-lines.md |
| 127 | docs/de/docs/tutorial/testing.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/tutorial/testing.md |
| 128 | docs/de/docs/virtual-environments.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/docs/virtual-environments.md |
| 129 | docs/de/llm-prompt.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/de/llm-prompt.md |
| 130 | docs/en/docs/_llm-test.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/_llm-test.md |
| 131 | docs/en/docs/about/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/about/index.md |
| 132 | docs/en/docs/advanced/additional-responses.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/additional-responses.md |
| 133 | docs/en/docs/advanced/additional-status-codes.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/additional-status-codes.md |
| 134 | docs/en/docs/advanced/advanced-dependencies.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/advanced-dependencies.md |
| 135 | docs/en/docs/advanced/advanced-python-types.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/advanced-python-types.md |
| 136 | docs/en/docs/advanced/async-tests.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/async-tests.md |
| 137 | docs/en/docs/advanced/behind-a-proxy.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/behind-a-proxy.md |
| 138 | docs/en/docs/advanced/custom-response.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/custom-response.md |
| 139 | docs/en/docs/advanced/dataclasses.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/dataclasses.md |
| 140 | docs/en/docs/advanced/events.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/events.md |
| 141 | docs/en/docs/advanced/generate-clients.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/generate-clients.md |
| 142 | docs/en/docs/advanced/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/index.md |
| 143 | docs/en/docs/advanced/json-base64-bytes.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/json-base64-bytes.md |
| 144 | docs/en/docs/advanced/middleware.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/middleware.md |
| 145 | docs/en/docs/advanced/openapi-callbacks.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/openapi-callbacks.md |
| 146 | docs/en/docs/advanced/openapi-webhooks.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/openapi-webhooks.md |
| 147 | docs/en/docs/advanced/opentelemetry.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/opentelemetry.md |
| 148 | docs/en/docs/advanced/path-operation-advanced-configuration.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/path-operation-advanced-configuration.md |
| 149 | docs/en/docs/advanced/request-body-limits.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/request-body-limits.md |
| 150 | docs/en/docs/advanced/response-change-status-code.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/response-change-status-code.md |
| 151 | docs/en/docs/advanced/response-cookies.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/response-cookies.md |
| 152 | docs/en/docs/advanced/response-directly.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/response-directly.md |
| 153 | docs/en/docs/advanced/response-headers.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/response-headers.md |
| 154 | docs/en/docs/advanced/security/http-basic-auth.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/security/http-basic-auth.md |
| 155 | docs/en/docs/advanced/security/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/security/index.md |
| 156 | docs/en/docs/advanced/security/oauth2-scopes.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/security/oauth2-scopes.md |
| 157 | docs/en/docs/advanced/settings.md | FastAPI | 4 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/settings.md |
| 158 | docs/en/docs/advanced/stream-data.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/stream-data.md |
| 159 | docs/en/docs/advanced/strict-content-type.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/strict-content-type.md |
| 160 | docs/en/docs/advanced/sub-applications.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/sub-applications.md |
| 161 | docs/en/docs/advanced/templates.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/templates.md |
| 162 | docs/en/docs/advanced/testing-dependencies.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/testing-dependencies.md |
| 163 | docs/en/docs/advanced/testing-events.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/testing-events.md |
| 164 | docs/en/docs/advanced/testing-websockets.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/testing-websockets.md |
| 165 | docs/en/docs/advanced/using-request-directly.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/using-request-directly.md |
| 166 | docs/en/docs/advanced/websockets.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/websockets.md |
| 167 | docs/en/docs/advanced/wsgi.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/advanced/wsgi.md |
| 168 | docs/en/docs/agent-banner.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/agent-banner.md |
| 169 | docs/en/docs/ai-development.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/ai-development.md |
| 170 | docs/en/docs/alternatives.md | FastAPI | 8 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/alternatives.md |
| 171 | docs/en/docs/async.md | FastAPI | 8 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/async.md |
| 172 | docs/en/docs/benchmarks.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/benchmarks.md |
| 173 | docs/en/docs/contributing.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/contributing.md |
| 174 | docs/en/docs/deployment/cloud.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/cloud.md |
| 175 | docs/en/docs/deployment/concepts.md | FastAPI | 6 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/concepts.md |
| 176 | docs/en/docs/deployment/docker.md | FastAPI | 10 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/docker.md |
| 177 | docs/en/docs/deployment/fastapicloud.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/fastapicloud.md |
| 178 | docs/en/docs/deployment/https.md | FastAPI | 5 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/https.md |
| 179 | docs/en/docs/deployment/index.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/index.md |
| 180 | docs/en/docs/deployment/manually.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/manually.md |
| 181 | docs/en/docs/deployment/server-workers.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/server-workers.md |
| 182 | docs/en/docs/deployment/versions.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/deployment/versions.md |
| 183 | docs/en/docs/editor-support.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/editor-support.md |
| 184 | docs/en/docs/environment-variables.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/environment-variables.md |
| 185 | docs/en/docs/external-links.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/external-links.md |
| 186 | docs/en/docs/fastapi-cli.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/fastapi-cli.md |
| 187 | docs/en/docs/fastapi-people.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/fastapi-people.md |
| 188 | docs/en/docs/features.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/features.md |
| 189 | docs/en/docs/help-fastapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/help-fastapi.md |
| 190 | docs/en/docs/history-design-future.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/history-design-future.md |
| 191 | docs/en/docs/how-to/authentication-error-status-code.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/authentication-error-status-code.md |
| 192 | docs/en/docs/how-to/conditional-openapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/conditional-openapi.md |
| 193 | docs/en/docs/how-to/configure-swagger-ui.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/configure-swagger-ui.md |
| 194 | docs/en/docs/how-to/custom-docs-ui-assets.md | FastAPI | 3 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/custom-docs-ui-assets.md |
| 195 | docs/en/docs/how-to/custom-request-and-route.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/custom-request-and-route.md |
| 196 | docs/en/docs/how-to/extending-openapi.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/extending-openapi.md |
| 197 | docs/en/docs/how-to/general.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/general.md |
| 198 | docs/en/docs/how-to/graphql.md | FastAPI | 1 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/graphql.md |
| 199 | docs/en/docs/how-to/index.md | FastAPI |  | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/index.md |
| 200 | docs/en/docs/how-to/migrate-from-pydantic-v1-to-pydantic-v2.md | FastAPI | 2 | 2026-11-23 | https://github.com/fastapi/fastapi/blob/HEAD/docs/en/docs/how-to/migrate-from-pydantic-v1-to-pydantic-v2.md |
<!-- generated:end -->

## Known gaps

- (what is still missing from the start target, and why)
