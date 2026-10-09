import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# Data from the Real Coordinate Table
steps = [0, 1, 2, 3, 4, 5]
real_coord = [0.00, 0.15, 0.40, 0.40, 0.70, 1.00]
net_advance = [0.00, 0.15, 0.25, 0.00, 0.30, 0.30]
stage_labels = [
    "Initial\nclosed curve",
    "Gravitational\nforce",
    "Expansion",
    "Involuting\nmode",
    "Return to\ncurve",
    "Terminal\nloop{∞|∞}"
]

# Chart 1: Real Coordinate Progression
ax = axes[0, 0]
ax.plot(steps, real_coord, 'o-', color='navy', lw=2.5, markersize=9)
ax.fill_between(steps, real_coord, alpha=0.15, color='navy')
for i, (x, y) in enumerate(zip(steps, real_coord)):
    ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0,12), ha='center', fontsize=9)
ax.set_xticks(steps)
ax.set_xticklabels([f'n={s}' for s in steps])
ax.set_ylabel('Real Coordinate')
ax.set_title('Real Coordinate vs Step n')
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.15)

# Chart 2: Net Real Advance per Step
ax = axes[0, 1]
colors = ['gray', 'steelblue', 'steelblue', 'darkorange', 'green', 'purple']
bars = ax.bar(steps, net_advance, color=colors, edgecolor='black', width=0.6)
ax.set_xticks(steps)
ax.set_xticklabels([f'n={s}' for s in steps])
ax.set_ylabel('Net Real Advance')
ax.set_title('Net Real Advance per Step')
ax.axhline(0, color='black', lw=0.8)
ax.grid(True, axis='y', alpha=0.3)
for bar, val in zip(bars, net_advance):
    if val != 0:
        ax.annotate(f'+{val:.2f}', xy=(bar.get_x() + bar.get_width()/2, val),
                    xytext=(0, 5), textcoords="offset points", ha='center', fontsize=9)

# Chart 3: Step labels with real coordinate
ax = axes[1, 0]
ax.plot(steps, real_coord, 'o-', color='darkred', lw=2)
ax.set_xticks(steps)
ax.set_xticklabels(stage_labels, fontsize=8)
ax.set_ylabel('Real Coordinate')
ax.set_title('Stages of the Protected Recursion')
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.15)

# Chart 4: Cumulative + Terminal Mode illustration
ax = axes[1, 1]
theta = np.linspace(0, 2*np.pi, 1000)
r = np.cos(2*theta)
x = r * np.cos(theta) + 1.0   # shifted by terminal real coordinate
y = r * np.sin(theta)
ax.plot(x, y, color='navy', lw=2.5)
ax.axvline(0, color='gray', ls='--', alpha=0.5, label='Original real = 0')
ax.axvline(1.0, color='green', ls='--', alpha=0.7, label='Terminal real = +1.00')
ax.set_aspect('equal')
ax.set_title(r'Terminal $\operatorname{loop}\{\infty\mid\infty\}$' + '\nat new real coordinate +1.00')
ax.legend(fontsize=8, loc='upper right')
ax.axis('off')

plt.suptitle('Real Coordinate Charts — Protected Recursion', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/workdir/real_coordinate_charts.png', dpi=160, bbox_inches='tight')
print("Real coordinate charts saved")
