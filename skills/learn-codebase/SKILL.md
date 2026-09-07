---
name: learn-codebase
description: Explain unfamiliar code by pairing intended behavior with source, tests, and design decisions. Use for feature onboarding, understanding AI-written changes, investigating spec/code drift, or assessing change impact.
---

# learn-codebase — Intent-Anchored Reading

Connect what a feature is meant to do with the code that implements it. Read-only analysis is the default; findings do not authorize fixes or issue creation.

## Scope and delivery

Start with the feature or question the user named. Use the shallowest level that answers it, and complete the requested explanation without forcing menu selections between sections. For an open-ended learning session, begin with a short map and offer a focused next step.

Match the user's language and demonstrated knowledge. In Korean, use `정상 흐름`, `진입점`, `판단 근거`, and `규칙 지도`; preserve source identifiers and exact errors. Explain unfamiliar terms once when needed. A plain summary usually suffices; use an analogy only if it clarifies the behavior. Do not assume a question proves a knowledge gap.

Lead with the answer, then the evidence. Keep tables and excerpts focused on the question; put extensive detail in a linked artifact when useful. [templates/plain-speech-checklist.md](templates/plain-speech-checklist.md) is a review aid for substantial explanations.

## Pair intent with implementation

For each important behavior or decision, capture:

| What this means | Intent (document section) | Code (file:line) | Test or contract | Rejected alternative and reason |
|---|---|---|---|---|
| A reviewer approves a candidate before it becomes a real item. | spec.md § Approval | review.py:42 | test_review.py::test_approval | Auto-approval rejected in ADR-3 |

Use [templates/sidebyside.md](templates/sidebyside.md) for a full walk. Mark missing evidence `?`; distinguish observed behavior, documented intent, and inference. Never invent rationale or claim a test ran merely because it exists.

Start from the canonical spec for **Forward (spec→code)** reading. Start from an entry function for **Reverse (code→spec)** reading when intent is sparse, drifted, or absent. Missing intent is a finding, not a reason to fabricate a spec or stop explaining the code.

Use the project's stated authority. Otherwise look for canonical specifications, ADRs and clarifications, contracts/schemas, tests, and relevant issue/commit history. Current code establishes implemented behavior; a conflicting document establishes a discrepancy to report. Read [references/finding-intent.md](references/finding-intent.md) when the source of intent is unclear or using Reverse reading.

## Choose the useful depth

| Level | Question | Evidence and result |
|---|---|---|
| 1 — Map | What does this feature do? | Overview, central user story, and an anchored entry function; short purpose/scope explanation. |
| 2 — Walk | How does the normal flow work? | Trace one story end to end, pairing meaningful stops with intent and tests/contracts; include relevant error paths and unknowns. |
| 3 — Probe | Why is it built this way? | Map relevant clarifications and ADRs to enforcing code, protecting tests, and recorded rejected alternatives. |
| 4 — Master | What breaks if X changes? | Map domain invariants to validators, schemas, assertions, and tests; identify module boundaries and affected contracts. |

These are depth choices, not mandatory sequential gates. Use a decision matrix or invariant map only when it answers the request. [templates/progression-checklist.md](templates/progression-checklist.md) helps review a substantial artifact; [examples/twin-question-platform.md](examples/twin-question-platform.md) demonstrates Levels 1–3.

## Drift and completion

For a drift investigation, use [references/diagnostic.md](references/diagnostic.md) to check required behavior, enforcement, boundary tests, and code without documented intent. Report discrepancies with both citations and the next check that would resolve uncertainty. Do not automatically implement, descope, create issues, or back-fill decisions.

Before reporting, confirm the explanation answers the requested question, cites the relevant intent and code, and labels missing evidence. Change-impact predictions remain predictions until verified. Stop when the requested depth is satisfied; expand only for an unresolved concern or user request.
