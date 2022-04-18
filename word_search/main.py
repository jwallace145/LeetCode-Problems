from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        if len(suffix) == 0:
            return True

        if (
            row not in range(self.ROWS)
            or col not in range(self.COLS)
            or self.board[row][col] != suffix[0]
        ):
            return False

        ret = False
        self.board[row][col] = "#"
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ret = self.backtrack(row + row_offset, col + col_offset, suffix[1:])
            if ret:
                return True
