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

    bottom_right_corner = (
        max(pos[0] for pos in red_tiles),
        max(pos[1] for pos in red_tiles)
    )
    enlarged_bottom_right = (
        bottom_right_corner[0] + 1,
        bottom_right_corner[1] + 1
    )

    print(enlarged_bottom_right)

    # Pre-compute all possible areas spanned by the red tiles
    possible_areas = dict()
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            possible_areas[(red_tiles[i], red_tiles[j])] = area(
                red_tiles[i], red_tiles[j]
            )

    # Sort areas from largest to smallest
    possible_areas = dict(
        sorted(possible_areas.items(), key=lambda item: item[1], reverse=True)
    )

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

    # My input does not have (0,0) as red tile, if yours does, then sorry :(
    if (0, 0) in red_tiles:
        print("Sorry, your input has (0,0) as a red tile, which contradicts my assumptions.")
        return

    """
    For reference:
    # are red tiles
    X are green tiles
    . are free tiles

    ..............
    .......#XXX#..
    .......X...X..
    ..#XXXX#...X..
    ..X........X..
    ..#XXXXXX#.X..
    .........X.X..
    .........#X#..
    ..............

    We want to find all the outside free tiles (not red or green)
    """


    from floodfill import flood_fill
    import array

    red_tiles = set(red_tiles)
    green_tiles = set(green_tiles)
    red_and_green_tiles = red_tiles.union(green_tiles)

    max_x, max_y = enlarged_bottom_right
    width = max_x + 1
    height = max_y + 1

    # Linearized blocked grid (C-friendly)
    blocked = array.array("B", [0]) * (width * height)

    def idx(x, y):
        return y * width + x

    for x, y in red_and_green_tiles:
        blocked[idx(x, y)] = 1

    # Call Cython flood fill
    visited = flood_fill(blocked, width, height)

    # Convert visited bytearray back to Python set
    not_red_or_green_tiles = set()
    for y in range(height):
        for x in range(width):
            if visited[idx(x, y)]:
                not_red_or_green_tiles.add((x, y))


    final_area = possible_areas.copy()

    for vecs in possible_areas.keys():
        x1, y1 = vecs[0]
        x2, y2 = vecs[1]
        min_x, max_x = sorted((x1, x2))
        min_y, max_y = sorted((y1, y2))
        positions_between_vectors = [
            (x, y)
            for x in range(min_x, max_x + 1)
            for y in range(min_y, max_y + 1)
        ]

        for position in positions_between_vectors:
            if position in not_red_or_green_tiles:
                final_area.pop(vecs)
                break

    print(
        f"Part 2:\nThe two positions: {list(final_area.keys())[:1]}\nThe largest area with only green and red tiles: {list(final_area.values())[:1]}"
    )


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
    
    # part1(input_data)
    part2(input_data) 