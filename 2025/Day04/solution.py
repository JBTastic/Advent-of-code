def part1(data: str):
    # Read the data as lines and cast to tuple for better memory allocation and therefore faster access
    lines = tuple(data.splitlines())
    number_of_accessable_rolls = 0
    
    for i, line in enumerate(lines):
        for j, position in enumerate(line):
            
            # Skip, if not a roll of paper
            if position != "@":
                continue
            
            # Check all adjacent positions
            num_adjacent_rolls = 0
            up = i > 0
            down = i < len(lines) - 1
            left = j > 0
            right = j < len(line) - 1
            
            # Up
            if up and lines[i-1][j] == "@":
                num_adjacent_rolls += 1
            # Down
            if down and lines[i+1][j] == "@":
                num_adjacent_rolls += 1
            # Left
            if left and lines[i][j-1] == "@":
                num_adjacent_rolls += 1
            # Right
            if right and lines[i][j+1] == "@":
                num_adjacent_rolls += 1
            # Up-Left
            if up and left and lines[i-1][j-1] == "@":
                num_adjacent_rolls += 1
            # Up-Right
            if up and right and lines[i-1][j+1] == "@":
                num_adjacent_rolls += 1
            # Down-Left
            if down and left and lines[i+1][j-1] == "@":
                num_adjacent_rolls += 1
            # Down-Right
            if down and right and lines[i+1][j+1] == "@":
                num_adjacent_rolls += 1
            
            # If fewer than 4 rolls of paper are adjacent, the current position is accessible
            if num_adjacent_rolls < 4:
                number_of_accessable_rolls += 1
                
    print("Part 1:", number_of_accessable_rolls)


def part2(data: str):
    # Read the data as lines
    lines = data.splitlines()
    number_of_accessable_rolls = 0
    
    # Repeat until no more rolls can be removed
    while True:
        removable_rolls = []
        for i, line in enumerate(lines):
            for j, position in enumerate(line):
                
                # Skip, if not a roll of paper
                if position != "@":
                    continue
                
                # Check all adjacent positions
                num_adjacent_rolls = 0
                up = i > 0
                down = i < len(lines) - 1
                left = j > 0
                right = j < len(line) - 1
                
                # Up
                if up and lines[i-1][j] == "@":
                    num_adjacent_rolls += 1
                # Down
                if down and lines[i+1][j] == "@":
                    num_adjacent_rolls += 1
                # Left
                if left and lines[i][j-1] == "@":
                    num_adjacent_rolls += 1
                # Right
                if right and lines[i][j+1] == "@":
                    num_adjacent_rolls += 1
                # Up-Left
                if up and left and lines[i-1][j-1] == "@":
                    num_adjacent_rolls += 1
                # Up-Right
                if up and right and lines[i-1][j+1] == "@":
                    num_adjacent_rolls += 1
                # Down-Left
                if down and left and lines[i+1][j-1] == "@":
                    num_adjacent_rolls += 1
                # Down-Right
                if down and right and lines[i+1][j+1] == "@":
                    num_adjacent_rolls += 1
                
                # If fewer than 4 rolls of paper are adjacent, the current position is accessible
                if num_adjacent_rolls < 4:
                    number_of_accessable_rolls += 1
                    removable_rolls.append((i, j))

        # No more rolls can be removed
        if not removable_rolls:
            break

        # Remove duplicates
        removable_rolls = set(removable_rolls)
        removable_rolls = list(removable_rolls)

        # Remove the rolls
        for i, j in removable_rolls:
            lines[i] = lines[i][:j] + "." + lines[i][j+1:]
    
    print("Part 2:", number_of_accessable_rolls)


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data) 