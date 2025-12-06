def part1(data: str):
    splitted_data = data.splitlines()
    
    # Split the data into two sections based on the empty line
    empty_line = splitted_data.index("") # Index of the empty line separating sections
    fresh_id_ranges = splitted_data[:empty_line]
    available_ids = splitted_data[empty_line + 1:]
    
    # All fresh IDs
    ranges = []
    for id_range in fresh_id_ranges:
        start, end = map(int, id_range.split("-"))
        # Only save the start and end of the ranges, because storing all IDs would be memory intensive
        # Python doesn't like calling range() with very large numbers
        ranges.append((start, end + 1))
        
    # Find out how many fresh IDs are also available
    num_available_and_fresh_ids = 0
    for available_id in available_ids:
        for start, end in ranges:
            if start <= int(available_id) <= end: # Check if the ID is in the range
                num_available_and_fresh_ids += 1
                break
    
    print(f"Part 1: {num_available_and_fresh_ids}")
    
def part2(data: str):
    pass


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data) 