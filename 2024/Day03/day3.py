import re

def mul(num1, num2) :
        return num1*num2

def part1() :
    input = open("day3input.txt", "r")
    input = input.read()

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    x = re.findall(pattern, input)

    sum = 0
    for i in x :
        sum += eval(i)

    print(sum)

def part2() :
    input = open("day3input.txt", "r")
    input = input.read()
    # print(input)

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't|do"

    x = re.findall(pattern, input)

    do = True
    list = []
    for i in x :

        if i == "don't" :
            do = False
        elif i == "do" :
            do = True
            continue

        if do == True :
            list.append(i)

    sum = 0
    for i in list :
        sum += eval(i)

    print(sum)



# part1()
part2()


