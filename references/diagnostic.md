# Intent ↔ Code Drift Diagnostic

A short self-audit to run after Level 2 or Level 3 to surface gaps before they bite.

Run it against a single feature, not the whole repo. Whole-repo audits don't end.

---

## D1. Every spec requirement has a code reference

For each `FR-XXX` / `SC-XXX` / numbered requirement in the spec:

```bash
# planning repo or monorepo: grep spec→code
grep -rEn 'FR-[0-9]+|SC-[0-9]+' <code-repo> || echo "no requirement refs in code"
```

Or open `tasks.md` if the project uses spec-kit — every `T0XX` task should map to a `FR-XXX`.

Flag:
- Requirements with **no code reference** → orphan spec (implement, descope, or move to backlog).
- Code references to **nonexistent requirements** → ghost code (write a back-fill ADR or delete).

## D2. Every ADR has an enforcing module *and* a protecting test

For each ADR / Clarification:

```bash
# do the cited modules exist?
grep -l '<adr-id-or-keyword>' <code-repo>/**/*.py  # or .ts, .go, etc.
# do tests reference the decision?
grep -l '<adr-id-or-keyword>' <code-repo>/tests/**
```

Flag:
- ADR with no module → undeployed decision.
- ADR with module but no test → unprotected decision (one refactor away from regression).

## D3. Every Constitution / principle has a guardian

Constitution principles are the most expensive things to lose. Each should have at least one:
- Validator
- Schema rule
- Runtime assert
- Property test
- Lint rule

If a principle has no guardian, refactors will silently violate it. File an issue.

## D4. No "ghost" code patterns without intent

Skim the largest modules. For each module whose purpose isn't immediately obvious from one of the intent sources (spec/ADR/contract/test name):

- Note in `ghosts.md`
- Ask the agent or author *why* this exists
- If no answer, candidate for deletion or for a back-fill ADR

This is the highest-yield diagnostic when an AI agent has been coding without supervision.

## D5. No "orphan" spec items without code

Inverse of D4. Spec items with no implementation either:
- Need implementation (still on roadmap → file an issue),
- Are out of scope (clarify in spec with a "Not in scope" note), or
- Were silently dropped (re-decide explicitly).

## D6. Test coverage of the **decision boundary**, not just the happy path

For each Level-3 decision (e.g., "auto-approve OFF in MVP1"):
- Is there a test that fails if the *opposite* behavior is shipped?
- Is there a test for the boundary condition (e.g., the exact confidence threshold)?

If no — the decision can flip in a refactor without anyone noticing.

---

## Diagnostic output template

```markdown
# Drift Diagnostic — <feature> — <YYYY-MM-DD>

## Summary
- Spec items: <N>, of which <K> have code references (<K/N>%)
- ADRs: <M>, of which <J> have enforcing module + test (<J/M>%)
- Constitution principles: <P>, of which <Q> have guardians (<Q/P>%)

## Orphan spec items (no code)
- FR-XXX: <description> → action: <implement/descope/backlog>

## Ghost code (no intent)
- <module/file>: <observed purpose> → action: <back-fill ADR/delete/ask author>

## Unprotected decisions (ADR with no test)
- <ADR id>: <decision> → action: <add test>

## Drift candidates
- <area>: spec says <X>, code does <Y> → action: <fix code / fix spec / accept with ADR>
```

---

## When to run this

- **After Level 2 Walk** — quick D1 + D4 pass while the trace is fresh.
- **Before approving an AI-generated PR** — D2 + D4 catch hallucinated structure.
- **At the end of a milestone** — full diagnostic, output stored alongside the release notes.
- **When onboarding a new teammate** — diagnostic surfaces "what to ask about" instead of vague intuitions.

A low score isn't a failure; it's a map of what to fix next. The point is **visibility**, not perfection.
