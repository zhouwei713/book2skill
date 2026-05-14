---
name: mvp
description: The user wants to test a product idea with the smallest useful experiment. Use when the user wants to apply The Lean Startup's Minimum Viable Product method to produce A concise MVP experiment plan with assumption, prototype scope, metric, threshold, timeline, risk, and next action..
---

# 最小可行产品

This skill helps the user define the smallest product or experiment that can test the riskiest assumption.

Source material: The Lean Startup
Source creator: Eric Ries
Confidence: high

## When to Use

1. The user wants to test a product idea with the smallest useful experiment.
2. The user needs to define the smallest product or experiment that can test the riskiest assumption.
3. The user wants an output such as: A concise MVP experiment plan with assumption, prototype scope, metric, threshold, timeline, risk, and next action..

## Inputs to Collect

Ask for missing information only when it is necessary.

```json
{
  "idea": "",
  "target_user": "",
  "core_assumption": "",
  "success_metric": "",
  "constraints": ""
}
```

## Process

### 1. Identify the riskiest assumption

Separate the user's idea into assumptions about users, value, acquisition, payment, retention, and feasibility. Pick the assumption that can invalidate the idea fastest.

### 2. Define the smallest experiment

Design the minimum product, landing page, concierge service, prototype, manual workflow, or test that can validate the assumption.

### 3. Set the learning metric

Choose one clear success metric and one decision threshold before the experiment starts.

### 4. Decide next action

Recommend persevere, iterate, or pivot based on the expected evidence.

## Output Format

```markdown
# 最小可行产品 Result

## Context

## Inputs

## Analysis

## Recommended Actions

## Risks

## Next Step

Expected output: A concise MVP experiment plan with assumption, prototype scope, metric, threshold, timeline, risk, and next action.
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
Evidence basis: Core Lean Startup methodology commonly associated with MVP and validated learning.
Evidence sources: source-pack:publisher, source-pack:author-interview
Risk notes: Exact chapter references should be confirmed during live research.
