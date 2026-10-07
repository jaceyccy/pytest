# DSC 198 - pytest Handbook Exercise

This repo has my work for the DSC 198 pytest handbook exercise.

- `solution.py` has the `two_sum` function, which uses a dictionary to find two indices that add up to the target (or returns `[]` if there's no pair).
- `test_solution.py` has my pytest test cases. They cover a typical case, an empty list, a case with no solution, and a duplicate/boundary case (`[3, 3]`).

To run the tests:

```
python -m pytest -v
```
