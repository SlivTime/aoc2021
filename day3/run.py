from collections import defaultdict


TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
PART1_TEST_ANSWER = 198
PART2_TEST_ANSWER = 230


def _get_data(source):
    for line in source:
        yield line


def get_data():
    with open("input.txt") as f:
        source_data = f.readlines()
    return _get_data(source_data)


def get_test_data():
    return _get_data(TEST_DATA)


def _get_most_common_bits(data):
    bit_counters = defaultdict(int)
    for row in data:
        for idx, bit in enumerate(row):
            match bit:
                case "0":
                    bit_counters[idx] -= 1
                case "1":
                    bit_counters[idx] += 1

    gamma_list = ["1" if val > 0 else "0" for val in bit_counters.values()]
    return "".join(gamma_list)


def invert(bits):
    return "".join("1" if bit == "0" else "0" for bit in bits)


def count_part1(data_generator):
    gamma = _get_most_common_bits(data_generator)
    epsilon = invert(gamma)
    return int("0b" + gamma, 2) * int("0b" + epsilon, 2)


def _get_most_common_bit(s):
    count = 0
    for bit in s:
        # print(bit, count)
        count += 1 if bit == "1" else -1
    return "1" if count >= 0 else "0"


def _get_least_common_bit(s):
    most = _get_most_common_bit(s)
    return "1" if most == "0" else "0"


def _filter_by_common(data, bits, counter_fn):
    local_data = data.copy()
    for idx, bit in enumerate(bits):
        # print(local_data)
        col = "".join(row[idx] for row in local_data)
        filter_bit = counter_fn(col)
        # print('filter', filter_bit)
        if len(local_data) == 1:
            return local_data[0]
        local_data = [value for value in local_data if value[idx] == filter_bit]
    return local_data[0]


def count_part2(data_generator):
    data = [line for line in data_generator]
    most_common = _get_most_common_bits(data)
    least_common = invert(most_common)

    oxy = _filter_by_common(data, most_common, _get_most_common_bit)
    co2 = _filter_by_common(data, least_common, _get_least_common_bit)

    return int("0b" + oxy, 2) * int("0b" + co2, 2)


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
