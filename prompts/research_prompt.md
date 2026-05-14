# Research Prompt

Use this prompt when the user only provides the title or name of a source, such as a book, course, article series, podcast, report, or manual.

## Task

Research the source using English-language sources. Confirm the source identity, build a source pack, and identify candidate methodologies that can become AI Agent Skills.

## Requirements

1. Confirm title, creator, publisher or platform, publication year, edition or version, content type, and ISBN when relevant.
2. Use official pages, creator pages, interviews, tables of contents, syllabi, episode lists, article indexes, and reputable English-language reviews first.
3. Do not use Chinese-language sources unless the user explicitly asks for them.
4. Avoid relying on generic low-quality summaries as the main evidence.
5. Record every source in `source-pack.json` with a stable lowercase kebab-case `id`.
6. Mark uncertainty clearly.

## Search queries

```text
"{source_title}" author
"{source_title}" creator
"{source_title}" publisher
"{source_title}" platform
"{source_title}" ISBN
"{source_title}" official page
"{source_title}" table of contents
"{source_title}" syllabus
"{source_title}" episode list
"{source_title}" article series
"{source_title}" framework
"{source_title}" methodology
"{source_title}" key concepts
"{source_title}" principles
"{source_title}" checklist
"{source_title}" exercises
"{creator_name}" "{source_title}" interview
```

## Output

Return:

1. Source identity
2. Source pack
3. Candidate methodologies
4. Research gaps
