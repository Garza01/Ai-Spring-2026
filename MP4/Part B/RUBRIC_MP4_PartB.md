# MP4 Part B — Grading Rubric

**Total:** 50 points
**Due:** Friday, May 29, 2026 at 11:59 PM
**Team submission:** all members submit the same team repo URL

---

Rubric is organized by deliverable to match the assignment structure:

| Deliverable | Points |
|---|---|
| 1. Linkage Comparison Worksheet | 8 |
| 2. Gear Pair Design Worksheet | 10 |
| 3. Per-Subsystem Trust Assessment | 12 |
| 4. DFM Checklist (completed) | 8 |
| 5. Team Centaur Log (5+ loops) | 8 |
| 6. MP5 Handoff Document | 4 |
| **Total** | **50** |

### How partial credit works

Each criterion is independently checkable. Item points may be fractional
(0.5 increments) when a criterion has clearly partial states. Each
deliverable's score is the sum of its component criteria.

> **Soft caps.**
> - Linkage Comparison Worksheet capped at 50% if the side-by-side plots
>   are missing entirely.
> - Per-Subsystem Trust Assessment capped at 50% if any subsystem is
>   missing a flag.
> - Team Centaur Log capped at 50% if `evidence/` for the team
>   submission is empty.
> - DFM Checklist capped at 50% if no completed version exists (i.e.,
>   only the unedited template was committed).

### Pillar mapping

The pillar weights for MP4 are: Centaur Engineering ★★★, Evaluation &
Trust ★★★, Tools & Integration ★★, Goal & Direction ★★, Context
Management ★★. The deliverable-based rubric maps naturally — the
Centaur Log and the per-subsystem Trust Assessment carry the pillar
weight; Gear Pair Design exercises Goal & Direction; Linkage Comparison
and DFM exercise Tools & Integration. The deliverable score is the grade
of record.

### Team grading

Every team member earns the same score on Part B unless the team
explicitly requests a differential allocation in writing (signed by all
members) at submission time.

---

## 1. Linkage Comparison Worksheet (8 pts)

Evidence path: `MP4_PartB_Linkage_Comparison.md` + plot images

| # | Pts | Criterion |
|---|-----|-----------|
| L.1 | **1.0** | Worksheet exists and team members are named. Each row of the Candidate Linkages table is filled in for one member's Part A linkage. |
| L.2 | **2.0** | The Candidate Linkages table has all required columns filled per row: link lengths, output pivot offset, single-side displacement, implied total jaw opening, min/max transmission angle, trust ledger highlight. Half credit (1.0) if any one column is missing across rows. |
| L.3 | **2.5** | **Combined displacement vs. input angle plot** — all candidates on one chart, target reference line marked. Half credit (1.25) if the plot exists but lacks the reference line or is per-candidate rather than overlaid. |
| L.4 | **1.5** | **Combined transmission angle vs. input angle plot** — all candidates on one chart, 40°–140° band marked. Half credit (0.75) if the band is not marked. |
| L.5 | **1.0** | "The Team's Selection" justification is concrete (cites min μ, displacement match, envelope fit, etc.). Half credit (0.5) for "best overall." |

> Soft cap of 4/8 if both plots are missing.

---

## 2. Gear Pair Design Worksheet (10 pts)

Evidence path: `MP4_PartB_Gear_Pair_Design.md` + sketch image

The worksheet supports four drive-train architectures: (A) single spur
pair, (B) compound spur train, (C) worm + worm wheel, (D) sync-only
spur pair + separate reduction element. Criteria below grade against
the team's chosen architecture; "drive train" is used as the generic
term for whatever hardware combines synchronization and reduction.

| # | Pts | Criterion |
|---|-----|-----------|
| G.1 | **1.0** | Architecture choice (A / B / C / D) is checked and the "why we chose this architecture" rationale (2–3 sentences) ties the pick to the envelope, the required reduction, or printability. |
| G.2 | **2.0** | Drive-train spec table for the chosen architecture is filled in (spur stage row(s) for A/B; worm-stage row for C; either stage row plus a named separate reduction element for D). Each missing required parameter subtracts 0.25. Half credit (1.0) if rows are present but mathematically inconsistent — stage ratios don't multiply to the stated overall N, or a spur stage's center distance ≠ `m × (z_driver + z_driven) / 2`. |
| G.3 | **1.5** | Overall reduction **N** is stated explicitly in the "Overall" row and equals the product of the per-stage ratios listed in the spec table (or the single-stage ratio for Architecture A). |
| G.4 | **1.5** | Rationale section ties the chosen N to the 2–3 thumb-wheel-turn target AND to the chosen linkage's input angle range (the coupling Part A deferred). The "does our N match N_needed?" question is answered explicitly (Yes/No + what the team accepted if No). Half credit (0.75) if only one of the two couplings is addressed. |
| G.5 | **1.5** | Symmetry arrangement section names the mechanism that achieves counter-rotation (mating final pair / idler between sides / mirrored worm wheels on a common worm shaft / other) AND explains how rotation reaches both sides simultaneously at the same rate. |
| G.6 | **2.0** | **Coupling check** is computed: the linkage input sweep implied by N (at the 2.5-turn target) is stated, the transmission angle band is re-checked at that implied range, and an explicit in/out-of-band call is made. Half credit (1.0) if the coupling check is mentioned but the implied sweep / re-checked band is not actually filled in. |
| G.7 | **0.5** | Labeled sketch committed and referenced from the worksheet (hand sketch, screenshot, or CAD export). |

> Lewis stress analysis (and the equivalent worm / lead-screw strength
> checks) are optional and not graded for absence; if attempted, sloppy
> work is penalized via the trust assessment.

---

## 3. Per-Subsystem Trust Assessment (12 pts)

Evidence path: `MP4_PartB_Trust_Assessment_Template.md` (completed)

| # | Pts | Criterion |
|---|-----|-----------|
| T.1 | **1.0** | Linkage base and design base are named with one-sentence rationale. |
| T.2 | **6.0** | Each of the 6 default subsystems (or the team's adjusted list, with full coverage of the gripper) carries: a flag, a verified list, an unverified list, and a one-sentence risk. Award 1.0 per fully populated subsystem. |
| T.3 | **2.0** | The four-bar linkage subsystem entry **explicitly addresses the symmetry assumption**, naming it as either now-verified (because the team's drive train handles it) or still-unverified (because the drive train hasn't been bench-tested). Half credit (1.0) for general acknowledgment without naming the assumption. |
| T.4 | **1.5** | The drive-train subsystem entry names at least one specific failure mode the team has not bench-tested (e.g., tooth strength under load, backlash, worm self-locking under back-drive, lead-screw friction, real-world meshing). |
| T.5 | **1.5** | Overall Prototype Readiness paragraph picks a position and defends it. "Mostly ready" without a defense gets 0.75. |

> Soft cap of 6/12 if any subsystem is missing a flag.

---

## 4. DFM Checklist — Completed (8 pts)

Evidence path: `MP4/Part B/dfm_checklist_completed.md` (or the same
content embedded in the team's README)

| # | Pts | Criterion |
|---|-----|-----------|
| D.1 | **1.0** | Print orientation table filled for each major part. |
| D.2 | **1.0** | Wall thickness / feature size table filled with explicit values; flagged items called out. |
| D.3 | **1.0** | Pin and joint clearances analyzed with tolerance stack (designed clearance ± expected FDM offset). |
| D.4 | **1.5** | Gear printability table filled (module, smallest tooth feature, tooth counts, face width, orientation). Half credit (0.75) for half the cells filled. |
| D.5 | **0.5** | Overhangs / bridges section identifies at least one specific feature with mitigation. |
| D.6 | **0.5** | Assembly sequence and accessibility check filled. |
| D.7 | **1.0** | Part count is stated and compared to the < 15 target. |
| D.8 | **0.5** | Print time and material budget given (rough estimate from any slicer). |
| D.9 | **1.0** | DFM bottom-line statement names the team's top 2–3 flags concretely. |

> Soft cap of 4/8 if no completed checklist exists in the repo (only
> the unedited template).

---

## 5. Team Centaur Log (8 pts)

Evidence path: `MP4_PartB_Team_Centaur_Log_Template.md` (completed) +
`evidence/` for screenshots, transcripts, MCP logs

Five required loops, each scored at ~1.6 pts. Apply the same per-loop
checklist to loops 1–5; bonus loops are not separately graded but can
be cited in MP5.

| # | Pts | Criterion (per loop, applied to loops 1–5) |
|---|-----|---|
| C.l.1 | **0.4** | Date, lead member, prompt/interaction captured. |
| C.l.2 | **0.4** | Context provided to AI is named (skill loaded, RAG used, screenshot pasted). |
| C.l.3 | **0.4** | At least one **evidence file** committed under `evidence/` for this loop, referenced by name. |
| C.l.4 | **0.4** | Team assessment names a specific moment of agreement OR pushback. Generic ("looked good") gets 0.2. |

Section subtotal: **5 loops × 1.6 pts = 8 pts**.

> Soft cap of 4/8 if `evidence/` is empty for the team submission.

---

## 6. MP5 Handoff Document (4 pts)

Evidence path: `MP4_PartB_MP5_Handoff_Template.md` (completed)

| # | Pts | Criterion |
|---|-----|-----------|
| H.1 | **0.5** | Final Design Summary names the chosen linkage and the team's drive-train design (architecture, overall reduction N, symmetry arrangement). |
| H.2 | **1.0** | What's Prototype-Ready and What's Not Ready are pulled from the trust assessment (not new claims), with at least 3 entries each. |
| H.3 | **1.0** | "What we're choosing to demonstrate in MP5" picks a specific demo and names what behavior shows the design is real. |
| H.4 | **0.5** | Open Questions Going Into MP5 has at least 2 honest entries. |
| H.5 | **0.5** | Team composition for MP5 confirms member names and any role notes. |
| H.6 | **0.5** | Pointers section links to all the underlying MP4 artifacts. |

---

## Stack hygiene (silent prerequisite — not separately graded)

- Team repo URL is submitted by every team member on Canvas
- Top-level README in the team repo lists every artifact's path
- All four members' Part A repos are linked
- `evidence/` exists and is populated for the centaur log
- The completed DFM checklist exists separately from the unedited
  template

If the grader cannot navigate from the team's README to the artifacts,
the deliverable is graded on what's findable. Don't make graders search.

---

## "Be a team that ships" tiebreaker

When two teams sit on the boundary between scores, the deciding question
is:

> If you handed this package to the next team and walked away, could
> they print, assemble, and operate the gripper without asking you a
> question?

The team whose trust assessment names what's NOT verified, whose DFM
checklist flags real concerns honestly, and whose centaur log shows the
team disagreeing with the AI in writing — that team earns the higher
score. Polish without honesty does not.
