from triangle import classify_triangle


def test_acceptance_customer_requirements():
    # Acceptance criterion 1: valid right triangles are flagged as right and buildable.
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    # Acceptance criterion 2: invalid or degenerate triangles are rejected without crashing.
    assert classify_triangle(1, 2, 3) == "Invalid"

    # Acceptance criterion 3: valid non-right triangles are classified by shape without false positives.
    assert classify_triangle(5, 5, 6) == "Isosceles"
