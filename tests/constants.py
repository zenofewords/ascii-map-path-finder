from constants import (
    START_SYMBOL,
    END_SYMBOL,
    CORNER_SYMBOL,
)


BASIC_MAP_PATH = 'ascii_maps/basic_map.txt'
COMPACT_MAP_PATH = 'ascii_maps/compact_map.txt'
INVALID_MAP_PATH = 'ascii_maps/empty_mapaaa.txt'
EMPTY_MAP_PATH = 'ascii_maps/empty_map.txt'
VALID_CHARS = [START_SYMBOL, END_SYMBOL, CORNER_SYMBOL, '|', '-']

VALID_DATA_ASCII_MAPS = [
    {
        'file_path': BASIC_MAP_PATH,
        'letters': 'ACB',
        'travel_path': '@---A---+|C|+---+|+-B-x'
    },
    {
        'file_path': 'ascii_maps/intersection_map.txt',
        'letters': 'ABCD',
        'travel_path': '@|A+---B--+|+--C-+|-||+---D--+|x'
    },
    {
        'file_path': 'ascii_maps/no_duplicate_map.txt',
        'letters': 'ABCD',
        'travel_path': '@--A-+|+-+|A|+--B--+C|+-+|+-C-+|D|x'
    },
    {
        'file_path': 'ascii_maps/letter_on_turn_map.txt',
        'letters': 'ACB',
        'travel_path': '@---A---+|||C---+|+-B-x'
    },
    {
        'file_path': COMPACT_MAP_PATH,
        'letters': 'ABCD',
        'travel_path': '@A+++A|+-B-+C+++C-+Dx'
    },
]

INVALID_DATA_ASCII_MAPS = [
    {
        'file_path': 'ascii_maps/invalid_multiple_ends_map.txt',
        'error': 'Unexpected number of "{}" found'.format(END_SYMBOL),
    },
    {
        'file_path': 'ascii_maps/invalid_multiple_starts_map.txt',
        'error': 'Unexpected number of "{}" found'.format(START_SYMBOL),
    },
    {
        'file_path': 'ascii_maps/invalid_no_end_map.txt',
        'error': 'Unexpected number of "{}" found'.format(END_SYMBOL),
    },
    {
        'file_path': 'ascii_maps/invalid_no_start_map.txt',
        'error': 'Unexpected number of "{}" found'.format(START_SYMBOL),
    },
    {
        'file_path': 'ascii_maps/invalid_t_forks_map.txt',
        'error': 'Unexpected number of "{}" found'.format(END_SYMBOL),
    },
]

INVALID_ASCII_MAPS = [
    {
        'file_path': EMPTY_MAP_PATH,
        'error': 'File is empty',
    },
    {
        'file_path': INVALID_MAP_PATH,
        'error': 'File does not exist',
    },
]
