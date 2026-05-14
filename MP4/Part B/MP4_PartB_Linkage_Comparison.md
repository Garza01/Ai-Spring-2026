# MP4 Part B — Linkage Comparison Worksheet

**Team:** _member names_

This is your day-one integration artifact. Each member arrives with a
four-bar linkage from Part A — same one-side problem, same BigClaw
reference, different design choices. Compare the candidates on the same
axes and pick (or merge) one. The team's first activity is concrete: this
worksheet.

> The plots come from combining your Part A data — they are not new
> analysis. Reuse each member's `compute_finger_position()` and
> `compute_transmission_angle()` outputs.

---

## Candidate Linkages

One row per team member. Pull the numbers from each member's Part A
Section 1 design summary and Section 7 trust ledger.

| Member | L1 / L2 / L3 / L4 (mm) | Output pivot offset (mm) | Single-side displacement (mm) | Implied total jaw opening (2× displacement, mm) | Min / max transmission angle | Part A trust ledger highlight |
|--------|-------------------------|---------------------------|-------------------------------|-------------------------------------------------|------------------------------|--------------------------------|
| _..._  | _..._ / _..._ / _..._ / _..._ | ( _..._ , _..._ ) | _..._ | _..._ | _..._° / _..._° | _e.g., "in band the whole time" or "borderline at θ_min"_ |
| _..._  |                         |                           |                               |                                                 |                              |                                |
| _..._  |                         |                           |                               |                                                 |                              |                                |
| _..._  |                         |                           |                               |                                                 |                              |                                |

---

## Side-by-Side Plots

Embed (or link to) two combined plots showing all candidate linkages on
the same axes:

1. **Single-side finger displacement vs. input angle** — all candidates
   on one chart, with a horizontal reference line at the displacement
   that produces the target 40 mm total jaw opening (i.e., 20 mm
   single-side).
2. **Transmission angle vs. input angle** — all candidates on one chart,
   with the 40°–140° workable band shaded.

`<!-- ![Displacement comparison](plots/displacement_comparison.png) -->`

`<!-- ![Transmission angle comparison](plots/mu_comparison.png) -->`

> A short Python script that reads each member's geometry and replots is
> the typical way to do this. The matplotlib animation starter from Part
> A has the kinematics — adapt it.

---

## Comparison Notes

For each candidate, 2–3 sentence assessment:

- **Linkage [member name]:** _What's good about it. What's questionable.
  What's unverified._
- **Linkage [member name]:** _..._
- **Linkage [member name]:** _..._
- **Linkage [member name]:** _..._

---

## The Team's Selection

**Chosen linkage:** _one member's, or a merged design — name it_

**Why this one (2–4 sentences of engineering reasoning):**

> _Be specific. "Better transmission angles across the range" or
> "tightest envelope fit" — not "best overall." If you merged, name the
> base and what got carried over._

**What got carried over from the others (if anything):**

- _..._
- _..._

**What got cut and why (be explicit):**

- _..._
- _..._

---

## Inputs to the Drive-Train Worksheet

Carry these forward into `MP4_PartB_Gear_Pair_Design.md`:

- **Chosen linkage's input angle range:** from _..._° to _..._°
- **Chosen linkage's transmission angle band across that range:** _..._° to _..._°
- **Implied input angle range tolerance** — how much can the
  drive-train reduction N shift this range before the transmission
  angle leaves the workable band? _..._°

> This last number is the coupling between Layer 1 (drive train) and
> Layer 2 (linkage). The drive-train design has to respect it.
