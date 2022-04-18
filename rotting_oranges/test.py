from rotting_oranges.main import RottingOranges
import pytest


class TestRottingOranges:
    @pytest.fixture(autouse=True)
    def init_test_rotting_oranges(self):
        self.rotting_oranges = RottingOranges()

    def test_find_rotten_oranges_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        rotten_oranges = self.rotting_oranges.find_rotten_oranges(grid)
        assert len(rotten_oranges) == 1
        assert rotten_oranges[0] == [0, 0]

    def test_find_rotten_oranges_2(self):
        grid = [[2, 2, 1], [2, 1, 0], [0, 1, 1]]
        rotten_oranges = self.rotting_oranges.find_rotten_oranges(grid)
        assert len(rotten_oranges) == 3
        assert [0, 0] in rotten_oranges
        assert [1, 0] in rotten_oranges
        assert [0, 1] in rotten_oranges

    def test_rotten_orange_if_possible_up(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        rotten_orange = [0, 0]
        direction = [-1, 0]
        coordinates = self.rotting_oranges.rotten_orange_if_possible(
            grid, rotten_orange, direction
        )
        assert coordinates is None

    def test_rotten_orange_if_possible_right(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        rotten_orange = [0, 0]
        direction = [0, 1]
        coordinates = self.rotting_oranges.rotten_orange_if_possible(
            grid, rotten_orange, direction
        )
        assert coordinates == [0, 1]

    def test_rotten_orange_if_possible_down(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        rotten_orange = [0, 0]
        direction = [1, 0]
        coordinates = self.rotting_oranges.rotten_orange_if_possible(
            grid, rotten_orange, direction
        )
        assert coordinates == [1, 0]

    def test_rotten_adjacent_oranges(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        rotten_oranges = [[0, 0]]
        new_rotten_oranges = self.rotting_oranges.rotten_adjacent_oranges(
            grid, rotten_oranges
        )
        assert len(new_rotten_oranges) == 2
        assert [1, 0] in new_rotten_oranges
        assert [0, 1] in new_rotten_oranges

    def test_check_for_fresh_oranges(self):
        grid = [[2, 2, 2], [0, 2, 2], [1, 0, 2]]
        assert self.rotting_oranges.check_fresh_oranges(grid) == True

    def test_minutes_until_all_rotten_oranges(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        assert self.rotting_oranges.minutes_until_all_rotten_oranges(grid) == 4
