import math

import pytest

from triangle import classify_triangle, is_valid_triangle


def test_invalid_for_non_positive_side_lengths():
    assert classify_triangle(0, 3, 4) == "Invalid"
    assert classify_triangle(-1, 2, 2) == "Invalid"


def test_is_valid_triangle_checks_positive_sides_and_strict_inequality():
    assert is_valid_triangle(3, 4, 5)
    assert not is_valid_triangle(0, 3, 4)
    assert not is_valid_triangle(1, 2, 3)


def test_equilateral_triangle():
    assert classify_triangle(4, 4, 4) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene"


def test_degenerate_boundary_case_is_invalid():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_triangle_with_non_integer_hypotenuse():
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"
