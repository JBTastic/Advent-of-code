
def find_invalid_ids_1(start: int, end: int) -> list[int]:
    invalid_ids = []
    
    for num in range(start, end + 1):
        num = str(num)
        num_digits = len(num)
        is_valid = True
        
        # go through the number of digits for every number in our range
        for i in range(num_digits//2):
            
            # if the number of digits is odd, skip the number
            if (num_digits % 2) != 0:
                continue
            
            # number of digits is even, i is an integer
            digits1 = num[0:i+1]
            digits2 = num[i+1:num_digits]
            
            # number of digits must be the same
            if len(str(digits1)) != len(str(digits2)):
                continue
            
            # we now know: 
            # both halves have the same number of digits
            if (digits1 == digits2):
                is_valid = False
                break
            else:
                is_valid = True
                break
            
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