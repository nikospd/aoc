import pytest
from main import MapSimulation


@pytest.fixture()
def ms() -> MapSimulation:
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    input_map = input_raw[:-2]
    return MapSimulation(input_map)


class TestCube(object):
    def test_no2_right(self, ms):
        ms.cur_position = (0, 149)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 2
        assert next_position == (149, 99)
        ms.cur_position = (49, 149)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 2
        assert next_position == (100, 99)

    def test_no3_right(self, ms):
        ms.cur_position = (50, 99)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 3
        assert next_position == (49, 100)
        ms.cur_position = (99, 99)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 3
        assert next_position == (49, 149)

    def test_no5_right(self, ms):
        ms.cur_position = (100, 99)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 2
        assert next_position == (49, 149)
        ms.cur_position = (149, 99)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 2
        assert next_position == (0, 149)

    def test_no6_right(self, ms):
        ms.cur_position = (150, 49)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 3
        assert next_position == (149, 50)
        ms.cur_position = (199, 49)
        ms.direction = 0
        next_position, next_direction = ms.find_next_position()
        assert next_direction == 3
        assert next_position == (149, 99)
