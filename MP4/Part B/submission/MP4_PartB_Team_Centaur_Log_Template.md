# MP4 Part B — Team Centaur Log

**Team:** Team Claw Alpha — Alberto Garza, Maya Chen, Jordan Park

> Common topics for Part B centaur loops: synthesizing across the linkage
> comparison, choosing a drive-train architecture (single spur pair,
> compound, worm, or sync-pair + separate reduction), sizing it (per-stage
> ratios, packaging), checking that the chosen reduction N doesn't push
> the linkage out of its workable transmission angle band, running DFM
> checks on the chosen geometry, identifying risks in the per-subsystem
> trust assessment, drafting the MP5 narrative.

Minimum: **5 loops across the team**. Quality, not volume. Different
team members can lead different loops; the lead member is captured in
the entry.

---

## Loop 1 — Linkage Comparison Synthesis

**Date:** 2026-05-22  
**Lead team member:** Alberto Garza  
**Context provided to AI:** All three Part A design summaries pasted inline (link lengths,
input ranges, displacement values, µ ranges, trust ledger highlights). `miniclaw_rag`
skill active in Claude Desktop.

**What we asked:**
> We have three Part A four-bar designs (Alberto: L2=26/45°/µ:45°–90°, Maya: L2=25/50°/µ:40°–90°,
> Jordan: L2=22/50°/µ:40°–90°). Which design should we select as the team base, and what
> trade-offs are we accepting? Are there merger opportunities?

**What we got back:**
> AI ranked designs: Alberto first for 5° µ margin; Maya second for displacement closest
> to overshoot (42mm is only slightly over spec); Jordan last for under-spec displacement
> and zero µ margin. AI recommended no merger — Alberto's design meets all constraints
> on its own. Evidence: `evidence/loop1_linkage_comparison_synthesis.md`

**Team assessment:**
> Agreed with the ranking. Pushed back on the "merger" topic — AI analyzed L2=24mm at 48°
> (giving µ_min=42°, Δ≈19.5mm) as a possible merge, but concluded the gain (2mm narrower
> crank) doesn't justify the complexity. We accepted that. We also pushed back on the
> over-spec displacement concern for Maya's design — 42mm total jaw (vs. 40mm spec) is
> within the "0–40mm" range interpretation. AI acknowledged but maintained Alberto's
> closer match to spec as a decision factor.

**What changed:**
> Alberto's Part A design selected unanimously. Key drive-train input carried forward:
> linkage sweep = 45°, µ tolerance = +5° (can accept up to 50° sweep before leaving
> workable band). This coupling tolerance bound was new information the team generated
> from the comparison — not present in any individual Part A submission.

---

## Loop 2 — Drive-Train Architecture Selection

**Date:** 2026-05-23  
**Lead team member:** Maya Chen  
**Context provided to AI:** Gear pair design worksheet structure (Architecture A/B/C/D options),
N_needed=20 calculation, housing envelope 92×46×55mm, MP1 brief constraints. `miniclaw_rag`
skill active; MCP `query_miniclaw_docs` called for BigClaw gear reference photos.

**What we asked:**
> Evaluate all four architectures (single spur pair, compound spur, worm+wheel, sync+reduction)
> for N=20 inside the 92×46×55mm envelope. Which one fits?

**What we got back:**
> AI evaluated all four: Architecture A ruled out (z_driven=240 teeth at minimum z_driver=12 —
> gear diameter 240mm). Architecture B marginally feasible at m=1.2mm (non-standard) but
> tight. Architecture C (worm) achieves N=20 with d_wheel=40mm in 46mm height — 2mm clearance.
> Architecture D adds complexity. AI recommended Architecture C. Evidence: `evidence/loop2_drivetrain_architecture_selection.md`

**Team assessment:**
> AI's Architecture B analysis was the decisive contribution — we hadn't computed the
> Stage 1 center distance and the AI's math showed it exceeded the envelope. We pushed
> back on the worm self-locking concern: "self-locking is a feature for a gripper, not
> a bug." AI agreed. One item the AI under-emphasized: the tight 2mm clearance for the
> worm wheel in the housing — we added this as a trust assessment risk independently.

**What changed:**
> Architecture C selected. Self-locking assessed as a feature (jaws hold position).
> 2mm worm wheel housing clearance flagged as "Needs work" in trust assessment.

---

## Loop 3 — Worm Gear Sizing and Coupling Check

**Date:** 2026-05-24  
**Lead team member:** Jordan Park  
**Context provided to AI:** Worm stage row from gear pair worksheet, N=20 target, linkage
parameters, housing envelope. No RAG needed — purely computational.

**What we asked:**
> Size the worm: m_n=1.0mm, 2 starts, z_wheel=40. Verify all gear parameters are
> consistent (N=z/starts, center distance). Run the coupling check: at 2.5 thumb-wheel
> turns with N=20, what is the implied linkage sweep and transmission angle?

**What we got back:**
> AI computed: d_worm=10mm (q=10), d_wheel=40mm, C=25mm, N=20 ✓. Lead angle λ=11.3°.
> Coupling check: implied sweep = 900°/20 = 45° = Part A range exactly. µ at 45° = 45°.
> In band: Yes. Evidence: `evidence/loop3_worm_coupling_check.md`

**Team assessment:**
> All computations verified independently by Jordan. The coupling check passes perfectly
> because N was derived from N_needed — this was expected, but it was still valuable to
> confirm. The AI noted the d_a = 42mm addendum clearance is 1mm per side in the housing —
> but stated it as a note, not a flag. Jordan raised this as a design risk and added it
> to the trust assessment explicitly (as a "Needs work" item) — the AI's framing of "note"
> was too casual for a feature this tight.

**What changed:**
> Worm parameters finalized in gear pair design worksheet. Addendum clearance (1mm/side)
> added to trust assessment drive-train unverified list with correct flag severity.

---

## Loop 4 — DFM Pass on Worm Gear and Linkage Joints

**Date:** 2026-05-26  
**Lead team member:** Alberto Garza  
**Context provided to AI:** Full DFM checklist template + team's design parameters.
`miniclaw_rag` skill active for FDM process context.

**What we asked:**
> Walk through the DFM checklist for our worm gear (m_n=1.0mm, z=40) and linkage joints
> (pin holes, clearances). Flag anything that would cause a failed print or non-functional
> assembly on a standard FDM printer (0.4mm nozzle, PLA).

**What we got back:**
> AI flagged five items. Top two: (1) Worm tooth root = 0.78mm < 0.8mm FDM minimum —
> high risk; (2) Pin clearance: designed 3.0mm hole ID + 2.8mm pin OD = 0.2mm clearance,
> but FDM shrinkage produces 0.0mm clearance → interference fit. Evidence: `evidence/loop4_dfm_review.md`

**Team assessment:**
> Both flags were correct and actionable. Flag 2 (pin clearance) was a genuine catch —
> we had not accounted for FDM dimensional shrinkage. The fix (hole ID 3.0→3.2mm) was
> implemented immediately. Flag 1 (tooth root size) is the more serious long-term
> concern: the AI recommended stepping to m=1.2mm immediately, but we pushed back:
> "a test print is the right diagnostic before re-designing." AI acknowledged this as
> the more conservative (and more rigorous) approach. The worm shaft print orientation
> flag (must be upright) was also useful — we hadn't considered it.

**What changed:**
> Pin hole ID updated 3.0→3.2mm across all linkage joints. Worm tooth risk flagged
> in trust assessment. Worm shaft orientation confirmed upright. These changes are
> reflected in the completed DFM checklist.

---

## Loop 5 — Trust Assessment Gap Review

**Date:** 2026-05-28  
**Lead team member:** Maya Chen  
**Context provided to AI:** Full draft per-subsystem trust assessment (all six subsystems
with flags, verified/unverified lists). Asked for review of over-confident claims and
hidden assumptions.

**What we asked:**
> Review our trust assessment for hidden assumptions and over-confident "verified" claims.
> What's the single biggest risk we've missed?

**What we got back:**
> AI identified three concerns: (1) "verified" claims conflate analytical verification
> with physical testing; (2) worm self-locking listed as a feature but also creates
> a jam risk if over-driven; (3) housing clearance for worm wheel not reflected in
> the trust assessment (only in DFM). AI named worm gear printability at m=1.0mm as
> the single biggest risk ("the only failure mode that produces zero jaw motion").
> Evidence: `evidence/loop5_trust_assessment_review.md`

**Team assessment:**
> All three concerns were valid. The language refinement on Concern 1 was the most
> useful: the AI gave us the phrase "analytically verified, not bench-tested" which is
> more precise than just "verified." We applied this language throughout the trust
> assessment. Concern 2 (jam risk) was a genuine blind spot — we had mentioned
> self-locking as a feature but not considered the over-drive failure mode. Added
> to the drive-train unverified list. We pushed back on the AI's suggestion to upgrade
> the worm printability flag from "Unknown" to "Needs work": "Unknown is more honest
> than 'Needs work' if we haven't run a test print." AI agreed — "Needs work" implies
> a specific fix is known; "Unknown" means the state is uncharacterized. Flag kept
> as "Unknown" pending a test print.

**What changed:**
> Trust assessment language updated throughout: "analytically verified, not bench-tested"
> added to Subsystem 1. Worm jam risk (over-drive failure mode) added to Subsystem 2
> unverified list. Housing clearance added to Subsystem 2 unverified list. Worm
> printability remains "Unknown" (not downgraded to "Needs work").
