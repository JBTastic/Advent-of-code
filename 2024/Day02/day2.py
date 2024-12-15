import copy

input = open("day2input.txt", "r")
input = input.read()


def testForStatements(reports) :
    countSafeReports = 0
    for report in reports :
        report = report.split()
        report = list(map(int, report))
        strictlyIncreasing = all(i < j for i, j in zip(report, report[1:]))
        strictlyDecreasing = all(i > j for i, j in zip(report, report[1:]))
        if strictlyDecreasing == True or strictlyIncreasing == True :
            statement1 = True
        else: 
            statement1 = False

        statement2 = all(1 <= abs(i-j) <= 3 for i, j in zip(report, report[1:]))

        if statement1 == True and statement2 == True :
            countSafeReports +=1

        # print(f"Statement1: {statement1}")
        # print(f"Statement2: {statement2}")
        # counter += 1
        # if counter == 3 :
        #     break
    return countSafeReports


def isSafe(report) :
    strictlyIncreasing = all(i < j for i, j in zip(report, report[1:]))
    strictlyDecreasing = all(i > j for i, j in zip(report, report[1:]))

    statement1 = strictlyIncreasing or strictlyDecreasing
    statement2 = all(1 <= abs(i-j) <= 3 for i, j in zip(report, report[1:]))

    return statement1 and statement2



def problemDampener(reports) :
    countSafeReports = 0

    for report in reports :
        report = report.split()
        report = list(map(int, report))

        if isSafe(report) :
            countSafeReports += 1
        else :
            for i in range(len(report)) :
                newReport = copy.deepcopy(report)
                del newReport[i]
                if isSafe(newReport) :
                    countSafeReports += 1
                    break
                
    return countSafeReports



def part1() :
    reports = input.split("\n")
    countSafeReports = testForStatements(reports)
    print(f"Number of safe reports: {countSafeReports}")


def part2() :
    reports = input.split("\n")
    countSafeReports = problemDampener(reports)
    print(f"Number of safe reports after problem dampener was applied: {countSafeReports}")


    

part1()
part2()