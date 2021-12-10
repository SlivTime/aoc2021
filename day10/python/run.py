from typing import List, Tuple


PART1_TEST_ANSWER = 26397
PART2_TEST_ANSWER = 288957


def _parse_line(s):
    return s.strip()


def _get_data(filename):
    with open(filename) as f:
        return [_parse_line(line) for line in f]


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


OPEN = ("(", "[", "{", "<")
CLOSE = (")", "]", "}", ">")
MAPPING = dict(zip(OPEN, CLOSE))


def validate(s: str) -> Tuple[str, List[str]]:
    stack = []
    for ch in s:
        if ch in OPEN:
            stack.append(ch)
        else:
            if stack:
                last = stack.pop()
                if ch != MAPPING[last]:
                    return ch, stack
            else:
                return ch, stack
    return None, stack


def count_part1(data):
    SCORES = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in data:
        invalid, _ = validate(line)
        if invalid is not None:
            score += SCORES[invalid]
    return score


def count_part2(data):
    SCORES = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for line in data:
        score = 0
        invalid, stack = validate(line)
        if invalid is None and stack:
            completion = [MAPPING[ch] for ch in stack[::-1]]
            for ch in completion:
                score = score * 5 + SCORES[ch]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
