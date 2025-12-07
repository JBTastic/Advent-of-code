def part1(data: str):
    lines = data.splitlines()    
    index_S = data.find("S")
    
    # Convert each line into a list of characters for mutability (the * unpacks the string into a list of characters)
    lines = [[*line] for line in lines]
    
    lines[1][index_S] = "|"
    splits = 0
    
    # Start in the line below the first "|"
    for i in range(2, len(lines) - 1):
        for j in range(len(lines[0])):
            # Skip current position if above it it isn't a "|"
            if lines[i-1][j] != "|":
                continue
            # Above our current position is a "|"
            # If we are currently at a ".", we can go down
            if lines[i][j] == ".":
                lines[i][j] = "|"
            # If we are currently at a "^", we go left and right, also we count our split counter
            elif lines[i][j] == "^" :
                if lines[i][j-1] == ".":
                    lines[i][j-1] = "|"
                if lines[i][j+1] == ".":
                    lines[i][j+1] = "|"
                if lines[i][j-1] == "|" or lines[i][j+1] == "|":
                    splits += 1

    print(f"Part 1: {splits}")


def part2(data: str):
    lines = data.splitlines()
    num_rows, num_cols = len(lines), len(lines[0])
    cache = {}

    def count_paths(row, col):
        # It uses "cache" dict to store results for (row, col) pairs
        # to avoid double work for paths that merge

        # If the particle goes off the grid at the sides, stop
        if not (0 <= col < num_cols):
            return 0
        
        # If the "|" moves below the last row, it has successfully completed a path
        if row == num_rows:
            return 1

        # If we have already computed the number of paths from this position, return the cached value
        if (row, col) in cache:
            return cache[(row, col)]

        char = lines[row][col]
        result = 0
        
        # If the current cell is empty space or the start, the particle continues downward
        if char in (".S"):
            result = count_paths(row + 1, col)
        # If the current cell is a "^", the particle splits into two
        elif char == "^":
            # The total timelines are the sum of timelines from the two new paths
            # which start on the next row to the left and right
            result = count_paths(row + 1, col - 1) + count_paths(row + 1, col + 1)
        
        # Cache the result for the current (row, col) state before returning
        cache[(row, col)] = result
        return result

    start_col = lines[0].find("S")
    
    # Start the process from the "S" position at the top
    total_universes = count_paths(0, start_col)
    print(f"Part 2: {total_universes}")
    

if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data) 