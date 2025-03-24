def isValidSudoku(board) -> bool:
    rows = {}
    cols = {}
    sqrs = {}

    for r in range(len(board)):
        rows[r] = set()
        for c in range(len(board)):
            if board[r][c] == ".":
                continue
            elif board[r][c] in rows[r]:
                return False
            rows[r].add(board[r][c])

    for c in range(len(board)):
        cols[c] = set() 
        for r in range(len(board)):
            if board[c][r] == ".":
                continue
            elif board[c][r] in cols[c]:
                return False
            cols[c].add(board[r][c])
    
    for sqr in range(len(board)):
        sqrs[sqr] = set()
        for r in range(3):
            for c in range(3):
                row = r * 3 * (sqr//3)
                col = c * 3 * (sqr % 3)
                if board[row][col] == ".":
                    continue
                elif board[row][col] in sqrs[sqr]:
                    return False
                sqrs[sqr].add(board[row][col])

    return True

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))