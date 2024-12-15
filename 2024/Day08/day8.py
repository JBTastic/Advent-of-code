def part1() :
    path = r"day8input.txt"
    with open(path, "r") as file :
        inputLines = file.read().splitlines()
    
    antennas = []

    rows = len(inputLines)
    columns = len(inputLines[0])

    # put all antennas in a list with x and y coordinates and the name of the frequency
    for y, line in enumerate(inputLines) :
        for x, char in enumerate(line) :
            if char != "." :
                antennas.append((x, y, char))

    sum = 0
    antinodes = set()

    # go through all possible pairs of two antennas of the same kind
    for i, (x1, y1, freq1) in enumerate(antennas) :
        for j, (x2, y2, freq2) in enumerate(antennas) :
            if i >= j or freq1 != freq2:
                continue

            # x and y distance between the antennas
            dx = x2 - x1
            dy = y2 - y1

            # antenna that is before x and y
            beforeX1 = x1 - dx
            beforeY1 = y1 - dy

            # antenna that is beyond x and y
            beyondX2 = x2 + dx
            beyondY2 = y2 + dy

            # coordinates of both antinodes
            antinode0 = (beforeX1, beforeY1)
            antinode1 = (beyondX2, beyondY2)

            # put the antinodes in a set so there are no double antinodes
            antinodes.add(antinode0)
            antinodes.add(antinode1)

    for antinode in antinodes :

        # if antinode is in bounds, add 1 to the sum
        if 0 <= antinode[0] < columns and 0 <= antinode[1] < rows :
            sum += 1


    print(f"Total unique antinode locations is: {sum}")


def part2() :
    path = r"day8input.txt"
    with open(path, "r") as file :
        inputLines = file.read().splitlines()
    
    antennas = []

    rows = len(inputLines)
    columns = len(inputLines[0])

    # put all antennas in a list with x and y coordinates and the name of the frequency
    for y, line in enumerate(inputLines) :
        for x, char in enumerate(line) :
            if char != "." :
                antennas.append((x, y, char))

    sum = 0
    antinodes = set()

    # go through all possible pairs of two antennas of the same kind
    for i, (x1, y1, freq1) in enumerate(antennas) :
        for j, (x2, y2, freq2) in enumerate(antennas) :
            if i >= j or freq1 != freq2:
                continue

            # x and y distance between the antennas
            dx = x2 - x1
            dy = y2 - y1

            # for every antenna pair, loop enough times to get all the possible antinodes, out of bounds doesn't matter because I test for it later
            maxAmountAntinodes = rows if rows >= columns else columns
            for k in range(1, maxAmountAntinodes+1) :

                # antenna that is before x and y
                beforeX1 = x1 - (dx * k)
                beforeY1 = y1 - (dy * k)

                # antenna that is beyond x and y
                beyondX2 = x2 + (dx * k)
                beyondY2 = y2 + (dy * k)

                # add all the possible antinodes in both directions
                antinodes.add((beforeX1, beforeY1))
                antinodes.add((beyondX2, beyondY2))

            # add both the antennas as antinodes too
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))

    for antinode in antinodes :

        # if antinode is in bounds, add 1 to the sum
        if 0 <= antinode[0] < columns and 0 <= antinode[1] < rows :
            sum += 1

    print(f"Total unique antinode locations is: {sum}")

# part1()
part2()