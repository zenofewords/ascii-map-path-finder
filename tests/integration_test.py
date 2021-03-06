import pytest

from ascii_map_path_finder import run_path_finder
from tests.constants import (
    VALID_DATA_ASCII_MAPS,
    INVALID_DATA_ASCII_MAPS,
    INVALID_ASCII_MAPS,
)


@pytest.mark.parametrize('ascii_map_data', VALID_DATA_ASCII_MAPS)
def test_path_finder_valid_data_map(ascii_map_data, capfd):
    """Output letters and full travel path for valid ASCII maps."""
    run_path_finder(ascii_map_data['file_path'])

    out, _ = capfd.readouterr()
    letters, travel_path, _ = out.split('\n', 2)

    assert letters == ascii_map_data['letters']
    assert travel_path == ascii_map_data['travel_path']


@pytest.mark.parametrize('ascii_map_data', INVALID_DATA_ASCII_MAPS)
def test_path_finder_invalid_data_map(ascii_map_data, capfd):
    """Return an error when an invalid ASCII map is passed."""
    map_path = ascii_map_data['file_path']
    run_path_finder(map_path)

    out, _ = capfd.readouterr()
    assert out.strip() == '{}: {}'.format(ascii_map_data['error'], map_path)


@pytest.mark.parametrize('ascii_map_data', INVALID_ASCII_MAPS)
def test_path_finder_invalid_map(ascii_map_data, capfd):
    """Return an error if the passed path is wrong."""
    map_path = ascii_map_data['file_path']
    run_path_finder(map_path)

    out, _ = capfd.readouterr()
    assert out.strip() == '{}: {}'.format(ascii_map_data['error'], map_path)
