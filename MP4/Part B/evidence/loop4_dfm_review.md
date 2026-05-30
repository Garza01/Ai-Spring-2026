# Team Centaur Loop 4 — DFM Pass on Worm Gear and Linkage

**Date:** 2026-05-26  
**Lead:** Alberto Garza  
**Context provided to AI:** Pasted the DFM checklist template and the team's design parameters (linkage links, worm gear specs, housing dimensions). Asked the AI to walk through the checklist for the most at-risk features.

## What we asked

> Walk through the DFM checklist for our MiniClaw design. Focus on the worm gear
> (m_n=1.0mm, z_wheel=40) and the linkage joints (pins, clearances). Flag anything
> that would cause a failed print or non-functional assembly. We're printing in PLA
> on a standard FDM printer (0.4mm nozzle).

## What we got back

The AI flagged five issues in priority order:

**Flag 1 (High) — Worm wheel tooth feature size:**
"At m_n=1.0mm, the worm wheel tooth root width ≈ 0.78×m = 0.78mm. Standard FDM PLA
with 0.4mm nozzle: minimum feature = ~0.8mm. The tooth root is AT the minimum. Any
over-extrusion or layer misregistration will fill the tooth gap partially, increasing
backlash or preventing mesh. Recommend m_n=1.2mm if the tooth count is adjusted to
maintain N=20 (e.g., z_w=40, N=20 still works at m=1.2mm with d_w=48mm — but now
d_a=50.4mm exceeds the 46mm housing height). There is no clean solution; flag for
bench testing."

**Flag 2 (High) — Pin hole diameter after FDM:**
"Designed hole ID=3.0mm, printed pin OD=2.8mm → designed clearance=0.2mm. FDM holes
print ~0.1mm undersize (artefacts in perimeter paths); pins print ~0.1mm oversize.
Net clearance after print ≈ 0.2 − 0.2 = 0.0mm. Interference fit. Joints will not
rotate freely. Recommendation: design hole ID=3.2mm for a 0.2mm sliding clearance
after FDM shrinkage."

**Flag 3 (Medium) — Worm shaft print orientation:**
"The worm helix is a continuous twisted feature. Printed upright (axis vertical): helix
requires very small steps per layer and is well-supported. Printed on its side (axis
horizontal): helix overhangs at up to 80° — requires supports that break off and damage
the thread. Print upright."

**Flag 4 (Medium) — Coupler link flatness:**
"The coupler (14mm long) printed flat on the bed is fine. If it is printed at angle to
avoid a support, the pin holes are drilled in the layer-line direction — FDM holes in
that orientation have worse roundness. Print couplers and cranks flat."

**Flag 5 (Low) — Housing snap fits or clips:**
"No snap fits are visible in the design description, which is good: PLA is brittle under
snap-fit deflection. Use through-bolts or screws instead."

## Team assessment

Flags 1 and 2 were the most actionable. The AI's arithmetic on the pin clearance was
correct — we verified the standard rule (FDM tolerance ~±0.1mm on features) from PrusaSlicer
documentation. This was a genuine catch; we had designed to the nominal dimensions without
accounting for FDM tolerance.

We pushed back on Flag 1: "Is m_n=1.2mm feasible if d_a=50.4mm exceeds the housing?"
The AI's response: "You could recess the worm wheel into the housing wall by 2mm
(machine a slot), gaining the clearance. Or reduce z_w to 36 and increase starts to 3
for N=12 — but that halves the reduction. The cleanest path is to test-print a single
tooth profile at m=1.0mm and check mesh quality before committing to the full gear."

Team agreed: print a test tooth profile at m=1.0mm before committing. If it fails, step
up to m=1.2mm and redesign. Flag as "Unknown" in trust assessment.

The pin clearance fix (hole ID 3.0→3.2mm) was implemented immediately in the design
parameters. No further analysis needed.

## What changed

1. Pin hole ID updated from 3.0mm to 3.2mm (FDM clearance correction).
2. Worm wheel tooth feature size flagged as "Unknown" — requires a test print.
3. Worm shaft print orientation confirmed: upright (helix axis vertical).
4. All linkage links confirmed: flat on bed.
These changes are reflected in the completed DFM checklist.
