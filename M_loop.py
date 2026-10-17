import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
theta = 6.5 * np.pi
c2 = 8.98755179e16
Y_max = 1.0

# Create output directory if needed
os.makedirs('/home/workdir', exist_ok=True)

# ============================================================
# Chart 1: Real-Angular Plane Domain with Mode
# ============================================================
fig1, ax1 = plt.subplots(figsize=(10, 10))

# Domain boundaries
ax1.axvline(0, color='black', lw=1.2)
ax1.axhline(0, color='black', lw=1.2)
ax1.axvline(-theta, color='gray', ls='--', lw=1, alpha=0.7)
ax1.axvline(theta, color='gray', ls='--', lw=1, alpha=0.7)
ax1.axhline(-c2, color='gray', ls='--', lw=1, alpha=0.7)
ax1.axhline(c2, color='gray', ls='--', lw=1, alpha=0.7)

# Fill quadrants
ax1.fill_between([-theta, 0], 0, c2, color='blue', alpha=0.08)
ax1.fill_between([0, theta], 0, c2, color='green', alpha=0.08)
ax1.fill_between([-theta, 0], -c2, 0, color='red', alpha=0.08)
ax1.fill_between([0, theta], -c2, 0, color='orange', alpha=0.08)

# Fill quadrants
ax1.fill_between([-theta, 0], 0, c2, color='blue', alpha=0.08)
ax1.fill_between([0, theta], 0, c2, color='green', alpha=0.08)
ax1.fill_between([-theta, 0], -c2, 0, color='red', alpha=0.08)
ax1.fill_between([0, theta], -c2, 0, color='orange', alpha=0.08)

# Labels
ax1.text(0, 0, '  origin (0,0)', fontsize=11, fontweight='bold', va='bottom')
ax1.text(-theta*0.98, -c2*0.98, r'$(-\theta,-c^2)$', fontsize=10, va='top', ha='left', color='darkred')
ax1.text(theta*0.98, -c2*0.98, r'$(\theta,-c^2)$', fontsize=10, va='top', ha='right', color='darkorange')
ax1.text(-theta*0.98, c2*0.98, r'$(-\theta,c^2)$', fontsize=10, va='bottom', ha='left', color='darkblue')
ax1.text(theta*0.98, c2*0.98, r'$(\theta,c^2)$', fontsize=10, va='bottom', ha='right', color='darkgreen')

# Draw a representative 4-lobed involuting mode (rhodonea)
t = np.linspace(0, 2*np.pi, 2000)
r = 0.28 * theta * np.abs(np.cos(2*t))
x = r * np.cos(t)
y = r * np.sin(t) * (c2 / theta) * 0.55
ax1.plot(x, y, color='navy', lw=2.5, label=r'$M_{\operatorname{loop}\{\infty\mid\infty\}}$')

# Real advance arrow
ax1.annotate('', xy=(0.12*theta, 0.85*c2), xytext=(0.12*theta, 0.08*c2),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2.5))
ax1.text(0.16*theta, 0.45*c2, r'Real advance $\to c^2$', fontsize=11, color='purple', rotation=90, va='center')

ax1.set_xlim(-1.15*theta, 1.15*theta)
ax1.set_ylim(-1.15*c2, 1.15*c2)
ax1.set_xlabel(r'Angular coordinate $\theta$', fontsize=12)
ax1.set_ylabel(r'Real coordinate (units of $c^2$)', fontsize=12)
ax1.set_title('Real–Angular Plane Domain\nwith Involuting Mode $M_{\\operatorname{loop}\\{\\infty\\mid\\infty\\}}$', fontsize=14, pad=12)
ax1.set_xticks([-theta, 0, theta])
ax1.set_xticklabels([r'$-\theta$', '0', r'$\theta$'])
ax1.set_yticks([-c2, 0, c2])
ax1.set_yticklabels([r'$-c^2$', '0', r'$c^2$'])
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=11)
plt.tight_layout()
fig1.savefig('/home/workdir/chart1_real_angular_plane.png', dpi=160, bbox_inches='tight')
plt.close(fig1)
print("Chart 1 saved")

# ============================================================
# Chart 2: 5-Stage Real Coordinate Progression
# ============================================================
fig2, axes = plt.subplots(1, 2, figsize=(13, 5.5))

steps = [0, 1, 2, 3, 4, 5]
Y = [0.00, 0.25, 0.50, 0.50, 0.75, 1.00]
delta_Y = [0.00, 0.25, 0.25, 0.00, 0.25, 0.25]
labels = [
    "Initial\nclosed curve",
    "Gravitational\nforce",
    "Expansion",
    "Involuting\nmode",
    "Return to\ncurve",
    "Terminal\nmode"
]

# Left: Cumulative Y
ax = axes[0]
ax.plot(steps, Y, 'o-', color='navy', lw=2.5, markersize=10)
ax.fill_between(steps, Y, alpha=0.15, color='navy')
for i, (x, y) in enumerate(zip(steps, Y)):
    ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 12), ha='center', fontsize=10)
ax.set_xticks(steps)
ax.set_xticklabels([f'n={s}' for s in steps])
ax.set_ylabel('Normalized Real Coordinate $Y$', fontsize=11)
ax.set_title('Protected Recursion: Cumulative $Y$', fontsize=13)
ax.set_ylim(-0.05, 1.15)
ax.grid(True, alpha=0.3)
ax.axhline(1.0, color='green', ls='--', alpha=0.6, label='Terminal $Y=1$')
ax.legend(loc='lower right')

# Right: Stage labels
ax = axes[1]
ax.plot(steps, Y, 'o-', color='darkred', lw=2.5, markersize=10)
for i, (x, y) in enumerate(zip(steps, Y)):
    ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0, 12), ha='center', fontsize=10)
ax.set_xticks(steps)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel('Normalized Real Coordinate $Y$', fontsize=11)
ax.set_title('Five Stages of the Recursion', fontsize=13)
ax.set_ylim(-0.05, 1.15)
ax.grid(True, alpha=0.3)

plt.suptitle('Real Coordinate Progression — Protected 5-Stage Recursion', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig2.savefig('/home/workdir/chart2_stage_progression.png', dpi=160, bbox_inches='tight')
plt.close(fig2)
print("Chart 2 saved")

# ============================================================
# Chart 3: Terminal Mode at Y=+1
# ============================================================
fig3, ax3 = plt.subplots(figsize=(8, 8))

t = np.linspace(0, 2*np.pi, 2000)
r = np.abs(np.cos(2*t))
x = r * np.cos(t) + 1.0   # shifted to terminal real coordinate
y = r * np.sin(t)

ax3.plot(x, y, color='navy', lw=2.8, label=r'Terminal $M_{\operatorname{loop}\{\infty\mid\infty\}}$')
ax3.axvline(0, color='gray', ls='--', alpha=0.6, label='Original real = 0')
ax3.axvline(1.0, color='green', ls='--', lw=2, alpha=0.8, label='Terminal real = +1.00')
ax3.scatter([1.0], [0], color='red', s=80, zorder=5, label='Seated at $Y=+1$')

ax3.set_aspect('equal')
ax3.set_title(r'Terminal Mode $M_{\operatorname{loop}\{\infty\mid\infty\}}$' + '\nseated at new real coordinate $Y=+1.00$', fontsize=13)
ax3.legend(fontsize=10, loc='upper right')
ax3.axis('off')
ax3.set_xlim(-1.5, 2.8)
ax3.set_ylim(-1.5, 1.5)

plt.tight_layout()
fig3.savefig('/home/workdir/chart3_terminal_mode.png', dpi=160, bbox_inches='tight')
plt.close(fig3)
print("Chart 3 saved")

# ============================================================
# Chart 4: Four Quadrant Paths (schematic)
# ============================================================
fig4, ax4 = plt.subplots(figsize=(9, 9))

# Simplified schematic using normalized coordinates for clarity
# Use Y and theta_norm
theta_n = 1.0
# Draw domain
ax4.axvline(0, color='black', lw=1)
ax4.axhline(0, color='black', lw=1)
ax4.axvline(-theta_n, color='gray', ls='--', alpha=0.5)
ax4.axvline(theta_n, color='gray', ls='--', alpha=0.5)
ax4.axhline(-1, color='gray', ls='--', alpha=0.5)
ax4.axhline(1, color='gray', ls='--', alpha=0.5)

# Approximate the four paths (schematic, not exact reciprocal scale)
def plot_path(xs, ys, color, label):
    ax4.plot(xs, ys, 'o-', color=color, lw=2, markersize=6, label=label)

# Bottom-Left
plot_path([0, -theta_n, -0.15, -0.15, 0], [0, -1, -1, -0.05, 0], 'crimson', 'Bottom-Left')
# Bottom-Right
plot_path([0, theta_n, 0.15, 0.15, 0], [0, -1, -1, -0.05, 0], 'darkorange', 'Bottom-Right')
# Top-Left
plot_path([0, -theta_n, -0.15, -0.15, 0], [0, 1, 1, 0.05, 0], 'royalblue', 'Top-Left')
# Top-Right
plot_path([0, theta_n, 0.15, 0.15, 0], [0, 1, 1, 0.05, 0], 'forestgreen', 'Top-Right')

ax4.set_xlim(-1.4, 1.4)
ax4.set_ylim(-1.4, 1.4)
ax4.set_xlabel(r'Normalized Angular $\theta$', fontsize=11)
ax4.set_ylabel(r'Normalized Real $Y$', fontsize=11)
ax4.set_title(r'Four Quadrant Paths of $M_{\operatorname{loop}\{\infty\mid\infty\}}$' + '\n(schematic)', fontsize=13)
ax4.legend(loc='upper right', fontsize=9)
ax4.grid(True, alpha=0.3)
ax4.set_aspect('equal')

plt.tight_layout()
fig4.savefig('/home/workdir/chart4_quadrant_paths.png', dpi=160, bbox_inches='tight')
plt.close(fig4)
print("Chart 4 saved")

print("\nAll charts generated successfully.")
