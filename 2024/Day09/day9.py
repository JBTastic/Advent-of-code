def part1() :
    path = r".\Day09\day9input.txt"
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
            rearranged.append([str(index), int(char)])
            file = False
        else :
            rearranged.append([".", int(char)])
            index += 1
            file = True

    for i, char in enumerate(rearranged) :
        if char[1] == 0 :
            del(rearranged[i])


    # go through the list backwards and search for the first number, then go through the list forwards and search for the first ".", put the number in its spot.
    indexI = len(rearranged) - 1
    indexJ = 0
    finished = False

    while finished == False :


        if indexJ >= indexI :
            finished = True

        elif rearranged[indexI][0] == "." :
            indexI -= 1
        else :
            if rearranged[indexJ][0] != "." :
                indexJ += 1
            else :
                # three cases:
                # we have exactly as many numbers in the end as we got . at the front
                # we have less numbers at the end than we got . at the front
                # we have more numbers at the end than we got . at the front

                # first case
                if rearranged[indexI][1] == rearranged[indexJ][1] :
                    rearranged[indexJ][0] = rearranged[indexI][0]
                    rearranged[indexI][0] = "."

                    indexI -= 1
                    indexJ += 1

                # second case
                elif rearranged[indexI][1] < rearranged[indexJ][1] :
                    difference = rearranged[indexJ][1] - rearranged[indexI][1]
                    rearranged[indexJ][1] = difference
                    rearranged.insert(indexJ, [rearranged[indexI][0], rearranged[indexI][1]])
                    rearranged[indexI+1][0] = "."

                    indexJ += 1

                # third case
                else :
                    difference = rearranged[indexI][1] - rearranged[indexJ][1]
                    rearranged[indexJ][0] = rearranged[indexI][0]
                    rearranged[indexI][1] = difference

                    indexJ += 1



    # multiply each number with its index, sum up the results
    sum = 0
    sumIndex = 0

    for i, entry in enumerate(rearranged) :
        if entry[0] != "." : 
            for j in range(entry[1]) :
                sum += int(entry[0]) * sumIndex
                sumIndex += 1

    print(f"The resulting filesystem checksum is {sum}")


def part2() :
    path = r".\Day09\day9input.txt"
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
            rearranged.append([str(index), int(char)])
            file = False
        else :
            rearranged.append([".", int(char)])
            index += 1
            file = True

    for i, char in enumerate(rearranged) :
        if char[1] == 0 :
            del(rearranged[i])


    # go through the list backwards and search for the first number, then go through the list forwards and search for the first ".", put the number in its spot.
    indexI = len(rearranged) - 1
    indexJ = 0
    finished = False
    currentJ = 0

    while finished == False :


        if indexI == 0 :
            finished = True

        elif indexI <= indexJ :
            indexJ = 0
            indexI -= 1
            continue
        
        # indexI found . instead of a number
        elif rearranged[indexI][0] == "." :
            indexI -= 1
            
        else :
            # indexJ found a number instead of a .
            if rearranged[indexJ][0] != "." :
                indexJ += 1
            else :
                # when indexJ found a .

                # three cases:
                # we have exactly as many numbers in the end as we got . at the front
                # we have less numbers at the end than we got . at the front
                # we have more numbers at the end than we got . at the front

                # first case
                if rearranged[indexI][1] == rearranged[indexJ][1] and indexI >= indexJ :
                    rearranged[indexJ][0] = rearranged[indexI][0]
                    rearranged[indexI][0] = "."

                    indexI -= 1
                    indexJ += 1

                # second case
                elif rearranged[indexI][1] < rearranged[indexJ][1] :
                    difference = rearranged[indexJ][1] - rearranged[indexI][1]
                    rearranged[indexJ][1] = difference
                    rearranged.insert(indexJ, [rearranged[indexI][0], rearranged[indexI][1]])
                    rearranged[indexI+1][0] = "."

                    indexJ += 1

                # third case
                else :
                    indexJ += 1
                    


        # print(indexI)
        # print()
        print("I:", indexI, "J:", indexJ)
        print()
        # print(rearranged)



    # multiply each number with its index, sum up the results
    sum = 0
    sumIndex = 0

    for i, entry in enumerate(rearranged) :
        if entry[0] != "." : 
            for j in range(entry[1]) :
                sum += int(entry[0]) * sumIndex
                sumIndex += 1
        else :
            for j in range(entry[1]) :
                sumIndex +=1
        
    print(rearranged)

    print(f"The resulting filesystem checksum is {sum}")

    with open(r".\Day09\day9output.txt", 'w', encoding='utf-8') as datei :
        datei.write(str(sum))


# part1()
part2()
