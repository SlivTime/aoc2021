from os import read
from typing import List, Tuple
from pprint import pprint


PART1_TEST_ANSWER = 1656
PART2_TEST_ANSWER = 195


def _parse_line(s):
    return [int(x) for x in s if x.isnumeric()]


def _get_data(filename):
    with open(filename) as f:
        return [_parse_line(line) for line in f]


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def get_neighbor(data, i, j):
    row = data[0]
    if i < 0 or j < 0 or i >= len(data) or j >= len(row):
        return None
    return data[i][j]


def get_neighbors(data: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    diffs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    neighbors = []
    for dx, dy in diffs:
        try:
            x = i + dx
            y = j + dy
            if x >= 0 and y >= 0:
                data[x][y]
                neighbors.append((x, y))
        except IndexError:
            pass

    return neighbors


def inc(data, x: int, y: int) -> bool:
    # Return True if ready to flash
    val = data[x][y]
    new_val = val + 1
    data[x][y] = new_val
    return new_val > 9


def cooldown(data, x, y):
    data[x][y] = 0


def flash(data: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    neighbors = get_neighbors(data, x, y)
    ready_to_flash = set()
    for x, y in neighbors:
        if inc(data, x, y):
            ready_to_flash.add((x, y))
    return ready_to_flash


def simulate(data, days):
    flash_counter = 0
    day = 0
    size = len(data) * len(data[0])
    while day < days:
        flashed_this_turn = set()
        ready_to_flash = set()
        # increment all
        for x, row in enumerate(data):
            for y, _ in enumerate(row):
                if inc(data, x, y):
                    ready_to_flash.add((x, y))
        # flash
        while ready_to_flash:
            x, y = ready_to_flash.pop()
            if (x, y) in flashed_this_turn:
                continue
            new_flashes = flash(data, x, y)
            flashed_this_turn.add((x, y))
            flash_counter += 1
            ready_to_flash |= new_flashes

        # cooldown, 9 -> 0
        for x, y in flashed_this_turn:
            cooldown(data, x, y)

        # for part 2
        if size == len(flashed_this_turn):
            return day + 1

        day += 1

    return flash_counter


def count_part1(data):
    return simulate(data, 100)


def count_part2(data):
    return simulate(data, 300)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
