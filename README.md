<p align="center"><img src="logo.png" width="120" alt="logo" /></p>

# learn-codebase

> *a collection of Claude Code skills for understanding code another agent (human or AI) has written*

This repo bundles paired skills that cover the two complementary halves of grokking an unfamiliar codebase:

| Skill | Direction | What it produces | When to reach for it |
|---|---|---|---|
| [`learn-codebase`](./skills/learn-codebase/) | code → understanding | intent-anchored reading artifacts (Map / Walk / Probe / Master) with a Feynman-style plain-speech gate on every output | "I need to grok feature X before I touch it" |
| [`quiz-codebase`](./skills/quiz-codebase/) | understanding → verification | Socratic questions with a 3-rung hint ladder; the answer is never revealed before attempt 4 | "I think I get it — prove it to me" |

> **Code without intent = ritual mimicry.**
> **Intent without code = aspiration.**
> **Side-by-side = bidirectional traceability you can act on.**
> **Being told ≠ understanding. The quiz is the gate.**

---

## The two skills, side by side

### `skills/learn-codebase/` — intent-anchored reading

Reads a feature in **4 progressive levels**, stopping at the depth your task actually needs:

| Level | Budget | Goal | Artifact |
|---|---|---|---|
| **1 — Map** | ≤5 min | What is this & why does it exist? | 3-line summary + one entry function |
| **2 — Walk** | ≤30 min | How does the happy path flow? | Side-by-side trace table |
| **3 — Probe** | ≤2 hr | Why is it built this way? | Decision matrix with rejected alternatives |
| **4 — Master** | Deep | What invariants hold it together? | Invariant + seam map |

Every artifact pairs an intent quote (from spec / ADR / contract / test) with the matching code (`file:line`) **and** a plain-language one-liner anyone outside the project can follow. If a cell is empty, that's a probe target — not a problem.

See [`skills/learn-codebase/SKILL.md`](./skills/learn-codebase/SKILL.md).

### `skills/quiz-codebase/` — Socratic verification

The inverse of learn-codebase. The agent becomes an **examiner**, not a tutor:

- For every question, attempts **1, 2, 3** earn hints only — never the answer.
- Attempt **4** reveals the full answer with a 2-sentence "why" and a follow-up probe.
- The hint ladder (Orient → Narrow → Scaffold → Reveal) is non-negotiable; skipping rungs destroys the learning signal.

Question types mirror learn-codebase Levels (Map / Walk / Probe / Master), with bias toward Level 2–3 because that's where useful gaps live.

See [`skills/quiz-codebase/SKILL.md`](./skills/quiz-codebase/SKILL.md).

### Pairing them

The intended loop:

1. Run `learn-codebase` to read the feature.
2. Run `quiz-codebase` against the *same* feature 24 hours later (or before a PR review) to surface what didn't stick.
3. Use the quiz's closing gap report as your re-read list for `learn-codebase`.

---

## Install

### As Claude Code skills

Both skills live as sibling directories under `skills/`. Install whichever you need — they're independent.

```bash
# clone the repo once, somewhere you'll keep it
git clone https://github.com/cskwork/learn-codebase ~/code/learn-codebase

# symlink each skill into Claude Code's skill directory
ln -s ~/code/learn-codebase/skills/learn-codebase ~/.claude/skills/learn-codebase
ln -s ~/code/learn-codebase/skills/quiz-codebase ~/.claude/skills/quiz-codebase
```

To pick up upstream updates:

```bash
cd ~/code/learn-codebase && git pull
```

Both symlinked skills pick up the new version automatically — no re-install needed.

Then in any Claude Code session, ask:

> "Use `learn-codebase` to walk me through feature X."
>
> "Quiz me on feature X with `quiz-codebase`."

Or invoke either skill explicitly with the `Skill` tool.

### As a human technique (no Claude Code required)

Read [`skills/learn-codebase/SKILL.md`](./skills/learn-codebase/SKILL.md) for the reading method.
Read [`skills/quiz-codebase/SKILL.md`](./skills/quiz-codebase/SKILL.md) for the self-testing method.
Open the templates under each skill's `templates/` folder. Follow the workflow. Stop when your task is done.

---

## Repository layout

```
learn-codebase/
├── README.md                                 # You are here
├── LICENSE
├── .gitignore
└── skills/
    ├── learn-codebase/
    │   ├── SKILL.md                          # The reading skill itself
    │   ├── templates/
    │   │   ├── plain-speech-checklist.md     # Mandatory Feynman-style output gate
    │   │   ├── sidebyside.md                 # The walk-table format
    │   │   └── progression-checklist.md      # Per-level checklist
    │   ├── examples/
    │   │   └── twin-question-platform.md     # Levels 1-3 applied to a real spec
    │   └── references/
    │       ├── finding-intent.md             # Where to look first (forward + reverse)
    │       └── diagnostic.md                 # Intent ↔ code drift self-audit
    └── quiz-codebase/
        ├── SKILL.md                          # The Socratic quizzing skill
        └── templates/
            ├── hint-ladder.md                # Pre-draft worksheet (mandatory)
            └── quiz-ledger.md                # Per-session log + gap report
```

---

## Use cases

- Joining an AI-assisted team mid-stream.
- Reviewing AI-generated PRs against a written spec.
- Teaching a junior dev one feature without overwhelming them.
- Planning a refactor: knowing every test that will turn red before you change anything.
- Recovering intent from code when documentation has lapsed.
- Verifying that a teammate (or yourself) actually grasped a feature before merging changes that depend on that grasp.

---

## Acknowledgements

The skills build on patterns from:

- **Domain-Driven Design** — ubiquitous language and bounded contexts.
- **Literate programming** — code paired with prose.
- **Requirements traceability** (IBM DOORS lineage) — bidirectional mapping.
- **Test-driven development** — tests as executable intent.
- **Socratic method / Feynman technique** — knowledge proved by re-derivation, not recitation.
- **Anthropic's skill-authoring guide** (`writing-skills`) — TDD applied to documentation.

---

## License

MIT. See [`LICENSE`](./LICENSE).

---

## Contributing

Issues and PRs welcome. If either skill fails on a real codebase you tried it on, that's the highest-value bug report — open an issue with:

- which skill (`learn-codebase` or `quiz-codebase`),
- the project type (mono-repo / split planning + code / etc.),
- which level/attempt you got stuck at,
- the missing piece in the skill or templates.

The skills' quality is measured by whether a fresh agent can apply them to a new codebase without prior context. Reports of failure on real codebases make them better.
