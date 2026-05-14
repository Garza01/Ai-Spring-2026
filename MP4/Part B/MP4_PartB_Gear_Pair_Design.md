# MP4 Part B — Gear Pair Design

**Team:** _member names_
**Chosen linkage (see Linkage Comparison):** _member name or "merged"_
**Linkage input angle range:** from _..._° to _..._° *(from chosen Part A design)*

---

This is the work that Part A explicitly deferred to the team. The drive
train sits between the thumb wheel input and the linkage input pivot —
it synchronizes the two sides (counter-rotation at the same rate) AND
sets the reduction between thumb wheel turns and linkage input angle.
The reduction and the linkage choice are coupled: if the chosen
reduction pushes the linkage outside its workable transmission angle
band, you fix one or the other.

A labeled sketch is enough — full production CAD on the drive train is
not required.

> "Gear pair" is short-hand. The actual hardware that does these two
> jobs is up to the team: a single spur pair, a compound (multi-stage)
> spur train, a worm + worm wheel, or a sync-only spur pair with a
> separate reduction element. A single spur pair is usually too small
> a ratio to handle 2–3 thumb-wheel turns alone (the envelope can't
> hold the tooth counts a one-stage 18:1 would need), so most teams
> end up at a compound train or worm. The worksheet below adapts.

---

## Ratio Convention (read this before filling anything in)

Everything below uses **overall reduction N**, defined unambiguously:

> **N = (thumb wheel angle range, deg) / (linkage input angle range, deg)**

N is a single dimensionless number ≥ 1 for a step-down (which is what
the MP1 brief asks for: 2–3 thumb-wheel turns into a small linkage
sweep). For a single spur pair with z₁ on the thumb-wheel side and z₂
on the linkage side, **N = z₂ / z₁**. For a compound train,
**N = (z₂/z₁) × (z₄/z₃) × …** — the product of per-stage ratios. For
a worm + worm wheel, **N ≈ z_wheel / (worm thread starts)**.

Use this one definition for every number on this page. Bigger N means
more reduction means more thumb-wheel turns per linkage degree.

---

## Architecture Choice

Pick one. The choice tells you which rows of the specs table to fill.

- [ ] **A. Single spur pair.** One pair of meshing spur gears does both
  jobs (sync + reduction). Simplest. Usually only feasible if the team
  accepts fewer thumb-wheel turns than the MP1 target — N values around
  18 don't fit a single spur pair in this envelope.
- [ ] **B. Compound spur train (multi-stage).** Two or more spur stages
  in series, each contributing part of the reduction. Common solution
  when N ≳ 5 and the envelope can't hold one big gear.
- [ ] **C. Worm + worm wheel.** High reduction in one stage, with a 90°
  axis change. Compact for big N. Note: worm gears tend to self-lock
  and are harder to print well at small scale.
- [ ] **D. Sync-only spur pair (1:1) + separate reduction element.**
  A 1:1 spur pair couples the two sides for counter-rotation; the
  reduction lives elsewhere (lead-screw, friction wheel, separate
  reduction stage). State what the separate reduction element is.

**Why we chose this architecture (2–3 sentences):**
> _..._

---

## Drive Train Specifications

Fill in the row(s) that match your architecture. For a compound train,
add a row per stage. For a worm + wheel, fill the worm-stage row. For
the sync-only architecture, fill stage 1 with z_driver = z_driven so
the stage ratio is 1.0, and name the separate reduction element below.

### Spur stages

| Stage | Module m (mm) | z_driver | z_driven | Stage ratio (z_driven / z_driver) | Center distance m × (z_driver + z_driven) / 2 (mm) | Face width (mm) |
|-------|---------------|----------|----------|------------------------------------|------------------------------------------------------|-----------------|
| 1 | _..._ | _..._ | _..._ | _..._ | _..._ | _..._ |
| 2 *(if compound)* | _..._ | _..._ | _..._ | _..._ | _..._ | _..._ |

### Worm stage *(if any)*

| Module m_n (mm) | Worm thread starts | Worm wheel z | Stage ratio (z_wheel / starts) | Center distance (mm) | Face width (mm) |
|------------------|--------------------|--------------|---------------------------------|----------------------|------------------|
| _..._ | _..._ | _..._ | _..._ | _..._ | _..._ |

### Separate reduction element *(Architecture D only)*

> _Name it (e.g., M3 lead screw at 0.5 mm pitch driving a follower on
> the input link), and state the reduction it provides._

### Overall

| Parameter | Value |
|-----------|-------|
| Overall reduction N (product of stage reductions) | _..._ |
| Drive-train bounding-box footprint (mm) | _..._ × _..._ × _..._ |
| Packaging position relative to linkage | _..._ *(sketch encouraged below)* |

> Typical FDM PLA values: module 1.0–1.5 mm for spur, ~1.0 for worm.
> z ≥ 12 for FDM spur gears; lower tooth counts have undercut issues
> and print poorly.

---

## Rationale

**Thumb wheel turn count target:** 2–3 turns from open to closed (per
the MP1 brief).

**Linkage input range (from chosen Part A design):** from _..._° to _..._°
→ linkage sweep = _..._°

**Reduction needed to hit the 2.5-turn target on this linkage:**
> N_needed = (thumb-wheel turns × 360°) / (linkage sweep, deg)
> = (2.5 × 360°) / (_..._°)
> = _..._

**Our overall reduction N (from the specs table):** _..._

**Does our N match N_needed?** _Yes / No._

> _If not — what did we accept? A different thumb-wheel turn count? A
> different linkage input range? A different architecture? Be explicit.
> The team is allowed to redefine the brief if the engineering reasoning
> is sound, but the deviation has to be on the page._

---

## Symmetry Arrangement

Both sides of the gripper share the drive train through some
arrangement that achieves counter-rotating symmetry. Common
arrangements:

- **Mating final pair:** the final reduction gear drives one side AND
  meshes with a same-size gear on the other side — counter-rotation by
  meshing.
- **Idler between the sides:** the final gear drives an idler that
  meshes with both side gears; the sides rotate in opposite directions
  naturally.
- **Mirrored worm wheels on a common worm shaft:** one worm drives two
  worm wheels (one per side) sitting on opposite sides of the worm.
- **Other:** describe.

**Our arrangement:**
> _2–3 sentences. Describe how the rotation reaches both sides
> simultaneously and how the two sides end up counter-rotating at the
> same rate._

---

## Coupling Check

The critical sanity check. If the team holds the thumb-wheel turn count
at the 2.5-turn target, the chosen N forces a specific linkage input
sweep — which may differ from the Part A-designed range. Re-check the
transmission angle at the implied range.

**Linkage input sweep implied by our N (at 2.5 thumb-wheel turns):**
> implied sweep = (2.5 × 360°) / N = _..._°

**Implied linkage input range:** from _..._° to _..._°
*(anchored at the start angle your linkage was designed around)*

**Transmission angle across this implied range:** _..._° to _..._°

**In band (40°–140°)?** _Yes / No._

> _If no — what changed? Did you adjust N, accept a different
> thumb-wheel turn count, or change the linkage geometry? Whatever it
> was, document it. If N_needed already matched the Part A range and
> the implied range is the Part A range, say so explicitly — the
> coupling check still counts when it passes._

---

## Packaging Within the Housing Envelope

The MP1 brief calls for a ~92 × 46 × 55 mm total envelope. Where does
the drive train live?

- **Driver location** (relative to thumb-wheel axis): _..._
- **Final-stage gear / worm-wheel location** (relative to linkage input
  pivot O₂): _..._
- **Total drive-train footprint vs. available housing volume:** _..._
- **Clearance to the linkage:** _..._

> _If the drive train doesn't fit, this is a "needs work" flag for the
> trust assessment. Don't paper over it._

---

## Labeled Sketch

Embed a labeled sketch or CAD screenshot showing:

1. The gears (or worm + wheel) with tooth counts and module called out
2. The center distance(s)
3. The synchronization arrangement (idler, mating connection, or
   mirrored wheels) between the two sides
4. Packaging within the MiniClaw housing envelope

`<!-- ![Drive train sketch](sketches/drive_train.png) -->`

> A hand sketch is fine. The point is that someone other than you can
> read it.

---

## Gear Strength (Optional)

Lewis bending stress analysis was practice work back in MP1 and tooth
strength at this scale is unlikely to be the failure mode. If your team
wants to do it anyway as a Part B trust-assessment input, fill this in
for the most loaded stage (usually the highest-torque pinion):

- **Tangential force at pitch radius:** _..._ N
- **Lewis form factor Y for the pinion:** _..._
- **Estimated bending stress:** _..._ MPa
- **Derated PLA limit you're using:** _..._ MPa
- **Verdict:** _PASS / MARGINAL / FAIL_

> Optional. Not graded for absence; graded for sloppy presence.
