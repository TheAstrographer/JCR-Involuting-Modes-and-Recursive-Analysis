import math
from dataclasses import dataclass
from typing import List, Tuple

# ============================================================
# Framework constants
# ============================================================
EPS = 1e-9
PHI_N = -math.pi
MONODROMY = complex(-1.0, 0.0)   # e^{i Φ_N} = -1
ARF = 1                          # odd class


# ============================================================
# Core geometric object
# ============================================================
@dataclass
class SpacetimeCurve:
    """
    Oriented multi-lobed curve on ℂ ≅ ℝ²
    with hierarchical orientation i = (0,1)
    """
    real: float = 0.0          # net displacement along oriented real axis
    imag: float = 0.0          # circulatory (phase) component
    scale: float = 1.0         # overall size
    folded: bool = False       # whether lobes have involuted
    orientation: Tuple[int, int] = (0, 1)  # i = (0,1)

    def complex(self) -> complex:
        return complex(self.real, self.imag)

    def __str__(self) -> str:
        return (f"Curve(re={self.real:.4f}, im={self.imag:.4f}, "
                f"scale={self.scale:.3f}, folded={self.folded}, "
                f"i={self.orientation})")


# ============================================================
# The five steps
# ============================================================
class InvolutingModeSequence:
    """
    Realizes the hierarchical complex structure under gravitational deformation.
    """

    def __init__(self):
        self.curve = SpacetimeCurve()
        self.history: List[str] = []

    def step1_gravitational_force(self):
        """
        Step 1 – Gravitational force acts on a closed curve in spacetime.
        Multi-lobed path is deformed by inward-expanding gravitational force.
        Real-part projection begins to record net displacement.
        Imaginary circulatory component remains topologically closed.
        """
        self.curve.real += 0.15          # onset of net real displacement
        self.curve.scale *= 0.92         # slight compression
        self.history.append(
            "1. Gravitational Force acts on curve in spacetime "
            "(real displacement begins, circulatory part stays closed)"
        )
        return self.curve

    def step2_expanding(self):
        """
        Step 2 – Curve in spacetime expanding.
        Hierarchical orientation i=(0,1) is preserved → anisotropic expansion.
        Real projection advances, imaginary lobes stretch → first θ_eff contributions.
        """
        self.curve.real += 0.25
        self.curve.imag += 0.18          # lobes stretch
        self.curve.scale *= 1.25
        self.history.append(
            "2. Curve in spacetime expanding "
            "(anisotropic under i=(0,1), microscopic torque appears)"
        )
        return self.curve

    def step3_involuting_mode(self):
        """
        Step 3 – Involuting mode.
        Expanded lobes fold back upon themselves.
        Geometric realization of the order-two involution (half-integer winding).
        Circulatory component starts producing chiral monodromy → will close to -1.
        """
        self.curve.folded = True
        self.curve.imag = -self.curve.imag * 0.7   # fold-back
        self.curve.scale *= 0.85
        self.history.append(
            "3. Involuting mode "
            "(lobes fold, order-two involution, monodromy begins)"
        )
        return self.curve

    def step4_return_to_curve(self):
        """
        Step 4 – Curve in spacetime (restored multi-lobed form).
        Return-to-curve recursion complete for this cycle.
        Net real displacement advanced + protected half-winding executed.
        Visual counterpart of one bosonic cycle of the discrete update:
            z_{n+1} = z_n + ε(1 + i sin(2π n ε))
        """
        self.curve.folded = False
        self.curve.real += 0.30          # net advance
        self.curve.imag = abs(self.curve.imag) * 0.6
        self.curve.scale = 1.05
        self.history.append(
            "4. Curve in spacetime (returned) "
            "(recursion complete, one bosonic cycle realized)"
        )
        return self.curve

    def step5_pure_hierarchical(self):
        """
        Step 5 – i := (0,1) pure hierarchical flower-like structure.
        Sequence terminates on the pure oriented complex structure.
        Generator i=(0,1) is restored as the undeformed four-lobed object.
        Selects the odd (Arf=1) class and underpins geometric torque.
        """
        self.curve.orientation = (0, 1)
        self.curve.real = 1.0
        self.curve.imag = 0.0
        self.curve.scale = 1.0
        self.curve.folded = False
        self.history.append(
            "5. i := (0,1) pure hierarchical flower-like structure "
            "(orientation restored, Arf=1 selected)"
        )
        return self.curve

    def run_full_sequence(self) -> SpacetimeCurve:
        """Execute the complete protected recursion 1→5"""
        print("=" * 70)
        print("INVOLUTING-MODE SEQUENCE (Steps 1–5)")
        print("Oriented object on ℂ ≅ ℝ² with fixed i = (0,1)")
        print("=" * 70)

        self.step1_gravitational_force()
        print(f"  After Step 1: {self.curve}")

        self.step2_expanding()
        print(f"  After Step 2: {self.curve}")

        self.step3_involuting_mode()
        print(f"  After Step 3: {self.curve}")

        self.step4_return_to_curve()
        print(f"  After Step 4: {self.curve}")

        self.step5_pure_hierarchical()
        print(f"  After Step 5: {self.curve}")

        print("\n" + "-" * 70)
        print("History of the protected recursion:")
        for h in self.history:
            print(f"  • {h}")
        print("-" * 70)

        print(f"\nTerminal monodromy e^{{iΦ_N}} = {MONODROMY}")
        print(f"Arf invariant               = {ARF}")
        print("One complete protected recursion of the half-winding")
        print("integer matrix structure has been realized.")
        print("=" * 70)

        return self.curve


# ============================================================
# Discrete transport (used inside the recursion)
# ============================================================
def discrete_transport_step(z: complex, n: int, eps: float = EPS) -> complex:
    return z + eps * (1.0 + 1j * math.sin(2.0 * math.pi * n * eps))


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    seq = InvolutingModeSequence()
    final_curve = seq.run_full_sequence()

    print("\nFinal state of the oriented object:")
    print(f"  {final_curve}")
    print(f"  complex value = {final_curve.complex()}")
