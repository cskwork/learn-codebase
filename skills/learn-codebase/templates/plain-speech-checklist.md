# Plain-Speech Checklist

Use for substantial explanations, adapting to the user's language and demonstrated knowledge.

- Lead with the concrete answer or a plain summary; use an analogy only when helpful.
- Explain unfamiliar domain terms at first use. Preserve exact identifiers and source citations without expanding obvious paths repeatedly.
- Connect technical detail to the behavior or decision it explains.
- Distinguish documented intent, observed code behavior, and inference.
- Check that the reader can identify the feature's purpose, relevant flow, and uncertainty. Add a closing summary only if it helps a long artifact.

Examples:

| Dense | Concrete |
|---|---|
| Intent-anchored bidirectional traceability | Read the spec and code together to see whether the implementation matches the requirement. |
| Idempotency prevents duplicate submissions | The same request identifier lets the server recognize a retry and avoid creating the item twice. |
