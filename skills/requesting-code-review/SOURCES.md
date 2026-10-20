# Sources: requesting-code-review

**This skill is a rewrite, not a copy.** It keeps the upstream idea (get a reviewer who has only the work product, early and often), makes it reviewer-agnostic, and adds what stronger variants require of a review.

Written by Nik Bear Brown with Claude, refactored from the sources below. Each source was fetched at the pinned commit the auditor recorded (github.com/nikbearbrown/github-claude-plugins), and each is MIT, Apache-2.0 or similarly permissive. Attribution is in the repository NOTICE.

## Derived from

| Source | File | Commit | License | What it contributed |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/requesting-code-review/SKILL.md) | `skills/requesting-code-review/SKILL.md` | `44c9b2d6e8` | MIT | Primary basis |
| [brunob54/superpowers-orchestrator](https://github.com/brunob54/superpowers-orchestrator/blob/90017a876a4d044934c9adcc7844a8cf1e34044d/skills/requesting-code-review/SKILL.md) | `skills/requesting-code-review/SKILL.md` | `90017a876a` | MIT | Added ideas |
| [thepragmaticbear/bearpaws](https://github.com/thepragmaticbear/bearpaws/blob/9141dd043814d5e5c292d5d9c619adbdffdc4a05/skills/requesting-code-review/SKILL.md) | `skills/requesting-code-review/SKILL.md` | `9141dd0438` | MIT | Added ideas |
| [lsy041015/orchestra](https://github.com/lsy041015/orchestra/blob/d23927aa31b1fcd1e2b2c2ac44c5e53136e27dc5/skills/requesting-code-review/SKILL.md) | `skills/requesting-code-review/SKILL.md` | `d23927aa31` | MIT | Added ideas |

## What was taken

- **obra/superpowers**: the early-and-often principle, when to request, fixing a base and head commit, handing the reviewer crafted context instead of the session history, the Critical/Important/Minor handling, pushing back with reasoning, and the worked example.
- **brunob54/superpowers-orchestrator**: the built-in security pass and the list of changes that trigger it, "Critical and High security findings block merge", the adversarial pass for tricky logic, and the requirement that a review give severity, file references and a merge-readiness verdict.
- **thepragmaticbear/bearpaws**: the brief a reviewer needs (project conventions, verification evidence, decisions already made, unresolved concerns) and the demand that a review enumerate failure modes, state what would make its own conclusion wrong, list what it did not check, and label break attempts as executed or reasoned.
- **lsy041015/orchestra**: never call a self-review independent, include staged, unstaged and untracked changes in the range, scope a re-review to the finding and its fix, and stop retrying after two failed fixes with the same cause.

## What was changed

- The description says what the skill covers and lists the phrases that should trigger it. Upstream's was only "Use when completing tasks, implementing major features, or before merging to verify work meets requirements".
- The reviewer can be another agent, a fresh session or a person. Upstream and every variant assume a particular subagent type.
- Upstream's reviewer template lived in a separate file (code-reviewer.md). Its content is replaced by a short brief and a list of what a good review contains, written inline, so the skill stands alone. The template file itself was not read.
- Added a severity table with what to do at each level.
- Removed the "superpowers" paths and namespaces from the example.

## What was dropped

- The red-team agent and the automatic fix pipeline from brunob54/superpowers-orchestrator, which need that repository's agents.
- The context-snapshot.json handling from the same source, which is specific to its tooling.
- The review-package helper script and ledger from lsy041015/orchestra.
- The coordinator-context-budget argument for dispatching a reviewer. The independence argument is kept.

## Audit findings on the sources

Problems found while reading them, so the next reader of a source knows what to watch for.

- **obra/superpowers**: The description gives only the trigger. The reviewer template is in a separate file (code-reviewer.md) that a lone copy does not have, and the skill assumes a "general-purpose subagent" exists. It does not say what a usable review must contain.
- **brunob54/superpowers-orchestrator**: Routed by other skills of its own (using-superpowers, executing-plans), reads a context-snapshot.json that only its tooling writes, and dispatches its own named reviewer and red-team agents.
- **thepragmaticbear/bearpaws**: Dispatches a bp:code-reviewer agent and the strict "four named gates" format only works with that agent's template. The idea is sound and is kept in a portable form.
- **lsy041015/orchestra**: Depends on a review-package helper that needs a plan file and on orchestra: skill names, and mixes tool names for two different hosts in one step.

## Examined, not used

Permissively licensed, read, and left out of the rewrite.

- **gylove1994/superpowers-deepseek-v4**: A variant of upstream (83% similar).
- **jnmetacode/superpowers-zh**: A Chinese translation of upstream.
- **leodorareluctant259/superpowers-zh**: A Chinese translation of upstream.
- **mzored/superpowers-cc-to-codex**: A Codex-backed port, tied to those tools.

## Excluded by license

These carry no declared license (or a copyleft one), so under the repository policy nothing was taken from them.

- Athyrr/aikit: no license declared
- Fintama/swisper-superpowers: no license declared
- Itzalive/resistance-ai: no license declared
- orkeren21/shipshape: no license declared
