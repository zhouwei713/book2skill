---
name: pivot
description: The user has product evidence and wants to decide whether to change direction. Use when the user wants to apply The Lean Startup's Pivot method to produce A pivot diagnosis report with evidence, failed assumption, recommended pivot, risks, and next validation experiment..
---

# 转型决策

This skill helps the user diagnose whether to persevere, iterate, or make a strategic pivot.

Source material: The Lean Startup
Source creator: Eric Ries
Confidence: high

## When to Use

1. The user has product evidence and wants to decide whether to change direction.
2. The user needs to diagnose whether to persevere, iterate, or make a strategic pivot.
3. The user wants an output such as: A pivot diagnosis report with evidence, failed assumption, recommended pivot, risks, and next validation experiment..

## Inputs to Collect

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

## Output Format

```markdown
# 转型决策 Result

## Context

## Inputs

## Analysis

## Recommended Actions

## Risks

## Next Step

Expected output: A pivot diagnosis report with evidence, failed assumption, recommended pivot, risks, and next validation experiment.
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
Evidence basis: Lean Startup pivot and persevere decision logic.
Evidence sources: source-pack:publisher, source-pack:author-interview
Risk notes: Do not recommend a pivot only because growth is temporarily slow.
