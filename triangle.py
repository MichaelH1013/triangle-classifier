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

    if math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9) and math.isclose(y, z, rel_tol=1e-9, abs_tol=1e-9):
        base_type = "Equilateral"
    elif (
        math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(y, z, rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(x, z, rel_tol=1e-9, abs_tol=1e-9)
    ):
        base_type = "Isosceles"
    else:
        base_type = "Scalene"

    is_right = math.isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-9)

    if is_right and base_type != "Equilateral":
        return f"Right {base_type}"

    return base_type
