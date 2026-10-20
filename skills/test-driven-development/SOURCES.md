# Sources: test-driven-development

**This skill is a rewrite, not a copy.** It keeps the discipline of the most widely cloned version (obra/superpowers) and adds what the better variants found missing.

Written by Nik Bear Brown with Claude, refactored from the sources below. Each source was fetched at the pinned commit the auditor recorded (github.com/nikbearbrown/github-claude-plugins), and each is MIT, Apache-2.0 or similarly permissive. Attribution is in the repository NOTICE.

## Derived from

| Source | File | Commit | License | What it contributed |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/test-driven-development/SKILL.md) | `skills/test-driven-development/SKILL.md` | `44c9b2d6e8` | MIT | Primary basis |
| [leobbaroni/cockpit](https://github.com/leobbaroni/cockpit/blob/67ad0773258f64a5e4a1bdbc0c3e7d757fc4fa84/skills/test-driven-development/SKILL.md) | `skills/test-driven-development/SKILL.md` | `67ad077325` | MIT | Added ideas |
| [j0hanz/squad-agents](https://github.com/j0hanz/squad-agents/blob/af44079009dd3f21dc2f4fd3c18807b0d2978d73/skills/test-driven-development/SKILL.md) | `skills/test-driven-development/SKILL.md` | `af44079009` | MIT | Added ideas |
| [thoughtbot/rails-consultant](https://github.com/thoughtbot/rails-consultant/blob/9807306250b2fa86886568be3a6d40cefabe5b4a/skills/test-driven-development/SKILL.md) | `skills/test-driven-development/SKILL.md` | `9807306250` | MIT | Added ideas |
| [lsy041015/orchestra](https://github.com/lsy041015/orchestra/blob/d23927aa31b1fcd1e2b2c2ac44c5e53136e27dc5/skills/test-driven-development/SKILL.md) | `skills/test-driven-development/SKILL.md` | `d23927aa31` | MIT | Added ideas |

## What was taken

- **obra/superpowers**: the core rule ("no production code without a failing test first"), the red-green-refactor cycle with good and bad examples, the verify-red and verify-green steps, the excuses table, the red-flags list, the checklist and the "when stuck" table. Every other source in this family reads as a copy, translation, adaptation or rewrite of it.
- **leobbaroni/cockpit**: why the failure matters, the "right reason" test for a red, the bug-fix-starts-with-a-test argument, the table of what actually proves a claim, and the rule that the iron law binds delegated work.
- **j0hanz/squad-agents**: the revert check (revert the implementation, expect red, restore, expect green), spikes must be thrown away and rebuilt through the cycle, never edit a test only to force a pass, and one full cycle before the next test.
- **thoughtbot/rails-consultant**: outside-in development: one change then one run, drop down a layer by writing the next failing test, and build inert glue directly. Kept framework-neutral; the Rails and RSpec specifics were left out.
- **lsy041015/orchestra**: the safety rule against deleting the user's own work, "report the evidence gap instead of claiming test-first", and the two cases where a failing test is the wrong tool (behavior-preserving refactors, docs and config).

## What was changed

- The description now says what the skill does and lists the phrases that should trigger it ("TDD", "test first", "red-green-refactor"). The upstream description was only "Use when implementing any feature or bugfix, before writing implementation code".
- Rewritten as one self-contained file with no references to companion files, other skills in a bundle, or a particular agent harness or tool.
- "Delete the code written first" became "set it aside; delete only what you wrote this session; never delete the user's own work". One source (lsy041015/orchestra) flags that the literal rule destroys real work.
- Replaced the Graphviz diagram with the numbered cycle, and the pseudo-tags around examples with plain Good and Bad labels, so it reads the same in any host.
- Added the revert check, the when-a-failing-test-is-the-wrong-tool section, and "report pre-existing failures by name" (the last from the VictorStochero/fluxo-orca fork of upstream).
- Replaced "your human partner" with "the user".

## What was dropped

- The Rails and RSpec specifics and the example-file references from thoughtbot/rails-consultant.
- The long "why order matters" essay, which repeats the excuses table; its points are kept in the table.
- Interview-the-user steps from j0hanz/squad-agents, which depend on a specific question tool.
- The upstream reference to writing-good-tests.md. Its four rules are folded into the cycle (name the change that would fail the test, assert real behavior, keep test-only code out of production, understand side effects before mocking).

## Audit findings on the sources

Problems found while reading them, so the next reader of a source knows what to watch for.

- **obra/superpowers**: The description gives only the trigger, so a model matching on "TDD" or "test first" has little to match. The skill refers to writing-good-tests.md, a file that exists only in the original repository, so a copy of the lone SKILL.md has a dangling reference. It uses a Graphviz block and <Good>/<Bad> pseudo-tags that most hosts do not render, and "your human partner" assumes a persona.
- **gylove1994/superpowers-deepseek-v4**: Adds a HARD-GATE that tells the agent to invoke a skill (confirming-worktree-before-edit) which is not part of this skill. Without that other skill present, the gate cannot be satisfied.
- **leobbaroni/cockpit**: Refers to sibling skills (diagnosing-bugs, orchestrate) that exist only in its own repository.
- **j0hanz/squad-agents**: Depends on an AskUserQuestion tool and a request-plan skill, so it is not portable outside its harness.
- **thoughtbot/rails-consultant**: Rails and RSpec specific, links to example files that are not in the skill folder, and sets disable-model-invocation so it never triggers on its own.
- **lsy041015/orchestra**: Strong ideas but compressed into dense paragraphs and tied to its own orchestra: namespace for the skills it refers to.

## Examined, not used

Permissively licensed, read, and left out of the rewrite.

- **VictorStochero/fluxo-orca**: A copy of upstream with one paragraph added, on running the project's whole suite. That paragraph is used.
- **gylove1994/superpowers-deepseek-v4**: A variant of upstream (82% similar) with a worktree hard-gate and the "why order matters" essay restored.
- **jnmetacode/superpowers-zh**: A Chinese translation of upstream.
- **leodorareluctant259/superpowers-zh**: A Chinese translation of upstream.
- **mzored/superpowers-cc-to-codex**: A port that hands implementation to a Codex tool; tied to that tool.
- **sitien173/superpowers-ccg**: A very short summary that also separates behavior-preserving refactors from changed behavior. The same point is made by orchestra and is used.
- **thepragmaticbear/bearpaws**: The upstream text recast in XML tags and shortened; no new ideas.

## Excluded by license

These carry no declared license (or a copyleft one), so under the repository policy nothing was taken from them.

- Athyrr/aikit: no license declared
- Fintama/swisper-superpowers: no license declared
- FlameMida/spec-dev: no license declared
- Itzalive/resistance-ai: no license declared
- lukekeith/builder: no license declared
- orkeren21/shipshape: no license declared
