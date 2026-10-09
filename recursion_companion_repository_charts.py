import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Chart 1: Five-Stage Protected Recursion with Cosmological Labels
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Canonical quarter-unit ladder (most consistent across repo files)
steps = [0, 1, 2, 3, 4, 5]
real_coord = [0.00, 0.25, 0.50, 0.50, 0.75, 1.00]
net_advance = [0.00, 0.25, 0.25, 0.00, 0.25, 0.25]

# Geometric stage names
geo_labels = [
    "Stage 0\nInitial closed curve\n(Origin)",
    "Stage 1\nGravitational force\n(+ΔY)",
    "Stage 2\nCurve expands\n(+ΔY)",
    "Stage 3\nInvoluting mode\n(ΔY=0, half-winding)",
    "Stage 4\nReturn multi-lobed\n(+ΔY)",
    "Stage 5\nTerminal loop{∞|∞}\n(Y=1 ↔ c²)"
]

# Cosmological pillar mapping (from Confronting-The-Data + Cosmological-Theses)
cosmo_labels = [
    "Baseline\n(ΛCDM / Bosonic)",
    "Planck 2018\n(TT/TE/EE + lensing)",
    "DESI DR2 BAO\n(geometric distances)",
    "DES Y6 3×2pt +\nKiDS-Legacy\n(growth / weak lensing)",
    "Pantheon+\n(luminosity distances)",
    "Local H₀ / Dual-Gate\n(+3.17 km s⁻¹ Mpc⁻¹)"
]

# Chart 1a: Real Coordinate Progression
ax = axes[0, 0]
ax.plot(steps, real_coord, 'o-', color='navy', lw=2.8, markersize=10, zorder=3)
ax.fill_between(steps, real_coord, alpha=0.12, color='navy')
for i, (x, y) in enumerate(zip(steps, real_coord)):
    ax.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0,14), ha='center', fontsize=10, fontweight='bold')
ax.axhline(1.0, color='green', ls='--', alpha=0.6, label='Y=1 ↔ c² horizon')
ax.axhline(0.5, color='darkorange', ls=':', alpha=0.7, label='Involuting plateau Y=0.50')
ax.set_xticks(steps)
ax.set_xticklabels([f'n={s}' for s in steps])
ax.set_ylabel('Normalized Real Coordinate Y = y / c²', fontsize=11)
ax.set_title('Real Coordinate vs Protected Recursion Step', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.08, 1.18)
ax.legend(fontsize=8, loc='upper left')

# Chart 1b: Net Real Advance per Step
ax = axes[0, 1]
colors = ['gray', 'steelblue', 'steelblue', 'darkorange', 'seagreen', 'purple']
bars = ax.bar(steps, net_advance, color=colors, edgecolor='black', width=0.65, zorder=3)
ax.set_xticks(steps)
ax.set_xticklabels([f'n={s}' for s in steps])
ax.set_ylabel('Net Real Advance ΔY', fontsize=11)
ax.set_title('Net Real Advance per Step\n(ΣΔY = 1.00 ↔ Dual-Gate torque +3.17)', fontsize=12, fontweight='bold')
ax.axhline(0, color='black', lw=0.9)
ax.grid(True, axis='y', alpha=0.3)
for bar, val in zip(bars, net_advance):
    if val != 0:
        ax.annotate(f'+{val:.2f}', xy=(bar.get_x() + bar.get_width()/2, val),
                    xytext=(0, 6), textcoords="offset points", ha='center', fontsize=10, fontweight='bold')
    else:
        ax.annotate('ΔY=0\n(fold)', xy=(bar.get_x() + bar.get_width()/2, 0.02),
                    xytext=(0, 8), textcoords="offset points", ha='center', fontsize=8, color='darkorange')

# Chart 1c: Stages with geometric labels
ax = axes[1, 0]
ax.plot(steps, real_coord, 'o-', color='darkred', lw=2.5, markersize=9)
ax.set_xticks(steps)
ax.set_xticklabels(geo_labels, fontsize=7.5)
ax.set_ylabel('Normalized Real Coordinate Y', fontsize=11)
ax.set_title('Geometric Stages of the Protected Recursion\n(Real–Angular Plane skeleton)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.08, 1.18)
ax.axhline(1.0, color='green', ls='--', alpha=0.5)
ax.axhline(0.5, color='darkorange', ls=':', alpha=0.6)

# Chart 1d: Cosmological pillar mapping
ax = axes[1, 1]
ax.plot(steps, real_coord, 'o-', color='darkviolet', lw=2.5, markersize=9)
ax.set_xticks(steps)
ax.set_xticklabels(cosmo_labels, fontsize=7.2)
ax.set_ylabel('Normalized Real Coordinate Y', fontsize=11)
ax.set_title('Cosmological Mapping onto Five-Pillar Master Joint Likelihood\n(Confronting-The-Data + Cosmological-Theses)', fontsize=11, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.08, 1.18)
ax.axhline(1.0, color='green', ls='--', alpha=0.5)
ax.axhline(0.5, color='darkorange', ls=':', alpha=0.6)

plt.suptitle('Involuting Mode Charts with Cosmological Labelling\n'
             'JCR-Involuting-Modes-and-Recursive-Analysis  →  Dual-Gate torque = +3.17 km s⁻¹ Mpc⁻¹',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('/home/workdir/involuting_cosmo_charts.png', dpi=160, bbox_inches='tight')
print("Chart 1 saved: involuting_cosmo_charts.png")
plt.close()
