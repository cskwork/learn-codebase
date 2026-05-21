---
name: learn-codebase
description: Use when learning a codebase another agent (human or AI) has built, reviewing an AI-generated PR against a spec, onboarding to a single feature mid-stream, planning a change to behavior whose blast radius you do not yet know, or diagnosing suspected spec-versus-code drift. Applies whether intent docs and implementation live in the same repo or in separate planning + code repos.
---

# learn-codebase — Intent-Anchored Reading

## Overview

To understand code another agent wrote, anchor every read on the intent that justifies it. Read intent and code as **paired columns**, never in sequence.

Code without intent = ritual mimicry (you copy the shape but can't extend it).
Intent without code = aspiration (theory you can't ship).
Side-by-side = bidirectional traceability you can act on.

## Plain-Speech Rule (Feynman Mode) — applies to ALL outputs

If a non-technical teammate cannot follow your output, the skill failed. Every artifact this skill produces (Map, Walk, Probe, Master) MUST pass `templates/plain-speech-checklist.md` before you ship it.

The five rules (memorize):

1. **Lead with an everyday analogy or one-line plain summary** before any jargon. Example — not "MVP2 generates twin candidates via 5-validator pipeline" but "MVP2 = 'make 3 lookalike math problems from 1 original, then a human picks the good ones'."
2. **Expand every identifier the first time it appears, in parentheses.** `FR-001` → `FR-001 (Functional Requirement 1, "what the system must do" rule #1)`. `twin_group` → `twin_group (a folder that holds the original problem and its lookalikes together)`. Do this even inside tables.
3. **Translate the why before the what.** Each row/section opens with one short clause on *why a normal person would care*, then technical detail.
4. **No naked acronyms, no naked code paths.** `idempotency_key` → `idempotency_key (a label that says "if you press send twice, only count once")`. `POST /api/.../approve` → `approve API (the button a reviewer clicks to say "yes, ship this candidate as a real problem")`.
5. **Close with a 1-minute summary block** titled "If you only read one thing" — 3 sentences max, zero jargon. If you cannot write those 3 sentences, you do not yet understand the thing.

Anti-pattern to avoid: "intent-anchored bidirectional traceability matrix between FR-009 and the materialization transaction." Rewrite as: "Did the spec say 'make a group on first approval'? Yes (FR-009). Where does the code do it? Step 9 of the approve flow. Who proves it works? The integration test that approves a candidate and checks the group exists."

Test your output by asking: *Could my parent, or a junior who joined yesterday, retell the gist?* If no, simplify.

### Red flags — stop and rewrite

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

### Level 1 — Map (≤5 min, beginner)
Goal: one paragraph + one entry function.
1. Read only the §0 / overview / README of the canonical intent doc.
2. Identify the **one** user story most central to the feature.
3. Locate **one** entry point in code (route handler, CLI command, top-level fn).
4. Output: an opening analogy (1 line: "This feature is like ___") + a 3-line plain summary using **no unexpanded jargon** + `entry: <file:line>` + 1-minute summary block.

### Level 2 — Walk (≤30 min, intermediate)
Goal: one happy-path trace with 5–10 anchored stops.
1. Pick the Story from Level 1.
2. Trace it end-to-end in code.
3. Fill the side-by-side table (see `templates/sidebyside.md`) — every row must have a populated "What this means (plain)" cell.
4. Output: `walk.md` opening with the analogy, the table, and closing with a 1-minute summary.

### Level 3 — Probe (≤2 h, advanced)
Goal: every decision → enforcement.
1. Read all `Clarifications` / ADRs / `research.md` Phase-0 sections.
2. For each decision, find the code that enforces it and the test that protects it.
3. Record the **rejected alternatives** and why.
4. Output: `decisions.md` matrix where each decision is stated *first* as a plain "We chose X over Y because Z" sentence, then with citations. Close with a 1-minute summary.

### Level 4 — Master (deep, expert)
Goal: invariants and seams.
1. Identify domain invariants (Constitution, contracts, schemas, type signatures).
2. Find their guardians (validators, schema checks, runtime asserts, property tests).
3. Map seams between bounded contexts (where one module's invariants end and another's begin).
4. Output: `invariants.md` + seam diagram. Each invariant must be stated in plain language ("the system never lets X happen because…") before the technical form. Close with a 1-minute summary.

## Quick Reference

| Symptom | Use level | Output artifact |
|---|---|---|
| "What does this feature even do?" | 1 | 3-line map |
| "How does the happy path flow?" | 2 | Walk table |
| "Why is it built this way?" | 3 | Decision matrix |
| "What will break if I change X?" | 4 | Invariant map |

## Where Intent Lives

Authority order (highest first): canonical spec docs → ADRs / Clarifications → contracts / schemas → tests → commit messages with issue refs → issue tracker / PRs → agent rule files (`CLAUDE.md`, `AGENTS.md`).

Full detection patterns (forward + reverse direction) in `references/finding-intent.md`.

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---|---|---|
| Reading code top-to-bottom | Memorize syntax, miss purpose | Open spec §0 first |
| Reading spec without opening code | Confident but wrong about behavior | Pair every claim with `file:line` |
| Skipping the citation | Can't audit later, can't share | Always cite `(doc§)` and `(file:line)` |
| Going to Level 4 immediately | Burn out, miss the why | Stop at the level your task needs |
| Ignoring "Why-not" | Repeat rejected designs | Pull rejected alternatives from ADR/Clarifications |
| Treating AI-generated code as spec | Codify hallucinations | Spec wins; flag drift, don't absorb it |

## Diagnose Spec ↔ Code Drift

When you suspect the agent shipped something the spec didn't ask for (or vice versa), run the diagnostic in `references/diagnostic.md`:

- Every `FR-XXX` in spec has at least one matching `file:line`.
- Every ADR has an enforcing module *and* a protecting test.
- Every Constitution principle has a guardian (validator/schema/contract).
- No "ghost" code patterns without intent (file an issue or write a back-fill ADR).
- No "orphan" spec items without code (implement, descope, or move to a backlog).

## Worked Example

`examples/twin-question-platform.md` — Levels 1–3 applied to a math-twin-question MVP1 spec from a real planning repo.

## Templates

- `templates/plain-speech-checklist.md` — **mandatory gate** every output must pass before shipping.
- `templates/sidebyside.md` — Walk/Probe table.
- `templates/progression-checklist.md` — Level-by-level checklist.

## Self-Test Scenarios

Three scenarios to verify the skill works for you. If you (or another agent) can't complete these from the skill alone, the skill has a gap — file an issue.

1. **Onboarding scenario.** Given a repo with `docs/<NNN>/spec.md` and a separate code repo, produce a Level-1 Map in 5 minutes. Pass if you can name the central User Story and one entry function.
2. **PR-review scenario.** Given an AI-generated PR with no description, run the **Reverse** direction to produce a Level-2 Walk citing which spec sections it claims to implement. Pass if you flag at least one drift.
3. **Change-impact scenario.** Given a request to alter behavior X, produce a Level-4 invariant map listing every guardian that would need to be updated. Pass if you locate every test that would change colour.
4. **Plain-speech scenario.** Hand any artifact this skill produced to someone outside the project (a sibling, a non-engineer friend, a brand-new hire on day one). Pass if they can paraphrase the feature's purpose, the happy path, and one risk in their own words after a single read. If they reach for a dictionary or ask "what does X mean", the artifact failed rule 2 — go back and expand.
