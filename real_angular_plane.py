import matplotlib.pyplot as plt
import numpy as np

# Constants
c2 = 8.98755179e16
theta_max = 6.5 * np.pi   # from notebook

fig, ax = plt.subplots(figsize=(10, 10))

# Draw the four quadrants / domain rectangle
# Vertical lines at -theta and +theta
ax.axvline(0, color='black', lw=1.2)
ax.axhline(0, color='black', lw=1.2)

# Domain boundaries
ax.axvline(-theta_max, color='gray', ls='--', lw=1, alpha=0.7)
ax.axvline(theta_max, color='gray', ls='--', lw=1, alpha=0.7)
ax.axhline(-c2, color='gray', ls='--', lw=1, alpha=0.7)
ax.axhline(c2, color='gray', ls='--', lw=1, alpha=0.7)

# Fill quadrants lightly
ax.fill_between([-theta_max, 0], 0, c2, color='blue', alpha=0.06, label='Top-left')
ax.fill_between([0, theta_max], 0, c2, color='green', alpha=0.06, label='Top-right')
ax.fill_between([-theta_max, 0], -c2, 0, color='red', alpha=0.06, label='Bottom-left')
ax.fill_between([0, theta_max], -c2, 0, color='orange', alpha=0.06, label='Bottom-right')

# Labels for corners
ax.text(0, 0, '  origin (0,0)', fontsize=11, fontweight='bold', va='bottom', ha='left')
ax.text(-theta_max, -c2, r'  $(-\theta,-c^2)$', fontsize=10, va='top', ha='left', color='darkred')
ax.text(theta_max, -c2, r'$(\theta,-c^2)$  ', fontsize=10, va='top', ha='right', color='darkorange')
ax.text(-theta_max, c2, r'  $(-\theta,c^2)$', fontsize=10, va='bottom', ha='left', color='darkblue')
ax.text(theta_max, c2, r'$(\theta,c^2)$  ', fontsize=10, va='bottom', ha='right', color='darkgreen')

# Draw a representative involuting mode (4-petal) centered at origin, scaled
t = np.linspace(0, 2*np.pi, 1000)
r = 0.35 * theta_max * np.abs(np.cos(2*t))
x = r * np.cos(t)
y = r * np.sin(t) * (c2 / theta_max) * 0.6   # scale to visible portion of c² axis
ax.plot(x, y, color='navy', lw=2.5, label=r'$\operatorname{loop}\{\infty\mid\infty\}$')

# Mark the real-advance path (vertical arrow along positive real = c² direction)
ax.annotate('', xy=(0.15*theta_max, 0.85*c2), xytext=(0.15*theta_max, 0.1*c2),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2.5))
ax.text(0.18*theta_max, 0.5*c2, r'Real advance $\to c^2$', fontsize=10, color='purple', rotation=90, va='center')

# Formatting
ax.set_xlim(-1.2*theta_max, 1.2*theta_max)
ax.set_ylim(-1.2*c2, 1.2*c2)
ax.set_xlabel(r'Angular coordinate $\theta$', fontsize=12)
ax.set_ylabel(r'Real coordinate (units of $c^2$)', fontsize=12)
ax.set_title(r'Domain of the Real–Angular Plane' + '\n' +
             r'origin $(0,0)$,  $\pm\theta=\pm 6.5\pi$,  $\pm c^2 = \pm 8.98755179\times10^{16}$',
             fontsize=13, pad=12)

# Custom ticks for clarity
ax.set_xticks([-theta_max, 0, theta_max])
ax.set_xticklabels([r'$-\theta$', '0', r'$\theta$'])
ax.set_yticks([-c2, 0, c2])
ax.set_yticklabels([r'$-c^2$', '0', r'$c^2$'])

ax.grid(True, alpha=0.3)
ax.set_aspect('auto')
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('/home/workdir/domain_quadrants_c2.png', dpi=160, bbox_inches='tight')
print("Domain chart saved")
print(f"θ = {theta_max:.4f}")
print(f"c² = {c2:.4e}")
