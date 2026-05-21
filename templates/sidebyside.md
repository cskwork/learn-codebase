# Side-by-side — {{Feature name}}

> Anchored reading artifact. Each row pairs an intent statement with the code that implements it. A row with empty cells is a probe target — mark it `?` and revisit, don't delete.

## Origin

- **Intent doc(s):** `<path/to/spec.md>` (commit `<sha>`)
- **Code repo(s):** `<repo-or-path>` (commit `<sha>`)
- **Read at level:** 1 / 2 / 3 / 4
- **Reader:** `<you or agent>`
- **Date:** `<YYYY-MM-DD>`

## Story (Level 1 carry-over)

One sentence: *who* does *what* to get *what outcome*.

> `<story sentence>`

Entry: `<file:line> :: <function name>`

## Trace (Level 2)

**Plain-language column is mandatory** — see Plain-Speech Rule in `SKILL.md`. A row whose "What this means" cell uses jargon is *not done*.

| # | What this means (plain) | Intent (quote + cite) | Code (file:line :: symbol) | Test / contract (file::name) | Why-not (rejected) |
|---|---|---|---|---|---|
| 1 | `<one sentence a non-expert understands>` | `"<quote>"` (`<doc> §<sec>`) | `<file:LL> :: <symbol>` | `<test_file::test_name>` | `<rejected alt + cite>` |
| 2 | | | | | |
| 3 | | | | | |

Aim for 5–10 rows on the happy path. Branches and error paths belong on their own table. Card-per-stop layout (one heading + small table per row) often reads better than one wide table — pick whichever the audience can scan faster.

## Decisions touched (Level 3 preview)

For each Clarification / ADR / research decision that touches this trace, drop the link in a "Decisions" section:

- `<cite>` → enforced at `<file:LL>` → guarded by `<test>` → rejected: `<alt>`

Full matrix goes in a separate `decisions.md` once the trace is stable.

## Open questions

- [ ] `<question>` — `<what evidence would resolve it>`
- [ ] `<question>` — `<what evidence would resolve it>`

## Glossary delta

New terms you learned that the spec assumes you know:

| Term | Meaning (in this domain) | First seen at |
|---|---|---|
| `<term>` | `<one-line meaning>` | `<doc§>` |
