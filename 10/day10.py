inputs = open("10/inputs.txt", "r").read().split("\n")


def part1():
    cycle = 0
    x = 1
    value = 0

    for i in inputs:
        splitted_input = i.split(" ")
        type = splitted_input[0]
        count = int(0 if len(splitted_input) == 1 else splitted_input[1])

        if type == "addx":
            for _ in range(0,2):
                cycle += 1
                value += CheckCycle(cycle, x)
            x += count  
        elif type == "noop":
            cycle += 1
            value += CheckCycle(cycle, x)
           
    print(value)
        
def CheckCycle(cycle, x):
    return x * cycle if cycle % 40 == 20 else 0

def part2():
    crt = "#"*240
    cycle = 0
    sprite = 1
    
    for i in inputs:
        splitted_input = i.split(" ")
        type = splitted_input[0]
        count = int(0 if len(splitted_input) == 1 else splitted_input[1])

        if type == "addx":
            for _ in range(0,2):
                if cycle == 8:
                    print()
                crt = CheckSprite(crt, cycle, sprite)
                cycle += 1
            sprite += count  
        elif type == "noop":
            crt = CheckSprite(crt, cycle, sprite)
            cycle += 1
   
    PrintResult(crt)

def CheckSprite(crt, cycle, sprite):
    letter = ""

    sprite = ((cycle + 1) // 40 ) * 40 + sprite
    
    if sprite == cycle or sprite + 1 == cycle or sprite - 1 == cycle:
        letter = "#"
    else:
        letter = '.'

    temp = list(crt)
    temp[cycle] = letter
    return "".join(temp)

def PrintResult(crt):
    output = ""
    for pos in range(0, len(crt)):
        if pos > 0 and pos % 40 == 0:
             output += "\n"
        output += crt[pos]
    print(output)
    
part1()
part2()