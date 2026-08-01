# Install learn-codebase

<details>
<summary><strong>Claude Code</strong></summary>

### Install

```bash
claude plugin marketplace add cskwork/learn-codebase
claude plugin install learn-codebase@learn-codebase
```

Type `/learn-codebase`.

### Verify

```bash
claude plugin list
```

### Update

```bash
claude plugin marketplace update learn-codebase
```

### Uninstall

```bash
claude plugin uninstall learn-codebase
claude plugin marketplace remove learn-codebase
```

</details>

<details>
<summary><strong>Codex</strong></summary>

### Install

```bash
codex plugin marketplace add cskwork/learn-codebase --ref main
codex plugin add learn-codebase@learn-codebase
```

Type `$learn-codebase`.

### Verify

```bash
codex plugin list
```

### Uninstall

```bash
codex plugin remove learn-codebase
codex plugin marketplace remove learn-codebase
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

### Install (extension, always-on)

```bash
gemini extensions install https://github.com/cskwork/learn-codebase
```

### Install (command, opt-in)

```bash
mkdir -p ~/.gemini/commands
curl -fsSL https://raw.githubusercontent.com/cskwork/learn-codebase/main/skills/learn-codebase/agents/gemini.toml \
  -o ~/.gemini/commands/learn-codebase.toml
```

Type `/learn-codebase` in a new session.

### Verify

```bash
gemini extensions list
```

### Uninstall

```bash
gemini extensions uninstall learn-codebase
```

</details>

<details>
<summary><strong>Cursor, OpenCode, Amp, and other agent-skills harnesses</strong></summary>

### Install

```bash
npx skills add cskwork/learn-codebase
npx skills add cskwork/learn-codebase -g
```

Type `/learn-codebase` in a new agent chat.

### Verify

```bash
npx skills list
```

### Update

```bash
npx skills update learn-codebase
```

### Uninstall

```bash
npx skills remove learn-codebase
```

</details>

<details>
<summary><strong>Antigravity (agy)</strong></summary>

### Install

```bash
agy plugin install https://github.com/cskwork/learn-codebase
```

### Verify

```bash
agy plugin list
```

### Uninstall

```bash
agy plugin uninstall learn-codebase
```

</details>
