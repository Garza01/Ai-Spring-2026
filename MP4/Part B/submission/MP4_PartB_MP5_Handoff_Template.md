# MP5 Handoff Document — Team Claw Alpha

This document explicitly bridges MP4 → MP5. The team uses it as the seed
for the MP5 presentation outline. Same team continues; same design
continues. Don't redo work in MP5 that this document already captured.

---

## Final Design Summary

Team Claw Alpha's MiniClaw uses Alberto Garza's Part A parallelogram four-bar linkage
(L1=L3=14mm, L2=L4=26mm, O4=(0,14), θ: 0°–45°) as the chosen single-side mechanism,
with the other side mirrored. The drive train is Architecture C: a worm + worm wheel
(2-start worm, z_wheel=40, m_n=1.0mm, N=20, center distance C=25mm). Synchronization
and counter-rotation of both sides is achieved by mounting two worm wheels — one per
side — on opposite sides of a common worm shaft, so both sides turn at the same rate
and in opposing directions when the thumb wheel is turned. At the 2.5-turn thumb-wheel
target, the implied linkage input sweep is exactly 45° — matching the Part A design
range and keeping the transmission angle at µ≥45° throughout.

---

## What's Prototype-Ready

*(Pulled from Per-Subsystem Trust Assessment — Subsystems with "Ready to print" flag
or verified analytical items)*

- **Linkage kinematics:** Single-side displacement = 19.89mm (total jaw = 39.78mm ≈
  40mm spec) verified by Python code, hand calc at three positions, and animation
  simulation — all three methods agree to <0.01mm. No out-of-band positions.
- **Transmission angle:** µ stays in [45°, 90°] across the full 0°–45° input range,
  5° above the workable-band floor. Verified analytically (µ = 90°−θ for vertical
  parallelogram) and confirmed numerically in Section 4 code.
- **Linkage envelope fit:** All joints stay within 26mm × 32.4mm (well within 46×55mm
  per-side budget), verified numerically at all 181 sweep angles.
- **Drive train coupling:** N=20 was derived from N_needed (2.5 turns × 360° / 45°) —
  coupling check passes exactly. No residual mismatch between drive-train reduction
  and linkage design range.
- **Counter-rotation arrangement:** Mirrored worm wheels on common shaft achieves
  simultaneous counter-rotation by geometry — verified by tangential force direction
  analysis (Loop 2).
- **Linkage print orientation and joint clearances:** Confirmed flat-on-bed for all
  linkage links; pin hole ID updated to 3.2mm after DFM review (Loop 4) to account
  for FDM shrinkage. Clearance after print: ~0.55mm per side — acceptable sliding fit.
- **Part count:** 12 printed parts — under the <15 target.

---

## What's Not Ready (and Why)

*(Pulled from Per-Subsystem Trust Assessment — Subsystems with "Needs work" or "Unknown" flag)*

- **Worm gear printability (Unknown):** Worm wheel tooth root = 0.78mm is at the FDM
  minimum feature threshold (~0.8mm). A test print of a worm wheel sector has not been
  done. This is the team's highest-risk single item — a failed print means zero jaw motion.
  Next step: print a 45° sector of the worm wheel and check tooth mesh quality.
- **Worm wheel housing clearance (Needs work):** Addendum circle diameter = 42mm in
  46mm housing height leaves 2mm total clearance (1mm per side). Below FDM recommended
  clearance. The housing bore pocket needs to be designed in CAD and the clearance
  verified after print.
- **Housing geometry (Needs work):** No 3D CAD model exists for the housing. Reference
  dimensions (92×46×55mm envelope, boss locations) are specified but no printable
  geometry exists. Housing is the highest-priority MP5 CAD task.
- **Jaw arm geometry (Unknown):** The 30mm tip extension is a kinematic dimension.
  The physical jaw arm shape (cross-section, rubber pad, mounting interface) is not
  designed. No jaw arm can be printed without this geometry.
- **Worm self-locking jam risk (Unknown):** Over-driving past the full-closed position
  self-locks the worm with a jam force that can snap teeth. A hard stop preventing
  θ > 45° has not been designed. Must be addressed before field use.
- **Symmetry under real worm shaft flex (Unknown):** Both worm wheels are on the same
  shaft. If the shaft flexes under load, one side may receive more torque and close
  faster. Not bench-tested.

---

## What We're Choosing to Demonstrate in MP5

The centerpiece demo is the **two-sided gripper closing on a cylindrical object**
(a soda can or similar, diameter 60–70mm). Both sides close symmetrically when the
thumb wheel is turned, demonstrating: (1) the jaw kinematics work as designed, (2)
both sides move at the same rate, and (3) the 40mm jaw opening spec is sufficient
for the target object.

The demo will use the **physical printed linkage** (Subsystem 1 only, mounted on a
flat plate) combined with the **Python animation** (showing the drive train's implied
motion in parallel) if the worm drive is not yet printed and verified. If the worm
test print passes before MP5, the full integrated demo (worm + linkage, two sides,
thumb wheel actuation) will be used. The "closing action" that shows the design is
real: both finger tips moving symmetrically from the open position (~44mm from ground)
to the closed position (~62mm from ground, ~8mm closer to center) in response to one
smooth thumb-wheel rotation.

---

## Open Questions Going Into MP5

- **Will the worm wheel mesh at m_n=1.0mm on a standard FDM printer?** This is the
  single question that determines whether the designed drive train is buildable without
  a module change. Answer requires a test print.
- **Does the 2mm worm-wheel-to-housing clearance survive the assembly process?** Even
  if the gear prints successfully, inserting the worm wheel into the housing bore may
  require post-processing (sanding, reaming) that is not currently planned for.
- **What is the actual grip force at the finger tips under realistic worm drive loading?**
  The < 5N estimate comes from the MP1 spring spec. With N=20 and the worm's mechanical
  efficiency (~30–40% for a lead angle of 11.3°), the thumb-wheel input torque needed to
  produce 5N at the tips may be higher than comfortable for a user. A torque analysis
  would close this question.
- **Can the housing be designed to close the depth constraint (worm drive + linkage =
  53mm in 55mm housing)?** Needs verification in a 3D CAD layout before printing the
  housing.

---

## Team Composition for MP5

Same team as MP4 Part B. Continuing through the final week.

- **Alberto Garza** — Lead on linkage analysis and MP5 technical narrative. Will run
  the linkage demo (physical print of single-side mechanism).
- **Maya Chen** — Lead on drive-train CAD. Priority: bring the worm gear into CAD
  (any tool: Onshape, Fusion, or FreeCAD) and print the test sector before the MP5
  demo.
- **Jordan Park** — Lead on housing CAD and integration layout. Priority: 3D layout
  of worm + linkage within the 92×46×55mm envelope to verify depth fit.

---

## Pointers Into MP4 Artifacts

For the MP5 portfolio narrative — link, don't copy:

- **Linkage Comparison Worksheet:** `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- **Drive-Train Design Worksheet:** `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- **Per-Subsystem Trust Assessment:** `MP4/Part B/MP4_PartB_Trust_Assessment_Template.md`
- **DFM Checklist (completed):** `MP4/Part B/dfm_checklist_completed.md`
- **Team Centaur Log:** `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md`
- **Part A notebook (Alberto):** `MP4/Part A/MP4_PartA_Build_to_Verify.ipynb`
- **Comparison plots:** `MP4/Part B/plots/displacement_comparison.png`, `MP4/Part B/plots/mu_comparison.png`
- **Drive train sketch:** `MP4/Part B/sketches/drive_train.png`
- **Part A motion artifacts:** `MP4/Part A/motion/four_bar_sweep.gif`
- **Part B evidence:** `MP4/Part B/evidence/` (5 centaur loop transcripts)
