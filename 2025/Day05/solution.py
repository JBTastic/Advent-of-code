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
    splitted_data = data.splitlines()
    
    # Split the data into two sections based on the empty line
    empty_line = splitted_data.index("") # Index of the empty line separating sections
    fresh_id_ranges = splitted_data[:empty_line]
    
    # Sort ranges by their starting ID
    fresh_id_ranges.sort(key=lambda x: int(x.split("-")[0]))
    
    for i in range(len(fresh_id_ranges)-1):
        current_start, current_end = map(int, fresh_id_ranges[i].split("-"))
        next_start, next_end = map(int, fresh_id_ranges[i+1].split("-"))
        
        # If the current range overlaps or touches the next range, merge them
        # Otherwise, do nothing
        if current_end >= next_start - 1:
            merged_range = f"{current_start}-{max(current_end, next_end)}"
            fresh_id_ranges[i+1] = merged_range
            fresh_id_ranges[i] = ""  # Mark the current range as merged
            
    # Remove merged ranges
    num_fresh_ids = 0
    for id_range in fresh_id_ranges:
        if id_range:  # Only consider not empty ranges
            start, end = map(int, id_range.split("-"))
            num_fresh_ids += (end - start + 1)
    
    print(f"Part 2: {num_fresh_ids}")


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data) 