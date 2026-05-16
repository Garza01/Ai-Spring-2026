---
name: unit-conversion-check
description: >
  Detect unit-mismatch or conversion errors in engineering calculations,
  dimensions, load cases, tolerances, and manufacturing notes before they
  become design mistakes.
---

# Skill: Unit Check for Engineering Work

## When to use this skill

Use this skill whenever the user presents engineering calculations, dimensions,
loads, or manufacturing instructions involving physical units and asks for
verification, explanation, or design review. Trigger it when unit systems are
mixed, quantities are converted, or a value appears in the wrong unit context.

## Steps

1. Identify every numeric quantity and its associated unit in the text.
2. Check whether each unit is appropriate for the quantity and whether the
   units are consistent across the same calculation or requirement.
3. Look for explicit conversions and verify the conversion factor and result.
4. Flag any mixed-unit usage without a clear conversion, especially in the same
   sentence or formula.
5. If you find a likely unit error, explain the mismatch clearly and provide the
   correct conversion or recommendation.

## What to flag

- Mixed units in a single calculation or dimension callout (e.g. inches and
  millimeters without explicit conversion).
- A changed physical quantity with no conversion shown (e.g. torque in N·m next
  to a diameter in inches).
- A conversion that looks like a plausible number but uses the wrong factor.
- Temperature units treated like pressure, length treated like force, or torque
  treated like linear force.
- A unit that is inconsistent with the described manufacturing process
  (e.g. tight machining tolerances expressed only in inches for a metric
  drawing).

## What NOT to do

- Do NOT invent values or guess the user's intent when the units are ambiguous.
  Instead, ask for clarification on the unit system or the missing quantity.
- Do NOT simply translate every number to the other unit system without checking
  whether the conversion is relevant to the user's question.
- Do NOT assume the user meant metric if the text explicitly uses imperial
  units.
- Do NOT treat a correct-looking conversion as correct if the units or the
  quantity type do not match.
