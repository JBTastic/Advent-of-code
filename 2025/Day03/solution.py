def twoSum(nums: list[str]) -> int:
    """Standard implementation to find the biggest number that we can get by adding two numbers of a list, but instead of adding we concatenate them

    Args:
        nums (list[str]): The input numbers, as a list of strings

    Returns:
        int: The maximum concatenated number formed by any two numbers in the list
    """
    max = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if int(nums[i] + nums[j]) > max:
                max = int(nums[i] + nums[j])
    return int(max)  


def twelveSum(nums: list[str]) -> int:
    """Finding the biggest possible number, that can be made by concatenating 12 digits of a list of digits and without changing their order

    Args:
        nums (list[str]): The input numbers, as a list of strings

    Returns:
        int: The maximum concatenated number formed by any 12 numbers in the list
    """
    # The idea:
    # We want the first digit. That has to be the biggest digit in the list between the first, and the 12th last digit
    # Then we want the second digit. That has to be the biggest digit in the list between the index of the first digit + 1, and the 11th last digit
    # And so on...
    # At the end we concatenate all the digits we found to get the maximum number
    
    digits = []
    indices = []
    
    for i in range(12):
        if i == 0:
            start = 0
        else:
            start = indices[i-1] + 1
        end = -(11 - i)
        if end == 0:
            end = None
        digits.append(max([int(x) for x in nums[start:end]]))
        indices.append(nums.index(str(digits[i]), start))
    
    max_num = int("".join([str(x) for x in digits]))
    return max_num


def part1(data: str):
    banks = data.splitlines()
    max = []
    
    for bank in banks:
        max.append(twoSum(list(bank)))
        
    print(sum(max))
    

def part2(data: str):
    banks = data.splitlines()
    max_numbers = []
    
    for bank in banks:
        max_numbers.append(twelveSum(list(bank)))
        
    print(sum(max_numbers))


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(input_data)
    part2(input_data)