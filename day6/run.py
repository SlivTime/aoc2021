from collections import defaultdict


PART1_TEST_ANSWER = 5934
PART2_TEST_ANSWER = 26984457539


def _parse_line(s):
    return [int(x) for x in s.split(",")]


def _get_data(filename):
    with open(filename) as f:
        return _parse_line(f.read().strip())

    return 0


def get_data():
    return _get_data("input.txt")


def get_test_data():
    return _get_data("test_input.txt")


def count(state, days):
    while days > 0:
        new_state = defaultdict(int)
        for day, count in state.items():
            if day == 0:
                next_day = 6
                new_state[8] = count
            else:
                next_day = day - 1
            new_state[next_day] += count
        state = new_state
        days -= 1

    return sum(state.values())


def prepare_state(data):
    state = defaultdict(int)
    for item in data:
        state[item] += 1
    return state


def count_part1(data):
    return count(prepare_state(data), days=80)


def count_part2(data):
    return count(prepare_state(data), days=256)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
