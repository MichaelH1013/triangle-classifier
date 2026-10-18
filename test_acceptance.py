from triangle import classify_triangle


def test_acceptance_customer_requirements():
    # Criterion 1: a valid right triangle is flagged with the prefix "Right ".
    result = classify_triangle(3, 4, 5)
    assert result.startswith("Right ")
    assert result == "Right Scalene"

    # Criterion 2: an invalid triangle returns exactly "Invalid" and does not crash.
    invalid_pieces = [(0, 4, 5), (-3, 4, 5), (1, 2, 3), (1, 1, 5)]
    for a, b, c in invalid_pieces:
        assert classify_triangle(a, b, c) == "Invalid"

    # Criterion 3: a valid non-right triangle returns its shape with no "Right " prefix.
    expected = {
        (4, 4, 4): "Equilateral",
        (5, 5, 6): "Isosceles",
        (2, 3, 4): "Scalene",
    }
    for sides, shape in expected.items():
        result = classify_triangle(*sides)
        assert result == shape
        assert not result.startswith("Right")
