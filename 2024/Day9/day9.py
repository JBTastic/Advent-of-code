def part1() :
    path = r".\Day9\day9exampleNew.txt"
    with open(path, "r") as file :
        matrix = [list(line) for line in file.read().strip().split()]
        matrix = matrix[0]

    # turn the numbers like the puzzle wants us in this text:
    """ The disk map uses a dense format to represent the layout of
    files and free space on the disk. The digits alternate between
    indicating the length of a file and the length of free space.
    So, a disk map like 12345 would represent a one-block file,
    two blocks of free space, a three-block file, four blocks of
    free space, and then a five-block file. A disk map like 90909
    would represent three nine-block files in a row (with no free space between them).
    Each file on disk also has an ID number based on the order of the
    files as they appear before they are rearranged, starting with
    ID 0. So, the disk map 12345 has three files: a one-block file
    with ID 0, a three-block file with ID 1, and a five-block file
    with ID 2. Using one character for each block where digits are
    the file ID and . is free space, the disk map 12345 represents
    these individual blocks:0..111....22222 """


    index = 0
    rearranged = []
    file = True
    for char in matrix :
        if file == True :
            rearranged.append(str(index) * int(char))
            file = False
        else :
            rearranged.append("." * int(char))
            index += 1
            file = True

    for i, char in enumerate(rearranged) :
        if char == "" :
            del(rearranged[i])

    # make the seperate entrys in the list one big entry
    movedFileBlocks = list("".join(rearranged))

    print("".join(movedFileBlocks))


    # go through the list backwards and search for the first number, then go through the list forwards and search for the first ".", put the number in its spot.
    indexI = len(movedFileBlocks) - 1
    indexJ = 0
    finished = False

    while finished == False :
        if indexJ >= indexI :
            finished = True
        elif movedFileBlocks[indexI] == "." :
            indexI -= 1
        else :
            if movedFileBlocks[indexJ] != "." :
                indexJ += 1
            else :
                movedFileBlocks[indexJ] = movedFileBlocks[indexI]
                movedFileBlocks[indexI] = "."
                indexI -= 1
                indexJ += 1
        # print(indexI)


    print("".join(movedFileBlocks))

    # multiply each number with its index, sum up the results
    sum = 0
    for i, char in enumerate(movedFileBlocks) :
        if char != "." :
            sum += i*int(char)
        else :
            break

    print(f"The resulting filesystem checksum is {sum}")

part1()
# part2()

def checksumTest() :
    path = r"day9myCompactFile.txt"
    with open(path, "r") as file :
        matrix = [list(line) for line in file.read().strip().split()]
        matrix = matrix[0]
    
    sum = 0
    for i, char in enumerate(matrix) :
        if char != "." :
            sum += i*int(char)
        else :
            break

    print(f"The resulting filesystem checksum is {sum}")

# checksumTest()