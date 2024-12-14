listinput = open("day1lists.txt", "r")
lists = listinput.read()
parts = lists.split()

list1 = []
list2 = []

inList1 = True

for i in range(len(parts)) :
    if inList1 :
        list1.append(parts[i])
        inList1 = False
    else :
        list2.append(parts[i])
        inList1 = True

list1.sort()
list2.sort()

list1 = list(map(int, list1))
list2 = list(map(int, list2))

def part1() :
    sum = 0

    # print(len(list1))
    # print(len(list2))

    for i in range(len(list1)) :
        sum += abs(list1[i] - list2[i])

    print(sum)

def part2() :
    similarity = 0
    for i in list1 :
        if i in list2 :
            similarity += i * list2.count(i)
    print(similarity)

part1()
part2()