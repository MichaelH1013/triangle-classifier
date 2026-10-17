import math


def is_valid_triangle(a, b, c) -> bool:
    """Return True when the three side lengths form a valid triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False

    x, y, z = sorted((a, b, c))
    return x + y > z


def classify_triangle(a, b, c) -> str:
    """Classify a triangle by validity, shape, and right-angle status."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    x, y, z = sorted((a, b, c))

    if x == y == z:
        base_type = "Equilateral"
    elif x == y or y == z:
        base_type = "Isosceles"
    else:
        base_type = "Scalene"

    is_right = math.isclose(math.hypot(x, y), z, rel_tol=1e-9, abs_tol=0.0)

    if is_right and base_type != "Equilateral":
        return f"Right {base_type}"

    return base_type
