# Sources: dispatching-parallel-agents

**This skill is a rewrite, not a copy.** It keeps the upstream pattern (one focused worker per independent problem, dispatched together) and adds a stricter independence test and a better list of what not to delegate.

Written by Nik Bear Brown with Claude, refactored from the sources below. Each source was fetched at the pinned commit the auditor recorded (github.com/nikbearbrown/github-claude-plugins), and each is MIT, Apache-2.0 or similarly permissive. Attribution is in the repository NOTICE.

## Derived from

| Source | File | Commit | License | What it contributed |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/dispatching-parallel-agents/SKILL.md) | `skills/dispatching-parallel-agents/SKILL.md` | `44c9b2d6e8` | MIT | Primary basis |
| [brunob54/superpowers-orchestrator](https://github.com/brunob54/superpowers-orchestrator/blob/90017a876a4d044934c9adcc7844a8cf1e34044d/skills/dispatching-parallel-agents/SKILL.md) | `skills/dispatching-parallel-agents/SKILL.md` | `90017a876a` | MIT | Added ideas |
| [lsy041015/orchestra](https://github.com/lsy041015/orchestra/blob/d23927aa31b1fcd1e2b2c2ac44c5e53136e27dc5/skills/dispatching-parallel-agents/SKILL.md) | `skills/dispatching-parallel-agents/SKILL.md` | `d23927aa31` | MIT | Added ideas |

## What was taken

- **obra/superpowers**: the principle, the four-step pattern (split into domains, write focused briefs, dispatch together, review and integrate), the brief structure, the good-and-bad brief contrasts, the example brief and the worked case.
- **brunob54/superpowers-orchestrator**: the three-condition decision check with "otherwise run sequentially", "do not use for content relay" (worker replies are compressed, so fetch raw content yourself), dispatching all workers in one step, never forwarding session history, running the full suite plus cross-domain checks before calling the work complete, and the risks list.
- **lsy041015/orchestra**: the boundary checklist, "worker reports are evidence, not approval", "do not use for exploration, planning, diagnosis, review or a second opinion", workers do not start workers, and stop retrying after two failed fixes with the same cause.

## What was changed

- The description says what the skill does and what it is not for. Upstream's was "Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies".
- Made it host-neutral: "workers" and "agents" instead of a specific subagent tool or call syntax.
- Replaced the Graphviz decision diagram with a plain checklist of conditions.
- Added the instruction to read every actual diff, not only each worker's summary.
- Removed the preset model names, the plugin namespaces and the cache-TTL discussion, which are specific to particular hosts and vendors.

## What was dropped

- The "skill leakage prevention" line telling workers not to invoke the originating plugin's skills, which only makes sense inside that plugin. The general version ("tell each worker it is a focused worker with one job") is kept.
- The model-tier routing, ledger and Ruling mechanics from lsy041015/orchestra.
- The prompt-cache rationale from brunob54/superpowers-orchestrator, which depends on a particular API and a five-minute default that may change.
- The "Key Benefits" and "Time saved" sections found in a variant, which restate the premise.

## Audit findings on the sources

Problems found while reading them, so the next reader of a source knows what to watch for.

- **obra/superpowers**: The description gives only the trigger. The skill assumes a "general-purpose subagent" and a Graphviz renderer, and the "when not to use" guidance is scattered over two places.
- **huangbaixun/harness-engineering**: The upstream text with two changes: the name is prefixed with "harness:", and a banner requires reading harness-delta.md before use. That file is not part of the skill, so a lone copy has an instruction it cannot follow.
- **gylove1994/superpowers-deepseek-v4**: Adds an instruction to invoke confirming-worktree-before-edit, a skill that is not here, and a "Time saved" claim with no measurement.
- **brunob54/superpowers-orchestrator**: Hard-wires its own plugin name into the brief ("Do NOT invoke any skills from the superpowers-orchestrator plugin") and relies on a five-minute prompt-cache default that is vendor- and time-specific.
- **lsy041015/orchestra**: Names specific models and agent presets and defers to another skill in its own namespace. Allowed only when the user explicitly asks for parallel work, which is stricter than the other sources but makes it unusable as a general skill.

## Examined, not used

Permissively licensed, read, and left out of the rewrite.

- **jnmetacode/superpowers-zh**: A Chinese translation of upstream.
- **leodorareluctant259/superpowers-zh**: A Chinese translation of upstream.
- **mzored/superpowers-cc-to-codex**: A Codex-backed port, tied to those tools.
- **thepragmaticbear/bearpaws**: Upstream recast in XML tags and shortened.

## Excluded by license

These carry no declared license (or a copyleft one), so under the repository policy nothing was taken from them.

- Athyrr/aikit: no license declared
- Fintama/swisper-superpowers: no license declared
- Itzalive/resistance-ai: no license declared
- orkeren21/shipshape: no license declared
