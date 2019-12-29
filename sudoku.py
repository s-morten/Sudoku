import keyboard
BOARDLENGTH = 9
#
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
        if keyboard.is_pressed('q'):
            printBoard()
            break;
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
                        while(given[xIdx][yIdx]):
                            if(not xIdx == 0):
                                xIdx = xIdx - 1
                            elif(not yIdx == 0):
                                xIdx = 8
                                yIdx = yIdx - 1
                        break
                    else:
                        #print("go one back y")
                        xIdx = 8
                        yIdx = yIdx-1
                        while(given[xIdx][yIdx]):
                            if(not xIdx == 0):
                                xIdx = xIdx - 1
                            elif(not yIdx == 0):
                                xIdx = 8
                                yIdx = yIdx - 1
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
