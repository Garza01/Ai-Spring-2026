# MP4 Part B — DFM Checklist

**Team:** _member names_

> If your team's chosen linkage geometry exists only as plots and not in
> CAD yet, prioritize bringing it (and the drive train) into a CAD tool
> of any team member's choice — SolidWorks, Fusion, Onshape, Blender,
> FreeCAD. A design that exists only in plot or sketch form will not
> survive Jordan's prototype review. He needs printable geometry.

This is the application checklist. Use your AI stack to walk it part by
part; commit your filled-in version as
`MP4/Part B/dfm_checklist_completed.md`. You can edit this file in place
or copy it to that name — either is fine, as long as the completed
version is in the repo.

The team is not expected to do a full formal DFM pass. The goal is to
identify the printability risks the team would actually flag at a print
queue review, and to document who looked at what.

---

## 1. Print Orientation

For each major part, name the orientation, why, and whether supports
are needed.

| Part | Orientation | Why | Supports? |
|------|-------------|-----|-----------|
| Linkage links (one of: ground, input, coupler, output) | _..._ | _e.g., flat — strongest in shear; layer lines perpendicular to load_ | _yes / no_ |
| Gear 1, Gear 2 | _..._ | _e.g., flat on the bed for tooth profile fidelity_ | _..._ |
| Jaw arm | _..._ | _..._ | _..._ |
| Housing (each shell, if split) | _..._ | _..._ | _..._ |
| Pins | _..._ | _e.g., upright; never along the layer line direction_ | _..._ |

**AI assist:** _which loop captured the most useful insight here? cite
the centaur log entry._

---

## 2. Wall Thickness and Feature Size

Minimum dimensions per part vs. FDM PLA capability. Standard FDM
nozzle: 0.4 mm; minimum feature: ~1 mm; minimum wall: 1.2 mm
(2 perimeters); minimum positive feature: ~0.8 mm.

| Part | Thinnest wall (mm) | Smallest feature (mm) | Flagged? |
|------|---------------------|------------------------|----------|
| _..._ | _..._ | _..._ | _..._ |
| _..._ | _..._ | _..._ | _..._ |

**Notes:** _which features are at risk and what would the team change?_

---

## 3. Pin and Joint Clearances

For each rotating joint:

- **Pin OD (CAD nominal):** _..._ mm
- **Hole ID (CAD nominal):** _..._ mm
- **Designed clearance:** _..._ mm
- **Expected clearance after print** (typical FDM: holes print ~0.10 mm
  undersize, pins ~0.10 mm oversize; net effect ≈ −0.20 mm on the
  designed clearance): _..._ mm
- **Fit class:** _interference / sliding / loose_
- **Accept?** _yes / no — if no, what changes_

> Repeat per joint type if your design uses different pin sizes.

---

## 4. Gear Printability

| Check | Value | Notes |
|-------|-------|-------|
| Module (mm) | _..._ | should be ≥ ~1.0 mm for FDM |
| Smallest tooth feature (root width or fillet) | _..._ mm | flag if < 1.0 mm |
| Tooth count (each gear) | _..._ / _..._ | low tooth counts (z < 12) print poorly |
| Face width (mm) | _..._ | flag if < ~3 mm |
| Print orientation | _..._ | flat on bed strongly preferred |
| Backlash designed in (mm) | _..._ | account for printer over-extrusion |

---

## 5. Overhangs and Bridges

Standard FDM PLA: overhangs to 45° usually clean; 60° often acceptable
with cooling; bridges up to ~10 mm typically fine.

| Feature | Angle / span | Concern? | Mitigation |
|---------|--------------|----------|------------|
| _e.g., housing top inner edge_ | 50° overhang | _..._ | _support / chamfer / re-orient_ |
| _..._ | _..._ | _..._ | _..._ |

---

## 6. Assembly Sequence

Order of operations from raw printed parts to functional gripper.

1. _..._
2. _..._
3. _..._
4. _..._

**Accessibility check:** can each fastener / pin be reached during
assembly without disassembling the part you just installed? _yes / no —
if no, name the conflict and the fix._

**Snap-fit engagement:** if the design uses snap fits, has the team
reviewed the deflection geometry against PLA brittleness? _yes / no_

---

## 7. Part Count

Target from the MP1 brief: **< 15 total parts**.

| Part | Count |
|------|-------|
| Linkage links (×4 per side × 2 sides) | _..._ |
| Pins | _..._ |
| Gears | _..._ |
| Jaw arms | _..._ |
| Housing pieces | _..._ |
| Input wheel / knob | _..._ |
| Other (name) | _..._ |
| **Total** | **_..._** |

**Under target?** _yes / no — if no, what merges or simplifications could the team explore in MP5?_

---

## 8. Print Time and Material Budget

Rough estimate from a slicer (PrusaSlicer, Bambu Studio, Cura) on the
team's chosen geometry. Don't sweat ±20% accuracy.

- **Total print time (hours):** _..._
- **Total material (grams or meters):** _..._
- **Print bed pieces (how many separate prints?):** _..._
- **Notes:** _e.g., "housing splits into two prints; everything else
  fits one bed."_

---

## DFM Pass Bottom Line

A 2–3 sentence team statement: would we send this to the print queue
tomorrow? Which two or three flags would the team most want to address
before we did?

> _..._

---

## AI Use During the DFM Pass

Document briefly which centaur loops in
`MP4_PartB_Team_Centaur_Log_Template.md` produced DFM findings, and
which AI suggestions the team rejected (and why).

> _..._
