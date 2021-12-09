from typing import List, Tuple


PART1_TEST_ANSWER = 15
PART2_TEST_ANSWER = 1134


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


def get_neighbor_coordinates(data: List[List[int]], i: int, j: int):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < len(data) - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < len(data[0]) - 1:
        neighbors.append((i, j + 1))
    return neighbors


def get_neighbors(data: List[List[int]], i: int, j: int):
    return [
        get_neighbor(data, *coords) for coords in get_neighbor_coordinates(data, i, j)
    ]


def is_basin_border(data: List[List[int]], i: int, j: int):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]) or data[i][j] == 9:
        return True
    return False


def get_basin_neighbors(data: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    ns_coords = get_neighbor_coordinates(data, i, j)
    return [n for n in ns_coords if not is_basin_border(data, *n)]


def is_lowest(data: List[List[int]], i: int, j: int):
    item = data[i][j]
    neighbors = get_neighbors(data, i, j)
    return item < min(neighbors)


def fill_basin(data: List[List[int]], visited: set[Tuple[int, int]], i: int, j: int):
    basin = set()
    current_ns = {(i, j)}
    while current_ns:
        next_ns = set()
        for point in current_ns:
            visited.add(point)
            basin.add(point)
            for n in get_basin_neighbors(data, *point):
                if n not in visited:
                    next_ns.add(n)
        current_ns = next_ns

    return basin


def count_part1(data):
    lowest = []
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if is_lowest(data, i, j):
                lowest.append(char)
    return sum([x + 1 for x in lowest])


def count_part2(data):
    visited = set()
    lengths = []

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            point = (i, j)
            if point not in visited:
                if char == 9:
                    visited.add(point)
                else:
                    basin = fill_basin(data, visited, i, j)
                    lengths.append(len(basin))

    top3_lengths = sorted(lengths, reverse=True)[:3]
    result = 1
    for l in top3_lengths:
        result *= l
    return result


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
