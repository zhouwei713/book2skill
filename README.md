<div align="center">

# Book2Skill

把长资料里的方法论，沉淀成可调用的 Agent Skills

![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-OpenClaw-blue)
![Platform](https://img.shields.io/badge/Platform-Claude%20Code-purple)
![Skill](https://img.shields.io/badge/Skill-book2skill-green)
![Source](https://img.shields.io/badge/Source--Grounded-Yes-brightgreen)

从书籍、课程、文章合集或逐字稿出发，生成有证据、有步骤、可复用的技能

</div>

## 中文说明

Book2Skill 是一个 Codex skill，用于把书籍、课程文稿、文章合集、播客逐字稿、工作坊笔记、报告、手册等长资料转换为有来源依据、可安装、可复用的 Agent Skills。

它适合处理包含实用方法、框架、清单、练习、决策模型、产品方法、管理系统或可重复思考工具的资料。最终产物是可执行的技能包，包含清晰的触发场景、输入、步骤、输出格式和来源说明。

## 它能做什么

1. 确认资料身份，避免混淆同名书、课程、节目、文章系列和不同版本。
2. 建立 `source-pack.json`，记录来源、可信度和用途。
3. 抽取资料中的候选方法论。
4. 筛选可以真正执行的方法，生成独立 skill。
5. 校验 `methodologies.json`，并可交叉检查来源引用。
6. 使用模板生成标准 `SKILL.md` 文件。
7. 将生成的 skill 文件夹打包为 `.skill.zip`。

## 核心特性

1. 支持只给资料名称、上传文件、名称加文件三种工作流。
2. 上传资料不限于书籍，也支持课程文稿、文章合集、播客逐字稿、工作坊笔记、报告、手册和内部文档。
3. 面向公开网络资料时优先使用英文来源。
4. 使用稳定来源 id，方便方法论引用证据。
5. 提供结构化 schema、提示词、模板和脚本。
6. 内置 Lean Startup 示例，便于理解完整产物。
7. 适合上传到 GitHub 作为可分发 skill 项目。

## 安装

复制 `book2skill` 文件夹到 Codex skills 目录：

```bash
~/.codex/skills/book2skill
```

Windows 默认路径通常是：

```powershell
C:\Users\<User>\.codex\skills\book2skill
```

校验 skill：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/book2skill
```

## 使用示例

```text
Use $book2skill to turn The Lean Startup into a source-grounded skill pack.
```

```text
Use $book2skill to extract practical methods from this uploaded PDF and generate installable skills.
```

```text
Use $book2skill to convert Atomic Habits into six reusable Agent Skills with source notes.
```

```text
Use $book2skill to turn these podcast transcripts into reusable workflow skills.
```

```text
Use $book2skill to extract practical frameworks from this course transcript collection.
```

## 常用命令

校验方法论数据：

```bash
python scripts/validate_methodologies.py examples/lean-startup/methodologies.json examples/lean-startup/source-pack.json
```

生成 skills：

```bash
python scripts/generate_skills.py examples/lean-startup/methodologies.json generated/lean-startup
```

打包生成的 skills：

```bash
python scripts/package_skills.py generated/lean-startup dist
```

如果生成的 skill 含有中文标题，在 Windows 上校验时建议启用 UTF8：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\<User>\.codex\skills\.system\skill-creator\scripts\quick_validate.py generated\lean-startup\skills\mvp
```

## 目录结构

```text
book2skill/
  SKILL.md
  README.md
  agents/
    openai.yaml
  templates/
    skill_template.md
    methodology_list_template.md
    install_template.md
    quality_report_template.md
  schemas/
    methodology.schema.json
    source_pack.schema.json
  prompts/
    research_prompt.md
    extraction_prompt.md
    generation_prompt.md
    review_prompt.md
  scripts/
    validate_methodologies.py
    generate_skills.py
    package_skills.py
  examples/
    lean-startup/
```

## English

Book2Skill is a Codex skill that converts books, course transcripts, article collections, podcast transcripts, workshop notes, reports, manuals, and other long-form source materials into source-grounded, installable Agent Skills.

It works best for source materials with practical methods, frameworks, checklists, exercises, decision models, product playbooks, management systems, or repeatable thinking tools. The output is a reusable skill pack with clear triggers, inputs, steps, output formats, and source notes.

## What It Does

1. Confirms the source identity.
2. Builds a `source-pack.json` file with evidence, trust levels, and usage notes.
3. Extracts candidate methodologies.
4. Selects practical methods that can become skills.
5. Validates `methodologies.json` and can cross-check source references.
6. Generates standard `SKILL.md` files from templates.
7. Packages generated skill folders as `.skill.zip` files.

## Features

1. Supports title-only, uploaded-file, and mixed workflows.
2. Supports uploaded books, course transcripts, article collections, podcast transcripts, workshop notes, reports, manuals, and internal docs.
3. Uses English-first source research for public web evidence.
4. Uses stable source ids for evidence references.
5. Includes schemas, prompts, templates, and scripts.
6. Includes a Lean Startup example pack.
7. Ready for GitHub distribution.

## License

MIT
