import pandas as pd
import numpy as np

# Physical and geometric constants
theta = 6.5 * np.pi                  # ≈ 20.4203522483
c2    = 8.98755179e16                # m²/s²

# Explicit path definitions (the matrix subscripts)
paths = {
    "Bottom-Left": [
        (0.0,          0.0),
        (-theta,      -c2),
        (1/-theta,    -c2),
        (1/-theta,  1/-c2),
        (0.0,          0.0)
    ],
    "Bottom-Right": [
        (0.0,          0.0),
        ( theta,      -c2),
        (1/theta,     -c2),
        (1/theta,   1/-c2),
        (0.0,          0.0)
    ],
    "Top-Left": [
        (0.0,          0.0),
        (-theta,       c2),
        (1/-theta,     c2),
        (1/-theta,   1/c2),
        (0.0,          0.0)
    ],
    "Top-Right": [
        (0.0,          0.0),
        ( theta,       c2),
        (1/theta,      c2),
        (1/theta,    1/c2),
        (0.0,          0.0)
    ]
}

# Build the multi-index DataFrame (the coded matrix)
rows = []
for quadrant, points in paths.items():
    for step, (x, y) in enumerate(points):
        rows.append({
            "Quadrant"      : quadrant,
            "Step"          : step,
            "x_angular"     : x,
            "y_real"        : y,
            "Y_normalized"  : y / c2
        })

M_loop = pd.DataFrame(rows).set_index(["Quadrant", "Step"])
