# skills

Claude skills, audited and rewritten.

Most skills in the wild are copies of copies: someone finds one, clones it into their repo, and the next person clones that. The same skill turns up dozens of times, usually with a few edits, a different name, a missing companion file, or a number nobody measured. This repository holds one canonical version of each useful skill, built from the best of the versions that exist, with every source cited.

**Each skill here is a rewrite, not a copy.** Open `skills/<name>/SOURCES.md` to see which repositories it came from (at which commit), what was taken from each, what was changed or dropped, and what was wrong with the sources.

Browse them, with search and the full text of each, at **https://www.bearbrown.co/skills**.

## Skills

<!-- skills:start -->
| Skill | What it does |
|---|---|
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/SKILL.md) | Split two or more truly independent problems across parallel agents or workers, one focused brief each, then integrate and verify the combined result |
| [`receiving-code-review`](skills/receiving-code-review/SKILL.md) | Handle review feedback with technical rigor - verify each comment against the code before acting on it, ask about anything unclear, and push back with evidence when it is wrong |
| [`requesting-code-review`](skills/requesting-code-review/SKILL.md) | Get a change independently reviewed against its requirements before it moves on |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Find the root cause of a bug before changing any code |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Drive a feature, bug fix, refactor or behavior change with strict red-green-refactor - write one failing test, watch it fail for the right reason, write the least code that passes, then clean up while green |
<!-- skills:end -->

## Use a skill

**Claude Code:** copy a folder into `~/.claude/skills/`.

```bash
git clone https://github.com/nikbearbrown/skills
cp -R skills/skills/test-driven-development ~/.claude/skills/
```

**Claude.ai:** zip the skill's folder and upload it under Settings, then Skills.

**Anywhere else:** `SKILL.md` is plain Markdown. Paste it as the system prompt or the first message.

## How they are made

See [REFACTOR.md](REFACTOR.md). In short: skills come from the auditor's ledger of public repositories, grouped into families of near-duplicates; only permissively licensed sources are used; each source is read and audited; one canonical skill is written; and the citation is generated from the audit record, never typed by hand.

`python3 tools/build.py` validates every skill and rebuilds `index.json` and `NOTICE.md`.

## License

MIT. The sources these skills were refactored from carry their own notices, reproduced in [NOTICE.md](NOTICE.md).
