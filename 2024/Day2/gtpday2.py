import copy

# Lese die Eingabedatei
input = open("day2input.txt", "r")
input = input.read()

# Funktion zur Überprüfung, ob ein Bericht sicher ist (Part 1)
def testForStatements(reports):
    countSafeReports = 0
    for report in reports:
        report = report.split()
        report = list(map(int, report))
        strictlyIncreasing = all(i < j for i, j in zip(report, report[1:]))
        strictlyDecreasing = all(i > j for i, j in zip(report, report[1:]))
        # Überprüfen, ob der Bericht vollständig zunehmend oder abnehmend ist
        if strictlyDecreasing or strictlyIncreasing:
            statement1 = True
        else:
            statement1 = False
        
        # Überprüfen, ob die Differenz zwischen benachbarten Levels zwischen 1 und 3 liegt
        statement2 = all(1 <= abs(i-j) <= 3 for i, j in zip(report, report[1:]))
        
        # Wenn beide Bedingungen erfüllt sind, ist der Bericht sicher
        if statement1 and statement2:
            countSafeReports += 1

    return countSafeReports

# Funktion zum Entfernen eines einzelnen Levels und Überprüfen, ob der Bericht sicher ist (Part 2)
def problemDampener(reports):
    countSafeReports = 0

    for report in reports:
        report = report.split()
        report = list(map(int, report))
        
        # Überprüfen, ob der Bericht sicher ist, ohne ein Level zu entfernen
        if isSafe(report):
            countSafeReports += 1
        else:
            # Versuchen, ein Level zu entfernen und zu prüfen, ob der Bericht dann sicher wird
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if isSafe(new_report):
                    countSafeReports += 1
                    break

    return countSafeReports

# Funktion zur Überprüfung, ob ein Bericht sicher ist (unter den gleichen Bedingungen wie Part 1)
def isSafe(report):
    strictlyIncreasing = all(i < j for i, j in zip(report, report[1:]))
    strictlyDecreasing = all(i > j for i, j in zip(report, report[1:]))
    statement1 = strictlyDecreasing or strictlyIncreasing
    statement2 = all(1 <= abs(i-j) <= 3 for i, j in zip(report, report[1:]))
    return statement1 and statement2

def part2():
    reports = input.split("\n")
    countSafeReports = problemDampener(reports)
    print(f"Number of safe reports after Problem Dampener was applied: {countSafeReports}")

# Aufruf von part2
part2()
