from collections import defaultdict
from pprint import pprint
import math


PART1_TEST_ANSWER = 37
PART2_TEST_ANSWER = 168


def _parse_line(s):
    return [int(x) for x in s.split(",")]


def _get_data(filename):
    with open(filename) as f:
        return _parse_line(f.read().strip())

    return 0


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def get_median(data):
    sorted_state = sorted(data)
    pos = len(sorted_state) // 2
    return sorted_state[pos]


def count(data, new_position, count_score_fn):
    dist = 0
    for val in data:
        score = count_score_fn(val, new_position)
        dist += score

    return dist


def get_float_average(data):
    avg = sum(data) / len(data)
    return avg


def flat_score(old, new):
    return abs(old - new)


def expensive_score(old, new):
    score = 0
    for cost in range(abs(old - new)):
        score += cost + 1
    return score


def count_part1(data):
    new_position = get_median(data)
    return count(data, new_position, flat_score)


def count_part2(data):
    avg = get_float_average(data)
    return min(
        count(data, math.floor(avg), expensive_score),
        count(data, math.ceil(avg), expensive_score),
    )


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
