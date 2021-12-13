from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Set, Callable
from pprint import pprint


PART1_TEST_ANSWER = 17
PART2_TEST_ANSWER = '#####\n#   #\n#   #\n#   #\n#####\n     \n     \n'


def _parse_dot(s):
    x, y = s.strip().split(",")
    return int(x), int(y)


def _parse_fold(s):
    value = s.strip().split()[-1]
    xy, coord = value.split("=")
    if xy == "x":
        return int(coord), 0
    else:
        return 0, int(coord)


def _get_data(filename):
    with open(filename) as f:
        paper = []
        folds = []
        for line in f:
            line = line.strip()
            if not line:
                break
            item = _parse_dot(line)
            paper.append(item)

        for line in f:
            item = _parse_fold(line)
            folds.append(item)

        return paper, folds


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def create_paper(raw_data: List[Tuple[int, int]]) -> List[List[int]]:
    size_x = 0
    size_y = 0
    for x, y in raw_data:
        size_x = max(size_x, x)
        size_y = max(size_y, y)

    field = []
    for _ in range(size_y + 1):
        field.append([0 for _ in range(size_x + 1)])

    for y, x in raw_data:
        field[x][y] = 1

    return field


def sum_ones(paper):
    return sum([sum(row) for row in paper])


def fold_vert(paper, fold_row):
    new_paper = paper[:fold_row]
    folded = paper[fold_row + 1 :]

    paper_cursor = len(new_paper) - 1
    folded_cursor = 0
    while paper_cursor >= 0:
        if folded_cursor >= len(folded):
            break
        paper_row = new_paper[paper_cursor]
        folded_row = folded[folded_cursor]
        for idx, val in enumerate(paper_row):
            paper_row[idx] = val or folded_row[idx]

        paper_cursor -= 1
        folded_cursor += 1

    return new_paper


def fold_hor(paper, fold_col):
    new_paper = []
    for row in paper:
        new_row = row[:fold_col]
        folded_row = row[fold_col + 1 :]
        for folded_idx, val in enumerate(folded_row):
            new_idx = fold_col - folded_idx - 1
            if new_idx >= 0:
                new_val = val or new_row[new_idx]
                new_row[new_idx] = new_val
        new_paper.append(new_row)
    return new_paper


def count_part1(data):
    dots, folds = data
    paper = create_paper(dots)
    folds = folds[:1]

    for x, y in folds:
        if x:
            paper = fold_hor(paper, x)
        elif y:
            paper = fold_vert(paper, y)
    return sum_ones(paper)


def count_part2(data):
    dots, folds = data
    paper = create_paper(dots)

    for x, y in folds:
        if x:
            paper = fold_hor(paper, x)
        elif y:
            paper = fold_vert(paper, y)
    word = ""
    for row in paper:
        for _, item in enumerate(row):
            ch = "#" if item else " "
            word += ch
        word += "\n"
    return word


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
