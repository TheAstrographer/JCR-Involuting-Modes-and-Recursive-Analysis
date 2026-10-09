import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Chart 3: Side-by-side Geometric ↔ Cosmological Dictionary
# ============================================================
fig, ax = plt.subplots(figsize=(13, 7))
ax.axis('off')

# Table data
headers = ['Stage', 'Geometric Action', 'ΔY', 'Y', 'Cosmological Pillar / Role', 'Key Observable']
rows = [
    ['0', 'Initial closed curve at origin', '0.00', '0.00', 'Bosonic Baseline (ΛCDM)', 'H₀_base ≈ 70'],
    ['1', 'Gravitational force acts', '+0.25', '0.25', 'Planck 2018 (high-z anchor)', 'r_d, A_s, early growth'],
    ['2', 'Curve expands (phase onset)', '+0.25', '0.50', 'DESI DR2 BAO', 'D_M(z)/r_d, D_H(z)/r_d'],
    ['3', 'Involuting fold (half-winding)', '0.00', '0.50', 'DES Y6 3×2pt + KiDS-Legacy', 'Growth / weak lensing (S₈)'],
    ['4', 'Return to multi-lobed curve', '+0.25', '0.75', 'Pantheon+ SNIa', 'd_L(z) shape'],
    ['5', 'Terminal loop{∞|∞} at Y=1', '+0.25', '1.00', 'Local H₀ / Dual-Gate torque', '+3.17 → H₀_local ≈ 73.17'],
]

# Draw table
col_widths = [0.07, 0.28, 0.07, 0.07, 0.28, 0.23]
x0, y0 = 0.02, 0.92
row_h = 0.11

# Header
x = x0
for i, h in enumerate(headers):
    ax.text(x + col_widths[i]/2, y0, h, ha='center', va='center', fontsize=9, fontweight='bold',
            transform=ax.transAxes, color='white',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#2c3e50', edgecolor='none'))
    x += col_widths[i]

# Rows
colors_row = ['#ecf0f1', '#d5e8f0', '#d5e8f0', '#fdebd0', '#d5f5e3', '#e8daef']
for r_idx, row in enumerate(rows):
    y = y0 - (r_idx + 1) * row_h
    x = x0
    for i, cell in enumerate(row):
        ax.text(x + col_widths[i]/2, y, cell, ha='center', va='center', fontsize=8.2,
                transform=ax.transAxes,
                bbox=dict(boxstyle='round,pad=0.25', facecolor=colors_row[r_idx], edgecolor='#bdc3c7', alpha=0.95))
        x += col_widths[i]

# Footer note
ax.text(0.5, 0.08,
        'Source geometry: JCR-Involuting-Modes-and-Recursive-Analysis  |  '
        'Statistical arena: Confronting-The-Data (five-pillar matrix)  |  '
        'Model config: Cosmological-Theses / jcrin_dual_gate_joint.yaml\n'
        'Net telescopic sum ΣΔY = 1.00  ↔  Dual-Gate torque = +3.17 km s⁻¹ Mpc⁻¹  |  '
        'Path independence: final Δχ² depends only on boundary states Y₀ and Y₅',
        ha='center', va='center', fontsize=8.5, transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef9e7', edgecolor='#f39c12'))

ax.set_title('Geometric ↔ Cosmological Dictionary of the Involuting Mode\n'
             'Protected 5-Stage Recursion on the Real–Angular Plane',
             fontsize=13, fontweight='bold', pad=8)

plt.tight_layout()
plt.savefig('/home/workdir/geo_cosmo_dictionary.png', dpi=160, bbox_inches='tight')
print("Chart 3 saved: geo_cosmo_dictionary.png")
plt.close()
