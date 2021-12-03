TEST_DATA = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]

def _get_data(source):
    for line in source:
        direction, n = line.split()
        yield direction, int(n)

def get_data():
    with open("input.txt") as f:
        source_data = f.readlines()
    return _get_data(source_data)

def get_test_data():
    return _get_data(TEST_DATA)


def count_part1(data_generator):
    x = 0
    y = 0
    for direction, n in data_generator:
        match direction:
            case "forward":
                x += n
            case "down":
                y += n
            case "up":
                y -= n
    return x * y

def count_part2(data_generator):
    x = 0
    y = 0
    aim = 0
    for direction, n in data_generator:
        match direction:
            case "down":
                aim += n
            case "up":
                aim -= n
            case "forward":
                x += n
                y += aim * n
    return x * y
    
if __name__ == '__main__':
    assert(count_part1(get_test_data()) == 150)
    assert(count_part2(get_test_data()) == 900)
    print(count_part1(get_data()))
    print(count_part2(get_data()))