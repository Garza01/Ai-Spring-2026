"""Generate Part B plots and sketches for MP4 Part B."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

BASE = Path(__file__).parent
PLOTS_DIR   = BASE / "plots"
SKETCHES_DIR = BASE / "sketches"
PLOTS_DIR.mkdir(exist_ok=True)
SKETCHES_DIR.mkdir(exist_ok=True)

# ─── Team linkage designs ─────────────────────────────────────────────────────
# All parallelogram four-bars with vertical ground link (O4 directly above O2)
# µ(θ) = arccos(sin θ) = 90° - θ for vertical parallelogram
# displacement(θ) = sqrt((L2 - L2·cosθ)² + (L2·sinθ)²) = 2·L2·sin(θ/2) ... no wait
# displacement_from_ref = sqrt((L2·cosθ_ref - L2·cosθ)² + (L2·sinθ_ref - L2·sinθ + 0)²)
# For ref=THETA_MIN:
# disp = 2·L2·sin((θ - θ_min)/2) ... actually:
# disp = L2 * sqrt((cosθ - cosθ_min)² + (sinθ - sinθ_min)²)
#       = L2 * sqrt(2 - 2·cos(θ - θ_min))
#       = 2·L2·sin((θ - θ_min)/2)
# (since tip moves same direction as joint A for parallelogram, TIP_EXT cancels)

CANDIDATES = {
    "Alberto Garza": {
        "L1": 14.0, "L2": 26.0, "L3": 14.0, "L4": 26.0,
        "O4": (0.0, 14.0), "TIP_EXT": 30.0,
        "theta_min": 0.0, "theta_max": 45.0,
        "color": "#2277cc",
    },
    "Maya Chen": {
        "L1": 12.0, "L2": 25.0, "L3": 12.0, "L4": 25.0,
        "O4": (0.0, 12.0), "TIP_EXT": 35.0,
        "theta_min": 0.0, "theta_max": 50.0,
        "color": "#ee6622",
    },
    "Jordan Park": {
        "L1": 16.0, "L2": 22.0, "L3": 16.0, "L4": 22.0,
        "O4": (0.0, 16.0), "TIP_EXT": 28.0,
        "theta_min": 0.0, "theta_max": 50.0,
        "color": "#22aa44",
    },
}


def compute_position(theta_deg, L2, theta_min_deg):
    """Euclidean displacement from tip at theta_min."""
    t    = np.radians(theta_deg)
    tmin = np.radians(theta_min_deg)
    return 2.0 * L2 * np.abs(np.sin((t - tmin) / 2.0))


def compute_mu(theta_deg):
    """Transmission angle for vertical parallelogram: µ = 90° - θ."""
    return 90.0 - theta_deg


TARGET_TOTAL_JAW = 40.0
TARGET_SINGLE = TARGET_TOTAL_JAW / 2   # 20 mm

# ── Plot 1: Displacement vs. input angle (all candidates) ─────────────────────
fig1, ax1 = plt.subplots(figsize=(9, 4.5))

for name, cfg in CANDIDATES.items():
    thetas = np.linspace(cfg["theta_min"], cfg["theta_max"], 200)
    disps  = [compute_position(t, cfg["L2"], cfg["theta_min"]) for t in thetas]
    ax1.plot(thetas, disps, color=cfg["color"], lw=2.2,
             label=f"{name}  (L2={cfg['L2']:.0f}, Δθ={cfg['theta_max']-cfg['theta_min']:.0f}°)")

ax1.axhline(TARGET_SINGLE, ls="--", color="#cc4444", lw=1.8,
            label=f"target single-side displacement = {TARGET_SINGLE:.0f} mm")
ax1.set_xlabel("input angle θ_in (deg)")
ax1.set_ylabel("single-side displacement from reference (mm)")
ax1.set_title("Displacement vs. Input Angle — All Candidate Linkages")
ax1.legend(fontsize=9, loc="upper left")
ax1.grid(alpha=0.3)
ax1.set_xlim(0, 55)
ax1.set_ylim(-0.5, 26)

# secondary y-axis: total jaw opening = 2× displacement
ax1b = ax1.twinx()
ax1b.set_ylim(-1, 52)
ax1b.set_ylabel("implied total jaw opening (mm)  [= 2 × disp.]")

fig1.tight_layout()
fig1.savefig(str(PLOTS_DIR / "displacement_comparison.png"), dpi=130, bbox_inches="tight")
plt.close(fig1)
print(f"Saved: {PLOTS_DIR/'displacement_comparison.png'}")

# ── Plot 2: Transmission angle vs. input angle (all candidates) ───────────────
fig2, ax2 = plt.subplots(figsize=(9, 4.5))

WORKABLE_BAND = (40.0, 140.0)
ax2.axhspan(*WORKABLE_BAND, color="green", alpha=0.08, label="workable band 40°–140°")
ax2.axhline(40.0, color="green", ls="--", lw=1.2)
ax2.axhline(140.0, color="green", ls="--", lw=1.2)

for name, cfg in CANDIDATES.items():
    thetas = np.linspace(cfg["theta_min"], cfg["theta_max"], 200)
    mus    = [compute_mu(t) for t in thetas]
    ax2.plot(thetas, mus, color=cfg["color"], lw=2.2,
             label=f"{name}  µ: {compute_mu(cfg['theta_min']):.0f}°→{compute_mu(cfg['theta_max']):.0f}°")

ax2.set_xlabel("input angle θ_in (deg)")
ax2.set_ylabel("transmission angle µ (deg)")
ax2.set_title("Transmission Angle vs. Input Angle — All Candidate Linkages")
ax2.legend(fontsize=9, loc="upper right")
ax2.set_ylim(30, 105)
ax2.set_xlim(0, 55)
ax2.grid(alpha=0.3)
fig2.tight_layout()
fig2.savefig(str(PLOTS_DIR / "mu_comparison.png"), dpi=130, bbox_inches="tight")
plt.close(fig2)
print(f"Saved: {PLOTS_DIR/'mu_comparison.png'}")

# ── Drive Train Sketch ─────────────────────────────────────────────────────────
# Worm + worm wheel arrangement (Architecture C)
# Worm shaft horizontal (left-right), two worm wheels above and below.
fig3, ax3 = plt.subplots(figsize=(9, 7))
ax3.set_aspect("equal")
ax3.set_facecolor("#f0f0f0")
fig3.patch.set_facecolor("#ffffff")

# Housing outline
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
housing = FancyBboxPatch((-47, -24), 94, 48,
                          boxstyle="round,pad=2", linewidth=2,
                          edgecolor="#666666", facecolor="#e8e8e8")
ax3.add_patch(housing)
ax3.text(0, 25, "MiniClaw Housing (92 × 46 × 55 mm)", ha="center", va="center",
         fontsize=9, color="#555")

# Worm shaft (horizontal, through center)
ax3.plot([-46, 46], [0, 0], color="#555555", lw=4, solid_capstyle="round", zorder=3)
ax3.text(-42, 1.5, "Worm shaft (2-start, m=1.0 mm)", fontsize=8, color="#333")

# Thumb wheel (left end of shaft)
thumb = Circle((-44, 0), 6, linewidth=2, edgecolor="#333", facecolor="#aaaaff", zorder=5)
ax3.add_patch(thumb)
ax3.text(-44, -8, "Thumb\nwheel", ha="center", fontsize=8, color="#333")

# Worm section (middle of shaft)
worm_rect = FancyBboxPatch((-8, -4), 16, 8,
                             boxstyle="round,pad=1", linewidth=1.5,
                             edgecolor="#444", facecolor="#cccccc", zorder=4)
ax3.add_patch(worm_rect)
ax3.text(0, 0, "Worm\n(2 starts)", ha="center", va="center", fontsize=8, color="#222")
ax3.text(0, -6, "d_w=10mm", ha="center", fontsize=7.5, color="#444")

# Left worm wheel (upper side = left jaw)
ww_l = Circle((-25, 20), 20, linewidth=2, edgecolor="#2277cc", facecolor="#aaddff",
               alpha=0.8, zorder=4)
ax3.add_patch(ww_l)
ax3.text(-25, 20, "Worm Wheel\nLeft side\nz=40, m=1.0", ha="center", va="center",
         fontsize=8, color="#1144aa")
ax3.text(-25, 38, "d=40 mm", ha="center", fontsize=7.5, color="#2277cc")

# Right worm wheel (lower side = right jaw) — counter-rotates
ww_r = Circle((25, -20), 20, linewidth=2, edgecolor="#ee6622", facecolor="#ffddaa",
               alpha=0.8, zorder=4)
ax3.add_patch(ww_r)
ax3.text(25, -20, "Worm Wheel\nRight side\nz=40, m=1.0", ha="center", va="center",
         fontsize=8, color="#cc4400")
ax3.text(25, -38, "d=40 mm", ha="center", fontsize=7.5, color="#ee6622")

# Center distance arrows
ax3.annotate("", xy=(-25, 0), xytext=(-25, 20),
             arrowprops=dict(arrowstyle="<->", color="#2277cc", lw=1.2))
ax3.text(-21, 10, "C=25mm", fontsize=8, color="#2277cc")
ax3.annotate("", xy=(25, 0), xytext=(25, -20),
             arrowprops=dict(arrowstyle="<->", color="#ee6622", lw=1.2))
ax3.text(27, -10, "C=25mm", fontsize=7.5, color="#ee6622")

# O2 pivots (left and right linkage input cranks)
o2l = Circle((-25, 20), 2.5, linewidth=1.5, edgecolor="#000", facecolor="#2277cc", zorder=6)
o2r = Circle((25, -20), 2.5, linewidth=1.5, edgecolor="#000", facecolor="#ee6622", zorder=6)
ax3.add_patch(o2l)
ax3.add_patch(o2r)
ax3.text(-25, 42.5, "O₂_L (left input pivot)", ha="center", fontsize=8, color="#1144aa")
ax3.text(25, -42.5, "O₂_R (right input pivot)", ha="center", fontsize=8, color="#cc4400")

# Rotation direction arrows
arrow_kwargs = dict(arrowstyle="->,head_width=0.3,head_length=0.4",
                    color="#555", lw=1.5, connectionstyle="arc3,rad=0.5")
ax3.annotate("", xy=(-25+14, 20+14), xytext=(-25-14, 20+14),
             arrowprops=dict(arrowstyle="->,head_width=0.3", color="#2277cc", lw=2.0,
                             connectionstyle="arc3,rad=0.4"))
ax3.text(-25, 34, "CCW →", ha="center", fontsize=8, color="#2277cc")
ax3.annotate("", xy=(25-14, -20-14), xytext=(25+14, -20-14),
             arrowprops=dict(arrowstyle="->,head_width=0.3", color="#ee6622", lw=2.0,
                             connectionstyle="arc3,rad=0.4"))
ax3.text(25, -34, "← CW", ha="center", fontsize=8, color="#ee6622")

# Gear parameters box
param_text = ("Drive Train Parameters\n"
              "Architecture: C (Worm + Worm Wheel)\n"
              "Worm: 2 starts, m_n = 1.0 mm, d_w = 10 mm\n"
              "Worm wheel: z = 40, m_n = 1.0 mm, d = 40 mm\n"
              "Stage ratio N = z / starts = 40/2 = 20\n"
              "Center distance C = 25 mm\n"
              "Face width = 8 mm\n"
              "Overall N = 20 (2.5 thumb-wheel turns → 45° sweep)")
ax3.text(33, 22, param_text, fontsize=7.5, va="top", ha="left",
         bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="#aaa", alpha=0.9))

ax3.set_xlim(-55, 65)
ax3.set_ylim(-50, 50)
ax3.set_title("MiniClaw Drive Train Sketch — Architecture C (Worm + Worm Wheel)\n"
              "Mirrored worm wheels on common worm shaft for counter-rotation",
              fontsize=10)
ax3.axis("off")
fig3.tight_layout()
fig3.savefig(str(SKETCHES_DIR / "drive_train.png"), dpi=130, bbox_inches="tight")
plt.close(fig3)
print(f"Saved: {SKETCHES_DIR/'drive_train.png'}")

print("All Part B artifacts generated.")
