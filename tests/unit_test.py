import pytest

from ascii_map_path_finder import (
    parse_map,
    create_map,
    parse_char,
    validate_map,
    verify_char_count,
    travel_map,
    find_beginning,
    update_letters,
    find_next_symbol,
    find_direction,
    follow_orientation,
    find_orientation,
    print_results,
)
from constants import (
    RIGHT,
    DOWN,
)
from tests.constants import (
    BASIC_MAP_PATH,
    EMPTY_MAP_PATH,
    INVALID_MAP_PATH,
    VALID_CHARS,
)


def test_parse_map():
    ascii_map = parse_map(BASIC_MAP_PATH)

    assert type(ascii_map) is list
    assert ascii_map[0][0]

    with pytest.raises(FileNotFoundError):
        parse_map(INVALID_MAP_PATH)

    with pytest.raises(ValueError):
        parse_map(EMPTY_MAP_PATH)


def test_create_map():
    lines = [
        ['@', '-', '|'],
        ['+', 'A', 'x'],
        ['žlj', '+,', ' ', '\n']
    ]
    ascii_map = create_map(lines)

    assert len(ascii_map) == 3
    assert len(ascii_map[0]) == 3
    assert len(ascii_map[2]) == 3

    for char in ascii_map[2]:
        assert not char


@pytest.mark.parametrize('char', VALID_CHARS)
def test_parse_char(char):
    assert parse_char(char) == char
    assert not parse_char(' ')
    assert not parse_char('?')


@pytest.mark.parametrize('map', [['@'], ['@', '@', 'x'], ['@', 'x', 'x']])
def test_raises_validate_map(map):
    with pytest.raises(ValueError):
        validate_map(map)


def test_validate_map():
    validate_map(['@', 'x'])


def test_verify_char_count():
    with pytest.raises(ValueError):
        verify_char_count([['@', '@']], '@', 1)
        verify_char_count([['x'], ['x']], 'x', 1)

    verify_char_count(['?', '?'], '?', 2)
    verify_char_count([['@', 'A', '|'], ['A']], 'A', 2)


def test_travel_map(valid_map):
    letters, travel_path = travel_map(valid_map)

    assert type(letters) == dict
    assert type(travel_path) == list


def test_find_beginning(valid_map):
    x, y = find_beginning(valid_map)

    assert x == 2
    assert y == 0


@pytest.mark.parametrize('char', ['@', 'x', '-', '?', 'č'])
def test_invalid_update_letters(char):
    letters = update_letters(char, {}, 3, 3)
    assert letters == {}


def test_update_letters():
    letters = {}
    letters = update_letters('A', letters, 3, 3)
    assert letters['33'] == 'A'

    letters = update_letters('B', letters, 1, 1)
    letters = update_letters('A', letters, 3, 3)
    assert (len(letters)) == 2

    letters = update_letters('A', letters, 2, 1)
    assert (len(letters)) == 3


def test_find_next_symbol(valid_map):
    x, y, orientation = find_next_symbol(valid_map, 2, 0, None)
    assert x == 2
    assert y == 1
    assert orientation == RIGHT

    x, y, orientation = find_next_symbol(valid_map, x, y, orientation)
    assert y == 2

    x, y, orientation = find_next_symbol(valid_map, x, y, orientation)
    assert x == 3
    assert orientation == DOWN


def test_find_direction(valid_map):
    x, y, orientation = find_direction(valid_map, 0, 5, RIGHT)
    assert orientation == DOWN
    assert valid_map[x][y] == 'C'


def test_follow_orientation():
    x, y, orientation = follow_orientation(0, 5, RIGHT)
    assert x == 0
    assert y == 6
    assert orientation == RIGHT


def test_find_orientation():
    x, y, orientation = find_orientation(0, 5, 0, 6)
    assert x == 0
    assert y == 6
    assert orientation == RIGHT


def test_print_results(capfd):
    print_results(
        {'key': 'A'},
        ['@', 'A', '+'],
    )
    out, _ = capfd.readouterr()
    letters, travel_path, _ = out.split('\n', 2)

    assert letters == 'A'
    assert travel_path == '@A+'
