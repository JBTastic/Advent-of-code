import re

def findXMAS(input) :
    pattern = r"XMAS"
    xmasHorizontal = re.findall(pattern, input)
    pattern = r"SAMX"
    samxHorizontal = re.findall(pattern, input)
    return xmasHorizontal, samxHorizontal


def part1() :
    input = open("day4input.txt", "r")
    input = input.read()
    
    # parses all "xmas" and reversed "samx" out of the input
    xmasHorizontal, samxHorizontal = findXMAS(input)

    # splits the input by lines and puts them in seperate lists
    splittedInput = input.split("\n")
    splittedInputTuple = []
    for line in splittedInput :
        splittedInputTuple.append(line)

    # rotates the list clockwise, now its tuples inside of a list
    rotatedClockwise = list(zip(*splittedInputTuple[::-1]))
    # rotatedCounterClockwise = list(zip(*splittedInputTuple))[::-1]

    # makes it so its lists instead of tuples inside the list
    for i in range(len(rotatedClockwise)) :
        rotatedClockwise[i] = list(rotatedClockwise[i])
    
    # now instead of the letters being in seperate strings, they get concatenated so in each list is a long string
    rotatedClockwiseList = []
    for i in rotatedClockwise :
        j = "".join(i)
        rotatedClockwiseList.append(j)
    
    # the list is converted to a string, seperated by line braks
    rotatedClockwiseString = "\n".join(rotatedClockwiseList)

    # finds the vertical "xmas" and reversed "samx"
    samxVertical, xmasVertical = findXMAS(rotatedClockwiseString)

    # makes a matrix out of the string, every letter is one entry, line brake means new list
    matrix = [list(line) for line in input.strip().split("\n")]
    rows = len(matrix)
    cols = len(matrix[0])
    word = "XMAS"
    count = 0

    # finds all instances of diagonal "XMAS" going from top left to bottom right
    for r in range(rows - 3) :
        for c in range(cols - 3) :
            if all(matrix[r+i][c+i] == word[i] for i in range(4)) :
                count +=1

    # finds all instances of diagonal "XMAS" going from top right to bottom left
    for r in range(rows - 3) :
        for c in range(3, cols) :
             if all(matrix[r+i][c-i] == word[i] for i in range(4)) :
                count +=1

    # finds all instances of diagonal "XMAS" going from bottom left to top right
    for r in range(3, rows) :
        for c in range(cols - 3) :
            if all(matrix[r-i][c+i] == word[i] for i in range(4)) :
                count +=1

    # finds all instances of diagonal "XMAS" going from bottom right to top left
    for r in range(3, rows) :
        for c in range(3, cols) :
            if all(matrix[r-i][c-i] == word[i] for i in range(4)) :
                count +=1


    

    xmasHorizontalCount = len(xmasHorizontal)
    samxHorizontalCount = len(samxHorizontal)
    xmasVerticalCount = len(xmasVertical)
    samxVerticalCount = len(samxVertical)

    finalCount = xmasHorizontalCount + samxHorizontalCount + xmasVerticalCount + samxVerticalCount + count
    print(f"XMAS appears {finalCount} times in the given input.")


def part2() :
    path = r"day4input.txt"
    input = open(path, "r")
    input = input.read()

    # convert input string to matrix
    matrix = [list(line) for line in input.strip().split("\n")]
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    search = {"MAS", "SAM"}

    #print(matrix)

    # look for the middle of the X
    for r in range(1, rows-1) :
        for c in range(1, cols-1) :
            
            # ↘️
            top_left = matrix[r-1][c-1] + matrix[r][c] + matrix[r+1][c+1]#

            # ↙️
            top_right = matrix[r-1][c+1] + matrix[r][c] + matrix[r+1][c-1]

            # ↗️
            bottom_left = matrix[r+1][c-1] + matrix[r][c] + matrix[r-1][c+1]

            # ↖️
            bottom_right = matrix[r+1][c+1] + matrix[r][c] + matrix[r-1][c-1]

            if (top_left in search and top_right in search) :
                count += 1
                #print("yes1")
            elif (bottom_left in search and bottom_right in search) :
                count +=1
                #print("yes2")

    print(f"The word MAS in X shape appears {count} times in the given input.")


#part1()
part2()