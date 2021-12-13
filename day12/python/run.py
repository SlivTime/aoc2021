from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Set, Callable


PART1_TEST_ANSWER = 10
PART2_TEST_ANSWER = 36


def _parse_line(s):
    return s.strip().split('-')


def _get_data(filename):
    with open(filename) as f:
        paths = defaultdict(list)
        for line in f:
            start, end = _parse_line(line)
            paths[start].append(end)
            paths[end].append(start)
        return paths


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def can_visit_once(paths: Dict[str, str], next_node: str, visited: List[str]):
    visited_set = set(visited)
    return next_node.isupper() or next_node not in visited_set

def can_visit_twice(paths: Dict[str, str], next_node: str, visited: List[str]):
    visit_counter = Counter(visited)
    if next_node == 'start':
        return False
    small_caves = [x for x in visit_counter if x.islower()]
    allowed_visits = 2
    for cave in small_caves:
        if visit_counter[cave] == 2:
            allowed_visits = 1
            break
    return next_node.isupper() or visit_counter[next_node] < allowed_visits


def go_travel(paths: Dict[str, str], current_path: List[str], can_visit: Callable[str, List[str]]) -> int:
    current_node = current_path[-1]
    if current_node == 'end':
        return 1
    result = 0
    for nxt in paths[current_node]:
        if can_visit(paths, nxt, current_path):
            result += go_travel(paths, current_path + [nxt], can_visit)
    return result



def count_part1(data):
    return go_travel(data, ['start'], can_visit_once)


def count_part2(data):
    r = go_travel(data, ['start'], can_visit_twice)
    return r


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
