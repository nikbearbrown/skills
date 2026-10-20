# Sources: receiving-code-review

**This skill is a rewrite, not a copy.** It keeps the upstream principle (verify before implementing, no performative agreement) and tightens the process with a decision record and source-specific handling from stronger variants.

Written by Nik Bear Brown with Claude, refactored from the sources below. Each source was fetched at the pinned commit the auditor recorded (github.com/nikbearbrown/github-claude-plugins), and each is MIT, Apache-2.0 or similarly permissive. Attribution is in the repository NOTICE.

## Derived from

| Source | File | Commit | License | What it contributed |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/receiving-code-review/SKILL.md) | `skills/receiving-code-review/SKILL.md` | `44c9b2d6e8` | MIT | Primary basis |
| [yimwoo/hotl-plugin](https://github.com/yimwoo/hotl-plugin/blob/d86bf87181adcef822c091f544c0a313ddbb40a7/skills/receiving-code-review/SKILL.md) | `skills/receiving-code-review/SKILL.md` | `d86bf87181` | MIT | Added ideas |
| [brunob54/superpowers-orchestrator](https://github.com/brunob54/superpowers-orchestrator/blob/90017a876a4d044934c9adcc7844a8cf1e34044d/skills/receiving-code-review/SKILL.md) | `skills/receiving-code-review/SKILL.md` | `90017a876a` | MIT | Added ideas |

## What was taken

- **obra/superpowers**: the six-step sequence, no agreement before verification, stop on anything unclear, source-specific handling, the "implement it properly" check, order of work, when and how to push back, how to correct a wrong pushback, the common-mistakes table and the examples.
- **yimwoo/hotl-plugin**: treat feedback as input to evaluate, re-check findings against the current code if it changed since the review, the accept/reject/defer decision with recorded evidence, severity from an automated reviewer as a first guess only, and escalating a conflict with an approved decision instead of overriding it.
- **brunob54/superpowers-orchestrator**: ordering fixes by effect (correctness and security first), treating Critical and High security findings as blocking, and the closing report of addressed items, deferrals, verification and remaining risks.

## What was changed

- The description says what the skill does and what it is not for. Upstream's describes the behavior but not the job.
- Softened "never any gratitude, ever" to "no agreement before you have verified". Once the reviewer is checked and right, a short factual acknowledgment is allowed. This is a judgment call: the upstream rule is the author's stylistic preference, and its own examples allow "Good catch - [issue]. Fixed in [location]".
- Replaced "your human partner" with "the person you work for", and removed the quoted personal rules attributed to that person.
- Added the accept, reject or defer decision with recorded evidence, and a closing report.
- Removed the marker "explicit instruction-file violation", which refers to the original author's private instructions.

## What was dropped

- The HOTL-specific contract vocabulary (intent contract, risk level, gates) from yimwoo/hotl-plugin, which only applies inside that system.
- The routing language from brunob54/superpowers-orchestrator ("routed by using-superpowers").

## Audit findings on the sources

Problems found while reading them, so the next reader of a source knows what to watch for.

- **obra/superpowers**: Calls "ANY gratitude expression" forbidden yet its own good examples include "Good catch - [specific issue]. Fixed". It quotes rules attributed to "your human partner" and mentions an "explicit instruction-file violation" that only make sense inside the author's setup.
- **yimwoo/hotl-plugin**: Good decision-record idea, but built on HOTL contracts (intent contract, success_criteria, risk_level, gates) that exist only in that plugin.
- **brunob54/superpowers-orchestrator**: Shorter and clear, but relies on another skill routing feedback to it and gives no worked examples.

## Examined, not used

Permissively licensed, read, and left out of the rewrite.

- **thepragmaticbear/bearpaws**: Upstream recast in XML tags and shortened; no new ideas.
- **gylove1994/superpowers-deepseek-v4**: A variant of upstream (97% similar).
- **jnmetacode/superpowers-zh**: A Chinese translation of upstream.
- **leodorareluctant259/superpowers-zh**: A Chinese translation of upstream.
- **lsy041015/orchestra**: A short summary tied to its own workflow.
- **VictorStochero/fluxo-orca**: Identical to upstream.
- **mzored/superpowers-cc-to-codex**: A Codex-backed port (87% similar to upstream).

## Excluded by license

These carry no declared license (or a copyleft one), so under the repository policy nothing was taken from them.

- Athyrr/aikit: no license declared
- Fintama/swisper-superpowers: no license declared
- Itzalive/resistance-ai: no license declared
- lukekeith/builder: no license declared
- orkeren21/shipshape: no license declared
