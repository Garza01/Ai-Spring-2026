# MP4 Part B — Team Integration

**Due:** Friday, May 29, 2026 at 11:59 PM (same as Part A)
**Team size:** 3–4 students
**Time budget:** 6–10 hours across the team in the final 4–5 days

---

## What this is

The first team work of the quarter. Each team member arrives with a
four-bar linkage design from Part A (one side of the MiniClaw gripper,
with the other side assumed to mirror). The team's job is to integrate
those individual designs into one prototype-ready MiniClaw — pick the
linkage, design the **drive train** that synchronizes the two sides
and sets the reduction from thumb-wheel turns to linkage input angle
(Layer 1 of the architecture, deferred from Part A on purpose), and
stand up the rest of the gripper around that combination.

The deliverable is the package the team would actually 3D print, with an
honest per-subsystem trust assessment of what's verified and what's not.

## Team formation

Target: form your team **by Thursday May 21**. With ~13 students, the
class makes 3 or 4 teams of 3–4. Same team continues into MP5 the day
Part B is due — pick people you can keep working with for the final week.

## Suggested workflow timeline

Adjust to your team's calendar; this is the natural shape.

- **Day 1 (Thu May 21 – Fri May 22)** — Form team. Share Part A
  artifacts (notebooks, design summaries, trust ledgers, motion
  artifacts). Fill in the **Linkage Comparison Worksheet**. By end of
  the weekend you should have a chosen linkage.
- **Day 2–3 (Sat May 23 – Mon May 25)** — Design the **drive train**
  (architecture choice, per-stage specs, overall reduction N). Run the
  coupling check (does the chosen N still leave the linkage in the
  workable transmission angle band?). Sketch the rest of the MiniClaw
  integration: housing, jaw arms, joints. Begin DFM.
- **Day 4 (Tue May 26 – Wed May 27)** — Complete the **per-subsystem
  trust assessment**, the **DFM checklist**, and the **team centaur
  log**.
- **Day 5 (Thu May 28 – Fri May 29)** — Finalize the **MP5 handoff
  document**. Submit by 11:59 PM Friday. (Note: Quiz 2 is in class on
  Thursday May 28 — plan team work around it.)

## Deliverables

| File | What it is |
|------|------------|
| `MP4_PartB_Integration_Memo.docx` | The in-world memo from Jordan Chen — read this first; it's what you would have received from your engineering manager. |
| `MP4_PartB_Linkage_Comparison.md` | Day-one worksheet. Compare candidate linkages on the same axes; pick or merge one. |
| `MP4_PartB_Gear_Pair_Design.md` | Drive-train design — architecture choice (single spur pair, compound, worm, or sync-pair + separate reduction), per-stage specs, overall reduction N, packaging, coupling check against the chosen linkage. ("Gear pair" is shorthand in the filename; the worksheet covers the broader drive-train concept.) |
| `MP4_PartB_DFM_Checklist.md` | Apply the DFM checklist to the team's chosen geometry. Save the completed version as `dfm_checklist_completed.md`. |
| `MP4_PartB_Trust_Assessment_Template.md` | Per-subsystem trust assessment with prototype-readiness flags. The central evaluation artifact. |
| `MP4_PartB_Team_Centaur_Log_Template.md` | Five+ team centaur loops with evidence. |
| `MP4_PartB_MP5_Handoff_Template.md` | The bridge into MP5 — final design summary, what's ready, what isn't, what you'll demo. |
| `RUBRIC_MP4_PartB.md` | Grading rubric — read it before you start. |

## Submission

- Pick **one** team repo. All team members submit the **same** repo URL
  on Canvas as the Part B Website URL submission.
- The team repo's root should contain or link to all the artifacts above
  — completed templates, trust assessment, centaur log, MP5 handoff.
- Add a top-level `MP4_PartB_README.md` (or just `README.md` in the
  team repo root) that lists every artifact's path.
- Each team member's individual Part A repo is also linked from the
  team's README so the grader can trace the lineage.

## Helpful patterns

- **Don't separate the engineering work from the MP5 narrative.** The
  per-subsystem trust assessment IS the MP5 portfolio's evidence
  layer. Write it once, well; reuse next week.
- **Don't redo Part A analyses.** The Linkage Comparison combines
  existing position and transmission angle plots. The team only
  re-checks the linkage if the chosen reduction N significantly
  changes the input angle range.
- **Use the AI stack to synthesize, not just to design.** Loops where
  the team asks the AI "what's the team missing?" or "review this
  trust assessment for a hidden assumption" tend to land harder than
  loops that ask the AI to design something from scratch.
- **Five centaur loops is the floor, not the ceiling.** Bonus loops
  are useful evidence in MP5.

## Help

- Questions about scope or grading: post in the `#mp4` Slack channel
  or office hours.
- Stuck on the drive-train coupling check: read the Coupling Check
  section of `MP4_PartB_Gear_Pair_Design.md`. The math is one line; the
  judgment call is the part that matters.
- Pre-MP5 question: that's exactly what `MP4_PartB_MP5_Handoff_Template.md`
  is for — you don't have to answer it now, but write it down.
