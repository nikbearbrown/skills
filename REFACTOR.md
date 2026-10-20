# The refactor

A second audit. The first one is the auditor's static scan of every public repository that contains a skill. This one reads the skills themselves, groups the ones that do the same job, and writes one canonical version.

## 1. Find

Every skill the auditor recorded: a `SKILL.md` in a repository that cleared its static checks. The ledger (`github-claude-plugins`) gives the repository, the file path, the commit the auditor pinned, and the skill's description. It does not hold the skill body, which is fetched at that pinned commit.

## 2. Is it worth a canonical version?

There is no count to hit. A skill is worth refactoring when it is a recurring job, general rather than tied to one repository or one vendor's product, and more than a one-line instruction. A skill that only makes sense inside its own plugin is left alone.

## 3. Group into families

Skills that claim the same job are grouped by name and description, then confirmed by reading the bodies. Inside a family, work out the lineage: which version the others copy, which are translations, which are ports to a particular tool, which add something real. Exact copies are found by SHA-256; near copies by text similarity.

## 4. Gate on license

Only sources under MIT, Apache-2.0, BSD, ISC or similar permissive licenses are used. Skills with no declared license, or a copyleft one, are listed in the family's `SOURCES.md` under "Excluded by license" and nothing is taken from them.

## 5. Fetch

Text only, at the pinned commit, into a quarantine folder. Nothing fetched is executed.

## 6. Audit each source

For every source read, check and record:

- **Trigger quality.** Does the description say what the skill does and when to use it, with the phrases a person would actually type? Is there a "not for" clause where confusion is likely?
- **Self-contained.** Does it point to companion files, other skills in a bundle, a plugin namespace, or a specific agent harness that a lone copy does not have?
- **Unsupported claims.** Any statistic, timing or success rate with no stated basis.
- **Safety.** Instructions that destroy the user's work, skip confirmation for irreversible steps, or hide actions.
- **Consistency.** Examples that contradict the rules around them, and references to sections that do not exist.
- **Portability.** Diagrams or markup most hosts do not render, tool names that only one host has.
- **Size.** Padding that repeats the same point, or a skill so long that loading it costs more than it saves.

## 7. Write the canonical skill

Start from the strongest source. Add what the better variants found that it missed. Fold companion material in, so the skill stands alone. Replace unsupported claims with the qualitative point or drop them. Write the description last: what it does, when it applies, the phrases that should trigger it, and what it is not for, within 1,024 characters.

## 8. Cite

`SOURCES.md` and `sources.json` are generated from a small spec by `auditor/skill-triage/refactor/sources.py` in the working repository, so the commit, license and SHA-256 come from the audit record and are never typed. They list: each source and what it contributed; what was taken, changed and dropped; the findings on each source; the family members that were read and not used; and the sources excluded by license.

## 9. Validate and publish

`python3 tools/build.py` must pass: names match folders, descriptions fit, every source is cited with a commit and a permissive license, no link points at a missing file, and no source-specific namespace is left in the text. Then the skill goes to https://www.bearbrown.co/skills with its citation.

## What this does not claim

A rewrite is not a test. The skills are not run against benchmarks, and the site labels them "not audited" by the auditor pipeline. They are a reading of the sources, written down carefully, with the sources named so you can check.
