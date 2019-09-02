def algorithm():
    for row in range(size):
        for col in range(size):
            if board_in_grid[row][col] == empty:
                for num in range(1,size+1):
                    if checkPossibleNum(row, col, num):
                        board_in_grid[row][col] = num
                        displayBoard()
                        if algorithm():
                            return True
                        else:
                            board_in_grid[row][col] = empty
                return False
    return True


def checkRow(row, num):
    for i in range(size):
        if board_in_grid[row][i] == num:
            return False
    return True

def checkCol(col, num):
    for i in range(size):
        if board_in_grid[i][col] == num:
            return False
    return True

def checkGrid(row, col, num):
    r = row - row % 3
    c = col - col % 3
    for i in range(r,r+3):
        for j in range(c,c+3):
            if board_in_grid[i][j] == num:
                return False
    return True


def checkPossibleNum(row, col, num):
    return checkRow(row, num) and checkCol(col, num) and checkGrid(row, col, num)


def solve(board):
    for idx, piece in enumerate(board):
        board_in_grid[int(idx / 9)][int(idx % 9)] = int(piece)
    displayBoard()
    result=""
    if algorithm():
        for row in range(size):
            for col in range(size):
                num = str(board_in_grid[row][col])
                result = result + num
        return result
    else:
        return "Unsolvable"

def displayBoard():
    for row in board_in_grid:
        print(row)
    print("===========================")



empty = 0
size = 9
board_in_grid = [
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
    ]
# solve("105802000090076405200400819019007306762083090000061050007600030430020501600308900")



