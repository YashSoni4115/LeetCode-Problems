class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def checkCells():
            for r in range(3):
                for c in range(3):
                    cell = set()
                    for cr in range(3):
                        for cc in range(3):
                            if not board[r*3+cr][c*3+cc].isdigit(): 
                                continue
                            digit = board[r*3+cr][c*3+cc]
                            if digit in cell: return False
                            cell.add(digit)
            return True
        
        def checkRows():
            for row in board:
                row_set = set()
                for digit in row:
                    if not digit.isdigit():
                        continue
                    if digit in row_set: 
                        return False
                    row_set.add(digit)
            return True

        def checkCols():
            for coli in range(9):
                col_set = set()
                for digiti in range(9):
                    digit = board[digiti][coli]
                    if not digit.isdigit():
                        continue
                    if digit in col_set:
                        return False
                    col_set.add(digit)
            return True

        return checkCells() and checkRows() and checkCols()