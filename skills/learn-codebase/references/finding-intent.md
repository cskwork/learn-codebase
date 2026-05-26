# Finding Intent: Where to Look First

Intent rarely lives in one place. Search in this order — highest authority first. Stop at the first source that gives you a concrete user story.

## 1. Canonical intent docs

Highest authority. If these exist, start here.

- `docs/<NNN-feature-slug>/spec.md` — spec-kit / Multica style feature spec
- `docs/<NNN>/README.md` — folder index
- `*/SPEC.md`, `*/PRD.md`, `*/requirements.md`
- `RFC*.md`, `RFD*.md` (request-for-comments / decisions)
- `docs/specs/`, `specs/`, `.specify/`

Skim `§0` / overview / "5-min entry" / TL;DR only at Level 1. Resist reading further until your task demands it.

## 2. Decisions (the "why-not" archive)

This is where rejected alternatives live. Without this layer, you'll re-debate decisions that are already settled.

- `docs/**/adr/*.md` — Architecture Decision Records
- `Clarifications` sections inside `spec.md` (often dated Q&A)
- `research.md` Phase-0 decisions, TBD lists
- `decisions/`, `decision-log.md`
- Commit messages tagged with issue keys: `[ITE-N]`, `[ABC-123]`, `feat(...)`
- PR descriptions with "Rejected alternatives" / "Considered" sections

## 3. Contracts (frozen intent)

When humans disagree, contracts are what actually executes.

- `**/contracts/*.yaml`, `*.json` — OpenAPI 3.x, JSON Schema
- `*.proto`, `*.graphql`, GraphQL SDL
- Type signatures: TypeScript `*.d.ts`, Python type hints, Rust traits
- Database DDL / migrations (`alembic/versions/`, `prisma/schema.prisma`, `migrations/`)
- Event schemas (Avro, CloudEvents, custom)

If the spec and the contract disagree, the **contract is what runs**. Note the drift and surface it.

## 4. Tests (executable intent)

Tests are intent that runs in CI. They survive code rewrites and team turnover.

- Integration tests over unit tests (integration tests live closer to user intent)
- `*.feature` Gherkin files (Given/When/Then = intent in plain English)
- Property-based tests (`hypothesis`, `fast-check`, `quickcheck`) — they encode invariants
- Contract tests (Pact, schema-compatibility tests)
- Snapshot tests — sometimes accidental intent ("this is what we shipped, do not break it")

A test that names the user story (`test_reviewer_confirms_metadata`) is a Level-2 anchor.

## 5. Process artifacts

- Issue tracker: Linear, Jira, GitHub Issues, Multica
- PR descriptions (use `gh pr view` or the platform UI)
- Release notes, changelog entries
- Constitution / principles (`.specify/memory/constitution.md`, `PRINCIPLES.md`)
- Contributing guides (`CONTRIBUTING.md`) — often encode review policies
- Internal wikis (Confluence, Gitea wiki, Notion)

## 6. Agent rules and runbooks

Where AI agents were instructed determines what they built.

- `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `COPILOT.md`
- `.cursor/rules/`, `.windsurfrules`, `.aiderrules`
- Skill catalogs (`.claude/skills/`, `~/.claude/skills/`)
- `.specify/` directory (spec-kit style)
- Project READMEs that include "How to talk to the AI here"

When an AI built a feature, its rules file is often the *real* spec. Read it.

---

# Reverse Direction: Code → Intent

When intent docs are sparse, drifted, or absent, recover intent from code in this order:

## 1. Public API surface
The contract you publish *is* the intent your users rely on. Start with:
- OpenAPI / GraphQL schemas
- Exported types, public functions/classes
- CLI `--help` output
- README quickstart sections

## 2. Tests as specs
- Integration tests with descriptive names = stories
- Property tests = invariants
- Regression tests with linked issues = historical decisions

## 3. Commit & PR archaeology
- `git log --follow <file>` → who/why for each line
- `git log --grep '<keyword>'` → find decision points
- `gh pr list --search '<file>'` → discussion threads

## 4. Comments and docstrings
- Hesitate before trusting comments — they drift. But comments that cite issue keys (`# ITE-123:`) survive.
- Comments with "TODO/FIXME/HACK" reveal known compromise points.

## 5. Configuration as intent
- `.env.example`, `config/*.yaml`, feature flags — what the system can be tuned to do is intent about its supported envelope.

---

# Anti-patterns to detect

- **Spec drift**: spec says X, code does Y, test doesn't cover either. Flag → write a back-fill ADR or update spec.
- **Ghost decisions**: code enforces a rule never written down. Either codify (write ADR) or remove.
- **Orphan ADR**: ADR records a decision no code enforces. Either implement, descope, or retire the ADR.
- **Comment-as-spec**: a code comment claims behavior contradicting the spec. Spec wins; fix comment, or update spec if the spec is wrong.
- **AI-hallucinated structure**: AI-generated module exists with no spec line, no ADR, no test. Probably hallucination — verify before adopting.
- **Trojan defaults**: a config value or feature-flag default silently changes behavior. Surface it in Level-3 decisions.

**Rule of resolution.** When intent and code disagree, *code is the truth of what runs today; spec is the truth of what should run.* Surface the gap explicitly, don't resolve it silently. Choose to fix code, fix spec, or accept the drift with an ADR — but make the choice visible.
