# Methodology Extraction Prompt

## Task

Extract practical methodologies from the source evidence. A methodology can become a skill only when it has a real trigger, input, process, output, and reusable value.

## Convert into a skill when

1. It can be called in a real user situation.
2. It has a clear input and output.
3. It can be executed step by step.
4. It can be reused across cases.
5. It has a clear source basis.
6. It is meaningfully different from the other candidates.

## Keep as background when

1. It is only a concept.
2. It is mainly a quote.
3. It is a story or example without a repeatable process.
4. It overlaps strongly with another selected method.
5. Its source basis is too weak.

## Output JSON shape

```json
{
  "book": {
    "title": "",
    "title_english": "",
    "author": "",
    "publisher": "",
    "content_type": "book | course | article_collection | podcast_transcript | workshop_notes | report | manual | other",
    "publication_year": "",
    "edition_or_version": "",
    "isbn": "",
    "identity_confidence": "high"
  },
  "methodologies": [
    {
      "skill_name": "",
      "name_en": "",
      "name_cn": "",
      "trigger_scenario": "",
      "core_goal": "",
      "inputs": [],
      "steps": [
        {"name": "", "instruction": ""}
      ],
      "expected_output": "",
      "source_basis": "",
      "evidence_sources": [],
      "confidence": "high",
      "risk_notes": ""
    }
  ]
}
```
