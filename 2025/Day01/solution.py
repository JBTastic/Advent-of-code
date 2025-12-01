from copy import copy

def part_1():
    with open("1.1_input.txt", "r") as input:
        dial = 50 # current dial number
        counter = 0 # number of times dial hits zero
        lines = input.readlines()
        for line in lines: # read line for line
            direction = line[0] # direction, either R or L
            number = int(line[1::]) # number of turns
            
            # make the turn
            if direction == "R":
                dial += number # right turn, so add
                dial %= 100 # modulo 100, because it only goes grom 0 to 99
            else:
                dial -= number # left turn, so subtract
                dial %= 100 # modulo 100, because it only goes grom 0 to 99
                
            # add 1 to counter if dial is at 0
            if dial == 0:
                counter += 1
                
        print(f"Final counter: {counter}")
        
        
        
def part_2():
    with open("1.2_example.txt", "r") as input:
        dial = 50 # current dial number
        counter = 0 # number of times dial hits zero
        lines = input.readlines()
        for line in lines: # read line for line
            direction = line[0] # direction, either R or L
            number = int(line[1::]) # number of turns
            
            # make the turn
            if direction == "R":
                dial += number # right turn, so add
                if dial >= 100: # dial crossed zero at least once
                    num_crosses = dial // 100 # number of zero crosses
                    counter += num_crosses # add to counter
                dial %= 100 # modulo 100, because it only goes grom 0 to 99
            else:
                old_dial = copy(dial)
                dial -= number # left turn, so subtract
                if (dial <= 0 and old_dial > 0): # dial crossed zero at least once
                    num_crosses = abs(dial // 100) # number of zero crosses
                    counter += num_crosses # add to counter
                elif (dial <= -100 and old_dial == 0): # e.g. counter starts from 0 and goes below -100
                    num_crosses = abs(dial // 100) - 1 # number of zero crosses (subtract one because we started at zero)
                    counter += num_crosses # add to counter
                    
                dial %= 100 # modulo 100, because it only goes grom 0 to 99
                if dial == 0:
                    counter += 1 # exactly hit zero, so add one more
                
            print(f"Direction: {direction}, Number: {number}")
            print(f"Dial: {dial}")
            print(f"Counter: {counter}")
            print("-----")
                
        print(f"Final counter: {counter}")
        
        
        
if __name__ == "__main__":
    part_1()
    part_2()