import numpy as np
import matplotlib.pyplot as plt

# Constants
theta_max = 6.5 * np.pi   # ≈ 20.4204
c2_norm = 1.0             # Normalized to units of c²

# Create a figure that matches the style of the screenshot
fig, ax = plt.subplots(figsize=(10, 8), facecolor='#1e1e1e')
ax.set_facecolor('#1e1e1e')

# Generate a four-leaf clover / lemniscate-like curve (figure-eight rotated / rhodonea)
# Using a polar rose with 4 petals: r = cos(2φ)
phi = np.linspace(0, 2*np.pi, 1000)
r = np.cos(2 * phi)

# Convert to Cartesian, then scale to the desired ranges
x = r * np.cos(phi) * theta_max
y = r * np.sin(phi) * c2_norm

# Plot the main curve
ax.plot(x, y, color='#4da6ff', linewidth=2.5, zorder=2)

# Mark the four extreme points
points = {
    'A': (-theta_max,  1.0),
    'B': ( theta_max,  1.0),
    'C': (-theta_max, -1.0),
    'D': ( theta_max, -1.0),
}

for label, (px, py) in points.items():
    ax.plot(px, py, 'o', color='#ffcc00', markersize=10, zorder=5)
    # Place labels slightly offset
    offset_x = -1.8 if px < 0 else 0.8
    offset_y = 0.12 if py > 0 else -0.18
    ax.text(px + offset_x, py + offset_y, f'Point {label} ({px/np.pi:.1f}π, {py:.1f})',
            color='white', fontsize=10, ha='left' if px > 0 else 'right')

# Origin
ax.plot(0, 0, 'o', color='white', markersize=6, zorder=5)
ax.text(0.8, 0.08, 'Origin (0,0)', color='white', fontsize=10)

# Axes lines
ax.axhline(0, color='#888888', linestyle='--', linewidth=1, alpha=0.7)
ax.axvline(0, color='#888888', linestyle='--', linewidth=1, alpha=0.7)

# Labels for the four quadrants
ax.text(-theta_max*0.55,  0.55, 'Top-Left Quadrant\n(-θ, +c²)', color='#aaaaaa', fontsize=9, ha='center')
ax.text( theta_max*0.55,  0.55, 'Top-Right Quadrant\n(+θ, +c²)', color='#aaaaaa', fontsize=9, ha='center')
ax.text(-theta_max*0.55, -0.55, 'Bottom-Left Quadrant\n(-θ, -c²)', color='#aaaaaa', fontsize=9, ha='center')
ax.text( theta_max*0.55, -0.55, 'Bottom-Right Quadrant\n(+θ, -c²)', color='#aaaaaa', fontsize=9, ha='center')

# Axis labels and ticks
ax.set_xlabel('Angular Phase (θ)', color='white', fontsize=12)
ax.set_ylabel('Normalized Real Coordinate (Units of c²)', color='white', fontsize=12)

# Custom ticks
xticks = [-theta_max, 0, theta_max]
ax.set_xticks(xticks)
ax.set_xticklabels([f'-6.5π\n(-20.42)', '0', f'6.5π\n(20.42)'], color='white')
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels(['-1.0', '0.0', '1.0'], color='white')

ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('#555555')

ax.set_xlim(-theta_max*1.25, theta_max*1.25)
ax.set_ylim(-1.25, 1.25)
ax.set_aspect('auto')

ax.set_title('The Symmetric Real-Angular Phase Space\nθ = 6.5π ≈ 20.4204    |    c² normalized to 1.0',
             color='white', fontsize=14, pad=15)

plt.tight_layout()
plt.savefig('/tmp/symmetric_phase_space.png', dpi=160, bbox_inches='tight',
            facecolor='#1e1e1e', edgecolor='none')
plt.close()

print("Plot saved to /tmp/symmetric_phase_space.png")
print(f"θ_max = {theta_max:.4f} rad")
