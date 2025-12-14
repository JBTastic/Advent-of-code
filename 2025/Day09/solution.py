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

    # Build a list of vertical segments from the perimeter tiles.
    # This is done once for efficiency.
    tiles_by_x = {}
    for x, y in red_and_green_tiles:
        if x not in tiles_by_x:
            tiles_by_x[x] = []
        tiles_by_x[x].append(y)
        
    vertical_segments = []
    for x, ys in tiles_by_x.items():
        if not ys:
            continue
        ys.sort()
        
        start_y = ys[0]
        end_y = ys[0]
        for i in range(1, len(ys)):
            if ys[i] == end_y + 1:
                end_y = ys[i] # Extend segment
            else:
                # End of a contiguous segment, add it and start a new one
                # y_end is inclusive, so for a half-open interval check, we need y_end + 1
                vertical_segments.append((x, start_y, end_y + 1))
                start_y = end_y = ys[i]
        # Add the last segment for this x
        vertical_segments.append((x, start_y, end_y + 1))

    def is_inside(point: tuple[int, int], perimeter_tiles: set[tuple[int, int]], segments: list) -> bool:
        """
        Checks if a point is inside a polygon using the Ray Casting (even-odd) rule.
        A point on the perimeter is considered inside for this problem's purpose.
        """
        px, py = point

        if point in perimeter_tiles:
            return True

        crossings = 0
        for x, y_min, y_max_exclusive in segments:
            # Consider only vertical segments to the right of the point
            if px < x:
                # Check if the point's y-coordinate lies within the segment's y-range.
                # The half-open interval [y_min, y_max_exclusive) is crucial for correctly
                # handling cases where the ray passes through a vertex or is collinear
                # with a horizontal edge.
                if y_min <= py < y_max_exclusive:
                    crossings += 1
        
        return crossings % 2 == 1

    counter = 0
    print(counter)
    final_area = possible_areas.copy()
    for vecs in possible_areas.keys():
        x1, y1 = vecs[0]
        x2, y2 = vecs[1]
        min_x, max_x = sorted((x1, x2))
        min_y, max_y = sorted((y1, y2))
        
        # Instead of checking every point inside the area,
        # we only check the perimeter points
        perimeter_points = []
        # Top and bottom edges
        for x in range(min_x, max_x + 1):
            perimeter_points.append((x, min_y))
            perimeter_points.append((x, max_y))
        # Left and right edges (excluding corners, which are already included)
        for y in range(min_y + 1, max_y):
            perimeter_points.append((min_x, y))
            perimeter_points.append((max_x, y))
        
        counter += 1
        print(counter)

        is_fully_inside = True
        for point in perimeter_points:
            if not is_inside(point, red_and_green_tiles, vertical_segments):
                is_fully_inside = False
                break
        
        if not is_fully_inside:
            final_area.pop(vecs)
            
        if vecs in final_area:
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