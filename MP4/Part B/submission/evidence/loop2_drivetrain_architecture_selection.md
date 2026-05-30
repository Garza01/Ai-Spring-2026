# Team Centaur Loop 2 — Drive-Train Architecture Selection

**Date:** 2026-05-23  
**Lead:** Maya Chen  
**Context provided to AI:** Pasted the Ratio Convention section from the Gear Pair Design worksheet, the chosen linkage's input range (0°–45°, sweep=45°), the MP1 brief constraint (2–3 thumb-wheel turns from open to closed), and the housing envelope (92 × 46 × 55 mm). `miniclaw_rag` skill active; MCP tool `query_miniclaw_docs` called with "drive train architecture thumb wheel gripper" — returned reference to BigClaw gear photo showing a 3-gear compound arrangement.

## What we asked

> We need a drive train that reduces 2–3 thumb-wheel turns (target: 2.5 turns) to 45°
> of linkage input sweep AND counter-rotates both sides simultaneously. The housing is
> 92 × 46 × 55 mm. N_needed = 2.5 × 360 / 45 = 20. Our options are:
>
> A. Single spur pair
> B. Compound spur train (two stages)
> C. Worm + worm wheel
> D. Sync-only spur pair + separate reduction
>
> Which architecture fits N=20 inside the 92 × 46 × 55 mm envelope? Evaluate each.

## What we got back

The AI evaluated all four architectures against the N=20 and envelope constraints:

**Architecture A (single spur pair):** To achieve N=20 with z_driver=12 (minimum for
FDM), z_driven = 240 teeth. At m=1.0mm, d_driven = 240mm — 5× the housing width.
"Single spur pair for N=20 is impossible in this envelope." Ruled out.

**Architecture B (compound spur, 2-stage):** For N=20 split evenly: each stage needs
ratio ≈ 4.47. Stage 1: z1=12, z2=54 at m=1.5mm → C1=49.5mm (housing width = 46mm).
"Stage 1 center distance exceeds the housing width per side. Marginally possible with
m=1.2mm (C1=39.6mm), but tight and requires non-standard module. Three stages are
needed for clean packaging, which raises part count."

**Architecture C (worm + worm wheel):** 2-start worm, z_w=40, N=20. Worm wheel
pitch diameter = 40mm in a 46mm housing height: 3mm clearance per side (tight).
Center distance = 25mm. "Compact for N=20 in one stage. The 3mm housing clearance
is tight for FDM (likely needs post-processing). Self-locking is a concern but not a
functional failure for this one-way-drive application (the user pushes the thumb wheel
— back-drive isn't needed)."

**Architecture D (sync spur 1:1 + worm reduction):** Same worm as Architecture C for
the reduction. The sync spur pair (z=16 each, m=1.5mm, C=24mm) handles counter-rotation
separately. Part count increases by 2 gears but packaging is more flexible. "Separates
the two functions clearly: reduction by worm, counter-rotation by spur pair."

**AI recommendation:** Architecture C for part count and simplicity; Architecture D if
the 3mm worm-wheel housing clearance is unacceptable.

## Team assessment

The AI's envelope analysis for Architecture B was decisive — we hadn't calculated
the center distances and the AI's arithmetic caught that two-stage spur is infeasible
at standard module in this envelope.

We pushed back on the self-locking concern: "Self-locking means the user can't release
the gripper by pushing the jaw open — they'd have to reverse the thumb wheel. Is that
acceptable?" The AI's response: "For a gripper, self-locking is actually desirable:
the jaws hold position without the user continuously holding the thumb wheel. It's only
a problem if you need back-drive, which this design doesn't." Team agreed — self-locking
is a feature, not a bug.

We chose **Architecture C** for its single-stage simplicity, lower part count (vs. D),
and the fact that mirrored worm wheels on one shaft is a clean counter-rotation solution.
The 3mm housing clearance on the worm wheel is flagged as a risk ("Needs work").

## What changed

Architecture C (worm + worm wheel) selected. Carry forward to Loop 3 for exact sizing.
The self-locking assessment is added to the trust assessment as a verified-by-reasoning
(not bench-tested) item.
