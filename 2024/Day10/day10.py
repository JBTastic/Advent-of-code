from collections import deque

def isValidStep(currentHeight, nextHeight) :

    # checks if the step from current height to next height is valid
    return nextHeight == currentHeight + 1


def bfs(matrix, start) :

    # starts a queue with the starting point (the found 0) and goes from there to do BFS
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([start])
    visited = set()
    visited.add(start)
    score = 0

    # as long as there are entrys in the queue, pop the left most entry, go from there in
    # all four directions if its in bounds, put the new positions in the queue and mark them
    # as visited, if the position is a 9 then add 1 to the score
    while queue :
        x, y = queue.popleft()

        for dx, dy in directions :
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited :
                if isValidStep(matrix[x][y], matrix[nx][ny]) :
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    if matrix[nx][ny] == 9 :
                        score += 1

    return score

def countTrails(matrix, start) :

     # counts the number of distinct trails starting from a trailhead
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # add the starting position and the path as list of positions so every path is unique
    queue = deque([(start, [start])]) 
    trailCount = 0

    # while there are still elements in queue do this
    while queue:

        # take the next element and its path out of the queue
        (x, y), path = queue.popleft()

        # calculate the next position
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # if the next position is in bounds and they aren't in the current path do this
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:

                # look if we can go that way (the number can only go up exactly 1 by each step)
                if isValidStep(matrix[x][y], matrix[nx][ny]):

                    # add the next position to the current path and save it as the new path
                    newPath = path + [(nx, ny)]

                    # put the next position and the new path in the queue for the next iteration of the while loop
                    queue.append(((nx, ny), newPath))

                    # if we find a trail end (a 9), then increase the trail count by 1
                    if matrix[nx][ny] == 9:
                        trailCount += 1

    return trailCount

def calculateTrailheadScores(matrix) :

    # calculates the scores for all trailheads in the matrix
    rows, cols = len(matrix), len(matrix[0])
    totalScore = 0

    # goes through every entry in the matrix, if it finds a starting position  it starts BFS
    for x in range(rows) :
        for y in range(cols) :
            if matrix[x][y] == 0:
                totalScore += bfs(matrix, (x, y))

    return totalScore

def calculateTrailheadRatings(matrix) : 
    # calculates the ratings for all trailheads in the matrix
    rows, cols = len(matrix), len(matrix[0])
    totalRating = 0

    # goes through every entry in the matrix, if it finds a starting position it starts with countTrails
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 0:  # Trailhead found
                totalRating += countTrails(matrix, (x, y))

    return totalRating

def part1() :
    path = r".\Day10\day10input.txt"
    with open(path, "r") as file :
        matrix = [list(map(int, line.strip())) for line in file]

    sum = calculateTrailheadScores(matrix)

    print(f"The sum of all the scores of all trailheads is {sum}")


def part2() :
    path = r".\Day10\day10input.txt"
    with open(path, "r") as file :
        matrix = [list(map(int, line.strip())) for line in file]

    sum = calculateTrailheadRatings(matrix)

    print(f" The sum of the ratings of all trailheads is {sum}")



# part1()
part2()
