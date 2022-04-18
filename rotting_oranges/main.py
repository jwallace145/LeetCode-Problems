from typing import List


class RottingOranges:
    def __init__(self) -> None:
        pass

    def find_rotten_oranges(self, grid: List[List[int]]) -> List[List[int]]:
        # travel through matrix and find all the 2's (aka rotten orange)
        rotten_oranges = []
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element == 2:
                    rotten_oranges.append([i, j])
        return rotten_oranges

    def check_fresh_oranges(self, grid: List[List[int]]) -> bool:
        for row in grid:
            for element in row:
                if element == 1:
                    return True
        return False

    def rotten_orange_if_possible(
        self,
        grid: List[List[int]],
        rotten_orange: List[int],
        direction: List[List[int]],
    ):
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])
        candidate_coordinates = [
            rotten_orange[0] + direction[0],
            rotten_orange[1] + direction[1],
        ]
        if candidate_coordinates[0] in range(num_of_rows) and candidate_coordinates[
            1
        ] in range(num_of_cols):
            if grid[candidate_coordinates[0]][candidate_coordinates[1]] == 1:
                grid[candidate_coordinates[0]][candidate_coordinates[1]] = 2
                return candidate_coordinates

    def rotten_adjacent_oranges(
        self, grid: List[List[int]], rotten_oranges: List[List[int]]
    ) -> List[List[int]]:
        new_rotten_oranges = []
        for rotten_orange in rotten_oranges:
            # up, down, left, right
            for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                coordinates = self.rotten_orange_if_possible(
                    grid, rotten_orange, direction
                )
                if coordinates:
                    new_rotten_oranges.append(coordinates)
        return new_rotten_oranges

    def minutes_until_all_rotten_oranges(self, grid: List[List[int]]) -> int:
        # initialize minutes to 0
        minutes = 0

        # find all initially rotten oranges to use as starting points
        rotten_oranges = self.find_rotten_oranges(grid)

        while rotten_oranges:
            rotten_oranges = self.rotten_adjacent_oranges(grid, rotten_oranges)
            if rotten_oranges:
                minutes += 1

        # parity check to make sure all oranges are rotten
        if self.check_fresh_oranges(grid):
            return -1

        return minutes
