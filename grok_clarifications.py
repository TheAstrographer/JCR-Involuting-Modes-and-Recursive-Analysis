import numpy as np
import pandas as pd
from dataclasses import dataclass

# ------------------------------------------------------------------
# Physical constant – universally accepted, no further derivation
# ------------------------------------------------------------------
C2 = 8.98755179e16          # m²/s²  (exact measured value used as scale)

# ------------------------------------------------------------------
# Real–Angular Plane
# ------------------------------------------------------------------
THETA_MAX = 6.5 * np.pi     # rad  (domain sized for 720° positive holonomy)
Y_MAX     = 1.0             # dimensionless  ↔  physical y = C2

@dataclass
class Stage:
    n: int
    name: str
    delta_Y: float          # may vary; only net sum is constrained
    Y: float
    theta_note: str

# Intermediate ΔY values are NOT privileged maturity rates.
# They are free samplings; the only mandatory constraint is net sum = 1.0
stages = [
    Stage(0, "Initial closed curve",          0.00, 0.00, "origin"),
    Stage(1, "Gravitational force acts",      0.25, 0.25, "onset"),
    Stage(2, "Curve expands",                 0.25, 0.50, "expansion"),
    Stage(3, "Involuting mode (freeze)",      0.00, 0.50, "half-winding / monodromy -1"),
    Stage(4, "Return to multi-lobed curve",   0.25, 0.75, "circulatory cancel"),
    Stage(5, "Terminal loop{∞|∞}",            0.25, 1.00, "seated at Y=1 ↔ c²"),
]

df = pd.DataFrame([s.__dict__ for s in stages])
df["physical_y"] = df["Y"] * C2

print("=== Protected 5-stage recursion ===")
print(df.to_string(index=False))
print()
print(f"Net telescopic sum  ΣΔY = {df['delta_Y'].sum():.2f}  (must equal 1.0)")
print(f"Terminal physical height = {df.loc[5,'physical_y']:.6e} m²/s²  (= c²)")
print(f"Angular domain: [{-THETA_MAX:.4f}, {+THETA_MAX:.4f}] rad")
print(f"  → full span 13π ≈ {13*np.pi:.4f} rad")
print(f"  → sized so geometry reaches 720° positive holonomy identity")
print()
print("Dual-Gate torque is the cosmological image of the forced net advance Y₅−Y₀ = 1.00")
