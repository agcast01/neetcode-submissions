class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        squares = {}
        
        for i in range(len(board)):
            row = i
            for j in range(len(board[i])):
                column = j
                square = math.floor(i / 3) * 3 + math.floor(j / 3)
                val = board[i][j]
                if val in '123456789':
                    rowsSet = rows.get(row, False)
                    columnSet = columns.get(column, False)
                    squareSet = squares.get(square, False)        
                    if rowsSet == False:
                        rows[row] = {val}
                    else:
                        if val in rowsSet:
                            return False
                        else:
                            rows[row].add(val)
                    if columnSet == False:
                        columns[column] = {val}
                    else:
                        if val in columnSet:
                            return False
                        else:
                            columnSet.add(val)
                    if squareSet == False:
                        squares[square] = {val}
                    else:
                        if val in squareSet:
                            return False
                        else:
                            squareSet.add(val)
        return True