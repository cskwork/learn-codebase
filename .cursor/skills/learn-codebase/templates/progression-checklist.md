# Progression Checklist — {{Feature name}}

Stop at the level your task actually needs. Going deeper is not virtue; it's procrastination.

> Review substantial output with `templates/plain-speech-checklist.md`; adapt detail to the user and requested depth.

## Level 1 — Map (≤5 min)
- [ ] Found canonical intent doc (`spec.md` / `README.md` / `RFC*.md`)
- [ ] Read ONLY §0 / overview / 5-min entry
- [ ] Identified ONE user story most central to the feature
- [ ] Located ONE entry function in code (`file:line`)
- [ ] Wrote 3-line plain-language summary

**Done when** a teammate who has never seen this feature can repeat back what it does after reading your summary.

## Level 2 — Walk (≤30 min)
- [ ] Picked the User Story from Level 1
- [ ] Opened intent doc and code in side-by-side panes (literal columns help)
- [ ] Built `walk.md` table with 5–10 rows
- [ ] Cited intent (`doc§`) and code (`file:line`) on every row
- [ ] Linked at least one test or contract per row (or marked `?` if missing)
- [ ] Captured open questions list

**Done when** you can trace the happy path on a whiteboard without re-opening the code.

## Level 3 — Probe (≤2 h)
- [ ] Listed every Clarification / ADR / research decision that touches this feature
- [ ] Mapped each decision to enforcing code
- [ ] Mapped each decision to protecting test (`?` if missing)
- [ ] Noted rejected alternatives for each decision
- [ ] Flagged any decision with no enforcement (drift candidate)
- [ ] Flagged any code pattern with no decision (ghost candidate)

**Done when** you can answer "why is this built this way instead of <alternative>?" for every decision.

## Level 4 — Master (deep)
- [ ] Listed domain invariants (Constitution, contracts, schemas, type signatures)
- [ ] Located guardian for each invariant (validator, schema check, runtime assert, property test)
- [ ] Identified seams between bounded contexts
- [ ] Drew seam diagram (one page max)
- [ ] Wrote a "what changes when" matrix: for each anticipated change, list invariants affected

**Done when** you can predict which tests will turn red for any proposed change without running them.

## Stop conditions

- The task no longer requires deeper reading → stop.
- You've spent more than 2× the level's budget → stop, re-scope, or hand off.
- Intent docs are insufficient → explain observed code behavior and mark the missing intent; do not invent or repair documents without a request.
