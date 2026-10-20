#!/usr/bin/env python3
"""Validate every skill and rebuild index.json and NOTICE.md.   Run from the repo root:  python3 tools/build.py
Checks (a failure exits 1): name equals folder; name <= 64 chars, lowercase/digits/hyphens; description present and <= 1024 chars;
license field present; SOURCES.md and sources.json exist; every source has repo, commit, license, sha256; every source license is permissive;
no Markdown link in SKILL.md points at a file that is not in the skill folder; no stray namespace prefix (superpowers: etc.).
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERMISSIVE = {'MIT', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', 'ISC', '0BSD', 'Unlicense'}
errors, index, notice = [], [], {}
for slug in sorted(os.listdir(os.path.join(ROOT, 'skills'))):
    d = os.path.join(ROOT, 'skills', slug)
    if not os.path.isdir(d): continue
    def bad(msg): errors.append(f'{slug}: {msg}')
    try: text = open(os.path.join(d, 'SKILL.md')).read()
    except FileNotFoundError: bad('no SKILL.md'); continue
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    if not m: bad('no frontmatter'); continue
    fm = {}
    for line in m.group(1).split('\n'):
        k, _, v = line.partition(':')
        if _: fm[k.strip()] = v.strip().strip('"')
    body = m.group(2)
    if fm.get('name') != slug: bad(f"name '{fm.get('name')}' differs from folder")
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', slug) or len(slug) > 64: bad('name must be lowercase letters, digits, hyphens, <= 64 chars')
    desc = fm.get('description', '')
    if not desc: bad('missing description')
    if len(desc) > 1024: bad(f'description is {len(desc)} chars (limit 1024)')
    if not fm.get('license'): bad('missing license')
    for link in re.findall(r'\]\(([^)#]+)\)', body):
        if not re.match(r'[a-z]+:', link) and not os.path.exists(os.path.join(d, link)): bad(f'links to missing file {link}')
    if re.search(r'\b(superpowers|orchestra|bp|hotl|harness):[a-z]', body): bad('contains a source-specific namespace prefix')
    try: src = json.load(open(os.path.join(d, 'sources.json')))
    except Exception: bad('no sources.json'); src = {'derivedFrom': []}
    if not os.path.exists(os.path.join(d, 'SOURCES.md')): bad('no SOURCES.md')
    if not src['derivedFrom']: bad('cites no sources')
    for s in src['derivedFrom']:
        for k in ('repo', 'commit', 'license', 'sha256'):
            if not s.get(k): bad(f"source {s.get('repo')} missing {k}")
        if s.get('license') not in PERMISSIVE: bad(f"source {s.get('repo')} license {s.get('license')} is not permissive")
        notice.setdefault(s['repo'], {'license': s['license'], 'copyright': s.get('copyright', ''), 'skills': []})['skills'].append(slug)
    index.append({'slug': slug, 'name': fm.get('name'), 'description': desc, 'license': fm.get('license'),
                  'words': len(body.split()), 'sources': [{k: s[k] for k in ('repo', 'path', 'commit', 'license', 'url')} for s in src['derivedFrom']],
                  'refactored': src.get('refactored')})
if errors:
    print('\n'.join(errors)); sys.exit(1)
json.dump(index, open(os.path.join(ROOT, 'index.json'), 'w'), indent=1, ensure_ascii=False)
lines = ['# Notice', '', 'The skills in this repository are rewrites. Each was refactored from the third-party skills listed below, all under permissive licenses, and each skill\'s `SOURCES.md` says exactly what was taken from which source. The notices below are reproduced as the licenses require.', '']
for repo, v in sorted(notice.items()):
    lines += [f'## {repo}', '', f"License: {v['license']}", f"{v['copyright']}" if v['copyright'] else '', f"Used in: {', '.join('`'+s+'`' for s in sorted(set(v['skills'])))}", f'Source: https://github.com/{repo}', '']
open(os.path.join(ROOT, 'NOTICE.md'), 'w').write('\n'.join(lines))
rd = os.path.join(ROOT, 'README.md')
if os.path.exists(rd):
    r = open(rd).read()
    table = '| Skill | What it does |\n|---|---|\n' + '\n'.join(f"| [`{e['slug']}`](skills/{e['slug']}/SKILL.md) | {e['description'].split('. ')[0].rstrip('.')} |" for e in index)
    r = re.sub(r'<!-- skills:start -->.*<!-- skills:end -->', lambda m: '<!-- skills:start -->\n' + table + '\n<!-- skills:end -->', r, flags=re.S)
    open(rd, 'w').write(r)
print(f'{len(index)} skills OK; {len(notice)} sources in NOTICE.md')
