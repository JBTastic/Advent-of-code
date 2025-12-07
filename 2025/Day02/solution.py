
def find_invalid_ids_1(start: int, end: int) -> list[int]:
    invalid_ids = []
    
    for num in range(start, end + 1):
        num = str(num)
        num_digits = len(num)
        is_valid = True
        
        # check if number has two identical halves
        if num_digits % 2 != 0:
            continue
        
        # split number in two halves
        num_half = num_digits // 2
        digits1 = num[0:num_half]
        digits2 = num[num_half:num_digits]
        
        # check if both halves are identical
        if digits1 == digits2:
            is_valid = False
        else:
            is_valid = True
                        
        if not is_valid:
            invalid_ids.append(int(num))
    
    return invalid_ids

# find invalid IDs and add them up
def part1():
    # read input from file
    with open("input.txt", "r") as input:
        data = input.read().split(",")
        
        invalid_ids = []
        
        for id_ranges in data:
            # id ranges
            id_range = str(id_ranges).split("-")
            
            # print(f"ID ranges: {id_range}")
            
            invalid_ids.extend(find_invalid_ids_1(int(id_range[0]), int(id_range[1])))
            
            # print(f"Invalid IDs: {invalid_ids}")
        print(f"Sum of invalid IDs Part 1: {sum(invalid_ids)}")


def find_invalid_ids_2(start: int, end: int) -> list[int]:
    invalid_ids = []
    
    for num in range(start, end + 1):
        num_string = str(num)
        num_length = len(num_string)
        is_invalid = False

        # Try block lengths: 1 to half of the total length
        for block_len in range(1, num_length // 2 + 1):
            
            # Length must be a multiple of the block length
            if num_length % block_len != 0:
                continue

            block = num_string[:block_len]
            repeats = num_length // block_len

            if block * repeats == num_string:
                is_invalid = True
                break

        if is_invalid:
            invalid_ids.append(num)

    return invalid_ids


def part2():
    with open("input.txt", "r") as input:
        data = input.read().split(",")
        
        invalid_ids = []
        
        for id_ranges in data:
            # id ranges
            id_range = str(id_ranges).split("-")
            
            # print(f"ID ranges: {id_range}")
            
            invalid_ids.extend(find_invalid_ids_2(int(id_range[0]), int(id_range[1])))
            
            # print(f"Invalid IDs: {invalid_ids}")
        print(f"Sum of invalid IDs Part 2: {sum(invalid_ids)}")


if __name__ == "__main__":
    part1()
    part2()