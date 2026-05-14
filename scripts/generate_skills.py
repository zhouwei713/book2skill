#!/usr/bin/env python3
"""Generate skill folders from a methodologies JSON file."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "skill_template.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def markdown_list(items: list[str]) -> str:
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, start=1))


def render_steps(steps: list[dict[str, str]]) -> str:
    chunks: list[str] = []
    for index, step in enumerate(steps, start=1):
        name = str(step.get("name", "")).strip()
        instruction = str(step.get("instruction", "")).strip()
        chunks.append(f"### {index}. {name}\n\n{instruction}")
    return "\n\n".join(chunks)


def render_inputs(inputs: list[str]) -> str:
    payload = {key: "" for key in inputs}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_output_format(name: str, expected_output: str) -> str:
    return f"""# {name} Result

## Context

## Inputs

## Analysis

## Recommended Actions

## Risks

## Next Step

Expected output: {expected_output}"""


def clean_yaml_value(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().replace('"', "'")


def replace_all(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def render_skill(template: str, book: dict[str, Any], method: dict[str, Any]) -> str:
    title = str(book.get("title", "")).strip()
    author = str(book.get("author", "")).strip()
    skill_name = str(method["skill_name"]).strip()
    name_en = str(method.get("name_en", skill_name)).strip()
    name_cn = str(method.get("name_cn", "")).strip()
    methodology_name = name_cn or name_en
    trigger = str(method.get("trigger_scenario", "")).strip()
    core_goal = str(method.get("core_goal", "")).strip()
    expected_output = str(method.get("expected_output", "")).strip()
    confidence = str(method.get("confidence", "medium")).strip()

    description = clean_yaml_value(
        f"{trigger} Use when the user wants to apply {title}'s {name_en} method to produce {expected_output}."
    )

    when_items = [
        trigger,
        f"The user needs to {core_goal}.",
        f"The user wants an output such as: {expected_output}.",
    ]

    evidence_sources = method.get("evidence_sources", [])
    values = {
        "skill_name": skill_name,
        "description": description,
        "methodology_name": methodology_name,
        "core_goal": core_goal,
        "book_title": title,
        "author": author,
        "confidence": confidence,
        "when_to_use": markdown_list([item for item in when_items if item]),
        "inputs_json": render_inputs(method.get("inputs", [])),
        "process_steps": render_steps(method.get("steps", [])),
        "output_format": render_output_format(methodology_name, expected_output),
        "source_basis": str(method.get("source_basis", "")).strip(),
        "evidence_sources": ", ".join(str(item) for item in evidence_sources),
        "risk_notes": str(method.get("risk_notes", "")).strip() or "None recorded.",
    }
    return replace_all(template, values).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python generate_skills.py <methodologies.json> <output_dir>")
        return 2

    try:
        data = load_json(Path(sys.argv[1]))
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"Generation failed: {exc}")
        return 1

    output_dir = Path(sys.argv[2])
    skills_dir = output_dir / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)

    book = data.get("book", {})
    count = 0
    for method in data.get("methodologies", []):
        skill_name = method["skill_name"]
        skill_dir = skills_dir / skill_name
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(render_skill(template, book, method), encoding="utf-8")
        count += 1

    (output_dir / "methodologies.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {count} skills in {skills_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
