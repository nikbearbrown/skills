# Sources: systematic-debugging

**This skill is a rewrite, not a copy.** It keeps the four-phase process of the version most others derive from (obra/superpowers), makes it stand alone, and removes claims no source backs up.

Written by Nik Bear Brown with Claude, refactored from the sources below. Each source was fetched at the pinned commit the auditor recorded (github.com/nikbearbrown/github-claude-plugins), and each is MIT, Apache-2.0 or similarly permissive. Attribution is in the repository NOTICE.

## Derived from

| Source | File | Commit | License | What it contributed |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/systematic-debugging/SKILL.md) | `skills/systematic-debugging/SKILL.md` | `44c9b2d6e8` | MIT | Primary basis |
| [phmatray/ai-migration-kit](https://github.com/phmatray/ai-migration-kit/blob/d84cb9774909e885529047fd82821fa16740a0f0/skills/systematic-debugging/SKILL.md) | `skills/systematic-debugging/SKILL.md` | `d84cb97749` | MIT | Structure and wording |
| [lsy041015/orchestra](https://github.com/lsy041015/orchestra/blob/d23927aa31b1fcd1e2b2c2ac44c5e53136e27dc5/skills/systematic-debugging/SKILL.md) | `skills/systematic-debugging/SKILL.md` | `d23927aa31` | MIT | Added idea |

## What was taken

- **obra/superpowers**: the rule (no fix without a root cause), the four phases, instrumenting component boundaries, the three-failed-fixes-means-question-the-design rule, the red-flags list, the excuses table and the quick reference.
- **phmatray/ai-migration-kit**: the framing that a symptom fix hides the cause, the sharper trigger description with an explicit "not for" clause, the point that "I don't understand yet" is the correct starting state, the "no single cause is a legitimate result, but check you did not stop early" section, and the list of companion techniques (tracing, defense in depth, condition-based waiting, bisecting for a polluting test).
- **lsy041015/orchestra**: when you were handed the work, report blocked with the evidence instead of making a fourth attempt.

## What was changed

- The description says what the skill does and what it is not for, with the symptoms that should trigger it. Upstream's was only "Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes".
- The four companion techniques (tracing a value backward, defense in depth, waiting on a condition, bisecting a test that pollutes state) were separate files in the sources. They are now short sections in the skill so a lone copy is complete. These were written fresh from the one-line descriptions the sources give; the companion files themselves were not fetched or read.
- Dropped every statistic. Upstream says "95% of no-root-cause cases are incomplete investigation", and older clones add a "Real-World Impact" table of timings and success rates. No source gives a basis for any of those numbers. The qualitative point is kept.
- Fixed upstream's dangling pointer "see Phase 4.5" (the section is Phase 4, step 5), and removed the "superpowers:" namespace on the skills it names.
- Replaced "your human partner" with "the user" or "a person", and the section of user catch-phrases with the same signals in neutral wording.
- Removed the macOS code-signing example for boundary logging in favor of a description that works for any chain of components.

## What was dropped

- The "Real-World Impact" timings and success rates found in older clones (see findings).
- The worktree hard-gate added by gylove1994/superpowers-deepseek-v4, which depends on a skill that is not here.
- The Codex-delegation machinery of mzored/superpowers-cc-to-codex, which is tied to those tools.

## Audit findings on the sources

Problems found while reading them, so the next reader of a source knows what to watch for.

- **obra/superpowers**: The description gives only the trigger. The skill points to three companion files and to skills by a "superpowers:" namespace, so a lone copy has dangling references. It cites "Phase 4.5", which does not exist (the section is Phase 4, step 5). It states "95% of no-root-cause cases are incomplete investigation" with no basis given.
- **jsonlee12138/agent-team**: Adds a "Real-World Impact" section: 15 to 30 minutes versus 2 to 3 hours, and a 95% versus 40% first-time fix rate. No source or measurement is given. The same table appears in gylove1994/superpowers-deepseek-v4.
- **gylove1994/superpowers-deepseek-v4**: Adds an instruction to invoke confirming-worktree-before-edit before any edit, a skill that is not part of this one. Cannot be satisfied without it.
- **phmatray/ai-migration-kit**: Names companion files (root-cause-tracing.md, defense-in-depth.md, condition-based-waiting.md, find-polluter.sh) and says they are in the same directory, but only SKILL.md was audited, so a lone copy points at files that are not there.

## Examined, not used

Permissively licensed, read, and left out of the rewrite.

- **VictorStochero/fluxo-orca**: Upstream with only the skill names re-pointed (identical apart from two lines).
- **gylove1994/superpowers-deepseek-v4**: Upstream plus the worktree gate, an opening sentence and the unsourced statistics.
- **jnmetacode/superpowers-zh**: A Chinese translation of upstream.
- **leodorareluctant259/superpowers-zh**: A Chinese translation of upstream.
- **cheng6563/litepowers**: A short Chinese-language summary (about 1 KB).
- **jsonlee12138/agent-team**: Upstream with its skill names changed plus the unsourced statistics.
- **mzored/superpowers-cc-to-codex**: A port that hands investigation and fixes to Codex tools, invocable only on request. Its header says it diverges from upstream deliberately.
- **sitien173/superpowers-ccg**: A very short summary that leaves delegation and the regression-test cycle to other skills.
- **thepragmaticbear/bearpaws**: Upstream recast in XML tags and shortened.

## Excluded by license

These carry no declared license (or a copyleft one), so under the repository policy nothing was taken from them.

- Athyrr/aikit: no license declared
- Fintama/swisper-superpowers: no license declared
- Itzalive/resistance-ai: no license declared
- lukekeith/builder: no license declared
- orkeren21/shipshape: no license declared
