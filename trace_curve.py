import matplotlib.pyplot as plt
import numpy as np

# Geometric example values for shape (normalized visual scale)
theta = 2.0
c2_vis = 2.25
inv_theta = 1.0 / theta
inv_c2_vis = 1.0 / c2_vis

# Actual physical values
c = 299792458
c2_real = c**2
inv_c2_real = 1.0 / c2_real

fig, ax = plt.subplots(figsize=(11, 11))

ax.plot(0, 0, 'ko', markersize=9, zorder=5, label='Origin (0,0)')

paths = {
    'Bottom Left': [(0, 0), (-theta, -c2_vis), (-inv_theta, -c2_vis), (-inv_theta, -inv_c2_vis), (0, 0)],
    'Bottom Right': [(0, 0), (theta, -c2_vis), (inv_theta, -c2_vis), (inv_theta, -inv_c2_vis), (0, 0)],
    'Top Left': [(0, 0), (-theta, c2_vis), (-inv_theta, c2_vis), (-inv_theta, inv_c2_vis), (0, 0)],
    'Top Right': [(0, 0), (theta, c2_vis), (inv_theta, c2_vis), (inv_theta, inv_c2_vis), (0, 0)]
}

colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
for (name, pts), color in zip(paths.items(), colors):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, linewidth=2.3, marker='o', markersize=7, label=name)
    ax.fill(xs, ys, color=color, alpha=0.12)

# Annotations with real numerical values
annots = [
    ((-theta, c2_vis), '(-θ, +c²)\nc² = 8.987552e+16 m²/s²', (-50, 10)),
    ((-inv_theta, c2_vis), '(-1/θ, +c²)', (-55, 10)),
    ((-inv_theta, inv_c2_vis), '(-1/θ, +1/c²)\n1/c² ≈ 1.11265e-17 s²/m²', (-90, -8)),
    ((theta, c2_vis), '(+θ, +c²)\nc² = 8.987552e+16 m²/s²', (8, 10)),
    ((inv_theta, c2_vis), '(+1/θ, +c²)', (8, 10)),
    ((inv_theta, inv_c2_vis), '(+1/θ, +1/c²)\n1/c² ≈ 1.11265e-17', (8, -8)),
    ((-theta, -c2_vis), '(-θ, -c²)\nc² = 8.987552e+16', (-50, -30)),
    ((-inv_theta, -c2_vis), '(-1/θ, -c²)', (-55, -30)),
    ((-inv_theta, -inv_c2_vis), '(-1/θ, -1/c²)\n1/c² ≈ 1.11265e-17', (-90, 5)),
    ((theta, -c2_vis), '(+θ, -c²)\nc² = 8.987552e+16', (8, -30)),
    ((inv_theta, -c2_vis), '(+1/θ, -c²)', (8, -30)),
    ((inv_theta, -inv_c2_vis), '(+1/θ, -1/c²)\n1/c² ≈ 1.11265e-17', (8, 5)),
]

for (x, y), text, offset in annots:
    ax.annotate(text, (x, y), textcoords="offset points", xytext=offset,
                fontsize=7.5, ha='left' if x >= 0 else 'right',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.88, edgecolor='gray', linewidth=0.5))

ax.axhline(0, color='black', linewidth=1.0)
ax.axvline(0, color='black', linewidth=1.0)
ax.set_xlim(-theta*1.45, theta*1.45)
ax.set_ylim(-c2_vis*1.45, c2_vis*1.45)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.45)
ax.legend(loc='upper right', fontsize=9, framealpha=0.9)

ax.set_title('Trace c² involution through origin\n'
             'Self-referential scaling: visual height of c² set to unity (spacetime curvature units)\n'
             'Actual labels: c² = 8.987551787368176e+16 m²/s² ,  1/c² ≈ 1.112650056e-17 s²/m²',
             fontsize=11)
ax.set_xlabel('x (θ-parameter scale)')
ax.set_ylabel('y (normalized: visual c² ≡ 1)')

plt.tight_layout()
plt.savefig('c2_involution_real_labels.png', dpi=160, bbox_inches='tight')
print('Saved successfully')
print(f'c² exact = {c2_real}')
print(f'1/c² ≈ {inv_c2_real}')
