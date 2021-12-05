from collections import defaultdict


PART1_TEST_ANSWER = 5
PART2_TEST_ANSWER = 12


def _parse_line(s):
    p1, p2 = s.split("->")
    x1, y1 = p1.strip().split(",")
    x2, y2 = p2.strip().split(",")
    return map(int, (x1, y1, x2, y2))


def _get_data(filename):
    with open(filename) as f:
        for line in f:
            yield _parse_line(line)

    return 0


def get_data():
    return _get_data("input.txt")


def get_test_data():
    return _get_data("test_input.txt")


def align(a, b):
    if a > b:
        return b, a
    return a, b


def count_dangerous(field):
    return sum([x > 1 for x in field.values()])


def make_path(x1, y1, x2, y2, allow_diagonal):
    if x1 == x2 or y1 == y2:
        x1, x2 = align(x1, x2)
        y1, y2 = align(y1, y2)
        for xn in range(x1, x2 + 1):
            for yn in range(y1, y2 + 1):
                yield (xn, yn)
    elif allow_diagonal and abs(x1 - x2) == abs(y1 - y2):
        while x1 != x2 and y1 != y2:
            yield (x1, y1)
            x1 += 1 if x1 < x2 else -1
            y1 += 1 if y1 < y2 else -1
        yield (x2, y2)


def _count(data, allow_diagonal):
    field = defaultdict(int)
    for (x1, y1, x2, y2) in data:
        for point in make_path(x1, y1, x2, y2, allow_diagonal):
            field[point] += 1

    return count_dangerous(field)


def count_part1(data):
    return _count(data, allow_diagonal=False)


def count_part2(data):
    return _count(data, allow_diagonal=True)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
