# MP4 Part B — Per-Subsystem Trust Assessment

**Team:** _member names_
**Linkage base:** _which team member's linkage, see Linkage Comparison_
**Design base for the rest of the MiniClaw:** _whose MP1/MP2/MP3 design
served as the base for housing, jaws, etc., why_

---

This is the central evaluation artifact. Every subsystem gets a flag —
**Ready to print**, **Needs work**, or **Unknown**. "Mostly there" is not
a flag. If the team doesn't know, that's also useful information; flag
it Unknown and write what you'd need in order to upgrade it.

The four-bar linkage and the drive train are top-level subsystems
because they are the two integration anchors. Subsystem categories
below can be adjusted if the team's design organizes differently — but
every part of the gripper must show up somewhere with a flag.

---

## Subsystem 1: Four-Bar Linkage (single side, mirrored for the other)

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:**
- _Pull from the chosen member's Part A trust ledger; cite the entries._
- _Note any additional team work, especially if the chosen reduction N
  shifted the linkage's input angle range and you re-checked the
  transmission angle band at the new range._
- _..._

**What's not verified:**
- _Specific. Including the symmetry assumption from Part A, which has
  now become "depends on the drive-train design (Subsystem 2) actually
  achieving counter-rotation at the same rate."_
- _..._

**Risk if we print as-is:** _one sentence._

---

## Subsystem 2: Drive Train

*(the hardware that synchronizes the two sides AND sets the reduction
from thumb-wheel turns to linkage input angle — your team's choice of
architecture from the worksheet: single spur pair, compound spur train,
worm + worm wheel, or sync-only pair + separate reduction element)*

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:**
- _Pull from the drive-train worksheet — architecture choice, per-stage
  spec consistency (stage ratios multiply to the stated overall N),
  packaging, symmetry arrangement, the coupling check against the
  linkage._
- _..._

**What's not verified:**
- _Architecture-appropriate failure modes the team has not bench-tested:_
  - _Spur stages: tooth strength under realistic load (Lewis was
    optional), backlash in printed gears, real-world meshing under load
    (printed PLA gears at small module deflect more than steel)_
  - _Worm + wheel: self-locking behavior under back-drive, sliding
    contact wear, thread accuracy at small module_
  - _Separate reduction element: friction / efficiency, slip, end-stop
    behavior_

**Risk if we print as-is:** _one sentence._

---

## Subsystem 3: Jaw Arms (gripper fingers)

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:** _..._
**What's not verified:** _..._
**Risk if we print as-is:** _..._

---

## Subsystem 4: Housing and Mounting

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:** _..._
**What's not verified:** _..._
**Risk if we print as-is:** _..._

---

## Subsystem 5: Input Wheel / Servo Coupling

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:** _..._
**What's not verified:** _..._
**Risk if we print as-is:** _..._

---

## Subsystem 6: Pin / Joint System

**Status:** _Ready to print / Needs work / Unknown_

**What's verified:** _..._
**What's not verified:** _..._
**Risk if we print as-is:** _..._

---

## Overall Prototype Readiness

> _2–3 paragraph team statement: would we print this tomorrow? What's
> the single biggest risk? What would we change first if Jordan handed
> us another day?_

---

## Pointers Into Source Artifacts

For graders and teammates who want the underlying evidence, list
explicit paths:

- Chosen Part A linkage source: `path/to/MP4_PartA_Build_to_Verify.ipynb`
  (which member's repo)
- Linkage Comparison Worksheet: `MP4_PartB_Linkage_Comparison.md`
- Drive-Train Design Worksheet: `MP4_PartB_Gear_Pair_Design.md`
- DFM Checklist (completed): `dfm_checklist_completed.md`
- Team Centaur Log: `MP4_PartB_Team_Centaur_Log_Template.md` (completed)
- CAD or sketches folder: _path_
