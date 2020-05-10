# https://leetcode.com/problems/valid-sudoku/
# https://www.youtube.com/watch?v=0MQqkd2BJYc, https://www.youtube.com/watch?v=i2YKwM9oCcY

from collections import defaultdict


def isValidSudoku(board):
    # why defaultDict: https://www.geeksforgeeks.org/defaultdict-in-python/
    colDict = defaultdict(int)
    rowDict = defaultdict(int)
    squareDict = defaultdict(int)
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue

            # index starts at 0, so we minus 1
            # 1 << 1 => 10
            # 1 << 3 => 1000
            curValue = 1 << int(board[row][col]) - 1

            # divide sudoku square into 9 small squares (left to right, top to bottom)
            curSquareIndex = 3*(row//3) + (col//3)

            # if current value appears in any Dict, this sudoku is invalid
            if curValue & colDict[col] or curValue & rowDict[row] or curValue & squareDict[curSquareIndex]:
                return False

            # add current value into Dicts for next round
            colDict[col] |= curValue
            rowDict[row] |= curValue
            squareDict[curSquareIndex] |= curValue

    return True


print(isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
) == True)

print(isValidSudoku(
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
) == False)

print(isValidSudoku(
    [
        [".", "8", "7", "6", "5", "4", "3", "2", "1"],
        ["2", ".", ".", ".", ".", ".", ".", ".", "."],
        ["3", ".", ".", ".", ".", ".", ".", ".", "."],
        ["4", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        ["6", ".", ".", ".", ".", ".", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
) == True)
