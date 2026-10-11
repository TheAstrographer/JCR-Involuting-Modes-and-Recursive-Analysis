import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the c² constant base scale unit (normalized to 1 for perfect layout proportions)
c2 = 1.0
tiers = [1 * c2, 2 * c2, 3 * c2]
tier_colors = {1: '#ff8c00', 2: '#4a90e2', 3: '#1f51a8'}  # Orange, Light Blue, Dark Blue

plt.figure(figsize=(9, 9), facecolor='white')
ax = plt.subplot(111)

# Generate continuous parametric loops routing smoothly through the Origin (0,0)
t = np.linspace(0, np.pi, 200)

for n in tiers:
    color = tier_colors[n]
    linestyle = '--' if n == 2 else '-'  # Matching the dashed signature of Tier 2
    linewidth = 2.0 if n == 3 else 1.5
    
    # 1. Top Lobe (Positive Y-Axis Family)
    x_top = n * np.sin(t) * np.cos(t + np.pi/2)
    y_top = n * np.sin(t) * np.sin(t + np.pi/2)
    ax.plot(x_top, y_top, color=color, linestyle=linestyle, linewidth=linewidth, label=f'Tier {int(n)} ({int(n)}c²)' if 'top' else "")

# 2. Bottom Lobe (Negative Y-Axis Family)
    x_bot = n * np.sin(t) * np.cos(t - np.pi/2)
    y_bot = n * np.sin(t) * np.sin(t - np.pi/2)
    ax.plot(x_bot, y_bot, color=color, linestyle=linestyle, linewidth=linewidth)
    
    # 3. Right Lobe (Positive X-Axis Family)
    x_right = n * np.sin(t) * np.cos(t)
    y_right = n * np.sin(t) * np.sin(t)
    ax.plot(x_right, y_right, color=color, linestyle=linestyle, linewidth=linewidth)
    
    # 4. Left Lobe (Negative X-Axis Family)
    x_left = n * np.sin(t) * np.cos(t + np.pi)
    y_left = n * np.sin(t) * np.sin(t + np.pi)
    ax.plot(x_left, y_left, color=color, linestyle=linestyle, linewidth=linewidth)

# Highlight and lock the central Origin Vertex
ax.plot(0, 0, 'ko', markersize=6, zorder=5)
ax.text(0.1, -0.15, '0', fontsize=12, fontweight='bold')

# Apply exact Axis Rung Labels matching your unicode environment specs
ax.set_xticks([-3, -2, -1, 1, 2, 3])
ax.set_xticklabels(['$-3c^2$', '$-2c^2$', '$-1c^2$', '$1c^2$', '$2c^2$', '$3c^2$'], fontsize=10)
ax.set_yticks([-3, -2, -1, 1, 2, 3])
ax.set_yticklabels(['$-3c^2$', '$-2c^2$', '$-1c^2$', '$1c^2$', '$2c^2$', '$3c^2$'], fontsize=10)

# Quad Text Annotations mapping your literal parameter strings
ax.text(1.1, 3.2, r'$(\theta, c^2)1c^2)2c^2)3c^2)$', fontsize=10, color='#333333')
ax.text(-2.9, 3.2, r'$(-\theta, c^2)1c^2)2c^2)3c^2)$', fontsize=10, color='#333333')
ax.text(-2.9, -3.4, r'$(-\theta, -1c^2)-2c^2)-3c^2)$', fontsize=10, color='#333333')
ax.text(1.1, -3.4, r'$(\theta, -1c^2)-2c^2)-3c^2)$', fontsize=10, color='#333333')

# Grid Configurations
ax.axhline(0, color='black', linewidth=0.8, zorder=1)
ax.axvline(0, color='black', linewidth=0.8, zorder=1)
ax.grid(True, which='both', linestyle=':', color='gray', alpha=0.6)
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_aspect('equal')

# Legend and Title
handles, labels = ax.get_legend_handles_labels()
# Filter unique legend labels
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right', framealpha=0.95)
ax.set_title("Real-Angular Plane: Hierarchical $c^2$ Involuting Loops", fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('/tmp/hierarchical_loops.png')
plt.close()
print("Plot regenerated successfully")
print("File exists:", os.path.exists('/tmp/hierarchical_loops.png'))
print("File size:", os.path.getsize('/tmp/hierarchical_loops.png'))
