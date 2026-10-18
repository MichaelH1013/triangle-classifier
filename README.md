# Triangle Classification Project

This program checks if three side lengths make a valid triangle, tells what kind of triangle it is, and flags right triangles.

## How to run the tests

1. Install pytest:
   python -m pip install -r requirements.txt
2. Run the tests:
   python -m pytest

## Equivalence classes and boundaries

- Invalid: any side that is 0 or less, for example (0, 3, 4)
- Invalid (boundary): two sides add up to exactly the third side, for example (1, 2, 3)
- Equilateral: all three sides are equal, for example (4, 4, 4)
- Isosceles: exactly two sides are equal, for example (5, 5, 6)
- Scalene: all three sides are different, for example (2, 3, 4)
- Right triangle: a squared + b squared = c squared, for example (3, 4, 5)
- Right isosceles with a decimal side: (5, 5, 5 * sqrt(2))

## Why an equilateral triangle can never be right

All three angles in an equilateral triangle are 60 degrees. A right triangle needs one 90 degree angle, so it can't be both.

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| --- | --- | --- | --- |
| test_right_scalene_triangle | Yes | Edited | Copilot used ==, but decimals can be slightly off, so I changed it to math.isclose. |
| test_right_isosceles_triangle_with_non_integer_hypotenuse | Yes | Kept | It matches the spec and tests a right triangle with a decimal side. |
| test_degenerate_boundary_case_is_invalid | Yes | Kept | The spec says two sides adding up to the third side is invalid, and this test checks that. |

## Acceptance criteria

The customer wants to enter three side lengths and be told the shape and whether it can be built. Invalid triangles should show a message and not crash. Right triangles should be flagged for reinforced corners. "Buildable" here means the result is not "Invalid".

1. A valid right triangle like (3, 4, 5) returns a result that starts with "Right " (here, "Right Scalene").
2. An invalid triangle (a side of 0 or less, or two sides that add up to the third, like (1, 2, 3)) returns exactly "Invalid" and does not raise an error.
3. A valid triangle that is not right returns exactly "Equilateral", "Isosceles", or "Scalene" with no "Right " prefix.

## AI-use disclosure

Tool 1: GitHub Copilot (autocomplete in my IDE)
What I used it for: drafting the unit tests in test_triangle.py.
What I verified: I checked each suggested test against the spec table, not against what my code returned. I changed the right-triangle test to use math.isclose instead of ==.

Tool 2: Claude (AI assistant from Anthropic)
What I used it for: checking my project against the assignment requirements, rewriting the acceptance criteria and test_acceptance.py, simplifying this README, and using Claude's agent tool to add the Markdown formatting to this README and to review my code.
What I verified: I ran all the tests myself and they pass.

No other AI tool used.
