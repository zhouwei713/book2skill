#!/usr/bin/env python3
"""Validate methodology JSON and optionally cross-check a source pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_SOURCE_TYPES = {"publisher", "author", "toc", "interview", "review", "summary", "other"}
VALID_TRUST_LEVELS = {"high", "medium", "low"}

REQUIRED_BOOK_FIELDS = ["title", "author"]
REQUIRED_METHODOLOGY_FIELDS = [
    "skill_name",
    "name_en",
    "name_cn",
    "trigger_scenario",
    "core_goal",
    "inputs",
    "steps",
    "expected_output",
    "source_basis",
    "evidence_sources",
    "confidence",
]
REQUIRED_SOURCE_FIELDS = ["id", "title", "url", "source_type", "trust_level", "used_for"]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def word_count(value: str) -> int:
    return len([part for part in re.split(r"\s+", value.strip()) if part])


def source_keys(source_pack: dict[str, Any], errors: list[str]) -> set[str]:
    sources = source_pack.get("sources")
    require(isinstance(sources, list) and bool(sources), "source_pack.sources must be a non-empty list.", errors)

    keys: set[str] = set()
    if not isinstance(sources, list):
        return keys

    for index, source in enumerate(sources, start=1):
        prefix = f"source_pack.sources[{index}]"
        require(isinstance(source, dict), f"{prefix} must be an object.", errors)
        if not isinstance(source, dict):
            continue

        for field in REQUIRED_SOURCE_FIELDS:
            require(field in source and source[field] not in (None, "", []), f"{prefix} missing `{field}`.", errors)

        source_type = source.get("source_type")
        trust_level = source.get("trust_level")
        require(source_type in VALID_SOURCE_TYPES, f"{prefix}.source_type is invalid.", errors)
        require(trust_level in VALID_TRUST_LEVELS, f"{prefix}.trust_level is invalid.", errors)
        require(isinstance(source.get("used_for"), list), f"{prefix}.used_for must be a list.", errors)

        source_id = str(source.get("id", "")).strip()
        title = str(source.get("title", "")).strip()
        url = str(source.get("url", "")).strip()
        if source_id:
            require(bool(SKILL_NAME_RE.match(source_id)), f"{prefix}.id must be lowercase kebab-case.", errors)
            keys.add(source_id)
            keys.add(f"source-pack:{source_id}")
        if title:
            keys.add(title)
        if url:
            keys.add(url)
        if source_type:
            keys.add(f"source-pack:{source_type}")

    return keys


def validate(data: dict[str, Any], source_pack: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    book = data.get("book")
    require(isinstance(book, dict), "Missing or invalid `book` object.", errors)
    if isinstance(book, dict):
        for field in REQUIRED_BOOK_FIELDS:
            require(bool(book.get(field)), f"Missing book.{field}.", errors)
        confidence = book.get("identity_confidence")
        if confidence is not None:
            require(confidence in VALID_CONFIDENCE, "book.identity_confidence must be high, medium, or low.", errors)

    methodologies = data.get("methodologies")
    require(isinstance(methodologies, list) and len(methodologies) > 0, "`methodologies` must be a non-empty list.", errors)

    available_sources: set[str] = set()
    if source_pack is not None:
        available_sources = source_keys(source_pack, errors)

    seen_names: set[str] = set()
    seen_goals: set[str] = set()
    if isinstance(methodologies, list):
        for index, item in enumerate(methodologies, start=1):
            prefix = f"methodologies[{index}]"
            require(isinstance(item, dict), f"{prefix} must be an object.", errors)
            if not isinstance(item, dict):
                continue

            for field in REQUIRED_METHODOLOGY_FIELDS:
                require(field in item and item[field] not in (None, "", []), f"{prefix} missing `{field}`.", errors)

            skill_name = str(item.get("skill_name", ""))
            require(bool(SKILL_NAME_RE.match(skill_name)), f"{prefix}.skill_name must be lowercase kebab-case.", errors)
            require(skill_name not in seen_names, f"Duplicate skill_name: {skill_name}.", errors)
            seen_names.add(skill_name)

            confidence = item.get("confidence")
            require(confidence in VALID_CONFIDENCE, f"{prefix}.confidence must be high, medium, or low.", errors)

            trigger = str(item.get("trigger_scenario", "")).strip()
            core_goal = str(item.get("core_goal", "")).strip()
            expected_output = str(item.get("expected_output", "")).strip()
            source_basis = str(item.get("source_basis", "")).strip()
            require(word_count(trigger) >= 6, f"{prefix}.trigger_scenario is too vague.", errors)
            require(word_count(core_goal) >= 5, f"{prefix}.core_goal is too vague.", errors)
            require(word_count(expected_output) >= 5, f"{prefix}.expected_output is too vague.", errors)
            require(word_count(source_basis) >= 5, f"{prefix}.source_basis is too vague.", errors)

            normalized_goal = re.sub(r"\W+", " ", core_goal.lower()).strip()
            require(normalized_goal not in seen_goals, f"{prefix}.core_goal duplicates another methodology.", errors)
            seen_goals.add(normalized_goal)

            inputs = item.get("inputs")
            require(isinstance(inputs, list) and len(inputs) > 0, f"{prefix}.inputs must be a non-empty list.", errors)
            if isinstance(inputs, list):
                require(all(isinstance(value, str) and value.strip() for value in inputs), f"{prefix}.inputs must contain non-empty strings.", errors)

            steps = item.get("steps")
            require(isinstance(steps, list) and len(steps) >= 2, f"{prefix}.steps must contain at least two steps.", errors)
            if isinstance(steps, list):
                for step_index, step in enumerate(steps, start=1):
                    require(isinstance(step, dict), f"{prefix}.steps[{step_index}] must be an object.", errors)
                    if isinstance(step, dict):
                        require(bool(step.get("name")), f"{prefix}.steps[{step_index}] missing name.", errors)
                        instruction = str(step.get("instruction", "")).strip()
                        require(word_count(instruction) >= 8, f"{prefix}.steps[{step_index}].instruction is too thin.", errors)

            evidence_sources = item.get("evidence_sources")
            require(isinstance(evidence_sources, list) and len(evidence_sources) > 0, f"{prefix}.evidence_sources must be a non-empty list.", errors)
            if source_pack is not None and isinstance(evidence_sources, list):
                for source in evidence_sources:
                    if source not in available_sources:
                        warnings.append(f"{prefix}.evidence_sources entry not found in source pack: {source}")

    return errors + [f"Warning: {warning}" for warning in warnings]


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: python validate_methodologies.py <methodologies.json> [source-pack.json]")
        return 2

    try:
        data = load_json(Path(sys.argv[1]))
        source_pack = load_json(Path(sys.argv[2])) if len(sys.argv) == 3 else None
        results = validate(data, source_pack)
    except Exception as exc:
        print(f"Validation failed: {exc}")
        return 1

    errors = [item for item in results if not item.startswith("Warning:")]
    warnings = [item for item in results if item.startswith("Warning:")]

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        for warning in warnings:
            print(f"  - {warning}")
        return 1

    print("Validation passed.")
    for warning in warnings:
        print(warning)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
