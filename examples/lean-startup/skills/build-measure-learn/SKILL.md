---
name: build-measure-learn
description: The user wants to run an iterative product learning cycle. Use when the user wants to apply The Lean Startup's Build Measure Learn method.
source_book: The Lean Startup
source_author: Eric Ries
confidence: high
---

# 构建测量学习循环

This skill helps the user turn an idea into a measurable experiment and convert results into a decision. It is based on The Lean Startup by Eric Ries.

## When to use

1. The user wants to test a hypothesis through a short product cycle.
2. The user has a feature, product, or growth idea and needs evidence.
3. The user wants a repeatable experiment record.

## Inputs to collect

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

## Output format

```markdown
# Build Measure Learn Plan

## Hypothesis

## Build action

## Measurement plan

## Decision rule

## Learning record

## Next cycle
```

## Quality rules

1. Use actionable metrics.
2. Avoid vanity metrics.
3. Keep each cycle focused on one major hypothesis.
4. State what evidence would change the decision.
5. Recommend a smaller loop when possible.

## Source note

Book: The Lean Startup
Author: Eric Ries
Evidence basis: Core Lean Startup feedback loop.
