import re
from typing import List, Tuple

PART1_TEST_ANSWER = 45
PART2_TEST_ANSWER = 112

LITERAL_TYPE_ID = "100"
LITERAL_BIT_LEN = 5


regex = re.compile(r"x=(-?\d+)..(-?\d+).*y=(-?\d+)..(-?\d+)")


def _get_data(filename):
    with open(filename) as f:
        raw = f.read()
        match = regex.search(raw)
        return (int(x) for x in match.groups())


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def get_progression_sum(x):
    result = 0
    for step in range(x + 1):
        result += step
    return result


def step(
    position: Tuple[int, int], velocity: Tuple[int, int]
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x, y = position
    vx, vy = velocity
    new_pos = (x + vx, y + vy)
    if vx > 0:
        new_vx = vx - 1
    elif vx < 0:
        new_vx = vx + 1
    else:
        new_vx = 0
    new_vy = vy - 1
    return (new_pos, (new_vx, new_vy))


def simulate(
    velocity: Tuple[int, int], target: Tuple[int, int, int, int]
) -> List[Tuple[int, int]]:
    pos = (0, 0)
    path = [pos]
    while is_undershoot(pos, target):
        pos, velocity = step(pos, velocity)
        if is_overshoot(pos, target):
            return []
        path.append(pos)
    return path


def is_undershoot(pos: Tuple[int, int], target: Tuple[int, int, int, int]) -> bool:
    x, y = pos
    x1, _, y1, _ = target
    return x < x1 or y > y1


def is_overshoot(pos: Tuple[int, int], target: Tuple[int, int, int, int]) -> bool:
    x, y = pos
    _, x2, _, y2 = target
    return x > x2 or y < y2


def get_max_y(paths):
    m = 0
    for path in paths:
        for _, y in path:
            if y > m:
                m = y
    return m


def find_paths(data):
    x1, x2, y2, y1 = data
    paths = []

    for vx in range(x2 + 1):
        for vy in range(-(abs(y2)), abs(y2) + 1):
            path = simulate((vx, vy), (x1, x2, y1, y2))

            if len(path) > 1:
                paths.append(path)

    return paths


def count_part1(data):
    return get_max_y(find_paths(data))


def count_part2(data):
    return len(find_paths(data))


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
