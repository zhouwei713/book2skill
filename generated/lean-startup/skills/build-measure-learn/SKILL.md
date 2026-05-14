---
name: build-measure-learn
description: The user wants to run an iterative product learning cycle. Use when the user wants to apply The Lean Startup's Build Measure Learn method to produce A Build Measure Learn cycle plan and learning record..
---

# 构建测量学习循环

This skill helps the user turn an idea into a measurable experiment and convert results into a decision.

Source material: The Lean Startup
Source creator: Eric Ries
Confidence: high

## When to Use

1. The user wants to run an iterative product learning cycle.
2. The user needs to turn an idea into a measurable experiment and convert results into a decision.
3. The user wants an output such as: A Build Measure Learn cycle plan and learning record..

## Inputs to Collect

Ask for missing information only when it is necessary.

```json
{
  "hypothesis": "",
  "build_plan": "",
  "metric": "",
  "data_source": "",
  "decision_rule": "",
  "timeline": ""
}
```

## Process

### 1. Build

Translate the hypothesis into the smallest build action that can generate real user evidence.

### 2. Measure

Define actionable metrics, collection method, sample, and observation period.

### 3. Learn

Interpret the results against the pre-set decision rule. Summarize what has been validated or invalidated.

### 4. Shorten the loop

Suggest ways to reduce cost, time, and complexity in the next cycle.

## Output Format

```markdown
# 构建测量学习循环 Result

## Context

## Inputs

## Analysis

## Recommended Actions

## Risks

## Next Step

Expected output: A Build Measure Learn cycle plan and learning record.
```

## Quality Rules

1. Keep the method practical.
2. Do not invent claims that are unsupported by the source pack.
3. Explain assumptions clearly.
4. If evidence is weak, say so.
5. Prefer concrete actions over abstract advice.

## Source Note

Source: The Lean Startup
Creator: Eric Ries
Evidence basis: Core Lean Startup feedback loop.
Evidence sources: source-pack:publisher, source-pack:author-interview
Risk notes: Keep metrics actionable and avoid vanity metrics.
