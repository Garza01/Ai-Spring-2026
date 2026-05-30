# MP4 Part B — Team Claw Alpha Submission

**Team:** Alberto Garza, Maya Chen, Jordan Park  
**Repo:** `Ai-Spring-2026` (Alberto Garza — team submission repo)  
**Submission date:** 2026-05-29

---

## Artifact Index

### Core Design Documents

| Artifact | Path | Description |
|----------|------|-------------|
| Linkage Comparison Worksheet | `MP4/Part B/MP4_PartB_Linkage_Comparison.md` | Compares all three Part A designs; selects Alberto's (µ_min=45°, 5° margin) |
| Drive-Train Design Worksheet | `MP4/Part B/MP4_PartB_Gear_Pair_Design.md` | Architecture C: worm + worm wheel, N=20, m_n=1.0mm, C=25mm |
| DFM Checklist (completed) | `MP4/Part B/dfm_checklist_completed.md` | Print orientation, wall/feature sizes, pin clearances, gear printability, assembly sequence, part count |
| Per-Subsystem Trust Assessment | `MP4/Part B/MP4_PartB_Trust_Assessment_Template.md` | Six subsystems with Ready/Needs work/Unknown flags |
| Team Centaur Log | `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md` | Five centaur loops (linkage comparison, arch selection, worm sizing, DFM, trust gap review) |
| MP5 Handoff Document | `MP4/Part B/MP4_PartB_MP5_Handoff_Template.md` | Final design summary, prototype-ready items, open risks, demo plan, role assignments |

### Visual Artifacts

| Artifact | Path | Description |
|----------|------|-------------|
| Displacement comparison plot | `MP4/Part B/plots/displacement_comparison.png` | All three candidate linkages vs. 20mm/side target |
| Transmission angle comparison plot | `MP4/Part B/plots/mu_comparison.png` | µ across θ sweep for all three candidates; 40°–140° workable band |
| Drive train sketch | `MP4/Part B/sketches/drive_train.png` | Worm shaft + mirrored worm wheels diagram with all parameters labeled |

### Centaur Loop Evidence

| Loop | Path | Topic |
|------|------|-------|
| Loop 1 | `MP4/Part B/evidence/loop1_linkage_comparison_synthesis.md` | Linkage ranking and team selection |
| Loop 2 | `MP4/Part B/evidence/loop2_drivetrain_architecture_selection.md` | Drive-train architecture evaluation (A/B/C/D) |
| Loop 3 | `MP4/Part B/evidence/loop3_worm_coupling_check.md` | Worm gear sizing and coupling check |
| Loop 4 | `MP4/Part B/evidence/loop4_dfm_review.md` | DFM pass — tooth root flag, pin clearance fix |
| Loop 5 | `MP4/Part B/evidence/loop5_trust_assessment_review.md` | Trust assessment gap review |

---

## Team Part A Repos

Each team member's individual Part A submission is in the same repo under `MP4/Part A/`:

| Team Member | Part A Notebook | Key Design Parameters |
|-------------|----------------|----------------------|
| **Alberto Garza** *(selected design)* | `MP4/Part A/MP4_PartA_Build_to_Verify.ipynb` | L1=L3=14mm, L2=L4=26mm, O4=(0,14), θ: 0°–45°, Δ=19.89mm/side, µ: 45°–90° |
| Maya Chen | *(Part A in Maya's repo)* | L2=25mm, Δθ=50°, Δ≈21mm/side, µ_min=40° |
| Jordan Park | *(Part A in Jordan's repo)* | L2=22mm, Δθ=50°, Δ≈17mm/side, µ_min=40° |

Alberto's Part A motion artifacts: `MP4/Part A/motion/four_bar_sweep.gif`  
Alberto's Part A linkage sketch: `MP4/Part A/evidence/linkage_sketch.png`

---

## Final Design Summary

- **Chosen linkage:** Alberto Garza's parallelogram four-bar (L1=L3=14mm, L2=L4=26mm). Selected for 5° transmission angle margin (µ_min=45°) above the workable-band floor.
- **Drive train:** Architecture C — worm + worm wheel (2-start worm, z_wheel=40, m_n=1.0mm, N=20, C=25mm). Counter-rotation via mirrored worm wheels on a common worm shaft.
- **Coupling:** At 2.5 thumb-wheel turns with N=20, implied linkage sweep = 45° exactly. Transmission angle stays in [45°, 90°].
- **Total jaw opening:** 39.78mm ≈ 40mm spec. Verified by Python code, hand calc, and animation — all agree to <0.01mm.
- **Highest risk:** Worm wheel tooth root = 0.78mm at FDM minimum feature threshold (~0.8mm). Test print of a worm wheel sector required before full drive train print.

---

## Artifact Generator

The script used to generate all plots and the drive train sketch:  
`MP4/Part B/generate_partb_artifacts.py`

Run with: `/Users/albertogarza/anaconda3/bin/python3 "MP4/Part B/generate_partb_artifacts.py"`
