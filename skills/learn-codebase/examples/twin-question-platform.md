# Worked Example — Math Twin-Question Platform MVP1

A real-world walk through Levels 1-3 of the skill, applied to a planning repo whose code lives in a separate repo. This is the common case when working with AI-assisted teams: intent docs are curated in one repo (`item-docs`), code is committed in another (`item-question-core`).

The example uses Korean source quotes from the actual spec and translates the citation pattern. Adapt to any language.

---

## Setup

- **Intent doc:** `docs/001-twin-question-platform/spec.md` (in planning repo `item-docs`)
- **Code repo:** `item-question-core` (Python FastAPI)
- **Feature:** AI metadata auto-tagging + human-confirm workflow for math questions
- **Reader goal:** Understand the candidate→final transition well enough to review an AI-generated PR touching the review API.

---

## Level 1 — Map (5 min)

**Step 1.** Open `spec.md §0 초급자용 5분 요약` only. Ignore everything else for now.

**Step 2.** Extract the central User Story from the spec. The first paragraph names it:

> "AI 가 수학 문항의 메타데이터(과목, 단원, 난이도 등)를 자동으로 뽑아내고, 검수자가 그 결과를 확인해서 승인하는 과정"

> "AI 가 후보를 제시하면, 사람이 최종 확정한다"

**Step 3.** Note the 6-step "한눈에 그림" pipeline (spec.md §0):

```
입력 → 본문 정규화+수식추출 → SymPy 분석 → LLM 메타 태깅(후보) → 자동 검증 → 검수자 검토 → 확정 메타 적재
```

**Step 4.** Locate the entry point. The spec doesn't ship code, so use the contract: `contracts/python-main-api.yaml` names the route `POST /api/questions/{id}/metadata/jobs`. That route handler in the code repo is the entry function.

### Level 1 Output

> AI가 수학 문항의 메타데이터(단원·성취기준·난이도)를 자동 태깅한 뒤 사람이 승인하여 최종 메타로 확정하는 검수 워크플로우. 한 검수자가 한 문항에 대해 후보 → 최종 전이를 만든다. 핵심 분리: **AI는 후보, 사람은 최종**.

`entry: POST /api/questions/{id}/metadata/jobs` (route handler to locate in `item-question-core`)

You can now explain the feature to a teammate in 5 minutes. Stop here unless the task requires more.

---

## Level 2 — Walk (30 min)

Pick the central story. Trace it through the 6-step pipeline. Fill the side-by-side table.

| # | Intent (quote + cite) | Code (file:line :: symbol) | Test / contract | Why this | Why-not (rejected) |
|---|---|---|---|---|---|
| 1 | "검수자가 AI 메타 태깅 job 요청" (spec.md §0 step 3) | `POST /api/questions/{id}/metadata/jobs` route | `contracts/python-main-api.yaml` | Idempotency-Key 헤더 권장 | 검수자 없는 자동 트리거 (MVP3+) |
| 2 | "본문 정규화 + 수식 추출" (spec.md §0 step 1) | `normalizer.py :: normalize_question()` (to locate) | unit test | HWP/이미지/텍스트 다중 입력 일원화 | 입력 그대로 LLM 투입 |
| 3 | "SymPy 분석 (수학 구조 파악)" (spec.md §0 step 2) | `sympy_adapter.py :: analyze()` (to locate) | property test | 수식 의미 추론 안정성 | LLM에 분석 위임 |
| 4 | "LLM 메타 태깅 → 후보 생성" (spec.md §0 step 3) | `llm_pipeline.py :: generate_candidate()` (to locate) | stub: `LLM_PROVIDER=fake` | Structured Outputs로 schema 보장 | 자유 텍스트 응답 파싱 |
| 5 | "자동 검증 (스키마·분류·규칙 확인)" (spec.md §0 step 4) | validator chain (to locate) | `M-VLD-01~09` contracts | 반려 시 3회 자동 재작업 | 1단계 검증만 |
| 6 | "검수자가 후보 검토 → 승인 / 수정 / 반려" (spec.md §0 step 5) | review API (to locate) | candidate→final transition test | 사람이 최종 (책임 추적) | confidence-threshold 자동 승인 |
| 7 | "확정 메타 저장 → DB 적재 완료" (spec.md §0 step 6) | final writer / publish (to locate) | `metadata_phase` 컬럼 검사 | candidate/final 분리 보존 | overwrite |

### Open questions captured during walk

- [ ] `?` row 5: which validator stages fire in which order? — open `M-VLD-01~09` contracts
- [ ] `?` row 6: where does "수정"(edit) save back? new candidate row or in-place? — search `metadata_phase` writes
- [ ] `?` how does `metadata_phase` interact with `4분류 메타 (A/B/C/D)`? — see Clarifications Q2

You can now trace the happy path without re-opening the code. Stop here unless asked to change behavior.

---

## Level 3 — Probe (2 hours)

Read all `Clarifications` sections. Each Q&A becomes a row.

| # | Decision (spec cite) | Enforcing code (to locate) | Protecting test | Rejected alternative |
|---|---|---|---|---|
| D1 | 2단계 검증 (1차 AI / 2차 휴먼). 반려 시 자동 재작업 최대 3회 (Clarifications 2026-05-20 Q1) | validator pipeline | `M-VLD-01~09` | 1단계만 |
| D2 | 4분류 메타 (A 속성·B 콘텐츠·C 서비스·D 운영). MVP1은 A+B+D만 (Q2) | metadata schema modules | `data-model.md` table set | 단일 그룹 메타 |
| D3 | 1차/2차 메타 분리, `metadata_phase` 컬럼 (Q3) | candidate table DDL | migration test | 1회성 단일 메타 |
| D4 | 6 상태 머신 (대기→Draft→검수중→승인→사용중지→폐기). 폐기=soft delete (Q4, R53) | state machine module | state transition test | published/unpublished 이진 |
| D5 | `render_mode` 자동 분류 PRINTABLE / ONLINE_ONLY (Q5, M-ITM-07) | parser auto-detect | render-mode classification test | 운영자 수동 지정 |
| D6 | 4 형식 × 13 유형 정답 모델 (Q6, R6~R26) | answer schema (oneOf) | `contracts/answer-payload.json` | 단일 답안 모델 |
| D7 | 쌍둥이 메타는 MVP1에 컬럼만 예약, 활성화는 MVP2 (Q7) | `twin_group_id` nullable column | `R52` constraint test | MVP1 동시 활성화 |
| D8 | 자동 추천 트리거: 생성 직후 + 운영자 검색 (Q8) | trigger handlers | unit test | 항상 자동 |
| D9 | 셋트 문항 1:N (`set_question_id`, `set_sequence_no`) (Q9, R48~R51) | set model | relation test | 단일 문항 |
| D10 | 그룹문항 ≠ 쌍둥이. `Gx_` 접두 vs `twin_group_id` 분리 (Q10) | distinct columns | constraint test | 동일 묶음 |
| D11 | `question.id` UUID + 표시용 `display_code` (Q11, R-011) | id column dual scheme | `display_code` uniqueness test | 합의된 단일 ID 형식 |
| D12 | MVP1 단일 테넌트 `donga-default`. `owner_tenant_id` 컬럼 예약 (2026-05-14) | column reserved, value pinned | tenant-isolation test | 활성 multi-tenant |
| D13 | 자동 승인 정책 MVP1 OFF (2026-05-14) | `auto_approval_policy` inactive | policy gate test | confidence-threshold ON |
| D14 | OpenAI 호환 + Structured Outputs. `gpt-4o`/`gpt-4o-mini` model_policy (2026-05-14) | `CredentialProvider` + model routing | provider abstraction test | 단일 모델 hardcode |
| D15 | OAuth2 resource server (검수자 role) (2026-05-14) | JWT middleware | auth test | basic auth / session |
| D16 | Python FastAPI 단일 서비스. Spring 모듈 없음 (2026-05-14) | main service repo only | (architectural) | Spring 분리 |
| D17 | Redis Streams는 옵션 queue mode. direct mode가 기본 (2026-05-14) | direct mode default | queue mode 토글 test | Redis 강제 |

### What you can do now

- Predict what changes if D13 flips to ON (autoapprove) — D1 validator confidence threshold becomes load-bearing.
- Predict what breaks if D17 flips to queue-only — direct-mode tests turn red, ai_job lifecycle changes.
- Spot an AI-generated PR that bypasses D6 (single answer model instead of oneOf) — drift.

---

## Lessons from this example

1. **Spec and code in separate repos is normal.** The skill works exactly the same; the `Code` column points to *the other repo's* paths.
2. **Contracts beat hand-written code as Level 2 anchors.** When you can cite `contracts/answer-payload.json` instead of grepping the codebase, do so.
3. **Clarifications are gold for Level 3.** A spec with an active Clarifications log gives you the rejected alternatives for free — that's the most expensive section to reconstruct otherwise.
4. **`?` is a valid row entry.** Mark gaps, don't paper over them. Open questions become the natural agenda for a 1:1 with whoever wrote the spec.
5. **Stop at the level your task needs.** Level 4 was unnecessary for "review one PR touching the review API" — Levels 1-3 covered it.
