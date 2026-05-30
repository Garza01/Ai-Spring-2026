# Team Centaur Loop 5 — Trust Assessment Gap Review

**Date:** 2026-05-28  
**Lead:** Maya Chen  
**Context provided to AI:** Pasted the draft Per-Subsystem Trust Assessment (all six subsystems, flags, verified/unverified lists) and asked the AI to review it for hidden assumptions, over-confident "verified" claims, and missing risks.

## What we asked

> Review this trust assessment for the MiniClaw gripper. We want to find any hidden
> assumptions or over-confident "verified" claims. Specifically: are there things
> we've said are "verified" that actually only passed an analytical check but not a
> physical test? What's the single biggest risk we've missed?

## What we got back

The AI identified three concerns:

**Concern 1 — Linkage "verified" claims conflate analysis with test:**
"Several items under 'What's verified' for the linkage are verified analytically or by
simulation, not by physical assembly. For example: 'transmission angle stays in band' —
verified by Python code, which itself is based on the two-circle intersection formula.
The formula is correct for an idealized rigid linkage. A real printed linkage has link
length tolerances of ±0.2–0.3mm per FDM part. A 0.3mm error in L2 (26mm nominal) is
1.2% — small but could shift µ_min by ~0.5°. At a 5° margin above 40°, this is fine.
You should say 'verified analytically to <0.01mm, physical tolerance not tested'
rather than just 'verified'."

**Concern 2 — Worm self-locking listed as feature, not risk:**
"The team lists 'worm self-locking is a feature for holding jaw position.' This is
true for normal operation. However, if the worm jams mid-stroke (e.g., over-driven
past a hard stop), the self-locking prevents the user from manually reversing — they
must continue driving in the jamming direction. This can snap the worm wheel teeth.
The trust assessment should note this as an unverified failure mode."

**Concern 3 — Housing clearance for worm wheel (1mm per side) is not flagged at subsystem level:**
"The 2mm total clearance for the worm wheel OD (42mm) in the 46mm housing height is
mentioned in the DFM checklist but not in the trust assessment's drive train section.
These should be consistent."

**AI's 'single biggest risk' identification:**
"The single biggest unverified risk is the worm gear printability at m=1.0mm. If the
tooth profile at this module doesn't mesh correctly after printing, the entire drive
train fails. This is the only failure mode that would prevent any jaw motion at all —
linkage tolerance errors would merely reduce performance, but a non-functional gear
would produce zero output. It deserves a 'Needs work' flag on the drive train subsystem,
not 'Unknown'."

## Team assessment

We agreed with Concerns 1 and 3. The AI's phrasing on Concern 1 was useful — it gave
us a model for how to state "analytically verified, physically untested" more precisely.
We updated all subsystem entries accordingly.

We pushed back on the worm printability flag severity: "Calling it 'Needs work' rather
than 'Unknown' implies we know it needs a specific fix. We don't — we need a test print
to determine IF it needs a fix. 'Unknown' is more honest." The AI acknowledged this:
"Fair. 'Unknown' is the honest flag if you haven't printed a test piece. 'Needs work'
would apply if you had a test piece that failed and had a specific fix in mind."

On Concern 2 (self-locking jam risk): we added it to the drive train unverified list.
The AI's suggested mitigation — "add a rubber-padded hard stop to prevent over-driving
past the full-closed position" — was noted as an MP5 design refinement.

## What changed

1. Linkage trust assessment updated: "analytically verified, not bench-tested" language added.
2. Worm wheel housing clearance added to drive-train unverified list.
3. Worm self-locking jam failure mode added to drive-train unverified list.
4. Worm gear printability remains flagged "Unknown" (not "Needs work") — requires a test print.
5. Overall prototype readiness flag confirmed as "Needs work" for drive train, "Ready to print"
   for the linkage mechanism (with the understanding that Part A analysis was thorough).
