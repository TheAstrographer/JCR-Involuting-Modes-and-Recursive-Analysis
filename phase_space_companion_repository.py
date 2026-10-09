import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Chart 2: Real–Angular Phase Space with Cosmological Annotations
# ============================================================
theta_max = 6.5 * np.pi   # ≈ 20.4204
c2_norm = 1.0

fig, ax = plt.subplots(figsize=(11, 9), facecolor='#1a1a2e')
ax.set_facecolor('#1a1a2e')

# Four-lobed involuting mode (rhodonea / polar rose)
phi = np.linspace(0, 2*np.pi, 1200)
r = np.cos(2 * phi)
x = r * np.cos(phi) * theta_max
y = r * np.sin(phi) * c2_norm

ax.plot(x, y, color='#4da6ff', linewidth=2.8, zorder=3, label=r'$\operatorname{loop}\{\infty\mid\infty\}$')

# Domain corners
corners = {
    'A (-θ,+1)': (-theta_max,  1.0),
    'B (+θ,+1)': ( theta_max,  1.0),
    'C (-θ,-1)': (-theta_max, -1.0),
    'D (+θ,-1)': ( theta_max, -1.0),
}
for label, (px, py) in corners.items():
    ax.plot(px, py, 'o', color='#ffcc00', markersize=11, zorder=5)
    offset_x = -2.2 if px < 0 else 1.0
    offset_y = 0.13 if py > 0 else -0.18
    ax.text(px + offset_x, py + offset_y, label, color='white', fontsize=9,
            ha='left' if px > 0 else 'right')

# Origin
ax.plot(0, 0, 'o', color='white', markersize=7, zorder=5)
ax.text(1.2, 0.08, 'Origin (0,0)\nStage 0', color='white', fontsize=9)

# Involuting plateau annotation
ax.axhline(0.50, color='#ff8c00', ls='--', lw=1.5, alpha=0.8, zorder=2)
ax.text(-theta_max*0.95, 0.55, 'Stage 3: Involuting Fold\n(ΔY=0, monodromy −1, Arf=1)\n→ DES Y6 + KiDS-Legacy growth',
        color='#ff8c00', fontsize=8.5, ha='left', va='bottom')

# Terminal horizon
ax.axhline(1.0, color='#00cc66', ls='--', lw=1.5, alpha=0.8, zorder=2)
ax.text(theta_max*0.15, 1.08, 'Y=1 ↔ c² horizon  →  Dual-Gate torque +3.17 km s⁻¹ Mpc⁻¹\n(H₀_local ≈ 73.17)',
        color='#00cc66', fontsize=9, ha='left')

# Axes
ax.axhline(0, color='#666666', linestyle='--', linewidth=1, alpha=0.6)
ax.axvline(0, color='#666666', linestyle='--', linewidth=1, alpha=0.6)

# Quadrant labels
ax.text(-theta_max*0.55,  0.72, 'Top-Left\n(−θ, +c²)', color='#aaaaaa', fontsize=8, ha='center')
ax.text( theta_max*0.55,  0.72, 'Top-Right\n(+θ, +c²)', color='#aaaaaa', fontsize=8, ha='center')
ax.text(-theta_max*0.55, -0.72, 'Bottom-Left\n(−θ, −c²)', color='#aaaaaa', fontsize=8, ha='center')
ax.text( theta_max*0.55, -0.72, 'Bottom-Right\n(+θ, −c²)', color='#aaaaaa', fontsize=8, ha='center')

ax.set_xlabel('Angular Phase θ  [rad]   (domain sized for 720° positive holonomy)', color='white', fontsize=11)
ax.set_ylabel('Normalized Real Coordinate Y = y / c²', color='white', fontsize=11)

xticks = [-theta_max, 0, theta_max]
ax.set_xticks(xticks)
ax.set_xticklabels([f'−6.5π\n(−20.42)', '0', f'+6.5π\n(+20.42)'], color='white')
ax.set_yticks([-1, 0, 0.5, 1])
ax.set_yticklabels(['−1.0', '0.0', '0.5 (fold)', '+1.0'], color='white')

ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('#444444')

ax.set_xlim(-theta_max*1.28, theta_max*1.28)
ax.set_ylim(-1.28, 1.35)

ax.set_title('Real–Angular Phase Space of the Involuting Mode\n'
             'θ ∈ [−6.5π, +6.5π]  |  Y ∈ [−1, +1]  |  Net advance Y₅−Y₀ = 1 ↔ Dual-Gate torque',
             color='white', fontsize=12, pad=12)

ax.legend(loc='lower right', fontsize=9, facecolor='#2a2a3e', edgecolor='white', labelcolor='white')

plt.tight_layout()
plt.savefig('/home/workdir/phase_space_cosmo.png', dpi=160, bbox_inches='tight',
            facecolor='#1a1a2e', edgecolor='none')
print("Chart 2 saved: phase_space_cosmo.png")
plt.close()
