# learn-codebase

> *intent-anchored reading for codebases another agent built*

A Claude Code skill (and a human technique) for understanding code another agent — human or AI — has written, by anchoring every read on its **intent** and reading both as **paired columns**.

> **Code without intent = ritual mimicry.**
> **Intent without code = aspiration.**
> **Side-by-side = bidirectional traceability you can act on.**

---

## What this skill does

It teaches you to read a feature in **4 progressive levels**, stopping at the depth your task actually needs:

| Level | Budget | Goal | Artifact |
|---|---|---|---|
| **1 — Map** | ≤5 min | What is this & why does it exist? | 3-line summary + one entry function |
| **2 — Walk** | ≤30 min | How does the happy path flow? | Side-by-side trace table |
| **3 — Probe** | ≤2 hr | Why is it built this way? | Decision matrix with rejected alternatives |
| **4 — Master** | Deep | What invariants hold it together? | Invariant + seam map |

Every artifact pairs an intent quote (from spec / ADR / contract / test) with the matching code (`file:line`) **and** a plain-language one-liner anyone outside the project can follow (the "Feynman" gate — see `templates/plain-speech-checklist.md`). If a cell is empty, that's a probe target — not a problem.

See [`SKILL.md`](./SKILL.md) for the full technique.

---

## Why this exists

Three pain points this skill addresses:

1. **AI shipped a PR.** You have a 100-file repo and a 40-page spec and need to review the diff. Top-down reading drowns; intent-anchored reading scales.
2. **Onboarding to one feature.** You don't need the whole product — you need to grok *this thing* in 30 minutes. The skill gives a stopping rule.
3. **Spec ↔ code drift.** Specs say X, code does Y, tests cover Z. The skill surfaces the gap explicitly via a [drift diagnostic](./references/diagnostic.md).

---

## Install

### As a Claude Code skill

```bash
# clone into your skills directory
git clone https://github.com/cskwork/learn-codebase \
  ~/.claude/skills/learn-codebase
```

Or symlink from a working directory you maintain:

```bash
git clone https://github.com/cskwork/learn-codebase ~/code/learn-codebase
ln -s ~/code/learn-codebase ~/.claude/skills/learn-codebase
```

Then in any Claude Code session, ask:

> "Use `learn-codebase` to walk me through feature X."

Or invoke the skill explicitly with the `Skill` tool when the agent asks how to proceed.

### As a human technique (no Claude Code required)

Read [`SKILL.md`](./SKILL.md). Open [`templates/sidebyside.md`](./templates/sidebyside.md). Follow the 4 levels. Stop when your task is done.

---

## Repository layout

```
learn-codebase/
├── SKILL.md                                  # The skill itself (the main read)
├── README.md                                 # You are here
├── LICENSE
├── templates/
│   ├── plain-speech-checklist.md             # Mandatory Feynman-style output gate
│   ├── sidebyside.md                         # The walk-table format
│   └── progression-checklist.md              # Per-level checklist
├── examples/
│   └── twin-question-platform.md             # Levels 1-3 applied to a real spec
└── references/
    ├── finding-intent.md                     # Where to look first (forward + reverse direction)
    └── diagnostic.md                         # Intent ↔ code drift self-audit
```

---

## Use cases

- Joining an AI-assisted team mid-stream.
- Reviewing AI-generated PRs against a written spec.
- Teaching a junior dev one feature without overwhelming them.
- Planning a refactor: knowing every test that will turn red before you change anything.
- Recovering intent from code when documentation has lapsed (Reverse direction).

---

## Acknowledgements

The skill builds on patterns from:

- **Domain-Driven Design** — ubiquitous language and bounded contexts.
- **Literate programming** — code paired with prose.
- **Requirements traceability** (IBM DOORS lineage) — bidirectional mapping.
- **Test-driven development** — tests as executable intent.
- **Anthropic's skill-authoring guide** (`writing-skills`) — TDD applied to documentation.

---

## License

MIT. See [`LICENSE`](./LICENSE).

---

## Contributing

Issues and PRs welcome. If the skill fails on a real codebase you tried it on, that's the highest-value bug report — open an issue with:

- the project type (mono-repo / split planning + code / etc.),
- which level you got stuck at,
- the missing piece in the skill or templates.

The skill's quality is measured by *whether a fresh agent can apply it to a new codebase without prior context*. Reports of failure on real codebases make the skill better.
