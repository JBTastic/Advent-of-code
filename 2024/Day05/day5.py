import copy

def findCorrectUpdates(updates, rules) :
    correctUpdates = []
    incorrectUpdates = []

    # go through every line in update
    for update in updates :
        incorrect = False

        # go through every line in rules
        for rule in rules :

            # make it so the two numbers are in a list
            rule = rule.split("|")

            # when both numbers from the rule are in the update
            if rule[0] in update and rule[1] in update :
                
                # when the rule is true, do nothing
                if (update.index(rule[0]) < update.index(rule[1])) :
                    continue

                # if the rule is violated, mark the update as incorrect / delete it
                else :
                    incorrect = True
                    break

            # when the numbers aren't both in the update, continue with the next rule
            else :
                continue

        # if the update was incorrect, delete it, else do nothing
        if incorrect == True :
            incorrectUpdates.append(update)
            # print("Incorrect")
        else :
            correctUpdates.append(update)
            # print("Correct")
    
    return correctUpdates, incorrectUpdates

def changeUpdatesUntilCorrect(updates, rules) :
    correctUpdates = []
    incorrectUpdates = []


    # go through every line in update
    for update in updates :
        incorrect = False
        # update = update.split(",")
        # print(update)

        # go through every line in rules
        for rule in rules :

            # make it so the two numbers are in a list
            rule = rule.split("|")

            # when both numbers from the rule are in the update
            if rule[0] in update and rule[1] in update :
                
                # when the rule is true, do nothing
                if (update.index(rule[0]) < update.index(rule[1])) :
                    continue

                # if the rule is violated, mark the update as incorrect and swap the numbers which violated the rule
                else :
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
                    incorrect = True
                    break

            # when the numbers aren't both in the update, continue with the next rule
            else :
                continue

        # if the update was incorrect, put it in the incorrectUpdates list, else put it in the correctUpdates list
        if incorrect == True :
            incorrectUpdates.append(update)
            # print("Incorrect")
        else :
            correctUpdates.append(update)
            # print("Correct")
    
    return correctUpdates, incorrectUpdates

def part1() :
    input = open("day5input.txt", "r")
    input = input.read()

    splittedInput = input.split("\n\n")

    rules = splittedInput[0].split()
    updates = splittedInput[1].split()

    correctUpdates, incorrectUpdates = findCorrectUpdates(updates, rules)
    del incorrectUpdates

    # iterate through every correct update, find the middle index and sum up the numbers
    sum = 0
    for correctUpdate in correctUpdates :
        correctUpdate = correctUpdate.split(",")
        middleIndex = (len(correctUpdate) - 1 ) // 2
        middle = int(correctUpdate[middleIndex])
        sum += middle

    print(f"The sum of the middle numbers of the correct updates is: {sum}")
    # print("Correct number for Example: 143")


def part2() :
    path = r"day5input.txt"
    input = open(path, "r")
    input = input.read()

    splittedInput = input.split("\n\n")

    rules = splittedInput[0].split()
    updates = splittedInput[1].split()

    newUpdates = []
    for update in updates :
        newUpdates.append(update.split(","))

    updates = newUpdates

    # try to change some stuff to make the updates correct
    correctUpdates, incorrectUpdates = changeUpdatesUntilCorrect(updates, rules)


    # find out which updates are now correct
    correctUpdates, incorrectUpdates = findCorrectUpdates(incorrectUpdates, rules)
    finalCorrectUpdates = copy.copy(correctUpdates)

    # repeat the changing stuff until the incorrectUpdates list is empty
    newCorrectUpdates = []
    while incorrectUpdates :
        correctUpdates, incorrectUpdates = changeUpdatesUntilCorrect(incorrectUpdates, rules)
        if correctUpdates != [] :
            finalCorrectUpdates.extend(correctUpdates)

    # without this it breaks
    for i in newCorrectUpdates :
        finalCorrectUpdates.append(i)


    # iterate through every correct update, find the middle index and sum up the numbers
    sum = 0
    for finalCorrectUpdate in finalCorrectUpdates :
        middleIndex = (len(finalCorrectUpdate) - 1 ) // 2
        middle = finalCorrectUpdate[middleIndex]
        sum += int(middle)

    print(f"The sum of the middle numbers of the correct updates is: {sum}")
    # print("Correct number for Example: 123")




# part1()
part2()