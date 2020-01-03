import keyboard
import random
import time
BOARDLENGTH = 9
STARTING_NUMBERS = 3

board = [[0] * 9 for n in range(9)]
solve_board = [[0] * 9 for n in range(9)]

board = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

#board = [[3,4,0,8,2,6,0,7,1],
#           [0,0,8,0,0,0,9,0,0],
#           [7,6,0,0,9,0,0,4,3],
#           [0,8,0,1,0,2,0,3,0],
#           [0,3,0,0,0,0,0,9,0],
#           [0,7,0,9,0,4,0,1,0],
#           [8,2,0,0,4,0,0,5,9],
#           [0,0,7,0,0,0,3,0,0],
#           [4,1,0,3,8,9,0,6,2]]
given = [[False] * 9 for n in range(9)]

def copy_to_solve_board():
    for x in range(0,9):
        for y in range(0,9):
            board[x][y] = solve_board[x][y]

def copy_board():
    for x in range(0,9):
        for y in range(0,9):
            full_board[x][y] = board[x][y]
            solve_board[x][y] = board[x][y]

def generate_full_board():
    try_count = 0
    for x in range(0,9):
        for y in range(0,9):
            while(True):
                if(try_count >= 50):
                    return False
                number = random.randint(1,9)
                try_count = try_count + 1
                if(keyboard.is_pressed('q')):
                    printBoard()
                    print("------------------------------------------------------------------------")
                    break
                print(f"random number is {number} at {x},{y} ------ Try: {try_count}")
                #time.sleep(0.5)
                board[x][y] = number
                if(checkRules(x, y)):
                    try_count = 0
                    break

            if(keyboard.is_pressed('q')):
                break
        if(keyboard.is_pressed('q')):
            break

    printBoard()
    return True

###################################################
def remove_numbers(numbers):
    removed = 0
    while(removed < numbers):
        row = random.randint(0,8)
        col = random.randint(0,8)
        if(not board[row][col] == 0):
            copy_to_solve_board()
            backup = board[row][col]
            board[row][col] = 0
            if(solve(0,0)):
                solve_board[row][col] = 0
                removed = removed + 1
            else:
                board[row][col] = backup
###################################################
def printBoard():
    for x in range(0,9):
        for y in range(0,9):
            print(board[x][y], end =" ")
        print("\n")

def checkRules(a, b):
    iAm = board[a][b]
    count = 0
    for x in range(0,9):
        if(board[x][b] == iAm):
            count = count + 1
            if (count >= 2):
                #print("error!")
                return False

    count = 0
    for y in range(0,9):
        if(board[a][y] == iAm):
            count = count + 1
            if (count >= 2):
                #print("error!")
                return False

    if(a == 0 or a == 3 or a == 6 ):
        if(b == 0 or b == 3 or b == 6):
            if(board[a + 1][b] == iAm or board[a + 2][b] == iAm):
                return False
            if(board[a + 1][b+1] == iAm or board[a + 2][b+1] == iAm or board[a][b+1] == iAm):
                return False
            if(board[a + 1][b+2] == iAm or board[a + 2][b+2] == iAm or board[a][b+2] == iAm):
                return False
        if(b == 1 or b == 4 or b == 7):
            if(board[a + 1][b] == iAm or board[a + 2][b] == iAm):
                return False
            if(board[a + 1][b-1] == iAm or board[a + 2][b-1] == iAm or board[a][b-1] == iAm):
                return False
            if(board[a + 1][b+1] == iAm or board[a + 2][b+1] == iAm or board[a][b+1] == iAm):
                return False
        if(b == 2 or b == 5 or b == 8):
            if(board[a + 1][b] == iAm or board[a + 2][b] == iAm):
                return False
            if(board[a + 1][b-2] == iAm or board[a + 2][b-2] == iAm or board[a][b-2] == iAm):
                return False
            if(board[a + 1][b-1] == iAm or board[a + 2][b-1] == iAm or board[a][b-1] == iAm):
                return False
    if(a == 1 or a == 4 or a == 7 ):
        if(b == 0 or b == 3 or b == 6):
            if(board[a + 1][b] == iAm or board[a - 1][b] == iAm):
                return False
            if(board[a + 1][b+1] == iAm or board[a - 1][b+1] == iAm or board[a][b+1] == iAm):
                return False
            if(board[a + 1][b+2] == iAm or board[a - 1][b+2] == iAm or board[a][b+2] == iAm):
                return False
        if(b == 1 or b == 4 or b == 7):
            if(board[a + 1][b] == iAm or board[a - 1][b] == iAm):
                return False
            if(board[a + 1][b-1] == iAm or board[a - 1][b-1] == iAm or board[a][b-1] == iAm):
                return False
            if(board[a + 1][b+1] == iAm or board[a - 1][b+1] == iAm or board[a][b+1] == iAm):
                return False
        if(b == 2 or b == 5 or b == 8):
            if(board[a + 1][b] == iAm or board[a - 1][b] == iAm):
                return False
            if(board[a + 1][b-2] == iAm or board[a - 1][b-2] == iAm or board[a][b-2] == iAm):
                return False
            if(board[a + 1][b-1] == iAm or board[a - 1][b-1] == iAm or board[a][b-1] == iAm):
                return False
    if(a == 2 or a == 5 or a == 8 ):
        if(b == 0 or b == 3 or b == 6):
            if(board[a - 1][b] == iAm or board[a - 2][b] == iAm):
                return False
            if(board[a - 1][b+1] == iAm or board[a - 2][b+1] == iAm or board[a][b+1] == iAm):
                return False
            if(board[a - 1][b+2] == iAm or board[a - 2][b+2] == iAm or board[a][b+2] == iAm):
                return False
        if(b == 1 or b == 4 or b == 7):
            if(board[a - 1][b] == iAm or board[a - 2][b] == iAm):
                return False
            if(board[a - 1][b-1] == iAm or board[a - 2][b-1] == iAm or board[a][b-1] == iAm):
                return False
            if(board[a - 1][b+1] == iAm or board[a - 2][b+1] == iAm or board[a][b+1] == iAm):
                return False
        if(b == 2 or b == 5 or b == 8):
            if(board[a - 2][b] == iAm or board[a - 1][b] == iAm):
                return False
            if(board[a - 2][b-2] == iAm or board[a - 1][b-2] == iAm or board[a][b-2] == iAm):
                return False
            if(board[a - 2][b-1] == iAm or board[a - 1][b-1] == iAm or board[a][b-1] == iAm):
                return False
    return True

def solve(a, b):
    #next number
    #check if correct
    #else higher
    #if no number possible last changed number one higher
    xIdx = a
    yIdx = b
    ruleBreak = False
    while(xIdx < 9 and yIdx < 9):
        if(not given[xIdx][yIdx]):
            # do while in python
            while(True):
                board[xIdx][yIdx] = board[xIdx][yIdx] + 1;
                print(f"Koordinates are {xIdx} {yIdx}, tried value is {board[xIdx][yIdx]}")
                if(board[xIdx][yIdx] == 10):
                    board[xIdx][yIdx] = 0
                    if(xIdx > 0):
                        #print("go one back x")
                        xIdx = xIdx - 1
                        if(xIdx < 0):
                            return False
                        while(given[xIdx][yIdx]):
                            if(not xIdx == 0):
                                xIdx = xIdx - 1
                            elif(not yIdx == 0):
                                xIdx = 8
                                yIdx = yIdx - 1
                            if(xIdx < 0 or yIdx < 0):
                                return False
                        break
                    else:
                        #print("go one back y")
                        xIdx = 8
                        yIdx = yIdx-1
                        if(xIdx < 0 or yIdx < 0):
                            return False
                        while(given[xIdx][yIdx]):
                            if(not xIdx == 0):
                                xIdx = xIdx - 1
                            elif(not yIdx == 0):
                                xIdx = 8
                                yIdx = yIdx - 1
                            if(xIdx < 0 or yIdx < 0):
                                return False
                        break
                if(checkRules(xIdx,yIdx)):
                    ruleBreak = True
                    break
        if(ruleBreak):
            if(xIdx < 8):
                xIdx = xIdx + 1
            else:
                xIdx = 0
                yIdx = yIdx + 1
            ruleBreak = False
        if(given[xIdx][yIdx]):
            if(xIdx < 8):
                xIdx = xIdx + 1
            else:
                xIdx = 0
                yIdx = yIdx + 1

    return True
def main():
    #generate_full_board()
    for x in range(0,9):
        for y in range(0,9):
            print(board[x][y], end =" ")
            if(board[x][y] != 0):
                given[x][y] = True
            else:
                given[x][y] = False
        print("\n")

    solve(0,0)

    print("\n\n--------------------------------------------------------------------------------\n\n")

    for x in range(0,9):
        for y in range(0,9):
            print(board[x][y], end =" ")
        print("\n")

if __name__ == "__main__":
    main()
    # need_to_generate = True
    # while(need_to_generate):
    #     board = [[0] * 9 for n in range(9)]
    #     need_to_generate = not generate_full_board()
    # full_board = [[0] * 9 for n in range(9)]
    # copy_board()
    # remove_numbers(3)
