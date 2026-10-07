from solution import two_sum


def test_pair_at_the_start():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_no_pair_exists():
    assert two_sum([1, 2, 3], 100) == []


def test_empty_list():
    assert two_sum([], 5) == []


def test_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]
