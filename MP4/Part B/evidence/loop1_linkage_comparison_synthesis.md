# Team Centaur Loop 1 — Linkage Comparison Synthesis

**Date:** 2026-05-22  
**Lead:** Alberto Garza  
**Context provided to AI:** Pasted all three Part A design summaries (link lengths, input ranges, displacement values, transmission angle ranges, trust ledger highlights) into Claude Desktop. `miniclaw_rag` skill active. No MCP tool call — all context was inline text.

## What we asked

> We have three Part A four-bar linkage designs for the MiniClaw gripper. All three are
> parallelogram four-bars with vertical ground links:
>
> 1. Alberto: L1=L3=14, L2=L4=26, θ: 0°–45°, displacement≈19.9mm, µ: 90°→45°
> 2. Maya:    L1=L3=12, L2=L4=25, θ: 0°–50°, displacement≈21.1mm, µ: 90°→40°
> 3. Jordan:  L1=L3=16, L2=L4=22, θ: 0°–50°, displacement≈18.6mm, µ: 90°→40°
>
> All target 40mm total jaw opening. Which design should we select as the team base,
> and what trade-offs are we accepting?

## What we got back

The AI ranked the designs on three axes:

1. **Transmission angle margin:** Alberto's design (µ_min=45°) wins. Maya and Jordan hit
   exactly 40° at their input maximum — right at the floor of the workable band. The AI
   noted: "At the workable-band floor, a small manufacturing error in link lengths or
   a slightly larger-than-designed input sweep (common if the gear pair is slightly
   off-ratio) will push the linkage out of band. Alberto's 5° margin is a meaningful
   buffer."

2. **Displacement match:** Alberto (19.9mm) is closest to the 20mm target. Maya (21.1mm)
   slightly overshoots — the griper would have 42mm total opening, not a problem but
   off-spec. Jordan (18.6mm) slightly undershoots — 37.2mm total, noticeably under the
   40mm target.

3. **Mechanism compactness:** Jordan uses the shortest crank (L2=22mm), fitting most
   compactly width-wise. Alberto's 26mm crank is the largest but still within the 46mm
   half-envelope budget.

**AI recommendation:** Alberto's design, citing the transmission angle margin as the
decisive factor. "A design on the floor of the workable band is at risk of binding
in use; 5° of margin costs nothing in terms of displacement or size."

## Team assessment

We agreed with the AI's ranking. Two pushbacks:

1. **Jordan's displacement under-target:** The AI said "37.2mm total opening is
   noticeably under the 40mm target." We pushed back: the MP1 brief says "0–40 mm,"
   meaning the target is 40mm maximum, not exactly 40mm. A 37.2mm device is within spec
   if Jordan's design has other benefits. The AI acknowledged this was fair, but noted
   that Alberto's design meets the spec more precisely.

2. **Merger option:** We asked whether merging designs (e.g., Alberto's transmission
   angle margin with Jordan's shorter crank) would improve things. The AI's response:
   "You could use L2=24mm (Jordan-length crank) with a θ range of 0°–48°: displacement =
   2×24×sin(24°) ≈ 19.5mm and µ_min = 42°. That's a modest improvement in width with
   a smaller transmission angle margin. The gain is ~2mm in crank width; the cost is
   2° less margin. Not clearly better." We agreed — not worth the complexity. Stick with
   Alberto's design unchanged.

## What changed

Team selected Alberto's Part A design (L1=L3=14, L2=L4=26, θ: 0°–45°) as the base.
Key drive-train input: linkage sweep = 45°, µ tolerance = 5° (input can go up to 50°
before leaving the workable band). This tolerance constraint was carried forward to
the gear pair design worksheet.
