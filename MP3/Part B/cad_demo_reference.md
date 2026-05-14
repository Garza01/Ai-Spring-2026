# CAD Interaction Reference Example

This is **one** example of what the CAD interaction deliverable can look
like. You don't have to use OpenSCAD — pick whatever CAD you have access
to (SolidWorks, Fusion 360, Onshape, OpenSCAD, even a hand sketch). The
graded deliverable is the **AI interaction evidence**, not the CAD itself.

The example below uses OpenSCAD because every student can run it for
free. Two checkpoints — initial concept and refined version — two short
documented exchanges, one short writeup that ties them together.

---

## Example: Reviewing a 30T Spur Gear in OpenSCAD

### Checkpoint 1 — Initial concept

![gear v1](cad_review/gear_v1.png)

**OpenSCAD source (`gear_v1.scad`):**
```openscad
// MiniClaw drive gear v1 — first-pass parameters
module = 0.8;
teeth  = 30;
face   = 4.0;     // mm
bore   = 4.0;     // mm — to clear an M4 shaft
// ... gear() module elided
```

**Prompt to AI host (Copilot agent, MiniClaw skill loaded):**
> Reviewing a 30T spur gear for the MiniClaw drive train at module 0.8,
> 4 mm face width. What should I check given our PLA constraints?

**AI response (excerpt):**
> Calling `query_miniclaw_rag` for ACME's printed-gear standards...
>
> Based on `ACME-ENG-001` and the WidgetBot test report, three things
> to check:
> 1. Module 0.8 is on the small side — the standard recommends a
>    minimum of 16 teeth at module 0.8 to avoid undercutting. You're
>    fine at 30T but lock that in your spec sheet.
> 2. 4 mm face width is *thin* for the 5–8 N grip force range. The
>    Lewis bending check on the WidgetBot 2.0 program failed at face
>    widths under 5 mm with PLA. Recommend 5 mm minimum.
> 3. Add 0.05–0.10 mm to nominal center distance for thermal/print
>    growth — `ACME-ENG-001` calls this out explicitly.

**What I changed:** widened face to 5 mm; bumped the root fillet from
0.4 mm to 0.6 mm based on the WidgetBot failure analysis; documented
the center-distance allowance in the assembly drawing.

---

### Checkpoint 2 — Refined version

![gear v2](cad_review/gear_v2.png)

**Prompt:**
> Updated face width to 5 mm, root fillet to 0.6 mm. Anything else
> you'd flag before I commit this?

**AI response (excerpt):**
> Calling `query_miniclaw_rag` for the design review checklist and
> ACME PLA properties...
>
> Lewis check at 0.7 N·m output torque: σ ≈ 14 MPa with a form factor
> of 0.32. Against ACME's interlayer working stress (~28 MPa from
> `ACME-MFG-002`), safety factor is ~2.0 — meets the SF ≥ 2.0 rule.
> Good.
>
> Per `ACME-ENG-002` (design review checklist), two items I'd verify
> before release:
> - [ ] Contact ratio — couldn't find a value in the file. Compute
>       and add to the drawing.
> - [ ] Print-orientation note — gears must print flat for the
>       interlayer-stress argument to hold (per `ACME-MFG-001`).

**What I changed:** added contact ratio (1.62) to the drawing; added a
print-orientation note ("PRINT FLAT — TEETH IN-PLANE").

---

## What to submit

Files in your `cad_review/` directory:

```
MP3/Part B/cad_review/
├── cad_interaction.md      ← writeup tying the two checkpoints together
├── gear_v1.png             ← initial concept screenshot
└── gear_v2.png             ← refined version screenshot
```

Plus the AI conversation evidence — either embedded in `cad_interaction.md`
as quoted blocks (like the example above) or as separate transcript
captures in the same folder.

The CAD doesn't have to be polished. Two rough screenshots that show
real iteration are worth more than one beauty render.
