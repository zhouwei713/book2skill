---
name: pivot
description: The user has product evidence and wants to decide whether to change direction. Use when the user wants to apply The Lean Startup's Pivot method.
source_book: The Lean Startup
source_author: Eric Ries
confidence: high
---

# 转型决策

This skill helps the user diagnose whether to persevere, iterate, or make a strategic pivot. It is based on The Lean Startup by Eric Ries.

## When to use

1. The user has experiment results but growth or retention is weak.
2. The user is unsure whether to continue the current product strategy.
3. The user wants to convert customer evidence into a new direction.

## Inputs to collect

Ask for missing information only when it is necessary.

```json
{
  "current_strategy": "",
  "experiment_results": "",
  "customer_feedback": "",
  "metrics": "",
  "constraints": ""
}
```

## Process

### 1. Review evidence

Summarize what the product team has learned from users, metrics, interviews, and experiments.

### 2. Identify the failed assumption

Find which assumption no longer holds, such as value, customer segment, channel, pricing, growth, or technology.

### 3. Select pivot type

Recommend the most suitable shift, such as customer segment pivot, zoom-in pivot, zoom-out pivot, channel pivot, value capture pivot, or technology pivot.

### 4. Design the next validation

Turn the pivot recommendation into a new testable hypothesis and experiment plan.

## Output format

```markdown
# Pivot Diagnosis Report

## Current strategy

## Evidence summary

## Failed assumption

## Pivot options

## Recommended pivot

## Risks

## Next validation experiment
```

## Quality rules

1. Do not recommend a pivot without evidence.
2. Separate temporary execution problems from strategic failure.
3. Keep the new direction testable.
4. Recommend the smallest next validation step.
5. Explain uncertainty clearly.

## Source note

Book: The Lean Startup
Author: Eric Ries
Evidence basis: Lean Startup pivot and persevere decision logic.
