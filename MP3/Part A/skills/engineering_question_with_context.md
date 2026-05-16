---
name: engineering-question-with-context
description: >
  Guide the AI to answer engineering questions by calling
  query_ridgeline_rag for Ridgeline project history and convert_units for
  unit conversions, then synthesize both into one engineering answer.
---

# Skill: Engineering Question with Context

## When to use this skill

Use this skill when the user asks an engineering question that may benefit from
Ridgeline-specific project history and when the question includes one or more
quantities in units that should be converted or compared. Trigger it for
questions about past projects, internal standards, design precedents, or any
project-specific details.

## Steps

1. Read the full user question and identify whether it refers to Ridgeline
   projects, internal practices, or specific historical examples.
2. If the question asks about a Ridgeline project or internal guideline, call the
   `query_ridgeline_rag` tool first to retrieve relevant project history and
   context.
3. If the question includes a quantity in one unit system and asks for the
   equivalent in another, call the `convert_units` tool.
4. Synthesize the answer by combining retrieved context with the converted
   quantity and the specific engineering decision requested.
5. Do not simply copy retrieved chunks; summarize the relevant context and
   explain how it applies to the current question.

## What to flag

- Questions that ask about a specific Ridgeline project, internal standard,
  or company-specific practice.
- Requests that mix units or ask for an equivalent value in another unit.
- Answers that would be too generic without the project-specific context.
- Cases where the RAG result is used as a direct citation instead of an
  applied insight.

## What NOT to do

- Do NOT answer solely from generic training data when the question is clearly
  about Ridgeline's past work.
- Do NOT return retrieved document excerpts without explaining their relevance.
- Do NOT perform unit conversion mentally instead of using the unit converter
  tool when the user explicitly asks for it.
- Do NOT treat retrieved context as authoritative without checking that it is
  relevant to the specific question.
