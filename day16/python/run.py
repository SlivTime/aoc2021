from typing import List, Tuple
from pprint import pprint

PART1_TEST_ANSWER = 8
PART2_TEST_ANSWER = 54

LITERAL_TYPE_ID = '100'
LITERAL_BIT_LEN = 5


def _get_data(filename):
    with open(filename) as f:
        return f.read().strip()


def get_data():
    return _get_data("../input/input.txt")


def get_test_data():
    return _get_data("../input/test_input.txt")


def to_binary(s):
    result = []
    for ch in s:
        bin_val = bin(int(f'0x{ch}', 16))[2:]
        result.append(
            bin_val.zfill(4)
        )
    return ''.join(result)


def read(stream, n):
    return ''.join([next(stream) for _ in range(n)])


def get_version(stream):
    return read(stream, 3)


def get_type_id(stream):
    return read(stream, 3)


def is_literal(type_id):
    return LITERAL_TYPE_ID == type_id


def read_literal_content(stream) -> Tuple[List[int], int]:
    result = []
    keep_reading = True
    while keep_reading:
        chunk = read(stream, LITERAL_BIT_LEN)
        keep_reading = chunk[0] == '1'
        value = chunk[1:]
        result.append(value)
    length = len(result) * LITERAL_BIT_LEN
    value = ''.join(result)
    return [to_int(value)], length


def to_int(bin_value):
    return int(f'0b{bin_value}', 2)


def create_packet(version, type_id, content):
    return {
        'version': to_int(version),
        'type_id': to_int(type_id),
        'content': content,
    }



def read_subpackets_by_len(stream, should_read):
    result = []
    read_len = 0
    while read_len < should_read:
        subpacket, length = parse(stream)
        result.append(subpacket)
        read_len += length
    return result, read_len


def read_n_subpackets(stream, n):
    result = []
    total_len = 0
    while n > 0:
        subpacket, length = parse(stream)
        total_len += length
        result.append(subpacket)
        n -= 1
    return result, total_len


def read_operator(stream):
    len_type_id = read(stream, 1)
    header_len = 1
    if len_type_id == '0':
        bit_length = read(stream, 15)
        header_len += len(bit_length)
        int_length = int(f'0b{bit_length}', 2)
        content, content_len = read_subpackets_by_len(stream, int_length)
    else:
        bit_length = read(stream, 11)
        header_len += len(bit_length)
        int_length = int(f'0b{bit_length}', 2)
        content, content_len = read_n_subpackets(stream, int_length)

    return content, header_len + content_len


def eval(packet) -> int:
    type_id = packet['type_id']
    value = 0
    content = packet['content']
    if type_id == 0:
        value = sum([eval(child) for child in content])
    elif type_id == 1:
        value = 1
        for child in content:
            value = value * eval(child)
    elif type_id == 2:
        value = min([eval(child) for child in content])
    elif type_id == 3:
        value = max([eval(child) for child in content])
    elif type_id == 4:
        value = content[0]
    elif type_id == 5:
        child1, child2 = content
        value = 1 if eval(child1) > eval(child2) else 0
    elif type_id == 6:
        child1, child2 = content
        value = 1 if eval(child1) < eval(child2) else 0
    elif type_id == 7:
        child1, child2 = content
        value = 1 if eval(child1) == eval(child2) else 0
    return value


def parse(stream):
    version = get_version(stream)
    type_id = get_type_id(stream)
    header_length = len(version) + len(type_id)
    if is_literal(type_id):
        content, content_length = read_literal_content(stream)
    else:
        content, content_length = read_operator(stream)

    packet = create_packet(version, type_id, content)
    return packet, header_length + content_length


def sum_versions(data):
    if isinstance(data, int):
        return 0
    if isinstance(data, dict):
        version = data['version']
        content = data['content']
        return version + sum_versions(content)
    elif isinstance(data, str):
        return 0
    elif isinstance(data, list):
        return sum([sum_versions(node) for node in data])


def count_part1(data):
    bin_data = to_binary(data)
    stream = iter(bin_data)
    root, length = parse(stream)
    result = sum_versions(root)
    return result


def count_part2(data):
    bin_data = to_binary(data)
    stream = iter(bin_data)
    root, length = parse(stream)
    result = eval(root)
    return result


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
