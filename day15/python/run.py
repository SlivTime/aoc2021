from typing import Any, List, Tuple, Dict, Set, Callable
from pprint import pprint
import heapq

PART1_TEST_ANSWER = 40
PART2_TEST_ANSWER = 315

INF = float("inf")


def _parse_line(s):
    return [int(x) for x in s.strip()]


def _get_data(filename):
    with open(filename) as f:
        field = []
        for line in f:
            field.append(_parse_line(line))

        return field


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def get_orto_neighbors(
    data: List[List[int]], point: Tuple[int, int]
) -> List[Tuple[int, int]]:
    diffs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    i, j = point
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


def inc(number, n):
    while n > 0:
        number += 1
        if number > 9:
            number = 1
        n -= 1
    return number


def multiply_inc(data, n):
    h = len(data)
    w = len(data[0])
    result = []
    new_height = h * n
    new_width = w * n
    for i in range(new_height):
        y = i % h
        y_coef = i // h
        row = []
        for j in range(new_width):
            x = j % w
            x_coef = j // w
            increment = x_coef + y_coef
            val = data[y][x]
            row.append(inc(val, increment))
        result.append(row)

    return result


def count_part1(data):
    start = (0, 0)
    size = len(data) * len(data[0])
    end = (len(data) - 1, len(data[0]) - 1)
    distances = {
        # coord, dist_from_zero
        start: 0,
    }
    seen = set()
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        _, p = heapq.heappop(queue)
        if p in seen:
            continue
        dist_from_start = distances[p]
        neighbors = get_orto_neighbors(data, p)
        for n in neighbors:
            n_dist = distances.get(n, INF)
            n_weight = data[n[0]][n[1]]
            if dist_from_start + n_weight < n_dist:
                distances[n] = dist_from_start + n_weight
            if n not in seen:
                heapq.heappush(queue, (distances[n], n))
        seen.add(p)
    return distances[end]


def count_part2(data):
    large_field = multiply_inc(data, 5)
    return count_part1(large_field)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
