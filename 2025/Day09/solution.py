def area(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    return (abs(pos1[0] - pos2[0])+1) * (abs(pos1[1] - pos2[1])+1)
    

def part1(data: str):
    lines = data.splitlines()
    vectors = [tuple(map(int, line.split(","))) for line in lines]
    
    # Pre-compute all areas spanned by the vectors
    areas = dict()
    for i in range(len(vectors)-1):
        for j in range(i+1, len(vectors)):
            areas[(vectors[i], vectors[j])] = area(vectors[i], vectors[j])
    
    # Sort areas from largest to smallest
    areas = dict(sorted(areas.items(), key=lambda item: item[1], reverse=True))

    print(f"Part 1:\nThe two positions: {list(areas.keys())[:1]}\nThe largest area: {list(areas.values())[:1]}\n\n")

def part2(data: str):
    lines = data.splitlines()
    red_tiles = [tuple(map(int, line.split(","))) for line in lines]
    
    rightmost = max(red_tiles, key=lambda item: item[0])[0]

    # Pre-compute all possible areas spanned by the red tiles
    possible_areas = dict()
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            possible_areas[(red_tiles[i], red_tiles[j])] = area(red_tiles[i], red_tiles[j])

    # Sort areas from largest to smallest
    possible_areas = dict(sorted(possible_areas.items(), key=lambda item: item[1], reverse=True))

    # Find all the green tiles by connecting the red tiles
    green_tiles = []
    for i in range(len(red_tiles) - 1):
        curr = red_tiles[i]
        next = red_tiles[i + 1]
        if curr[0] == next[0]:  # same x coordinate
            for y in range(min(curr[1], next[1]) + 1, max(curr[1], next[1])):
                green_tiles.append((curr[0], y))
        elif curr[1] == next[1]:  # same y coordinate
            for x in range(min(curr[0], next[0]) + 1, max(curr[0], next[0])):
                green_tiles.append((x, curr[1]))

    # Connect last and first red tile
    curr = red_tiles[-1]
    next = red_tiles[0]
    if curr[0] == next[0]:  # same x coordinate
        for y in range(min(curr[1], next[1]) + 1, max(curr[1], next[1])):
            green_tiles.append((curr[0], y))
    elif curr[1] == next[1]:  # same y coordinate
        for x in range(min(curr[0], next[0]) + 1, max(curr[0], next[0])):
            green_tiles.append((x, curr[1]))

    red_tiles = set(red_tiles)
    green_tiles = set(green_tiles)
    red_and_green_tiles = red_tiles.union(green_tiles)
    
    def raycast(start: tuple[int, int], red_and_green: set[tuple[int, int]]) -> bool:
        """For one position, do a raycast to the right and count how many red/green tiles are crossed.
        If an odd number is crossed, the position is inside the area (return True).
        If even, the position is outside (return False).

        Args:
            start (tuple[int, int]): starting position of the raycast
            red_and_green (set[tuple[int, int]]): set of all red and green tiles

        Returns:
            bool: False if outside the area, True if inside
        """
        
        # Count how many red/green tiles are crossed
        # When crossing multiple in a row, count as one
        counter = 0
        just_crossed = False
        
        if start in red_and_green:
            return True
        
        for i in range(start[0]+1,rightmost+1):
            if (i, start[1]) in red_and_green:
                if not just_crossed:
                    counter += 1
                just_crossed = True
            else:
                just_crossed = False
        
        return counter % 2 == 1


    counter = 0
    print(counter)
    final_area = possible_areas.copy()
    for vecs in possible_areas.keys():
        x1, y1 = vecs[0]
        x2, y2 = vecs[1]
        min_x, max_x = sorted((x1, x2))
        min_y, max_y = sorted((y1, y2))
        print("stuff")
        positions_between_vectors = [
            (x, y)
            for x in range(min_x, max_x + 1)
            for y in range(min_y, max_y + 1)
        ]

        counter += 1
        print(counter, end="\r")
        # Instead of checking if a position is outside/inside the area,
        # we do a "raycast": for any position we go all the way to the right,
        # and count how many red/green tiles we cross.
        for position in positions_between_vectors:
            if not raycast(position, red_and_green_tiles):
                final_area.pop(vecs)
                break
            
        if vecs in final_area:
            break

    print(f"Part 2:\nThe two positions: {list(final_area.keys())[:1]}\nThe largest area with only green and red tiles: {list(final_area.values())[:1]}")


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
    
    # part1(input_data)
    part2(input_data) 