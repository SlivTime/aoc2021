from collections import Counter, defaultdict
from typing import Any, List, Tuple, Dict, Set, Callable


PART1_TEST_ANSWER = 1588
PART2_TEST_ANSWER = 2188189693529


def _parse_line(s):
    k, v = s.strip().split(" -> ")
    return k, v


def _get_data(filename):
    with open(filename) as f:
        template = f.readline().strip()
        next(f)
        rules = {}
        for line in f:
            k, v = _parse_line(line)
            rules[k] = v

        return template, rules


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def run_fast_step(state, rules):
    new_pairs = defaultdict(int)
    pairs = state["pairs"]
    counter = state["counter"]
    for k, v in pairs.items():
        a, b = k
        new_char = rules[k]
        counter.update({new_char: v})
        new_pairs[a + new_char] += v
        new_pairs[new_char + b] += v
    return {
        "pairs": new_pairs,
        "counter": counter,
    }


def to_map(template: str) -> Dict[str, int]:
    mapping = defaultdict(int)
    for idx, ch in enumerate(template[:-1]):
        next_ch = template[idx + 1]
        key = ch + next_ch
        mapping[key] += 1
    return mapping


def create_state(template: str) -> Dict[str, Any]:
    return {"pairs": to_map(template), "counter": Counter(template)}


def simulate(template: str, rules: Dict[str, str], steps: int) -> Dict[str, int]:
    state = create_state(template)
    for _ in range(steps):
        state = run_fast_step(state, rules)
    return state


def _count(data, steps):
    template, rules = data
    state = simulate(template, rules, steps)
    values = state["counter"].values()
    return max(values) - min(values)


def count_part1(data):
    steps = 10
    return _count(data, steps)


def count_part2(data):
    steps = 40
    return _count(data, steps)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
