# Plain-Speech Checklist (mandatory gate)

Every artifact this skill produces — Map, Walk, Probe, Master — must pass all five checks below **before** you ship it to the user. This is the Feynman gate: if it fails, the reader will not understand, and the work was wasted.

## The five checks

- [ ] **1. Analogy lead.** The first 1–2 sentences contain an everyday comparison or a plain-language one-liner. Not "MVP2 generates twin candidates via 5-validator pipeline." Instead: "MVP2 = make 3 lookalike math problems from 1 original, then a human picks the good ones."

- [ ] **2. Every identifier expanded on first use.** Every `FR-XXX`, table name, status enum, column, file path, API path, and acronym gets a parenthetical plain expansion the first time it appears. Repeat the expansion in tables — readers do not always start at the top.

  - Example: `twin_group` → `twin_group (a folder that holds the original problem and all its approved lookalikes together)`
  - Example: `409 SOURCE_METADATA_REQUIRED` → `409 SOURCE_METADATA_REQUIRED (HTTP error meaning "you can't generate lookalikes yet — the original problem's metadata isn't finalized")`

- [ ] **3. Why before what.** Each section, table row, or bullet opens with one short clause on *why a normal person would care*, then the technical detail. "So a reviewer never approves a duplicate by accident → the pipeline runs a 5-check validator before showing the candidate."

- [ ] **4. No naked jargon in the conclusion.** Scan the closing paragraph. Strike every word the reader has not had explained earlier. If a term is unavoidable in the conclusion, expand it again.

- [ ] **5. One-minute summary block.** End with a section titled exactly **"If you only read one thing"** — three sentences, zero jargon, telling the reader what the feature does, who uses it, and the single biggest risk or rule. If you can't write those three sentences, you do not yet understand the thing.

## The retell test

Read your draft once. Then close it and try to retell the gist to an imagined sibling or junior in your own voice. If you reach for a paragraph, the draft is too dense. Split, expand, or cut until the retell flows.

## Anti-patterns

| Don't write | Write instead |
|---|---|
| "Anchors on intent via bidirectional traceability." | "Reads the spec and the code side-by-side, so you can see why each line exists." |
| "FR-009 mandates twin_group creation on first approval." | "Rule FR-009 says: the very first time a reviewer approves a lookalike, the system makes a new folder (`twin_group`) and drops both the original and the new problem into it." |
| "POST /approve materializes the candidate." | "When the reviewer clicks 'approve' (the approve API), the system turns the AI draft into a real problem and saves it." |
| "Idempotency-key prevents duplicate submissions." | "If the reviewer accidentally clicks submit twice, the system sees the same `Idempotency-Key` (a label that says 'this is the same request') and only counts it once." |
