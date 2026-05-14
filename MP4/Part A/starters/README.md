# MP4 Part A — Four-Bar Linkage Starters

Two starters for the four-bar linkage you'll design and analyze in
`MP4_PartA_Build_to_Verify.ipynb`. Use whichever fits your workflow.

| File | When to use |
|------|-------------|
| `four_bar_rapier_starter.html` | You want a fast browser visualization with sliders to feel the geometry. |
| `four_bar_matplotlib_animation_starter.ipynb` | You'd rather stay in Python and reuse the kinematics in your notebook. |

Both starters animate **one side** of the MiniClaw four-bar with an optional
mirrored other side. They use the same analytical kinematics (vector loop
closure via two-circle intersection) so the numbers agree.

## How to run

**HTML starter:** double-click `four_bar_rapier_starter.html` (or right-click
→ Open With → your browser). No install, no local server. The page lets you
edit link lengths, the output ground pivot, the input range, and a tip
extension; you can sweep the input automatically and toggle the mirrored
other side.

**matplotlib starter:** open
`four_bar_matplotlib_animation_starter.ipynb` in your Codespace or local
Jupyter. Edit the constants in the second cell, run all cells, and the
animation appears inline. The last cell shows how to save the animation
as MP4 or GIF for your Section 5 evidence.

## Other tools you can use

The notebook accepts any tool that produces a visible-motion artifact for
your linkage. Common alternatives:

- **Linkage Mechanism Designer** (free Windows desktop tool, popular for
  this kind of work) — design four-bars graphically and export a screen
  recording. Search "Linkage David Rector" or "linkage mechanism designer."
- **GeoGebra** — set up the linkage as constrained geometry, animate the
  input angle, export an animation.
- **CAD motion analysis** — Fusion 360, SolidWorks, and Onshape all have
  motion studies that can drive a four-bar through its range and export a
  video.
- **Python + matplotlib** — what `four_bar_matplotlib_animation_starter`
  uses; you can adapt it to any geometry.
- **three.js or other JS** — if you want a 3D rendering.

Whatever you use, save the visible-motion artifact (video, animated plot,
or sequence of stills) under `MP4/Part A/motion/` and reference it from
Section 5 of the notebook.

## Note on the "Rapier.js" filename

The HTML starter is named `four_bar_rapier_starter.html` to match the spec,
but the implementation uses pure-JS analytical kinematics rather than the
Rapier.js physics engine. The reason: the spec note acknowledges this is a
**kinematic visualization, not a dynamic simulation** — analytical kinematics
is honest about that, has zero dependencies, and works reliably by
double-click without a local web server. If you'd prefer Rapier.js or
another physics library for your evidence, that's accepted.

## Help

- The starters' kinematics is the same math your `compute_finger_position()`
  function (notebook Section 3) needs. Reading either starter is a fine
  way to bootstrap your implementation.
- If a starter takes more than 5 minutes to figure out, that's a bug —
  message the instructor.
