#!/usr/bin/env python3
"""
multi_stage_trace_curve.py
--------------
JCR Involuting Modes / Half-Winding Integer Matrix System
Traces the protected five-stage recursion on the Real–Angular Plane.

Y = y / c²  ∈ [-1, +1]
θ ∈ [-6.5π, +6.5π]
Net advance: Y₅ − Y₀ = 1.00  (y₅ − y₀ = c²)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# ------------------------------------------------------------------
# Physical & geometric constants
# ------------------------------------------------------------------
c = 299792458.0
c2 = c**2                          # 8.987551787368176e+16 m²/s²
theta_max = 6.5 * np.pi            # full angular domain span = 13π
epsilon = 0.25                     # discrete ratchet

# ------------------------------------------------------------------
# Stage data (matches 5_stage_matrix.py)
# ------------------------------------------------------------------
stages = {
    0: {"Y": 0.00, "label": "Stage 0 – Initial closed curve",   "color": "#555555"},
    1: {"Y": 0.25, "label": "Stage 1 – Gravitational force",    "color": "#1f77b4"},
    2: {"Y": 0.50, "label": "Stage 2 – Expansion",              "color": "#2ca02c"},
    3: {"Y": 0.50, "label": "Stage 3 – Involuting fold (½-winding)", "color": "#d62728"},
    4: {"Y": 0.75, "label": "Stage 4 – Multi-lobed return",     "color": "#9467bd"},
    5: {"Y": 1.00, "label": "Stage 5 – Terminal loop{∞|∞}",     "color": "#ff7f0e"},
}

# ------------------------------------------------------------------
# Curve generators
# ------------------------------------------------------------------
def simple_closed(Y, n_points=400):
    """Stage 0 / 1 style simple oval."""
    t = np.linspace(0, 2*np.pi, n_points)
    r = 0.18 + 0.04*np.cos(2*t)
    x = r * np.cos(t)
    y = Y + r * np.sin(t) * 0.6
    return x, y

def expanded(Y, n_points=400):
    """Stage 2 expanded curve."""
    t = np.linspace(0, 2*np.pi, n_points)
    r = 0.28 + 0.08*np.cos(2*t)
    x = r * np.cos(t)
    y = Y + r * np.sin(t) * 0.55
    return x, y

def involuting_fold(Y=0.50, n_points=600):
    """Stage 3 – pure circulatory half-winding (lemniscate-like)."""
    t = np.linspace(0, 2*np.pi, n_points)
    # Lemniscate of Bernoulli scaled & oriented for half-winding
    a = 0.32
    x = a * np.sqrt(2) * np.cos(t) / (np.sin(t)**2 + 1)
    y = a * np.sqrt(2) * np.cos(t) * np.sin(t) / (np.sin(t)**2 + 1)
    return x, Y + y

def multi_lobed(Y, n_points=500):
    """Stage 4 multi-lobed return."""
    t = np.linspace(0, 2*np.pi, n_points)
    r = 0.22 + 0.12*np.cos(3*t)
    x = r * np.cos(t)
    y = Y + r * np.sin(t) * 0.5
    return x, y

def terminal_four_lobed(Y=1.00, n_points=800):
    """Stage 5 – four-lobed rhodonea / hierarchical mode i=(0,1)."""
    t = np.linspace(0, 2*np.pi, n_points)
    r = 0.35 * np.cos(2*t)          # rhodonea (rose curve) with 4 petals
    x = r * np.cos(t)
    y = Y + r * np.sin(t) * 0.45
    return x, y

# ------------------------------------------------------------------
# Main plot
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 14))

# Background Real–Angular Plane hints
ax.axhline(0, color='black', lw=0.8, alpha=0.6)
ax.axhline(1, color='green', lw=1.2, ls='--', alpha=0.7, label='Upper boundary Y = +1')
ax.axvline(0, color='black', lw=0.8, alpha=0.6)

# Draw each stage
generators = {
    0: simple_closed,
    1: simple_closed,
    2: expanded,
    3: involuting_fold,
    4: multi_lobed,
    5: terminal_four_lobed,
}

for s in range(6):
    Y = stages[s]["Y"]
    gen = generators[s]
    x, y = gen(Y)
    ax.plot(x, y, color=stages[s]["color"], lw=2.4, label=stages[s]["label"], zorder=5-s*0.1)
    # small marker at the “center” of each stage
    ax.plot(0, Y, 'o', color=stages[s]["color"], markersize=7, zorder=10)

# Vertical progression arrow
ax.annotate('', xy=(1.05, 1.0), xytext=(1.05, 0.0),
            arrowprops=dict(arrowstyle='->', color='navy', lw=2.0))
ax.text(1.12, 0.5, 'Net advance\nΔY = 1.00\n(y = c²)', fontsize=11,
        rotation=90, va='center', ha='left', color='navy')

# Stage labels on the right
for s in range(6):
    ax.text(-1.15, stages[s]["Y"], f'Y = {stages[s]["Y"]:.2f}',
            fontsize=9, ha='right', va='center', color=stages[s]["color"])

ax.set_xlim(-1.4, 1.5)
ax.set_ylim(-0.35, 1.45)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.4)
ax.set_xlabel(r'Angular coordinate $\theta$ (schematic)', fontsize=12)
ax.set_ylabel(r'Real coordinate $Y = y / c^2$', fontsize=12)
ax.set_title(
    'JCR Protected Five-Stage Recursion\n'
    r'Trace of the involuting mode on the Real–Angular Plane' + '\n'
    r'$c^2 = 8.987551787368176 \times 10^{16}\,\mathrm{m}^2/\mathrm{s}^2$'
    r'  $\rightarrow$  net advance $Y_5-Y_0 = 1$',
    fontsize=13, pad=12
)

ax.legend(loc='upper left', fontsize=9, framealpha=0.92)
plt.tight_layout()
plt.savefig('jcr_trace_curve_five_stage.png', dpi=180, bbox_inches='tight')
print("Saved: jcr_trace_curve_five_stage.png")
print(f"c² = {c2:.10e} m²/s²")
print("Telescopic sum ΔY = 0.25+0.25+0.00+0.25+0.25 = 1.00  ✓")
