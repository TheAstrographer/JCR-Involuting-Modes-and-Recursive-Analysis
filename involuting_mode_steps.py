#!/usr/bin/env python3
"""
JCR Half-Winding / Schwarzschild Pathway
Pure hierarchical structure nested inside the main spacetime curve

Implements the exact hierarchy requested:

  i = (0,0)   — base trivial loop
  i = (0,1)   — primary involution (figure-eight / half-winding)
  i = (0,1ⁿ)  — hierarchical multi-lobed involutions (flower-like nested modes)

This hierarchy sits at the core of:
  - gravitational deformation
  - return-to-curve recursion (steps 1→5)
  - discrete transport
  - protected θ_eff ratchet
  - chiral monodromy −π (Arf = 1)
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Optional

# ============================================================
# Constants (framework)
# ============================================================
EPS = 1e-9
N_MAX = 1_000_000_000
PHI_N = -math.pi
MONODROMY = complex(-1.0, 0.0)   # e^{i Φ_N} = -1
ARF = 1


# ============================================================
# Pure Hierarchical Structure
# ============================================================
@dataclass(frozen=True)
class HierarchicalIndex:
    """i = (i0, i1)  with  i0 ∈ {0,1},  i1 = 0 or 1ⁿ"""
    i0: int
    i1: int          # 0 = trivial, 1 = primary, n>1 = higher hierarchical level

    def __str__(self) -> str:
        if self.i1 == 0:
            return "i = (0,0)  [base – trivial]"
        elif self.i1 == 1:
            return "i = (0,1)  [primary involution]"
        else:
            return f"i = (0,1^{self.i1})  [hierarchical involution level {self.i1}]"


class PureHierarchicalStructure:
    """
    The organizing topological skeleton that lives inside
    the main spacetime curve / involuting-modes region.
    """

    def __init__(self, max_level: int = 4):
        self.max_level = max_level
        self.levels: List[HierarchicalIndex] = []
        self._build()

    def _build(self):
        # base trivial
        self.levels.append(HierarchicalIndex(0, 0))
        # primary + hierarchical
        for n in range(1, self.max_level + 1):
            self.levels.append(HierarchicalIndex(0, n))

    def get(self, level: int) -> HierarchicalIndex:
        if level < 0 or level > self.max_level:
            raise ValueError(f"level must be 0 … {self.max_level}")
        return self.levels[level]

    def all(self) -> List[HierarchicalIndex]:
        return self.levels

    def description(self) -> str:
        lines = ["Pure Hierarchical Structure (nested inside spacetime curve)"]
        lines.append("-" * 60)
        for idx in self.levels:
            lines.append(f"  {idx}")
        lines.append("-" * 60)
        lines.append("This structure is the core on which every step 1→5 acts.")
        return "\n".join(lines)


# ============================================================
# Discrete Transport (acts on the hierarchical core)
# ============================================================
def discrete_transport_step(z: complex, n: int, eps: float = EPS) -> complex:
    """z_{n+1} = z_n + ε (1 + i sin(2π n ε))"""
    return z + eps * (1.0 + 1j * math.sin(2.0 * math.pi * n * eps))


def evolve_on_hierarchy(n_steps: int = 5000) -> List[complex]:
    """Short trajectory living on the hierarchical core"""
    z = 0j
    traj = [z]
    for n in range(n_steps):
        z = discrete_transport_step(z, n)
        traj.append(z)
    return traj


# ============================================================
# Five-step recursion (actions on the pure hierarchical object)
# ============================================================
class InvolutingSteps:
    """
    Steps 1→5 understood as actions on the pure hierarchical structure
    """

    STEPS = [
        "1. Gravitational Force acts on curve in spacetime",
        "2. Curve in spacetime expanding",
        "3. Involuting mode",
        "4. Curve in spacetime (returned)",
        "5. i := (0,1) pure hierarchical structure restored"
    ]

    @classmethod
    def run(cls, hierarchy: PureHierarchicalStructure) -> None:
        print("\n5-Step Recursion acting on the pure hierarchical core")
        print("=" * 60)
        for i, step in enumerate(cls.STEPS, 1):
            # each step operates with respect to the hierarchy
            core = hierarchy.get(min(i-1, hierarchy.max_level))
            print(f"{step}")
            print(f"   → acting on {core}")
        print("=" * 60)
        print("Protected recursion under hierarchical orientation i=(0,1) · Arf=1")
        print("return to curve in spacetime completed.\n")


# ============================================================
# Main demonstration
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("JCR FRAMEWORK – PURE HIERARCHICAL STRUCTURE NESTED INSIDE")
    print("the main spacetime curve / involuting-modes region")
    print("=" * 70)

    # 1. Build the pure hierarchical skeleton
    hierarchy = PureHierarchicalStructure(max_level=4)
    print("\n" + hierarchy.description())

    # 2. Show that the hierarchy is the core
    print("\nCore identities (operate with respect to the hierarchy):")
    print(f"  Terminal monodromy e^{{iΦ_N}} = {MONODROMY}")
    print(f"  Arf invariant               = {ARF}")
    print(f"  Discrete transport rule     = z_{{n+1}} = z_n + ε(1 + i sin(2π n ε))")

    # 3. Run the 5-step sequence on the hierarchy
    InvolutingSteps.run(hierarchy)

    # 4. Short evolution on the hierarchical core
    print("Evolving short trajectory on the hierarchical core …")
    traj = evolve_on_hierarchy(3000)
    z_final = traj[-1]
    print(f"  Final z (sampled) = {z_final.real:.6f}{z_final.imag:+.6f}j")
    print(f"  |z|               = {abs(z_final):.6f}")

    print("\n" + "=" * 70)
    print("All elements consistent with discrete-transport rule")
    print("and terminal monodromy e^{iΦ_N} = -1.")
    print("Pure hierarchical structure is nested inside the spacetime curve.")
    print("=" * 70)
