from collections import defaultdict


PART1_TEST_ANSWER = 5934
PART2_TEST_ANSWER = -1


def _parse_line(s):
    return [int(x) for x in s.split(',')]


def _get_data(filename):
    with open(filename) as f:
        return _parse_line(f.read().strip())

    return 0


def get_data():
    return _get_data("input.txt")


def get_test_data():
    return _get_data("test_input.txt")


def count_part1(state, days=80):
    new_fish = 0
    while days > 0:
        for idx, fish_state in enumerate(state):
            if fish_state == 0:
                state[idx] = 6
                new_fish += 1
            else:
                state[idx] = fish_state - 1
        state.extend([8 for _ in range(new_fish)])
        new_fish = 0
        days -= 1
    return len(state)

def count_part2(data):
    return -1


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
