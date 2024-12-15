import copy

# SYMBOLS:
# X = where the guard already was in the initial run
# . = free tile
# ^, v, <, > = the guard in different orientations
# O = artificially placed obstacle to see if I get a loop
# T = spot which was an O in a previous loop and should now be ignored

def whatOrientation(guard) :
    if guard == "^" :
        return "up"
    elif guard == "v" :
        return "down"
    elif guard == "<" :
        return "left"
    elif guard == ">" :
        return "right"
    else :
        return 0
    
def moveGuard(input, guardDirection, guardColumn, guardRow) :

    movementOK = {".", "X", "T"}

    OOM = False

    # if guard is facing up, move him or turn him 90°
    if guardDirection == "up" :
        if guardRow == 0 :
            OOM = True
            # print("out of map")
        elif input[guardRow-1][guardColumn] == "#" :
            input[guardRow][guardColumn] = ">"
        elif input[guardRow-1][guardColumn] in movementOK :
            input[guardRow][guardColumn] = "X"
            input[guardRow-1][guardColumn] = "^"
        else :
            OOM = True
            # print("out of map")

    # if guard is facing down
    elif guardDirection == "down" :
        if guardRow == len(input)-1 :
            OOM = True
            # print("out of map")
        elif input[guardRow+1][guardColumn] == "#" :
            input[guardRow][guardColumn] = "<"
        elif input[guardRow+1][guardColumn] in movementOK :
            input[guardRow][guardColumn] = "X"
            input[guardRow+1][guardColumn] = "v"
        else :
            OOM = True
            # print("out of map")

    # if guard is facing left
    elif guardDirection == "left" :
        if guardColumn == 0 :
            OOM = True
            # print("out of map")
        elif input[guardRow][guardColumn-1] == "#" :
            input[guardRow][guardColumn] = "^"
        elif input[guardRow][guardColumn-1] in movementOK :
            input[guardRow][guardColumn] = "X"
            input[guardRow][guardColumn-1] = "<"
        else :
            OOM = True
            # print("out of map")
    
    # if guard is facing right
    else :
        if guardColumn == len(input[0])-1 :
            OOM = True
            # print("out of map")
        elif input[guardRow][guardColumn+1] == "#" :
            input[guardRow][guardColumn] = "v"
        elif input[guardRow][guardColumn+1] in movementOK :
            input[guardRow][guardColumn] = "X"
            input[guardRow][guardColumn+1] = ">"
        else :
            OOM = True
            # print("out of map")

    return input, OOM


def findLoop(input, guardDirection, guardColumn, guardRow) :

    input = copy.deepcopy(input)
    movementOK = {".", "X", "T"}
    obstacle = {"#", "O"}
    possibleGuard = {"^", "v", "<", ">"}

    OOM = False
    foundLoop = False

    setUp = set()
    setDown = set()
    setLeft = set()
    setRight = set()

    # for line in input :
    #     print(line)

    while (OOM == False and foundLoop == False) :

        # for line in input :
        #     print(line)
        # print()


        for line in input :
            for char in line :
                if char in possibleGuard :

                    # find out what direction the guard is facing
                    guardDirection = whatOrientation(char)
                    guardColumn = line.index(char)
                    guardRow = input.index(line)

        # if guard is facing up, move him or turn him 90°
        if guardDirection == "up" :
            if guardRow == 0 :
                OOM = True
            elif (guardRow, guardColumn) in setUp :
                foundLoop = True
            elif input[guardRow-1][guardColumn] in obstacle :
                input[guardRow][guardColumn] = ">"
            elif input[guardRow-1][guardColumn] in movementOK :
                setUp.add(tuple([guardRow, guardColumn]))
                input[guardRow][guardColumn] = "X"
                input[guardRow-1][guardColumn] = "^"
            else :
                OOM = True
                # print("out of map")

        # if guard is facing down
        elif guardDirection == "down" :
            if guardRow == len(input)-1 :
                OOM = True
                # print("out of map")
            elif (guardRow, guardColumn) in setDown :
                foundLoop = True
            elif input[guardRow+1][guardColumn] in obstacle :
                input[guardRow][guardColumn] = "<"
            elif input[guardRow+1][guardColumn] in movementOK :
                setDown.add(tuple([guardRow, guardColumn]))
                input[guardRow][guardColumn] = "X"
                input[guardRow+1][guardColumn] = "v"
            else :
                OOM = True
                # print("out of map")

        # if guard is facing left
        elif guardDirection == "left" :
            if guardColumn == 0 :
                OOM = True
                # print("out of map")
            elif (guardRow, guardColumn) in setLeft :
                foundLoop = True
            elif input[guardRow][guardColumn-1] in obstacle :
                input[guardRow][guardColumn] = "^"
            elif input[guardRow][guardColumn-1] in movementOK :
                setLeft.add(tuple([guardRow, guardColumn]))
                input[guardRow][guardColumn] = "X"
                input[guardRow][guardColumn-1] = "<"
            else :
                OOM = True
                # print("out of map")
        
        # if guard is facing right
        else :
            if guardColumn == len(input[0])-1 :
                OOM = True
                # print("out of map")
            elif (guardRow, guardColumn) in setRight :
                foundLoop = True
            elif input[guardRow][guardColumn+1] in obstacle :
                input[guardRow][guardColumn] = "v"
            elif input[guardRow][guardColumn+1] in movementOK :
                setRight.add(tuple([guardRow, guardColumn]))
                input[guardRow][guardColumn] = "X"
                input[guardRow][guardColumn+1] = ">"
            else :
                OOM = True
                # print("out of map")
            

    if OOM == True :
        foundLoop = False

    # print(foundLoop)
    return foundLoop




def part1() :
    path = r"day6input.txt"
    input = open(path, "r")
    input = input.read()
    possibleGuard = {"^", "v", "<", ">"}


    matrix = [list(line) for line in input.strip().split("\n")]

    OOM = False

    # let the guard walk until he is out of map
    while (OOM != True) :

        # find out where the guard is and how he is facing
        for line in matrix :
            for char in line :
                if char in possibleGuard :

                    # find out what direction the guard is facing
                    guardOrientation = whatOrientation(char)
                    guardColumn = line.index(char)
                    guardRow = matrix.index(line)
                    
        # moves the guard one time or turns him 90°            
        input, OOM = moveGuard(matrix, guardOrientation, guardColumn, guardRow)

    # sum up the X and the position where the guard is currently
    sum = 0
    for line in input :
        # print(line)
        for char in line :
            if char == "X" or char in possibleGuard :
                sum += 1

    print(f"The guard visited {sum} distinct positions before leaving the mapped area.")


    
def part2() :
    path = r"day6input.txt"
    input = open(path, "r")
    input = input.read()
    possibleGuard = {"^", "v", "<", ">"}


    matrix = [list(line) for line in input.strip().split("\n")]

    OOM = False

    # find out where the guard is at the start
    for line in matrix :
        for char in line :
            if char in possibleGuard :

                # find out what direction the guard is facing
                starting_guardOrientation = whatOrientation(char)
                starting_guardColumn = line.index(char)
                starting_guardRow = matrix.index(line)

    # let the guard walk until he is out of map
    while (OOM != True) :

        # find out where the guard is and how he is facing
        for line in matrix :
            for char in line :
                if char in possibleGuard :

                    # find out what direction the guard is facing
                    guardOrientation = whatOrientation(char)
                    guardColumn = line.index(char)
                    guardRow = matrix.index(line)
                    
        # moves the guard one time or turns him 90°            
        input, OOM = moveGuard(matrix, guardOrientation, guardColumn, guardRow)

    # sum up the X and the position where the guard is currently
    sum = 0
    for line in input :
        # print(line)
        for char in line :
            if char == "X" or char in possibleGuard :
                sum += 1

    countOfX = sum

    # make it so the end position of the guard is now also an X
    for line in input :
        for char in line :
            if char in possibleGuard :
                index = line.index(char)
                line[index] = "X"

    # make a matrix with the path of the guard and the guard in it
    matrixWithX = copy.deepcopy(input)
    if starting_guardOrientation == "up" :
        matrixWithX[starting_guardRow][starting_guardColumn] = "^"
    elif starting_guardOrientation == "down" :
        matrixWithX[starting_guardRow][starting_guardColumn] = "v"
    elif starting_guardOrientation == "left" :
        matrixWithX[starting_guardRow][starting_guardColumn] = "<"
    else :
        matrixWithX[starting_guardRow][starting_guardColumn] = ">"

    newO = False
    sum = 0
    foundLoop = 0

    # do the loop the same amount of times as there are destinct fields the gaurd walks by, -1 because of the starting position
    for _ in range(countOfX-1) :

        # for line in matrixWithX :
        #     for i in range(len(line)) :
        #         if line[i] in possibleGuard : line[i] = "X"

        # go through every X and make it O
        for line in matrixWithX :

            for i in range(len(line)) :

                # if we already tried the position, call it T for tried, then go on with the next X
                if line[i] == "O" : line[i] = "T"
                if line[i] == "X" :
                    line[i] = "O"
                    newO = True
                    break

            if newO == True :
                break

        # print(starting_guardRow, starting_guardColumn)
        if starting_guardOrientation == "up" :
            matrixWithX[starting_guardRow][starting_guardColumn] = "^"
        foundLoop = findLoop(matrixWithX, starting_guardOrientation, starting_guardColumn, starting_guardRow)
        print(_)
        print(foundLoop)
        print(sum)
        print()
        newO = False
        sum += foundLoop

        # for line in matrixWithX :
        #     print(line)
        # print(sum)
        # print("\n")



    
    # for line in matrixWithX :
    #     print(line)


    print(f"There are {sum} different positions I could choose for a obstruction that makes the guard and up in a loop.")




# part1()
part2()