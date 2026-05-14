---
name: mvp
description: The user wants to test a product idea with the smallest useful experiment. Use when the user wants to apply The Lean Startup's Minimum Viable Product method.
source_book: The Lean Startup
source_author: Eric Ries
confidence: high
---

# 最小可行产品

This skill helps the user define the smallest product or experiment that can test the riskiest assumption. It is based on The Lean Startup by Eric Ries.

## When to use

1. The user has a product idea and wants to test whether it is worth building.
2. The user is unsure which first version to build.
3. The user wants evidence before spending too much time or money.

## Inputs to collect

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

Separate the idea into assumptions about users, value, acquisition, payment, retention, and feasibility. Pick the assumption that can invalidate the idea fastest.

### 2. Define the smallest experiment

Design the minimum product, landing page, concierge service, prototype, manual workflow, or test that can validate the assumption.

### 3. Set the learning metric

Choose one clear success metric and one decision threshold before the experiment starts.

### 4. Decide next action

Recommend persevere, iterate, or pivot based on the expected evidence.

## Output format

```markdown
# MVP Experiment Plan

## Idea

## Riskiest assumption

## Target user

## Minimum experiment

## Success metric

## Decision threshold

## Timeline

## Risks

## Next action
```

## Quality rules

1. Keep the experiment small.
2. Validate learning before polish.
3. Do not recommend building a full product too early.
4. Make the metric actionable.
5. State assumptions clearly.

## Source note

Book: The Lean Startup
Author: Eric Ries
Evidence basis: Core Lean Startup methodology commonly associated with MVP and validated learning.
