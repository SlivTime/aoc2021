from collections import defaultdict
from pprint import pprint
import math
from typing import List


PART1_TEST_ANSWER = 26
PART2_TEST_ANSWER = 61229


def _parse_line(s):
    left, right = s.split("|")
    return left.strip().split(), right.strip().split()


def _get_data(filename):
    with open(filename) as f:
        for line in f:
            yield _parse_line(line)

    return 0


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def fit(a: str, b: str):
    # a fit in b
    s_a = set(a)
    s_b = set(b)
    return s_a | s_b == s_b


def _pop_by_condition(alfabeth, condition_fn) -> str:
    for idx, digit in enumerate(alfabeth):
        if condition_fn(digit):
            return alfabeth.pop(idx)


def _pop_by_len(alfabeth, n):
    condition = lambda digit: len(digit) == n
    return _pop_by_condition(alfabeth, condition)


def _prepare_key(s):
    return "".join(sorted(s))


def get_transforms(alfabeth):
    d = {
        "1": _pop_by_len(alfabeth, 2),
        "4": _pop_by_len(alfabeth, 4),
        "7": _pop_by_len(alfabeth, 3),
        "8": _pop_by_len(alfabeth, 7),
    }
    d["3"] = _pop_by_condition(alfabeth, lambda x: len(x) == 5 and fit(d["7"], x))
    d["9"] = _pop_by_condition(alfabeth, lambda x: len(x) == 6 and fit(d["3"], x))
    d["0"] = _pop_by_condition(alfabeth, lambda x: len(x) == 6 and fit(d["7"], x))
    d["5"] = _pop_by_condition(alfabeth, lambda x: len(x) == 5 and fit(x, d["9"]))
    d["2"] = _pop_by_len(alfabeth, 5)
    d["6"] = _pop_by_len(alfabeth, 6)
    return {_prepare_key(v): str(k) for k, v in d.items()}


def to_number(alfabeth, display):
    number_string = "".join([alfabeth[_prepare_key(digit)] for digit in display])
    return int(number_string)


def to_set(alfabeth, display):
    print(alfabeth)
    return set([alfabeth[_prepare_key(digit)] for digit in display])


def count_part1(data):
    result = 0
    look_for_lengths = {2, 3, 4, 7}

    for _, right in data:
        result += len([x for x in right if len(x) in look_for_lengths])

    return result


def count_part2(data):
    displayed_numbers = []
    for alfabeth, display in data:
        transforms = get_transforms(alfabeth)
        displayed_numbers.append(
            to_number(
                transforms,
                display,
            )
        )
    return sum(displayed_numbers)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
