# Team Centaur Loop 3 — Worm Gear Sizing and Coupling Check

**Date:** 2026-05-24  
**Lead:** Jordan Park  
**Context provided to AI:** Pasted the worm stage row template from the Gear Pair worksheet, the chosen linkage parameters, and the N=20 target. Asked for specific worm gear sizing (module, tooth counts, center distance) and the coupling check at the 2.5-turn target.

## What we asked

> We're using Architecture C: worm + worm wheel, N=20. Size the worm for:
> - m_n = 1.0 mm (minimum for FDM per our DFM notes)
> - 2-start worm
> - z_wheel = 40 teeth
> - Envelope: worm wheel must fit in 46mm housing height
>
> Verify: (1) all gear parameters are consistent (N=z/starts, center distance formula),
> (2) the coupling check passes for 2.5 thumb-wheel turns producing a 45° linkage sweep,
> (3) the transmission angle at the implied sweep is within the 40°–140° workable band.

## What we got back

The AI worked through the worm sizing step by step:

**Worm parameters:**
- m_n = 1.0 mm, 2 starts
- Worm pitch diameter: using worm diameter quotient q=10, d_worm = m_n × q = 10 mm
- Lead per revolution of worm = starts × axial pitch = 2 × π × m_n = 2π mm ≈ 6.28 mm
- Lead angle: λ = arctan(lead / (π × d_worm)) = arctan(6.28 / 31.4) ≈ 11.3°

**Worm wheel parameters:**
- z_wheel = 40, m_n = 1.0 mm
- Pitch diameter d_w = m_n × z_wheel = 40 mm
- Addendum circle diameter d_a ≈ 40 + 2×1.0 = 42 mm (fits in 46mm housing: 2mm clearance)

**Center distance:** C = (d_worm + d_wheel) / 2 = (10 + 40) / 2 = 25 mm

**N check:** N = z_wheel / starts = 40 / 2 = 20 ✓

**Coupling check at 2.5 thumb-wheel turns:**
- Implied linkage sweep = (2.5 × 360°) / N = 900° / 20 = 45°
- This equals the Part A design range exactly (θ: 0°–45°) ✓
- Transmission angle at θ=45°: µ = 90° − 45° = 45° (in the 40°–140° band, 5° margin) ✓

**In-band call:** YES. The coupling check passes. N=20 was derived from N_needed, so the implied sweep matches the Part A range exactly. No residual mismatch.

## Team assessment

The AI's derivation was correct — we verified the center distance formula independently
(standard worm gear formula: C = (d_worm + d_wheel)/2). The gear dimensions are consistent.

One pushback: "You said d_a ≈ 42mm with 2mm clearance in a 46mm housing. That's 1mm
per side after assembly clearance." The AI had calculated the clearance as 2mm total
(1mm per side), which is below the FDM process capability (minimum clearance for FDM PLA
≈ 0.5mm per surface, so 1mm per side is marginal but not impossible). Jordan flagged this
in the trust assessment under "drive train housing clearance" — a specific failure mode
we have not verified by printing a test piece.

We also asked: "Does worm self-locking affect the coupling check?" Answer: No — the
coupling check verifies the kinematic ratio (implied sweep vs. actual part A sweep).
Self-locking is a quasi-static load consideration, not a kinematic one. The coupling
check passes.

## What changed

Worm gear parameters finalized: m_n=1.0mm, 2 starts, z_w=40, N=20, C=25mm. Coupling
check passes. Housing clearance (1mm per side for worm wheel OD in 46mm housing) flagged
as a "Needs work" item in the trust assessment. Confirmed in the gear pair worksheet:
"coupling check passes — implied sweep = Part A range exactly."
