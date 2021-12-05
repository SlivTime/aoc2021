import collections
from pprint import pprint



PART1_TEST_ANSWER = 4512
PART2_TEST_ANSWER = 1924

_TICKET_ROWS = 5

def _parse_ints(s, sep=' '):
    return [int(x) for x in s.strip().split(sep) if x]

def _get_columns(rows):
    cols = [list() for _ in range(len(rows))]
    for row in rows:
        for col_idx, item in enumerate(row):
            cols[col_idx].append(item)

    return cols

def create_ticket(rows):
    cols = _get_columns(rows)
    return {
        'rows': [set(x) for x in rows],
        'cols': [set(x) for x in cols],
    }

def _get_data(filename):
    tickets = []
    with open(filename) as f:
        numbers = _parse_ints(next(f), ',')
        next(f)
        rows = []
        for line in f:
            line = line.strip()
            if line:
                rows.append(
                    _parse_ints(line)
                )
            if len(rows) == _TICKET_ROWS:
                tickets.append(
                    create_ticket(rows)
                )
                rows = []
                
    return numbers, tickets


def get_data():
    return _get_data('input.txt')


def get_test_data():
    return _get_data('test_input.txt')


    
    


def get_ticket_boundaries(current_row_num):
    while current_row_num % _TICKET_ROWS != 0:
        current_row_num -= 1
    return current_row_num, current_row_num + _TICKET_ROWS


def sum_ticket(ticket):
    result = 0
    for row in ticket['rows']:
        result += sum(row)
    return result

def ticket_won(ticket):
    for entity in ticket.values():
        for x in entity:
            if not x:
                return True
    return False

def count_part1(data):
    numbers, tickets = data
    results = {
        # id, sum
    }
    for num in numbers:
        for idx, ticket in enumerate(tickets):
            if idx in results:
                continue
            for entity in ticket.values():
                for s in entity:
                    s.discard(num)
            print(ticket)
            if ticket_won(ticket):
                current_sum = sum_ticket(ticket)
                results[idx] = current_sum
                return num * current_sum
    
    return 0


def count_part2(data):
    numbers, tickets = data
    results = {
        # id, sum
    }
    for num in numbers:
        for idx, ticket in enumerate(tickets):
            if idx in results:
                continue
            for entity in ticket.values():
                for s in entity:
                    s.discard(num)
            # print(ticket)
            if ticket_won(ticket):
                current_sum = sum_ticket(ticket)
                results[idx] = current_sum
                if len(results) == len(tickets):
                    return num * current_sum
    
    return 0


if __name__ == "__main__":
    assert count_part1(get_test_data()) == PART1_TEST_ANSWER
    assert count_part2(get_test_data()) == PART2_TEST_ANSWER
    print(count_part1(get_data()))
    print(count_part2(get_data()))
