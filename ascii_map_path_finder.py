import argparse
import re

from constants import (
    regex_lookup,
    start_symbol,
    end_symbol,
    intersection_symbol,
    up,
    right,
    down,
    left,
)
parser = argparse.ArgumentParser(description='Find travel path in arbitrary ASCII map.')
parser.add_argument('ascii_maps', type=str, nargs='+', help='a path to an ASCII map text file')


def parse_map(ascii_map_path):
    with open(ascii_map_path, 'r') as ascii_map:
        lines = ascii_map.readlines()

        if len(lines) < 1:
            raise ValueError('File is empty')
        return create_map(lines)


def create_map(lines):
    ascii_map = []

    for line in lines:
        map_row = []
        [map_row.append(parse_char(char)) for char in line if char != '\n']
        ascii_map.append(map_row)
    return ascii_map


def parse_char(char):
    match = re.search(regex_lookup, char)
    return match.string if match else None


def validate_map(ascii_map):
    verify_char_count(ascii_map, start_symbol, 1)
    verify_char_count(ascii_map, end_symbol, 1)


def verify_char_count(ascii_map, char, count):
    if len([True for row in ascii_map if row.count(char) == count]) != count:
        raise ValueError('Unexpected number of "{}" found'.format(char))


def travel_map(ascii_map):
    x, y = find_beginning(ascii_map)
    letters = {}
    travel_path = []
    orientation = None

    while True:
        symbol = ascii_map[x][y]
        update_letters(symbol, letters, x, y)
        travel_path.append(symbol)

        if symbol == end_symbol:
            break
        x, y, orientation = find_next_symbol(ascii_map, x, y, orientation)

    return letters, travel_path


def find_beginning(ascii_map):
    for x, column in enumerate(ascii_map):
        for y, row in enumerate(column):
            if row and start_symbol in row:
                return x, y


def update_letters(symbol, letters, x, y):
    match = re.search(r'^[A-Z]$', symbol)
    if match:
        letters.update({
            '{}{}'.format(x, y): symbol,
        })
    return letters


def find_next_symbol(ascii_map, x, y, orientation):
    if ascii_map[x][y] in [start_symbol, intersection_symbol]:
        return find_direction(ascii_map, x, y, orientation)

    try:
        new_x, new_y, new_orientation = follow_orientation(x, y, orientation)
        if ascii_map[new_x][new_y]:
            return new_x, new_y, new_orientation
    except IndexError:
        pass
    return find_direction(ascii_map, x, y, orientation)


def find_direction(ascii_map, x, y, orientation):
    x_spread = [x]
    if x > 0 and orientation != down:
        x_spread.append(x - 1)
    if orientation != up:
        x_spread.append(x + 1)

    y_spread = [y]
    if y > 0 and orientation != right:
        y_spread.append(y - 1)
    if orientation != left:
        y_spread.append(y + 1)

    coordinates = [(a, b) for a in x_spread for b in y_spread]
    coordinates.remove((x, y))

    for new_x, new_y in coordinates:
        try:
            if ascii_map[new_x][new_y]:
                return find_orientation(x, y, new_x, new_y)
        except IndexError:
            pass


def follow_orientation(x, y, orientation):
    x = x + 1 if orientation == down else x
    x = x - 1 if orientation == up else x
    y = y + 1 if orientation == right else y
    y = y - 1 if orientation == left else y
    return x, y, orientation


def find_orientation(x, y, new_x, new_y):
    orientation = None

    if x != new_x:
        orientation = down if x < new_x else up
    if y != new_y:
        orientation = right if y < new_y else left
    return new_x, new_y, orientation


def print_results(letters, travel_path):
    print(''.join(letters.values()))
    print(''.join(travel_path))


def run_path_finder(args):
    for ascii_map_path in args.ascii_maps:
        try:
            ascii_map = parse_map(ascii_map_path)
            validate_map(ascii_map)
            print_results(*travel_map(ascii_map))
        except FileNotFoundError:
            print('File does not exist: {}'.format(ascii_map_path))
        except ValueError as error_message:
            print('{}: {}'.format(error_message, ascii_map_path))


run_path_finder(parser.parse_args())
