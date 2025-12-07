def part1(data: str):
    lines = data.strip().splitlines()
    
    # Split each line into its components
    splitted_lines = []
    for line in lines:
        splitted_lines.append(line.split())
    
    num_calculation = len(splitted_lines[0])
    len_per_calculation = len(splitted_lines)
    
    # Evaluate each calculation and sum the results
    sum_problems = 0
    for i in range(num_calculation):
        operation = ""
        for j in range(len_per_calculation - 1):
            operation += splitted_lines[j][i]
            if j < len_per_calculation - 2:
                operation += splitted_lines[len_per_calculation-1][i]
        sum_problems += eval(operation)
    
    print(f"Part 1: {sum_problems}")
    
def part2(data: str):
    lines = data.splitlines()
    
    len_lines = len(lines)
    len_operation = len(lines[0])
    
    # Declare variables
    final_operation = ""
    curr_number = ""
    sum_problems = 0
    
    # First we go through the input from left to right
    for i in range(len_operation):
        
        # Determine the operator
        if lines[len_lines-1][i] in "+*":
            operator = lines[len_lines-1][i]
            
        # Go through from top to bottom to get the current number
        for j in range(len_lines-1):
            curr_number += lines[j][i].strip()
            
        # If we found at least one digit, we add it to the final operation
        if curr_number:
            final_operation += curr_number
            curr_number = ""
            final_operation += operator
            
        # This means it is a blank column, which indicates the end of a problem, so we evaluate the current operation
        else:
            final_operation = final_operation[:-1]  # Remove last operator if no number found
            sum_problems += eval(final_operation)
            final_operation = ""
            
        # Also at the very end, we evaluate the final operation
        if i == len_operation - 1:
            final_operation = final_operation[:-1]  # Remove last operator
            sum_problems += eval(final_operation)

    print(f"Part 2: {sum_problems}")


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data) 