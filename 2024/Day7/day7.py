from itertools import product

def evaluateExpression(numbers, operators) :

    # evaluate the expression using the given numbers and operators, left-to-right.
    result = numbers[0]

    # iterate over the index and the operator itself
    for i, op in enumerate(operators):
        if op == "+" :
            result += numbers[i + 1]
        elif op == "*" :
            result *= numbers[i + 1]
        elif op == "||" :
            strResult = str(result)
            strNumbers = str(numbers[i + 1])
            result = int(strResult + strNumbers)

    return result

def part1() :
    path = r"day7input.txt"
    with open(path, "r") as file:
        inputLines = file.read().strip().split("\n")

    # print(inputLines)

    sum = 0

    for line in inputLines :
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split(" ")))

        # print(target)
        # print(numbers)

        # generate all combinations of operators for the amount of given numbers
        operatorCombinations = product(["+", "*"], repeat=len(numbers) - 1)

        # check if there is a operator combination so we get the target number
        for operators in operatorCombinations :
            if evaluateExpression(numbers, operators) == target :
                sum += target
                break 

    print(f"Total Calibration Result is {sum}")


def part2() :
    path = r"day7input.txt"
    with open(path, "r") as file:
        inputLines = file.read().strip().split("\n")

    # print(inputLines)

    sum = 0

    for line in inputLines :
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split(" ")))

        # print(target)
        # print(numbers)

        # generate all combinations of operators for the amount of given numbers
        operatorCombinations = product(["+", "*", "||"], repeat=len(numbers) - 1)

        # check if there is a operator combination so we get the target number
        for operators in operatorCombinations :
            if evaluateExpression(numbers, operators) == target :
                sum += target
                break 

    print(f"Total Calibration Result is {sum}")

# part1()
part2()
