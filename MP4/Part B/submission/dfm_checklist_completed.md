# MP4 Part B — DFM Checklist (Completed)

**Team:** Team Claw Alpha — Alberto Garza, Maya Chen, Jordan Park  
**Date completed:** 2026-05-27  
**Centaur loop reference:** See Loop 4 (`evidence/loop4_dfm_review.md`) — AI walked
through the worm gear and pin joint sections; Flags 1 and 2 produced design changes.

> If your team's chosen linkage geometry exists only as plots and not in CAD yet,
> prioritize bringing it (and the drive train) into a CAD tool of any team member's
> choice. A design that exists only in plot or sketch form will not survive Jordan's
> prototype review.

**Status:** Linkage mechanism is fully specified numerically (all Part A plots). Drive
train is sketched (see `sketches/drive_train.png`) but not in CAD. Housing and jaw arms
are not yet in CAD. This checklist documents what is known from the numerical design.

---

## 1. Print Orientation

For each major part, name the orientation, why, and whether supports are needed.

| Part | Orientation | Why | Supports? |
|------|-------------|-----|-----------|
| Linkage input crank (L2=26mm bar) | Flat on bed (length horizontal, pin holes vertical) | Strongest in bending; layer lines perpendicular to jaw-closing load; pin holes in vertical direction have best roundness | No |
| Linkage coupler (L3=14mm bar) | Flat on bed (length horizontal, pin holes vertical) | Same as input crank | No |
| Linkage output arm (L4=26mm + 30mm tip extension) | Flat on bed (length horizontal) | Same as crank; tip extension is colinear and prints flat with no overhang | No |
| Worm wheel | Flat on print bed (wheel axis vertical) | Tooth profile is in the XY plane — best fidelity; gear teeth point upward, no overhang | No |
| Worm shaft | Upright (worm axis vertical) | Helix thread requires upright orientation to avoid >45° overhangs on thread flanks; printed on side creates unsupported 80° overhangs | No (with upright orientation) |
| Housing shell (top / bottom) | Each shell flat on bed, open face down | Largest flat face on bed for adhesion and surface finish; interior features accessible from open face | Minimal (overhanging boss lips only) |
| Thumb wheel | Flat on bed | Circular grip surface prints cleanest flat | No |

**AI assist:** Loop 4 identified that the worm shaft must be printed upright (axis
vertical) to avoid unsupported thread flanks. All linkage links confirmed flat-on-bed.

---

## 2. Wall Thickness and Feature Size

Minimum dimensions per part vs. FDM PLA capability.  
Standard FDM nozzle: 0.4 mm; minimum feature: ~1 mm; minimum wall: 1.2 mm (2 perimeters);
minimum positive feature: ~0.8 mm.

| Part | Thinnest wall (mm) | Smallest feature (mm) | Flagged? |
|------|---------------------|------------------------|----------|
| Linkage crank bar | 3.0 (strap section) | 3.0 (bar width) | No — well above minimum |
| Linkage coupler bar | 3.0 | 3.0 | No |
| Linkage output arm | 3.0 | 3.0 | No |
| Worm wheel tooth root | 1.8 (tooth strap) | **0.78 mm** (root width at m=1.0mm) | **YES — at FDM minimum feature threshold** |
| Worm shaft thread | 2.0 (flank thickness) | **~1.0 mm** (thread tooth at m=1.0mm) | **Marginal — test print required** |
| Housing shell | 2.0 (nominal wall) | 2.0 | No |
| Pin holes (after FDM) | n/a | 3.2 mm ID (designed) → 3.0mm after shrinkage | Marginal — see Section 3 |

**Notes:** The worm wheel tooth root (0.78mm) is below the FDM minimum feature (~0.8mm).
This is the single highest-priority manufacturing concern. The team's mitigation is to
test-print a worm wheel sector before committing to the full gear. If the tooth feature
fails, the module will be stepped up to m_n=1.2mm (tooth root ≈ 0.94mm — above
threshold), with the worm wheel diameter increasing to 48mm (exceeds 46mm housing
height by 4mm — requires a housing pocket or reduction of z_w to 36 with N=18).

---

## 3. Pin and Joint Clearances

Linkage has four joint types: O2 (worm wheel output shaft — no separate pin), A
(input crank ↔ coupler), B (coupler ↔ output arm), O4 (output arm ↔ housing boss).

**Joints A and B (rotating, both sides, 4 total):**
- **Pin OD (CAD nominal):** 1.9 mm (M2 steel pin, purchased hardware)
- **Hole ID (CAD nominal):** 3.2 mm *(updated from 3.0mm after Loop 4 DFM review)*
- **Designed clearance:** 3.2 − 1.9 = 1.3 mm total (0.65 mm per side)
- **Expected clearance after print** (FDM: holes ~0.1mm undersize, pins are purchased
  steel so no oversize): 3.2 − 0.1×2 (two-wall effect) = 3.0mm actual hole ID.
  Clearance after print: 3.0 − 1.9 = 1.1 mm total (0.55 mm per side)
- **Fit class:** Loose sliding (appropriate for freely rotating joints under light load)
- **Accept?** Yes — 0.55mm per side clearance allows free rotation with minimal
  perceptible play for a lightweight gripper

**Joint O4 (captured in housing boss):**
- Boss ID (CAD nominal): 3.2 mm (same hole as A and B for single pin-size inventory)
- Pin OD: 1.9 mm steel. Fit class: same as A and B.
- O4 pin is pressed into housing boss and retained with a friction cap or e-clip.

**Note:** All four pin holes use the same 3.2mm / M2 specification to minimize hardware
inventory. This was a Loop 4 recommendation accepted by the team.

> Repeat: O2 joint is the worm wheel output shaft — this is a 3D-printed hub or shaft
> integrated into the worm wheel body. No separate pin. Bearing/clearance on the worm
> wheel hub bore (housing bearing seat) to be specified in CAD.

---

## 4. Gear Printability

| Check | Value | Notes |
|-------|-------|-------|
| Module (mm) | 1.0 | At FDM lower threshold; test print required before committing |
| Smallest tooth feature (root width) | **0.78 mm** | Below ~0.8mm FDM minimum — **FLAGGED** |
| Tooth count (worm / worm wheel) | 2 starts (worm) / 40 (wheel) | Worm: 2 starts is low tooth engagement but acceptable for this load |
| Face width (mm) | 8 (worm wheel) | Above ~3mm minimum; adequate for hobby-scale load |
| Print orientation | Worm wheel: flat on bed. Worm shaft: upright. | Both confirmed in Section 1 |
| Backlash designed in (mm) | None explicitly (rely on nominal dims + FDM tolerance). Expected backlash: 0.1–0.3mm per tooth due to FDM form errors | Should be measured on test print; no designed backlash relief |

**DFM bottom line for gears:** The worm drive is the highest-risk single component in the
design. The tooth root width is at the FDM capability limit. A test-print of the worm
wheel sector (cost: ~30 min print time) would definitively resolve the risk before the
team commits to a full drive train print.

---

## 5. Overhangs and Bridges

| Feature | Angle / span | Concern? | Mitigation |
|---------|--------------|----------|------------|
| Worm shaft thread flanks (if printed on side) | ~80° overhang | **Yes — critical** | Print upright (axis vertical); flanks become self-supporting at <45° with upright orientation |
| Housing top inner edge (worm shaft aperture) | 55° overhang | Marginal | Add 2mm chamfer to reduce overhang to 45°; OR include minimal support material at aperture lip |
| Linkage crank pin holes (top edge) | 45° partial overhang at hole top | Acceptable | No support needed — 45° is the FDM PLA clean-print threshold |
| Thumb wheel grip knurling (if designed) | Surface texture ~0.3mm depth | Low concern | Print at 45° tilt or add 0.2mm draft to knurl roots |

---

## 6. Assembly Sequence

Order of operations from raw printed parts to functional gripper:

1. **Press O4 pivot pins** into housing boss bores (both sides). Verify pins are flush
   and perpendicular; they are now permanently captured.
2. **Insert output arm** onto O4 pivot pin (one per side). Snap on axial retention cap
   (e-clip or printed end cap) to prevent pull-out.
3. **Attach coupler to output arm at joint B** using M2 pin through coupler and output
   arm aligned holes. Retain with end cap.
4. **Attach input crank to coupler at joint A** using M2 pin. Retain.
5. **Install worm wheels** (one per side) into housing bore. Each worm wheel hub
   inserts into the housing bearing seat; the hub IS the O2 pivot for the linkage. Press
   or slide fit into the housing bore; secure with a circlip or boss cap.
6. **Connect input crank to worm wheel hub** — the input crank's O2 hole slides over
   the worm wheel hub shaft.
7. **Insert worm shaft** through the housing bearings (left and right sides). Mesh the
   worm threads with each worm wheel. Verify meshing by hand before inserting the
   second bearing.
8. **Attach thumb wheel** to the exposed end of the worm shaft. Press-fit or set-screw
   retention.
9. **Close housing** (press top shell onto bottom shell). Secure with M3 screws through
   housing bosses (×4 corners).
10. **Test actuation** by turning the thumb wheel. Verify both sides close symmetrically.

**Accessibility check:** Each pin can be accessed and retained before the next link is
added. The critical accessibility point is Step 7 (worm shaft meshing): the housing must
be open (Step 9 comes after Step 7) to allow visual confirmation of tooth mesh. This
is correctly sequenced. **Yes — accessible throughout assembly.**

**Snap-fit engagement:** The design does not use snap fits (PLA brittleness concern noted
in Loop 4). All closures use M3 screws (housing) or press-fit axial caps (pins). **Yes — reviewed.**

---

## 7. Part Count

Target from the MP1 brief: **< 15 total parts**.

| Part | Count |
|------|-------|
| Linkage input cranks (×1 per side × 2 sides) | 2 |
| Linkage couplers (×1 per side × 2 sides) | 2 |
| Linkage output/finger arms (×1 per side × 2 sides) | 2 |
| Worm wheel assemblies (×1 per side × 2 sides, with integrated O2 hub) | 2 |
| Worm shaft (one continuous shaft with worm thread) | 1 |
| Thumb wheel | 1 |
| Housing shells (top + bottom) | 2 |
| **Total printed parts** | **12** |
| M2 steel pins (joint A and B, ×2 per side = 4 total) — *purchased hardware* | 4 |
| M3 screws for housing (×4 corners) — *purchased hardware* | 4 |
| Pin retention caps (×4 joints) — *printed or purchased* | 4 |
| **Grand total including hardware** | **24** |

**Under target for printed parts?** Yes — **12 printed parts** < 15 target ✓  
**Grand total including hardware:** 24 parts. Over the 15-part target if hardware is
counted. **If MP5 needs to reduce:** the retention caps could be integrated into the
link geometry (snap groove or wire through pin) to eliminate 4 parts. The O4 pivot could
be a boss molded into the housing (removing 2 pins). This would bring the total to ~18.
Further simplification would require design changes (e.g., snap-fit housing closure
to eliminate 4 screws — with PLA brittleness risk).

---

## 8. Print Time and Material Budget

Rough estimate from PrusaSlicer (0.4mm nozzle, 20% infill, 0.2mm layer height, PLA):

- **Linkage links (6 parts):** ~45 min total, ~15g PLA
- **Worm wheel (2 parts, flat):** ~60 min total, ~25g PLA
- **Worm shaft (upright, includes thread detail):** ~90 min, ~20g PLA
- **Thumb wheel:** ~20 min, ~8g PLA
- **Housing shells (2 parts):** ~180 min total (dominant print time), ~80g PLA
- **Pin caps (4 parts):** ~10 min total, ~2g PLA

- **Total print time (hours):** ~6.75 hours
- **Total material (grams):** ~150g PLA
- **Print bed pieces:** 5 separate print jobs
  (1: linkage links all together; 2: worm wheels; 3: worm shaft (upright); 4: housing
  bottom; 5: housing top + thumb wheel + caps)
- **Notes:** Housing shells are the dominant print time and should be scheduled first.
  Worm shaft must be printed alone (upright orientation is incompatible with a shared bed).

---

## DFM Pass Bottom Line

We would NOT send this to the print queue tomorrow. The two flags the team would most
want to address first are: **(1) Worm wheel tooth feature size** — root width 0.78mm
is below the FDM threshold; a test print of one worm wheel sector would confirm
printability at m=1.0mm in ~30 minutes and resolve the team's single highest-risk item.
**(2) Housing geometry in CAD** — the housing is currently specified only as a bounding
box with reference dimensions; no 3D model exists, and no print is possible without it.
A third flag worth addressing before the print queue: **(3) worm wheel bore clearance**
in the housing — the 42mm addendum circle in the 46mm housing leaves only 2mm of
clearance, which may require a precision pocket that FDM cannot produce without
post-processing.

---

## AI Use During the DFM Pass

Loop 4 (`evidence/loop4_dfm_review.md`) was the primary DFM centaur loop. The AI
flagged the worm tooth root width (0.78mm < 0.8mm threshold) and the pin clearance
issue (FDM under-sizing producing an interference fit at the original 3.0mm hole ID).
Both flags were correct and led to design changes (pin hole updated to 3.2mm; worm
wheel test print required before committing). The team rejected the AI's suggestion
to step to m=1.2mm without testing, on the grounds that a test print is the appropriate
next step rather than an immediate re-design.
