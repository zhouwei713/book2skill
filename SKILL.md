---
name: book2skill
description: Convert books, course transcripts, article collections, podcast transcripts, workshop notes, reports, manuals, or other methodology-rich source materials into source-grounded installable Agent Skills. Use when the user wants to extract practical methods, frameworks, checklists, exercises, decision models, product playbooks, management systems, or repeatable thinking tools from long-form material and package them as reusable skills.
---

# Book2Skill

Turn a book or long-form source material into a reusable skill pack. The output is a set of operational skills, not a normal summary.

Only create a skill when the method can be triggered, executed, and evaluated. Keep concepts, stories, quotes, episodes, cases, examples, and weakly sourced ideas in the methodology list as background.

## Inputs

Use one of these workflows:

1. Title only: verify the book or named material identity with reliable English sources, then build the evidence base.
2. Uploaded material: treat uploaded books, course transcripts, article collections, podcast transcripts, workshop notes, reports, manuals, or docs as primary evidence.
3. Title plus uploaded material: use the uploaded material as primary evidence and external sources only for identity, creator context, and missing metadata.

## Workflow

### 1. Confirm identity

For title only or mixed workflows, search with English queries:

```text
"{book_title}" author
"{book_title}" ISBN
"{book_title}" publisher
"{book_title}" official book page
"{book_title}" table of contents
"{book_title}" "{author_name}"
```

Record title, English title if different, author or creator, publisher or platform, publication year, edition or version, ISBN when relevant, content type, and identity confidence.

If there are multiple plausible sources, ask the user to choose before extracting methods.

### 2. Build source pack

Prioritize:

1. Publisher, platform, creator, or official source page
2. Author or creator site, interview, talk, newsletter, course page, or official notes
3. Table of contents, syllabus, episode list, article index, module list, or preview
4. Reputable English reviews from media, universities, business schools, professional blogs, or specialist publications
5. High quality English summaries and notes

Avoid low trust sources as primary evidence. Do not use Chinese sources unless the user explicitly asks for them.

Create `source-pack.json` with source id, title, URL, source type, trust level, used for, and notes. Use lowercase kebab-case ids so methodologies can cite sources as `source-pack:{id}`.

### 3. Extract candidate methodologies

Search and scan for repeatable structures:

```text
framework, model, loop, cycle, law, principle, checklist, canvas, matrix,
scorecard, playbook, habit, protocol, decision tree, diagnostic question,
worksheet, exercise, ritual, review process
```

For each candidate, record:

```json
{
  "skill_name": "lowercase-kebab-case",
  "name_en": "",
  "name_cn": "",
  "trigger_scenario": "",
  "core_goal": "",
  "inputs": [],
  "steps": [{"name": "", "instruction": ""}],
  "expected_output": "",
  "source_basis": "",
  "evidence_sources": [],
  "confidence": "high | medium | low",
  "risk_notes": ""
}
```

### 4. Select skills

Approve a candidate only when all are true:

1. It maps to a real user situation.
2. It has clear inputs and outputs.
3. It can be run as concrete steps.
4. It is reusable across cases.
5. It is distinct from other selected methods.
6. The source basis is clear enough to explain.

Recommended limits:

```text
Short material or single article set: 2 to 4 skills
Small book or compact course: 3 to 5 skills
Normal method book, course, or transcript set: 6 to 10 skills
Dense business, technical, or multi-part source: 8 to 12 skills
Default maximum: 12 skills
```

### 5. Generate package

Deliver:

```text
{source_slug}/
  source-pack.json
  methodologies.json
  methodology-list.md
  quality-report.md
  install.md
  skills/
    {skill_name}/
      SKILL.md
```

Use `scripts/validate_methodologies.py` before generation. When a source pack exists, pass it as the second argument:

```bash
python scripts/validate_methodologies.py methodologies.json source-pack.json
```

Generate skills:

```bash
python scripts/generate_skills.py methodologies.json ./generated-book-pack
```

Package generated skills:

```bash
python scripts/package_skills.py ./generated-book-pack ./dist
```

## Quality rules

1. Summarize copyrighted source material instead of copying it.
2. Mark weak evidence and missing chapter references clearly.
3. Prefer specific outputs such as plans, checklists, scorecards, decision records, and review tables.
4. Ask for missing information only when it blocks execution.
5. Keep generated skill frontmatter to `name` and `description`; put source metadata in the body.
6. Do not fabricate a full pack when sources are insufficient. Provide a limited draft with gaps.
