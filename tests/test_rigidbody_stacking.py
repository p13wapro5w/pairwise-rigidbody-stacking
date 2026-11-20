import pytest
import math
from gameplay import rigidbody_stacking as mod

CASES = [
    ("iter", 'm.solver_iterations(4, 8) == 8'),
    ("points", 'm.manifold_points(6) == 4'),
    ("sleep", 'm.sleep_ok(0.1, 0.1, 0.2, 0.2) is True'),
    ("mass", 'm.mass_ratio_clamp(4, 2, 3) == approx(2.0)'),
    ("ccd", 'm.ccd_enabled(10, 10) is True'),
    ("step", 'm.fixed_step(0.016, 0.01) == 0.01'),
    ("friction", 'm.friction_cone(5, 0.5) == approx(2.5)'),
    ("order", 'm.stable_order([3, 1, 2]) == [1, 2, 3]'),
    ("omega", 'm.sync_angular(2) == 2'),
    ("cluster", 'm.cluster_count(10, 4) == 3'),
    ("pen", 'm.penetration(0.1, 0.5, 0.01) == approx(0.045)'),
    ("id", 'm.contact_id(3, 2) == "3:2"'),
    ("area", 'm.manifold_area(2, 3) == 6'),
    ("sleepc", 'm.sleep_counter(10, 10) is True'),
    ("stack", 'm.stack_height(4) == 4')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
