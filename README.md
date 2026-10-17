# Triangle Classification Project

This project determines whether three side lengths form a valid triangle, classifies the triangle shape, and flags right triangles for reinforcement.

## How to run the tests

1. Create or activate a Python environment.
2. Install dependencies:
   python -m pip install -r requirements.txt
3. Run the test suite:
   python -m pytest -q

## Equivalence classes and boundaries identified

- Invalid inputs: any side length <= 0
- Invalid degenerate case: the sum of two sides equals the third side, e.g. (1, 2, 3)
- Valid equilateral: all three sides are equal, e.g. (4, 4, 4)
- Valid isosceles: exactly two sides are equal, e.g. (5, 5, 6)
- Valid scalene: all three sides differ, e.g. (2, 3, 4)
- Valid right triangle: satisfies a^2 + b^2 = c^2 within a tolerance, e.g. (3, 4, 5)
- Right isosceles with non-integer hypotenuse: (5, 5, 5 * sqrt(2)); this catches floating-point comparisons that use == instead of a tolerance

## Why an equilateral triangle can never be right

An equilateral triangle has three equal sides, which means each interior angle is 60 degrees. A right triangle must have one 90-degree angle, so an equilateral triangle cannot also be right.

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| --- | --- | --- | --- |
| test_right_triangle | Yes | Edited | Copilot originally asserted with ==; changed it to math.isclose because the spec requires a tolerance-based right-triangle check. |
| test_right_isosceles_triangle_with_non_integer_hypotenuse | Yes | Kept | The test matches the specification and guards against floating-point equality mistakes. |
| test_degenerate_boundary_case_is_invalid | Yes | Kept | This matches the boundary condition exactly: a + b == c is invalid. |

## Acceptance criteria

1. For any three side lengths entered, the classifier must return either a valid triangle classification or "Invalid" without crashing.
2. A valid right triangle must be labeled with the prefix "Right " and marked as buildable for reinforcement checks.
3. If the triangle is invalid or degenerate, the result must be "Invalid" and not misclassify the shape.

## AI-use disclosure

Tool: GitHub Copilot (IDE autocomplete)
What used for: drafting the initial test ideas and checking whether the generated assertions matched the specification.
What verified: each suggestion was checked against the assignment requirements; the right-triangle test was edited to use math.isclose instead of exact equality.
No other AI tool used.

## Acceptance test summary

The acceptance test calls classify_triangle() end-to-end and verifies the required customer-facing behavior for valid right triangles, invalid triangles, and valid non-right triangles.
