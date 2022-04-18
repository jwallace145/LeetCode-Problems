# Word Search

## Description
Given an `m x n` grid of characters `board` and a string `word`, return `True` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1
Input: `board` = `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word` = `"ABCCED"`

Output: `True`

### Constraints
- `m` = `board.length`
- `n` = `board[i].length`
- 1 <= `m`, `n` <= 6
- 1 <= `word.length` <= 15
- `board` and `word` only consists of lowercase and uppercase English letters
