---
name: miniclaw_gear_dfm_review
description: >
  Guide MiniClaw gear and jaw-drive reviews for ACME students by combining
  printed-gear design rules, Prusa MK4S manufacturing limits, BigClaw teardown
  precedent, and FilaTech PLA+ material constraints before a CAD design is
  released for the 500-unit RobotExpo build.
---

# MiniClaw Gear and DFM Review Skill

## When to use this skill

Use this skill when reviewing MiniClaw gears, jaw arms, gear housings, or
drive-train interfaces for the ACME MiniClaw project. Trigger it when the user
asks whether a MiniClaw CAD change is printable, whether a gear geometry is
strong enough, whether a tolerance is realistic for ACME's Prusa MK4S print
shop, or whether a BigClaw-inspired mechanism was scaled into PLA safely.

Do not use this skill for generic material selection, generic CAD aesthetics,
or project logistics that do not affect the MiniClaw mechanical design.

## Workflow

1. Identify the MiniClaw subassembly and design intent: gear, jaw arm, housing,
   pin, bore, or linkage. Name the load path and the interface being judged.
2. Consult `ACME-ENG-001` for printed spur-gear limits: preferred modules
   0.8, 1.0, and 1.25; minimum tooth counts; 20-degree pressure angle; face
   width at least 3x module and preferably 4-6x module for production.
3. Compare the design to the Hiwonder BigClaw teardown in `ACME-VND-002`.
   Use BigClaw as a geometry precedent, not a material precedent: its
   0.8-1.2 mm aluminum walls should become roughly 1.5-2.0 mm PLA walls.
4. Check ACME print-shop capability from `ACME-MFG-001`: Prusa MK4S fleet,
   0.4 mm nozzle, 250 x 210 x 220 mm build volume, general tolerance
   +/-0.25 mm, press-fit tolerance +/-0.15 mm, and critical dimensions no
   tighter than +/-0.10 mm with process control.
5. Check PLA+ stress assumptions from `ACME-MFG-002`: use 28 MPa interlayer
   adhesion for layer-critical features, not the 52 MPa bulk tensile strength.
   For printed gears, verify flat print orientation and 100% infill.
6. Check printed-assembly stack-up with `ACME-ENG-003`; for the MiniClaw gear
   mesh, prefer a single printed gear cavity so housing bore spacing is not
   split across two assembled halves.
7. Return a short engineering decision: PASS, FLAG, or FAIL. Tie each flag to
   a specific ACME document, MiniClaw feature, and recommended CAD change.

## What to flag

- Module below 0.8, a 14.5-degree pressure angle, or a tooth count below the
  `ACME-ENG-001` limit for the selected module.
- Gear face width below 3x module, or below the 4-6x module production range
  when the part is intended for repeated MiniClaw use.
- Backlash below 0.10 mm or above 0.15 mm for PLA gears, especially if thermal
  growth and print tolerance were not considered.
- PLA walls copied from BigClaw aluminum wall thickness; load-bearing MiniClaw
  housing walls should be about 1.5-2.0 mm, not 0.8 mm.
- Press-fit or bore tolerances tighter than the Prusa MK4S process can hold
  across a production run.
- Tolerance tighter than the ACME print shop can hold, especially a press-fit
  interface specified tighter than +/-0.15 mm without post-processing.
- Layer-critical features justified with 52 MPa bulk tensile strength instead
  of the 28 MPa interlayer adhesion value from `ACME-MFG-002`.
- PLA interlayer stress under-spec: gear teeth, snap fits, pins, or jaw arms
  loaded across layer lines without using the 28 MPa interlayer allowable.
- Gears printed on edge, jaw arms printed with layer lines across bending
  tension, or any support-heavy geometry that slows a 500-unit build.

## What NOT to do

- Do not approve a MiniClaw gear solely because it resembles the BigClaw. The
  BigClaw is machined aluminum; the MiniClaw is printed PLA+ and must use ACME
  print-shop limits.
- Do not treat RAG excerpts as a design signoff. Use the retrieved ACME
  standards to form a checkable recommendation and still name the remaining
  calculation or CAD measurement needed.
- Do not recommend tighter tolerances as the first fix. Prefer geometry that
  is robust to the +/-0.15 mm production capability unless the feature is truly
  critical and process control is documented.
