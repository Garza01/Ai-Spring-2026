---
name: 3d-printed-part-design-review
description: >
  Review a 3D-printable mechanical part for FDM-printability, structural
  adequacy, and annotation hygiene before the part is sent to a print queue.
  Use when a user pastes a sketch, render, drawing, or description of a part
  that will be printed in PLA, PETG, or similar FDM material on a desktop
  machine (Prusa-class, Bambu-class, hobby Ender-class).
---

# Skill: 3D-Printed Part Design Review

## When to use this skill

Trigger this skill any time the user presents a part — image, screenshot,
verbal description, or CAD export — and asks for a review, critique, or
"what's wrong with this." Use it whenever the part will be printed via FDM.
Do NOT trigger for SLA, SLS, or machined parts; the constraints are
different.

## Steps

1. **Identify the part class.** Bracket, gear, housing, snap-fit, jig,
   hand tool, decorative? Different classes have different failure modes.
2. **Walk the print orientation.** What direction will the layers run? FDM
   parts are 30–50% weaker across layers than along them. Call out any
   load that crosses a layer line.
3. **Check feature minimums.** Walls thinner than 0.8 mm, holes smaller
   than 1 mm, overhangs beyond 45°, unsupported bridges over 5 mm,
   lettering smaller than 2 mm tall — flag each one explicitly.
4. **Check tolerance specifications.** Anything tighter than ±0.1 mm
   (±0.004") on an FDM part is a red flag — it implies post-machining or
   the user does not understand FDM capability.
5. **Check annotation hygiene.** Are dimension callouts consistent? Are
   units mixed? Does the part name on the drawing match the file name?

## What to flag

- Tolerance specs tighter than the process can hold (±0.001", ±0.025 mm
  on an FDM print)
- Wall thicknesses below 0.8 mm
- Unsupported overhangs and undercuts that will fail without supports
- Press-fits or interference fits without a documented allowance for
  process dimensional accuracy
- Mixed-unit annotations (mm and inches on the same drawing without
  explicit conversion)
- Threaded features printed directly (recommend heat-set inserts or
  through-bolts unless the part is decorative)

## What NOT to do

- Do NOT recommend a different manufacturing process unless the user
  asked. The user has already committed to FDM. Your job is to make the
  FDM part work, not to talk them out of it.
- Do NOT assume an industrial printer. Default is desktop FDM with a
  0.4 mm nozzle and 0.2 mm layer height unless the user specifies
  otherwise.
- Do NOT speculate about features you can't see. If the image is unclear,
  say so and ask for a different view rather than inventing problems.

## Output format

Return findings as a numbered list, most-critical first. Each finding
should include: (1) what you see, (2) why it's a problem, (3) a concrete
fix. End with a one-sentence verdict ("ready to print," "ready after
edits," or "needs redesign").
