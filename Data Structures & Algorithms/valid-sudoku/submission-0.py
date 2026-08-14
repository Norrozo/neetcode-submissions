class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #look through all 81
        #store values based on row / column / 3x3
        #if seen before, false
        #else true

        #make hashset / dictionary of all the rows, cols, squares
        seen = set()

        #loop through the 81
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                #empty cells
                if val == ".":
                    continue

                #unique signatures for row, col, box
                row_key = ("row", r, val)
                col_key = ("col", c, val)
                box_key = (r // 3, c // 3, val)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True

