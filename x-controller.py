# Work in Progress

import random
import time
grid = []


def board(len, wid, xCoords, exitCoords):
    for i in range(len):
        grid.append([])
        for _ in range(wid):
            grid[i].append('O')

    grid[xCoords[0]][xCoords[1]] = 'X'
    grid[exitCoords[0]][exitCoords[1]] = '[]'
    return grid


def findXLocation(grid, len, wid):
    for j in range(len):
        for i in range(wid):
            if grid[i][j] == 'X':
                return i, j


def findExitLocation(grid, len, wid):
    for j in range(len):
        for i in range(wid):
            if grid[i][j] == '[]':
                return i, j


def searchReplace(direction, len, wid):
    xLocation = findXLocation(grid, len, wid)
    if xLocation is not None:
        xRow, xColumn = xLocation
        eRow, eColumn = findExitLocation(grid, len, wid)
        grid[xRow][xColumn] = 'O'
        grid[eRow][eColumn] = '[]'
        if direction == 'w':
            grid[xRow - 1][xColumn] = 'X'
            return grid
        if direction == 'a':
            grid[xRow][xColumn - 1] = 'X'
            return grid
        if direction == 's':
            grid[xRow + 1][xColumn] = 'X'
            return grid
    if direction == 'd':
        grid[xRow][xColumn + 1] = 'X'
        return grid


def successCheck(grid, len, wid):
    try:
        xRow, xColumn = findXLocation(grid, len, wid)
        eRow, eColumn = findExitLocation(grid, len, wid)
        return grid[xRow][xColumn] == grid[eRow][eColumn]
    except:
        return True


def main(grid, length, wid, xCoords, exitCoords):
    grid = board(length, wid, xCoords, exitCoords)
    # for i in range(3):
    #     for j in range(3):
    #         print(f'{grid[i][j]} ', end = '')
    #     print('\n')
    while True:
        success = successCheck(grid, length, wid)
        if success:
            print("Congrats, you made it!")
            time.sleep(1)
            break
        direction = input(
            "You are the X. Move to the [] to win! Enter W/A/S/D to move a direction: ")
        if len(direction) == 1:
            if direction.lower() == "w":
                grid = searchReplace('w', length, wid)
                for i in range(length):
                    for j in range(wid):
                        print(f'{grid[i][j]} ', end='')
                    print('\n')
            if direction.lower() == "a":
                grid = searchReplace('a', length, wid)
                for i in range(length):
                    for j in range(wid):
                        print(f'{grid[i][j]} ', end='')
                    print('\n')
            if direction.lower() == "s":
                grid = searchReplace('s', length, wid)
                for i in range(length):
                    for j in range(wid):
                        print(f'{grid[i][j]} ', end='')
                    print('\n')
            if direction.lower() == "d":
                grid = searchReplace('d', length, wid)
                for i in range(length):
                    for j in range(wid):
                        print(f'{grid[i][j]} ', end='')
                    print('\n')
        else:
            print('You may only enter one of: W A S D\n')


# Round 1
startGrid = board(3, 3, [0, 0], [2, 2])
for i in range(3):
    for j in range(3):
        print(f'{startGrid[i][j]} ', end='')
    print('\n')

main(startGrid, 3, 3, [0, 0], [2, 2])


# Round 2+
length = random.randint(3, 10)
wid = random.randint(3, 10)
e1 = random.choice(list(range(length)))
e2 = random.choice([x for x in range(length) if x != e1])
x1 = random.choice([x for x in range(length) if x != e1])
x2 = random.choice([x for x in range(length) if x not in [e2, x1]])
print(e1, e2, x1, x2)

newGrid = board(length, wid, [x1, x2], [e1, e2])
for i in range(length):
    for j in range(wid):
        print(f'{newGrid[i][j]} ', end='')
    print('\n')

main(grid, length, wid, [4, 0], [e1, e2])
