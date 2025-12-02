
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
def part_1():
    # read input from file
    with open("2.1_input.txt", "r") as input:
        data = input.read().split(",")
        
        invalid_ids = []
        
        for id_ranges in data:
            # id ranges
            id_range = str(id_ranges).split("-")
            
            print(f"ID ranges: {id_range}")
            
            invalid_ids.extend(find_invalid_ids_1(int(id_range[0]), int(id_range[1])))
            
            # print(f"Invalid IDs: {invalid_ids}")
        print(f"Sum of invalid IDs: {sum(invalid_ids)}")


        
if __name__ == "__main__":
    part_1()
    # part_2()