#!/usr/bin/env python3
"""Package generated skill folders into zip files."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


def package_skill(skill_dir: Path, dist_dir: Path) -> Path:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"Missing SKILL.md in {skill_dir}")

    output = dist_dir / f"{skill_dir.name}.skill.zip"
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(skill_dir))
    return output


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python package_skills.py <generated_pack_dir> <dist_dir>")
        return 2

    pack_dir = Path(sys.argv[1])
    dist_dir = Path(sys.argv[2])
    skills_dir = pack_dir / "skills"
    dist_dir.mkdir(parents=True, exist_ok=True)

    if not skills_dir.exists():
        print(f"No skills directory found: {skills_dir}")
        return 1

    try:
        skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
        packaged = [package_skill(skill_dir, dist_dir) for skill_dir in skill_dirs]
    except Exception as exc:
        print(f"Packaging failed: {exc}")
        return 1

    print(f"Packaged {len(packaged)} skills into {dist_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
