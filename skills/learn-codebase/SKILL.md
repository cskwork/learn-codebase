---
name: learn-codebase
description: Intent-anchored code reading. Use when learning unfamiliar code, reviewing an AI-written PR, planning a change whose blast radius is unknown, or checking spec ↔ code drift.
---

# learn-codebase — Intent-Anchored Reading

## Overview

To understand code another agent wrote, anchor every read on the intent that justifies it. Read intent and code as **paired columns**, never in sequence.

Code without intent = ritual mimicry (you copy the shape but can't extend it).
Intent without code = aspiration (theory you can't ship).
Side-by-side = bidirectional traceability you can act on.

## Response Language Rule — applies to ALL outputs

Match the user's language. If the user writes in Korean or the repo/team context is Korean, produce the learn-codebase response in Korean by default while preserving code identifiers, file paths, API names, SQL, and exact error text.

Use natural Korean product/engineering terms instead of untranslated workflow labels:

- `happy path` → `정상 흐름` or `기본 성공 흐름`
- `If you only read one thing` → `하나만 읽는다면`
- `next options` / `menu` → `다음 선택지`
- `TL;DR` → `핵심 요약`
- `Level` / `Stage` output labels → `단계` / `기본 응답`
- `Map` / `Walk` / `Probe` / `Master` output labels → `지도` / `흐름 추적` / `판단 근거 점검` / `규칙 지도`
- `trace` → `흐름 추적`
- `entry` → `진입점`
- `exit` → `종료 지점`
- `error path` → `오류 흐름`

Do not output English section labels such as `Level 1 Map` or `Happy Path` for Korean users unless the user explicitly asks for English.

## Plain-Speech Rule (Feynman Mode) — applies to ALL outputs

If a non-technical teammate cannot follow your output, the skill failed. Every artifact this skill produces (Map, Walk, Probe, Master) MUST pass `templates/plain-speech-checklist.md` before you ship it.

The five rules (memorize):

1. **Lead with an everyday analogy or one-line plain summary** before any jargon. Example — not "MVP2 generates twin candidates via 5-validator pipeline" but "MVP2 = 'make 3 lookalike math problems from 1 original, then a human picks the good ones'."
2. **Expand every identifier the first time it appears, in parentheses.** `FR-001` → `FR-001 (Functional Requirement 1, "what the system must do" rule #1)`. `twin_group` → `twin_group (a folder that holds the original problem and its lookalikes together)`. Do this even inside tables.
3. **Translate the why before the what.** Each row/section opens with one short clause on *why a normal person would care*, then technical detail.
4. **No naked acronyms, no naked code paths.** `idempotency_key` → `idempotency_key (a label that says "if you press send twice, only count once")`. `POST /api/.../approve` → `approve API (the button a reviewer clicks to say "yes, ship this candidate as a real problem")`.
5. **Close with a 1-minute summary block** titled in the response language, e.g. Korean `하나만 읽는다면` or English `If you only read one thing` — 3 sentences max, zero jargon. If you cannot write those 3 sentences, you do not yet understand the thing.

Anti-pattern to avoid: "intent-anchored bidirectional traceability matrix between FR-009 and the materialization transaction." Rewrite as: "Did the spec say 'make a group on first approval'? Yes (FR-009). Where does the code do it? Step 9 of the approve flow. Who proves it works? The integration test that approves a candidate and checks the group exists."

Test your output by asking: *Could my parent, or a junior who joined yesterday, retell the gist?* If no, simplify.

## Bite-Size Delivery Rule — also applies to ALL outputs

If the reader has to scroll more than one screen to find the next decision they care about, the skill failed. Pair every output with **stage delivery**: ship the smallest useful chunk first, then wait for the reader to ask for more.

The five rules (memorize):

1. **One response = one chunk.** Default chunk size = a 30-second TL;DR (≤3 sentences) plus *one* anchored citation. Never dump multiple Levels in a single response unless the user explicitly says "전부 한 번에" / "give me everything".
2. **TL;DR first, every time.** Even within a single Level's output, the first 3 lines must be the conclusion a reader could act on without reading the rest. Detail follows the TL;DR; never precedes it.
3. **End every chunk with a response-language "next options" menu — 2 to 4 choices, max.** Korean example: "다음 선택지: (A) 진입점 코드 한 함수만, (B) 데이터 흐름 다이어그램, (C) 의심 라인 핀포인트, (D) 종료". Make options concrete, name an artifact each one produces, and never make the user guess what's behind option B.
4. **Cap chunk size by surface.** Per chunk: ≤5 headings, ≤8 table rows, ≤1 fenced code block ≤30 lines. If you need more, split with a response-language label such as Korean `N부 중 1부` or English `Part 1 of N`, with the menu pointing to the next part.
5. **Park the rest, don't summarize it.** When you split, do not write "and there are 14 more rows below" — write "remaining 14 rows live behind option (A): say 'A' to load". Summaries of unread content waste the reader's attention.

Anti-pattern to avoid: a single response containing Level 1 + Level 2 table + Level 3 decision matrix + a "what to do next" appendix. Rewrite as: Level 1 TL;DR in response #1, the user picks (A) Walk or (B) Probe in response #2, only that one expands.

Test your output by asking: *Can a reader who only reads my first 3 lines and the menu still make the right next move?* If no, the TL;DR is too vague or the menu is missing.

### Red flags — stop and rewrite (bite-size)

| Thought | What it really means | Fix |
|---|---|---|
| "The reader will scroll to find what they need." | They will not. They will leave. | Hoist the one thing they need into the top 3 lines. |
| "I'll dump everything so they have it." | You have replaced their judgment with your dump. | Park detail behind a menu option, ship the TL;DR. |
| "The next options menu is obvious." | If it were obvious, you'd have written it already. Write it. | Write 2–4 concrete option labels with the artifact each yields. |
| "Splitting feels less helpful." | Splitting is the help. One chunk = one decision. | Ship the chunk; trust the menu to deliver the rest. |
| "It's only 12 rows over the cap." | Caps exist because attention is finite, not because 12 is magic. | Split at the cap, link the rest. |

### Red flags — stop and rewrite (plain-speech)

If you catch yourself thinking any of these while drafting an output, the Plain-Speech Rule is about to be violated. Stop, simplify, then resume.

| Thought | What it really means | Fix |
|---|---|---|
| "The reader will know what FR-XXX means." | You skipped rule 2 (expand on first use). | Add `(Functional Requirement N — …)` inline. |
| "The analogy is cheesy." | You skipped rule 1 because it felt undignified. | Ship the analogy anyway. Dignity is not the goal; understanding is. |
| "The summary is too obvious." | The summary is correct. Ship it. | Keep it. Obvious-to-you ≠ obvious-to-reader. |
| "Adding the why-clause makes the row long." | You skipped rule 3 to save vertical space. | Long rows beat unread rows. |
| "I'll explain the term in the conclusion." | The reader has already given up by the conclusion. | Expand on first use, always. |
| "Three sentences isn't enough to be accurate." | You're conflating accuracy with completeness. | The 1-minute summary is a hook, not the whole truth. Ship it. |

## When to Use

Symptoms that mean *use this skill*:

- "AI shipped this PR last week and I have no idea what it does."
- "There's a 40-page spec and a 100-file repo. Where do I even start?"
- "I need to onboard a junior dev to one feature, not the whole product."
- "Did the implementation actually match what we asked for?"
- "I need to change behavior X but I'm scared of what depends on it."

When **not** to use:
- No intent docs exist at all → write one first, or use a discovery skill to reverse-engineer one before applying this skill.
- One-file utility or trivial change → just read it.

## The Core Move

For every code chunk you read, find the intent that justifies it. Record both in a side-by-side row. Cite both. If you cannot fill a row, you do not yet understand that code.

Each row needs a **plain-language "What this means" cell** — one sentence a non-expert understands — *in addition to* the citation cells. Identifiers alone are not enough.

```
| What this means (plain)                                | Intent (cite)                                  | Code (file:line)            | Test/Contract       | Why-not (rejected)                    |
| ------------------------------------------------------ | ---------------------------------------------- | --------------------------- | ------------------- | ------------------------------------- |
| The AI suggests, a human approves — never the reverse. | spec.md§"MVP2 원칙": AI는 후보, 사람은 최종    | submit_review() review.py:42 | test_review.py::T1 | auto-approve on confidence (rejected, Q1: false-positive risk) |
```

A row with empty cells is a probe target, not a problem. Add `?` and revisit. A row whose "What this means" cell uses jargon is **not done** — rewrite until your parent could read it.

## Two Reading Directions

| Direction | Start | Used for |
|---|---|---|
| **Forward (spec→code)** | open `spec.md` §0 | onboarding, learning, change planning |
| **Reverse (code→spec)** | open the entry function | reviewing AI output, recovering lost intent |

Forward is the default. Use Reverse when spec is sparse, drifted, or absent.

## The 4 Levels

Stop at the level your task actually needs. Going deeper is not virtue.

> **All Level outputs MUST start with an everyday analogy + close with a 1-minute summary block.** This is non-negotiable — see Plain-Speech Rule.
>
> **Default delivery is TL;DR-first, one Level per response, with a next-options menu at the end.** Do not chain Levels in a single message unless the user explicitly asks for it — see Bite-Size Delivery Rule.

Each Level below ships in 3 stages — A (TL;DR), B (full artifact on request), C (linked deep dives). Stage A is the default response; B and C only fire when the menu picks them.

### Level 1 — Map (≤5 min, beginner)
Goal: one paragraph + one entry function.
1. Read only the §0 / overview / README of the canonical intent doc.
2. Identify the **one** user story most central to the feature.
3. Locate **one** entry point in code (route handler, CLI command, top-level fn).
- **Stage A (default)**: analogy line + 3-line plain summary + `entry: <file:line>` + menu. Korean example: "(A) 정상 흐름 추적  (B) 의심 버그 라인 보기  (C) 종료". Stop here.
- **Stage B (on request)**: 1-minute summary block expanded with user story, key actors, scope boundary.
- **Stage C (on request)**: link to spec section + entry function source excerpt.

### Level 2 — Walk (≤30 min, intermediate)
Goal: one normal-success-flow trace with 5–10 anchored stops. For Korean responses, call this `정상 흐름` or `기본 성공 흐름`.
1. Pick the Story from Level 1.
2. Trace it end-to-end in code.
3. Fill the side-by-side table (see `templates/sidebyside.md`) — every row must have a populated "What this means (plain)" cell.
- **Stage A (default)**: 3-line trace summary + first 3 rows of the table (entry, midpoint, exit) + menu. Korean example: "(A) 전체 5~10행 흐름표  (B) 오류 흐름  (C) 데이터 모양  (D) 종료". Stop here.
- **Stage B (on request)**: the full table, capped at 8 rows per chunk; split if longer with a "Part 2 of N" menu.
- **Stage C (on request)**: error paths, alternative flows, or specific row deep-dives one at a time.

### Level 3 — Probe (≤2 h, advanced)
Goal: every decision → enforcement.
1. Read all `Clarifications` / ADRs / `research.md` Phase-0 sections.
2. For each decision, find the code that enforces it and the test that protects it.
3. Record the **rejected alternatives** and why.
- **Stage A (default)**: list the 3 decisions most likely to surprise the reader, one plain sentence each + menu. Korean example: "(A) 전체 결정표  (B) 결정 하나의 강제 코드  (C) 제외한 대안  (D) 종료". Stop here.
- **Stage B (on request)**: `decisions.md` matrix in chunks of ≤8 rows.
- **Stage C (on request)**: per-decision deep dive with citations and rejected alternatives.

### Level 4 — Master (deep, expert)
Goal: invariants and seams.
1. Identify domain invariants (Constitution, contracts, schemas, type signatures).
2. Find their guardians (validators, schema checks, runtime asserts, property tests).
3. Map seams between bounded contexts (where one module's invariants end and another's begin).
- **Stage A (default)**: name the top 3 invariants in plain language + one-line guardian for each + menu. Korean example: "(A) 전체 불변 규칙 지도  (B) 경계 다이어그램  (C) 특정 규칙 변경 영향  (D) 종료". Stop here.
- **Stage B (on request)**: `invariants.md` with guardians, one section at a time.
- **Stage C (on request)**: seam diagram + cross-context contract details on the specific seam asked for.

## Quick Reference

| Symptom | Use level | Output artifact |
|---|---|---|
| "What does this feature even do?" | 1 | 3-line map |
| "How does the normal success flow work?" / "정상 흐름은 어떻게 이어지나?" | 2 | Walk table |
| "Why is it built this way?" | 3 | Decision matrix |
| "What will break if I change X?" | 4 | Invariant map |

## Where Intent Lives

Authority order (highest first): canonical spec docs → ADRs / Clarifications → contracts / schemas → tests → commit messages with issue refs → issue tracker / PRs → agent rule files (`CLAUDE.md`, `AGENTS.md`).

Read `references/finding-intent.md` before your first Level-1 read when the canonical doc is not obvious, and whenever you run the Reverse direction.

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---|---|---|
| Reading code top-to-bottom | Memorize syntax, miss purpose | Open spec §0 first |
| Reading spec without opening code | Confident but wrong about behavior | Pair every claim with `file:line` |
| Skipping the citation | Can't audit later, can't share | Always cite `(doc§)` and `(file:line)` |
| Going to Level 4 immediately | Burn out, miss the why | Stop at the level your task needs |
| Ignoring "Why-not" | Repeat rejected designs | Pull rejected alternatives from ADR/Clarifications |
| Treating AI-generated code as spec | Codify hallucinations | Spec wins; flag drift, don't absorb it |
| Dumping all Levels in one response | Reader scrolls past, picks nothing, leaves | Stage A only, then menu — see Bite-Size Delivery Rule |
| Writing a 30-row table in a single chunk | Eyes glaze, nothing is read | Cap 8 rows per chunk, park the rest behind a menu option |

## Diagnose Spec ↔ Code Drift

When you suspect the agent shipped something the spec didn't ask for (or vice versa), run the diagnostic in `references/diagnostic.md`:

- Every `FR-XXX` in spec has at least one matching `file:line`.
- Every ADR has an enforcing module *and* a protecting test.
- Every Constitution principle has a guardian (validator/schema/contract).
- No "ghost" code patterns without intent (file an issue or write a back-fill ADR).
- No "orphan" spec items without code (implement, descope, or move to a backlog).
- Every Level-3 decision has a test on its *boundary*, not only on the happy path.

## Worked Example

`examples/twin-question-platform.md` — Levels 1–3 applied to a math-twin-question MVP1 spec from a real planning repo.

## Templates

- `templates/plain-speech-checklist.md` — **mandatory gate** every output must pass before shipping.
- `templates/sidebyside.md` — Walk/Probe table.
- `templates/progression-checklist.md` — Level-by-level checklist.

## Self-Test Scenarios

Five scenarios to verify the skill works for you. If you (or another agent) can't complete these from the skill alone, the skill has a gap — file an issue.

1. **Onboarding scenario.** Given a repo with `docs/<NNN>/spec.md` and a separate code repo, produce a Level-1 Map in 5 minutes. Pass if you can name the central User Story and one entry function.
2. **PR-review scenario.** Given an AI-generated PR with no description, run the **Reverse** direction to produce a Level-2 Walk citing which spec sections it claims to implement. Pass if you flag at least one drift.
3. **Change-impact scenario.** Given a request to alter behavior X, produce a Level-4 invariant map listing every guardian that would need to be updated. Pass if you locate every test that would change colour.
4. **Plain-speech scenario.** Hand any artifact this skill produced to someone outside the project (a sibling, a non-engineer friend, a brand-new hire on day one). Pass if they can paraphrase the feature's purpose, the normal flow, and one risk in their own words after a single read. If they reach for a dictionary or ask "what does X mean", the artifact failed rule 2 — go back and expand.
5. **Bite-size scenario.** Watch the user's first response after Stage A. Pass if they pick a single option from the menu and you reply with only that chunk. Fail if they say "너무 길어 / too long / 그만 / stop" — that means Stage A overran the 30-second TL;DR target. If they say "전부 / give me everything" you may stream remaining chunks back-to-back, but each must still be ≤8 rows or ≤5 headings.
