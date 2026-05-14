# MP4 Part A — Grading Rubric

**Notebook:** `MP4_PartA_Build_to_Verify.ipynb`
**Total:** 50 points
**Due:** Friday, May 29, 2026 at 11:59 PM

This rubric matches the assignment in `MP4_Build_to_Verify.docx`. Grading
philosophy is **substance over format**: a triangulation that honestly
names where the three paths disagree beats a polished writeup whose three
numbers "all roughly agree" without engineering reasoning.

### How partial credit works

Each section's score is the **sum** of its component criteria. Every
criterion is independently checkable — the grader awards the listed points
per item, and the section total is whatever they add up to. Item points
may be fractional (0.5 increments) when the criterion has clearly partial
states.

> **Soft caps.** A section's score is capped at 50% if the proof-of-work
> evidence is missing entirely:
> - Section 2 cap if `evidence/` is empty
> - Section 5 cap if `motion/` is empty AND no public link is provided
> - Section 6 cap if no hand calc is visible (markdown empty AND
>   `handcalc/` empty)

---

## Section 1 — Design Summary (6 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 1.1 | **1.5** | All four link lengths (L1, L2, L3, L4) given in mm with explicit values. Half credit (0.75) if any one is missing. |
| 1.2 | **1.0** | Output ground pivot position (x, y) given relative to the input ground pivot at the origin. |
| 1.3 | **0.5** | Tip extension and input range (θ_min, θ_max) both stated. |
| 1.4 | **0.5** | Target single-side displacement and the implied total jaw opening both stated, in mm. |
| 1.5 | **1.5** | Labeled sketch present (hand-drawn photo, CAD screenshot, or annotated diagram) and embedded or referenced from the cell. Half credit (0.75) if the sketch is present but unlabeled. |
| 1.6 | **1.0** | Design rationale (3–4 sentences) ties choices to the BigClaw reference or the MP1 envelope constraints. Half credit (0.5) for generic rationale ("seemed like a reasonable starting point"). |

> The symmetry assumption ("the other side mirrors mine") and the
> gear-pair-handles-synchronization assumption are pre-printed in the
> template; the student does not need to restate them, but they must
> not be deleted.

---

## Section 2 — Centaur Loop with Your Stack (10 pts)

Three iteration rounds, each independently scored at ~3.3 pts. The grader
applies the same checklist three times.

| # | Pts | Criterion (per round, applied to rounds 1, 2, 3) |
|---|-----|---|
| 2.r.1 | **0.5** | Date/time and host/stack named. |
| 2.r.2 | **0.5** | Prompt or interaction is captured (not just a vague description). |
| 2.r.3 | **1.0** | At least one **evidence file** committed under `evidence/` for this round (screenshot, transcript snippet, MCP log). The round's text references it by name. |
| 2.r.4 | **0.5** | "Engineering assessment" names a specific moment of agreement OR pushback. Generic praise ("looked reasonable") gets 0.25. |
| 2.r.5 | **0.83** | "What changed for the next round" makes a concrete adjustment (prompt, context, framing) tied to what came back. Round 3 substitutes "stack notes" — same criterion: name what worked and what didn't in your stack. |

Section subtotal: **3 rounds × 3.33 pts ≈ 10 pts**.

> Soft cap of 5/10 if `evidence/` is empty for the entire section.

---

## Section 3 — Position Analysis (10 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 3.1 | **3.0** | `compute_finger_position()` is implemented, runs without error, and produces sensible numbers (the closed-position displacement is ~0; tip XY is in the same order of magnitude as link lengths). Half credit (1.5) if the function exists but errors at one or more input angles in the range. |
| 3.2 | **2.5** | Finger tip trajectory plot rendered, axes equal, axes labeled with units. Half credit (1.25) if the plot exists but is unlabeled or has wrong aspect. |
| 3.3 | **2.5** | Displacement-vs.-input-angle plot rendered, with **a horizontal reference line at the target single-side displacement** (= TARGET_TOTAL_JAW / 2). Half credit (1.25) if the line is missing. |
| 3.4 | **1.0** | Total-jaw-opening axis or annotation visible (secondary y-axis or text annotation). |
| 3.5 | **1.0** | Constants in Step 2 (L1..L4, GROUND_PIVOT_OUTPUT, TIP_EXTENSION, range) match the values stated in the Section 1 design summary. Half credit (0.5) if any value differs without explanation. |

---

## Section 4 — Transmission Angle Analysis (8 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 4.1 | **3.0** | `compute_transmission_angle()` is implemented and runs across the input range; values are sensible (between 0° and 180°, no NaN). Half credit (1.5) if function exists but errors at some inputs. |
| 4.2 | **2.5** | Transmission angle plot rendered with the **40°–140° workable band marked** (axhspan or two axhlines). Axes labeled. |
| 4.3 | **2.0** | In-band note is filled in: explicitly says whether the linkage stays in band throughout, OR names the input angles where it leaves and what would change to fix it. Half credit (1.0) for vague conclusion ("mostly in band"). |
| 4.4 | **0.5** | Min/max μ values referenced (in the note OR visible from the plot annotation). |

---

## Section 5 — Simulation and Interference Check (6 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 5.1 | **1.0** | Tool used is named (HTML starter, matplotlib starter, Linkage Mechanism Designer, CAD motion study, etc.). |
| 5.2 | **2.5** | Motion artifact committed under `motion/` — video, animated GIF, sequence of stills, or a public link with a representative still committed. Half credit (1.25) if a still exists but no full-range animation is shown. |
| 5.3 | **2.0** | Interference check writeup (2–3 sentences): explicit yes/no on intersections, plus closest-approach observation OR fix description. Half credit (1.0) for generic ("looks fine"). |
| 5.4 | **0.5** | Geometry used in the sim matches the Section 1 design summary. |

> Soft cap of 3/6 if `motion/` is empty AND no public link is provided.

---

## Section 6 — Hand Calc at Three Positions (4 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 6.1 | **0.5** | Method named ("vector loop closure", "two-circle intersection", "law of cosines"). |
| 6.2 | **2.0** | Three positions worked out (open / mid / closed) with **working shown** at each (numbers substituted, intermediate steps visible). Photo of paper math counts. Half credit per position if only the result is shown. |
| 6.3 | **1.0** | Comparison to the Section 3 plot is filled in: do the three points fall on the curve? Within what tolerance? If not, which is wrong and how was it identified? |
| 6.4 | **0.5** | Units are consistent across the three positions. |

> Soft cap of 2/4 if no hand calc is visible (markdown empty AND
> `handcalc/` empty).

---

## Section 7 — Triangulation and Trust (4 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 7.1 | **1.0** | "Where do they agree" names a quantitative range or specific overlap (not "they roughly agree"). |
| 7.2 | **1.0** | "Where do they disagree" names the spread quantitatively, OR explicitly states all three paths agreed and at what tolerance. |
| 7.3 | **1.0** | "Which one do you trust and why" cites the assumption that drove the difference, or (if no disagreement) names the failure mode least covered by the triangulation. |
| 7.4 | **1.0** | Trust ledger has at least three entries on each side, each entry quantitative or design-specific. **The symmetry assumption AND/OR the gear-pair assumption appears in the "still needs checking" column** (these are the explicit inputs to Part B). |

---

## Section 8 — Reflection (2 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 8.1 | **2.0** | Reflection is 3–4 sentences (0.5), names a **specific moment** from the work — a function bug, a tool error, a converged answer (1.0), and identifies a durable skill that survives a tooling change (0.5). |

---

## Notebook hygiene (silent prerequisite — not separately graded)

These don't earn points but missing them caps the section above:

- The notebook itself runs end-to-end without errors (Section 0 cell
  succeeds; the helper-check cells in Sections 2/5/6 print without
  crashing; Sections 3 and 4 plot cells render once the student fills in
  the functions)
- Evidence folders are committed and not empty for the sections that
  require them (see soft caps above)
- The notebook is committed AND pushed — the grader reads what's in
  GitHub, not what's in the student's Codespace
- All three required folders exist: `evidence/`, `motion/`, `handcalc/`
  (the `starters/` folder ships with the assignment)

If the grader cannot find the proof-of-work artifacts referenced by the
notebook, the relevant section is capped per the soft caps above.

---

## Connection to Part B

Section 1's design summary and Section 7's trust ledger are the input
artifacts for your team's day-one Linkage Comparison Worksheet in Part B.
The team rubric (`MP4/Part B/RUBRIC_MP4_PartB.md`, when published) will
reward teams that meaningfully use individual designs and trust ledgers
in the comparison and the per-subsystem assessment. Write yours so a
teammate can read it cold.
