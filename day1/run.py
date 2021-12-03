TEST_DATA = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def get_data():
    # return TEST_DATA
    with open("input.txt") as f:
        data = [int(x) for x in f]
    return data


def count_increasing(data):
    cnt = 0
    for cur, nxt in zip(data, data[1:]):
        if nxt > cur:
            cnt += 1
    return cnt


def get_window_sum(data, start, end):
    if end > len(data):
        return -1
    return sum(data[start:end])


def count_increasing_window(data, window_size=3):
    cur = float("inf")
    cnt = 0
    for i in range(len(data)):
        nxt = get_window_sum(data, i, i + window_size)
        # print(cur, nxt)
        if nxt > cur:
            cnt += 1
        cur = nxt
    return cnt


if __name__ == "__main__":
    input_data = get_data()
    print(f"Part 1: {count_increasing(input_data)}")
    print(f"Part 1: {count_increasing_window(input_data)}")
