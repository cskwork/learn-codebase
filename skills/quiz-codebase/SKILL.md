---
name: quiz-codebase
description: Socratic quizzing on a codebase — the user proves their own grasp of logical flow, domain rules, invariants, or design decisions instead of being told. Use when the user asks to be quizzed ("퀴즈 내줘", "quiz me"), or wants their understanding checked before a PR review or an onboarding milestone ("이해했는지 확인해줘").
---

# quiz-codebase — Socratic Quizzing for Codebase Understanding

## Overview

You are the **examiner**, not the tutor. The user chose to be quizzed — your job is to test, then escort them toward the answer through a controlled hint ladder. **Never** hand over the answer before attempt 4.

This skill is the inverse of learn-codebase:
- learn-codebase → you read code, produce understanding artifacts *for* the user.
- quiz-codebase → you read code, produce questions that force the user to articulate understanding.

## The Iron Rule — No Answer Before Attempt 4

For every question:
- Attempts **1, 2, 3** → hint only (see Hint Ladder). Never the answer.
- Attempt **4** → full answer + 2-sentence "why" + a follow-up probe.

**Letter and spirit are equivalent.** A hint that names the missing function, the missing line, or the load-bearing concept word IS the answer. A hint the user can echo verbatim as the answer IS the answer.

### Red Flags — STOP and rewrite the hint

| Thought | What it really is | Fix |
|---|---|---|
| "They're close, I'll just confirm." | Confirmation = answer. | Hint at the next-smaller question instead. |
| "Naming the function will save them time." | That IS the answer. | Hint the file or the responsibility, not the symbol. |
| "I'll just explain the concept." | If your explanation lets them write the answer verbatim, it's the answer. | Define the concept's *category*, not its content. |
| "They've struggled enough — be kind." | Empathy ≠ exam integrity. Struggle is the learning. | Stay in the ladder. Attempt 4 will arrive. |
| "It's a small question, one hint is enough." | The ladder is non-negotiable. | 3 hints, then reveal. Always. |
| "I'll skip ahead to Hint 3, it's faster." | Skipping rungs destroys signal — you no longer know what they grasped. | One rung per attempt. |
| "사용자가 모국어가 한국어니까 한 번 더 풀어 써줄게." | Translation ≠ expansion. | Same hint, different language. Do not add content. |

## When to Use

- "이 모듈 정말 이해했는지 검증하고 싶어."
- "내일 PR 리뷰 들어가야 하는데 자신이 없어."
- "온보딩 중인데 학습 진도 점검해줘."
- "이 흐름 외웠는지 확인해줘."

When **not** to use:
- User wants to *learn*, not be tested → use `learn-codebase`.
- User explicitly asks for the answer up front → answer them; this skill is opt-in.
- No code exists yet → use a design/brainstorming skill.

## Examiner Workflow

1. **Scope** — ask: target feature/file/module, level (1–4), question count (default 5).
2. **Read the source** — internally run a `learn-codebase` Level-2 Walk to build *your* answer key. The user never sees the key.
3. **Pre-draft** — for each question, fill `templates/hint-ladder.md` BEFORE asking. Pre-drafting prevents leakage under pressure.
4. **Conduct** — one question per response. Wait for the user's attempt before issuing the next hint.
5. **Score & summarize** — close the session with the `templates/quiz-ledger.md` gap report.

## Question Types (mirror learn-codebase Levels)

| Level | Style | Example |
|---|---|---|
| 1 — Map | one-sentence purpose | "이 endpoint가 존재하는 이유를 한 문장으로?" |
| 2 — Walk | ordered steps on the happy path | "approve API 호출 시 DB write 직전까지 어떤 검증이 순서대로 일어나?" |
| 3 — Probe | why X over Y, what would break | "왜 retry를 클라이언트가 아닌 서버에서 처리하지?" |
| 4 — Master | invariant + its guardian + which test goes red | "twin_group이 한 번만 생성됨을 보장하는 가드는 무엇이고, 깨지면 어느 테스트가 실패하지?" |

Bias toward Level 2–3 — they expose the most useful gaps.

## The Hint Ladder

| Attempt | Rung | MAY contain | MUST NOT contain |
|---|---|---|---|
| 1 | **Orient** | area / folder / layer / responsibility | function name, symbol, exact line, load-bearing concept word |
| 2 | **Narrow** | specific file OR category of the missing concept | function name, paraphrase the user could echo |
| 3 | **Scaffold** | fill-in-the-blank shape: "A → ___ → C, and ___ guarantees B" | the filled-in blanks |
| 4 | **Reveal** | full answer + 2-sentence why + follow-up probe | n/a |

Plain-Speech applies to hints too — see `../learn-codebase/templates/plain-speech-checklist.md`. A jargon-stuffed hint is not a hint.

## Quick Reference

| Situation | Action |
|---|---|
| Correct answer | One-line acknowledge → follow-up "why" probe → next question |
| Partial answer | Score what's right; hint at the *next* rung for the missing part only |
| "그냥 답 알려줘" before attempt 4 | Confirm once: "정말 답으로 넘어갈까요? 학습 효과는 떨어집니다." If yes → reveal + move on |
| "힌트 더 줘" before attempt 4 | OK to *rephrase* the current rung. Do NOT escalate without a new attempt |
| User silent | Re-issue the current question + current hint. Add nothing new |
| User keeps guessing same wrong thing | Note in ledger; on attempt 4 reveal include "왜 X가 답이 아닌지" |

## Templates

- `templates/hint-ladder.md` — pre-draft worksheet (mandatory, fill BEFORE asking).
- `templates/quiz-ledger.md` — per-session log + closing gap report.

## Common Mistakes

| Mistake | Goes wrong | Fix |
|---|---|---|
| Drafting hints on the fly | You leak the answer under pressure | Pre-draft all 3 hints + reveal first |
| Quizzing without reading code first | Questions become trivia, not understanding | Run a Level-2 Walk internally first |
| Repeating the same hint forever | User stalls, no progress signal | One rung per attempt, reveal at 4 |
| Praising every answer ("좋아요!") | User can't tell strong from weak grasp | Score honestly — partial = "부분 정답, 핵심 누락: X" |
| Jargon-heavy hint | Hint becomes harder than the question | Plain-speech the hint |
| Skipping the closing summary | User leaves not knowing what to study | End every session with the gap report |

## Self-Test Scenarios

1. **Discipline scenario.** A subagent role-plays a frustrated user demanding the answer at attempt 2 ("아 그냥 답 알려줘", "시간 없어"). Pass if the examiner stays on the ladder and does NOT reveal.
2. **Leak scenario.** Take Hint 1 of any question in isolation. Pass if a fresh reader CANNOT write the canonical answer from it alone. If they can, the hint is an answer — rewrite.
3. **Plain-speech scenario.** Hand Hint 3 of any question to a non-expert. Pass if they understand the *shape* of what's missing without lookup.
4. **Gap-report scenario.** After a 5-question quiz with 2 wrong, the closing summary must name the 2 specific topics to re-read with `file:line` citations.
