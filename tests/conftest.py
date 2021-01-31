import pytest

from ascii_map_path_finder import parse_map
from tests.constants import COMPACT_MAP_PATH


@pytest.fixture
def valid_map():
    return parse_map(COMPACT_MAP_PATH)
