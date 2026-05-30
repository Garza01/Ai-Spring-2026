# MP4 Part B — Per-Subsystem Trust Assessment

**Team:** Team Claw Alpha — Alberto Garza, Maya Chen, Jordan Park  
**Linkage base:** Alberto Garza's Part A design (L1=L3=14mm, L2=L4=26mm, O4=(0,14),
θ: 0°–45°). Selected in the Linkage Comparison Worksheet on Day 1 for its 5° transmission
angle margin above the workable-band floor.  
**Design base for the rest of the MiniClaw:** Alberto Garza's MP1/MP2/MP3 housing
and jaw geometry. The BigClaw reference dimensions (92 × 46 × 55 mm housing, rubber
fingertip jaw arms) were used throughout Part A and inform the housing and jaw arm
sub-system entries here.

---

This is the central evaluation artifact. Every subsystem gets a flag —
**Ready to print**, **Needs work**, or **Unknown**. "Mostly there" is not
a flag. If the team doesn't know, that's also useful information; flag
it Unknown and write what you'd need in order to upgrade it.

---

## Subsystem 1: Four-Bar Linkage (single side, mirrored for the other)

**Status:** Ready to print

**What's verified** *(analytically verified, not bench-tested — see Loop 5 note)*:
- Single-side displacement = 19.89 mm at θ=45°, giving total jaw opening = 39.78 mm ≈ 40 mm.
  Verified by: Python `compute_finger_position()` code (two-circle intersection, <0.01mm
  numerical precision), hand calc at three positions (θ=0°, 22.5°, 45°) to <0.01mm,
  and matplotlib animation sweep. All three methods agree to within 0.01mm.
- Transmission angle stays in [45°, 90°] throughout θ=0°–45°. Verified analytically
  (µ = arccos(sin θ) = 90°−θ for vertical parallelogram) and confirmed numerically in
  Section 4 Python code. Min µ = 45° (5° above 40° workable-band floor).
- Parallelogram identity B = A + (O4−O2) holds at all θ, verified algebraically and
  numerically (branch=−1 cross-checked vs. link-length formula at θ=0°).
- Mechanism envelope: max width = 26mm, max joint height = 32.4mm — both within the
  46mm per-side width and 55mm depth housing budget, checked at all 181 sweep angles.
- No link interference across full input range: minimum link-to-link gap = 14mm
  (= L1, at θ=0°). Checked visually in animation and geometrically.
- Coupling check with the drive train (Subsystem 2): at N=20, implied linkage sweep
  = 45° = Part A range exactly. Transmission angle remains 5° above the workable
  band floor at the maximum implied input angle.

**What's not verified:**
- **Symmetry assumption:** The other side will mirror this linkage only if the drive
  train (Subsystem 2) counter-rotates both sides at exactly the same rate. This has
  been designed for (mirrored worm wheels on a common worm shaft) but not bench-tested.
  If the worm shaft flexes or one wheel has more backlash than the other, the two sides
  will not close symmetrically.
- **Physical link length tolerance:** The Part A analysis assumes ideal link lengths
  (error < 0.01mm from numerical precision). Real FDM PLA links have ±0.2–0.3mm
  dimensional accuracy. A 0.3mm error in L2 (26mm nominal, 1.2%) shifts µ_min by ~0.5°
  — negligible at 5° margin, but not zero. Not bench-tested.
- **Joint friction and wear:** The kinematic analysis treats joints as frictionless pins.
  Real PLA-on-PLA joint friction is uncharacterized for this geometry. Could affect
  jaw-closing force and smoothness.

**Risk if we print as-is:** If the drive train's worm wheels deliver slightly asymmetric
input to the two sides (due to backlash or shaft flex), the jaw will close unevenly —
manageable for a prototype but visible in a demo.

---

## Subsystem 2: Drive Train

*(Architecture C: worm + worm wheel, N=20, m_n=1.0mm, 2-start worm, z_w=40, C=25mm)*

**Status:** Needs work

**What's verified:**
- Architecture choice (C: worm + worm wheel) was evaluated against all four options in
  Loop 2. Architectures A and B are not feasible in this envelope at N=20. Architecture
  C is the compact single-stage solution.
- Stage ratio consistency: N = z_wheel / starts = 40 / 2 = 20 ✓
- Center distance formula: C = (d_worm + d_wheel)/2 = (10+40)/2 = 25mm ✓
- Coupling check: at N=20, implied linkage sweep at 2.5 turns = 45° = Part A range ✓
- Transmission angle at implied range: µ = [45°, 90°] — in the workable band ✓
- Counter-rotation arrangement: mirrored worm wheels on common worm shaft achieve
  counter-rotation by tangential force direction reversal (Loop 2 analysis).
- Self-locking assessment: worm with λ=11.3° lead angle and µ_f ≈ 0.1 (PLA–PLA) is
  self-locking under back-drive. This is desirable for the MiniClaw (jaws hold position
  without the user maintaining pressure on the thumb wheel).

**What's not verified:**
- **Worm gear printability at m_n=1.0mm:** Tooth root width ≈ 0.78mm is AT the FDM
  minimum feature threshold (~0.8mm). Print quality of the worm thread and wheel teeth
  at this module has not been verified by a test print. This is the team's single highest-
  risk item (flagged in Loop 4 and Loop 5).
- **Worm wheel housing clearance:** Worm wheel addendum circle diameter = 42mm in 46mm
  housing height — 2mm total clearance (1mm per side). This is below the FDM printed-
  part clearance recommendation (~1.5mm per surface). The housing bore for the worm
  wheel may need to be machined or post-processed.
- **Total depth fit:** Worm drive occupies ~20mm of the 55mm housing depth; linkage
  occupies ~33mm. Sum = 53mm with 2mm clearance to housing wall. Tight. Not verified
  in a 3D layout.
- **Backlash in printed worm mesh:** FDM worms at small module have unpredictable
  tooth-to-tooth variation. Backlash may produce perceptible jaw deadband near the
  open and closed limits. Not characterized.
- **Self-locking jam risk:** If the jaw is driven past the full-closed hard stop, the
  worm self-locks with the jam force in the worm thread — the user cannot reverse by
  hand. Over-driving can snap the worm wheel teeth. A hard stop on the linkage's input
  range (to prevent θ > 45°) has not been designed.
- **Symmetry at equal rate:** Both worm wheels are on the same worm shaft, which should
  synchronize them. But if the worm shaft flexes under load, one wheel may receive more
  torque than the other. Not bench-tested.

**Risk if we print as-is:** The worm gear tooth profile may not print at m=1.0mm, and
the worm wheel may not fit in the housing without post-processing. Either failure produces
zero jaw motion. This is the team's highest-risk subsystem.

---

## Subsystem 3: Jaw Arms (gripper fingers)

**Status:** Unknown

**What's verified:**
- The Part A design uses a 30mm tip extension past joint B along the coupler direction
  (vertical). For a parallelogram linkage, the finger translates without rotating —
  the contact face stays parallel throughout the jaw travel. This is the correct
  geometry for a parallel-jaw gripper.
- The finger tip is 62.4mm above O2 at maximum opening (θ=45°) and 44mm at the
  reference position (θ=0°). The tip traces a Euclidean arc of ~20mm displacement.

**What's not verified:**
- Physical jaw arm geometry: the 30mm tip extension is a kinematic dimension, not a
  designed finger arm shape. The arm cross-section, mounting interface to joint B, and
  any rubber fingertip pad geometry have not been designed.
- Grip force: the expected grip force (< 5N from the MP1 spring spec) has not been
  verified against the worm output torque at the jaw arm. Kinematic analysis only.
- Jaw arm stiffness: FDM PLA arms printed flat are strong in bending (layers
  perpendicular to load), but the arm geometry (width, thickness) is not specified.

**Risk if we print as-is:** Without a designed jaw arm geometry, there is nothing to
print for this subsystem. The kinematic pivot interface exists but the physical finger
shape is undefined.

---

## Subsystem 4: Housing and Mounting

**Status:** Needs work

**What's verified:**
- The housing envelope (92 × 46 × 55 mm) is consistent with the BigClaw reference
  and the MP1 brief.
- The housing must accommodate: two worm wheel bores (Ø42mm addendum circle), two O4
  pivot bosses (output ground pivots at (0,14) local from each O2), the worm shaft
  bearing seats, and the thumb wheel access aperture.
- Two-shell split (top + bottom) is a standard FDM approach for enclosed mechanism
  housings.

**What's not verified:**
- Housing geometry has not been modeled in CAD. The boss locations for O2, O4, and
  the worm shaft bearing seats are specified only as coordinates, not as designed features.
- Worm wheel bore clearance (Ø42mm addendum in 46mm housing): requires 2mm wall
  pocket — needs to be designed and verified in CAD.
- Total depth fit (worm drive + linkage = 53mm in 55mm housing): 2mm clearance at the
  back wall. Must be verified in 3D layout.
- Mount points for attaching the housing to an external structure (table clamp, robot
  arm, etc.) are not designed.

**Risk if we print as-is:** Without a CAD housing model, there is nothing to print. The
housing is the most unfinished subsystem in terms of designed geometry.

---

## Subsystem 5: Input Wheel / Thumb Wheel

**Status:** Unknown

**What's verified:**
- The MP1 brief specifies a "thumb wheel" or "knob" for manual actuation. The worm shaft
  accepts an input at one end (right side of housing). The required input torque is
  low (< 5N grip force × small moment arm through the worm).
- At N=20, the user needs to rotate the thumb wheel through 2.5 turns (900°) to fully
  open or close the jaw. This is a comfortable manual actuation range.

**What's not verified:**
- Thumb wheel geometry (OD, knurling, hub bore, shaft interface) is not designed.
- The worm shaft / thumb wheel coupling (press fit, set screw, keyed interface) is
  not specified.
- One-way operation: the worm is self-locking, so the thumb wheel can only drive the
  worm forward. Whether the user can feel the closed position (soft stop via worm
  torque increase) is not characterized.

**Risk if we print as-is:** Thumb wheel needs at minimum a designed hub and grip
surface before printing. No functional risk beyond assembly — the worm shaft can be
turned with a wrench in a pinch for testing.

---

## Subsystem 6: Pin / Joint System

**Status:** Needs work

**What's verified:**
- Four rotating joints per side: O2 (worm wheel output shaft — no separate pin), A
  (input crank to coupler), B (coupler to output crank), O4 (output crank to housing
  boss — captured pin in housing).
- Designed pin OD: M2 standard pins (1.9mm nominal OD). Designed hole ID: 3.2mm
  (updated from 3.0mm per Loop 4 DFM finding — accounts for FDM hole under-sizing
  of ~0.1mm per surface).
- Designed clearance: 3.2mm − 1.9mm = 1.3mm total (0.65mm per side) — loose fit,
  appropriate for rotating joints with light loads.
- Link length tolerance effect on joints: ±0.2–0.3mm FDM accuracy on link geometry
  (joint hole placement). Acceptable for this application.

**What's not verified:**
- Hole roundness in FDM: holes printed in the vertical (layer-line) direction have
  better roundness than holes printed perpendicular to layers. All linkage links are
  printed flat (hole axes vertical) — orientation is correct, but roundness after print
  has not been measured.
- Axial retention: pins through the link arms need retention (e-clips, through-cotter
  pins, or press-fit end caps) to prevent pull-out in use. Retention hardware is not
  specified.
- Friction and wear: PLA-on-steel pin contact (if using steel M2 pins) or PLA-on-PLA
  (if using printed pins). Contact friction and wear over cycle life are not characterized.

**Risk if we print as-is:** Joint holes at the specified 3.2mm ID with M2 pins (1.9mm OD)
will have ~0.65mm clearance — likely acceptable for a prototype but noisier than a
precision joint. Axial retention hardware must be specified before final assembly.

---

## Overall Prototype Readiness

The MiniClaw is partially prototype-ready. The **four-bar linkage mechanism** (Subsystem 1)
is the most thoroughly analyzed subsystem in the entire project — it has been verified
by three independent methods (Python code, hand calc, and animation) and all three agree
to within 0.01mm. If we were printing only the linkage on a flat plate, we would print
it tomorrow. The **drive train** (Subsystem 2) is the team's biggest risk: the worm gear
printability at m_n=1.0mm has not been tested, and a failed worm print means zero jaw
motion. We would not print the drive train without first test-printing a single worm
tooth profile and confirming it meshes correctly.

If Jordan handed us one more day before the print queue, we would use it to test-print
a worm wheel sector (a 1/8th arc of the z=40 wheel at m=1.0mm), mesh it against a short
worm test piece, and assess tooth engagement quality. If the mesh fails, we would step
to m=1.2mm and recalculate the worm wheel diameter (48mm — exceeds the 46mm housing
height by 4mm, which would require either a housing pocket or a change to z=36 teeth
and N=18). If the mesh passes, we would proceed to print the full drive train.

The **housing and jaw arms** (Subsystems 3 and 4) are the most underspecified: both
exist as kinematic parameters and reference dimensions but have no designed 3D geometry.
These are the MP5 priority items — the team needs to bring them into CAD before printing
is meaningful.

---

## Pointers Into Source Artifacts

- Chosen Part A linkage source: `MP4/Part A/MP4_PartA_Build_to_Verify.ipynb`
  (Alberto Garza's repo — same repo as this Part B submission)
- Linkage Comparison Worksheet: `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- Drive-Train Design Worksheet: `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- DFM Checklist (completed): `MP4/Part B/dfm_checklist_completed.md`
- Team Centaur Log: `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md` (completed)
- CAD or sketches folder: `MP4/Part B/sketches/` (drive train sketch), `MP4/Part B/plots/` (comparison plots)
- Part A motion artifacts: `MP4/Part A/motion/`
- Part A evidence: `MP4/Part A/evidence/`
