from instruction import Instruction

input_instructions = open("05/inputs.txt", "r").read().split("\n")
input_basestacks = open("05/basestacks.txt", "r").read().split("\n")


def part1():
    stacks = getStacks()
    instructions = getInstructions()

    for x in instructions:
        for _ in range(x.MoveCount):
            stacks[x.Dest].append(stacks[x.Source].pop())

    answer = "" 
    for x in range(len(stacks)):
        answer += stacks[x][-1]
    print(answer)


def part2():
    stacks = getStacks()
    instructions = getInstructions()

    for x in instructions:
        move = stacks[x.Source][-x.MoveCount:]
        del stacks[x.Source][-x.MoveCount:]
        stacks[x.Dest].extend(move)
            
    answer = "" 
    for x in range(len(stacks)):
        answer += stacks[x][-1]
    print(answer)



def getInstructions():
    instructions = []

    for x in input_instructions:
        parts = x.replace("move ","").replace("from ","").replace("to ","").split(" ")
        instructions.append(Instruction(int(parts[1])-1, int(parts[2])-1, int(parts[0])))

    return instructions


def getStacks():
    stacks = []
    for i in range(len(input_basestacks)-1,-1,-1):
        line = input_basestacks[i]
        for column in range(0, len(line), 4):
            if not line[column:column+3].isspace():
                if (len(stacks) <= int(column/4)):
                    stacks.append([])
                stacks[int(column/4)].append(line[column+1:column+2])

    return stacks




#part1()
part2()