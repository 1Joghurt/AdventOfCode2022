from collections import deque


input = open("08/inputs.txt", "r").read().split("\n")


def part1():
    visible = {}
    map = []
    index = 0
    for line in input:
        line_list = []
        for number in line:
            line_list.append((int(number), index))
            index += 1
        map.append(line_list)

    #left
    for list in range(0, len(map)):
        highest = -1
        for key in range(0, len(map[list])):
            if (map[list][key][0] > highest):
                highest = map[list][key][0]
                visible[map[list][key][1]] = map[list][key][0]

    #top
    for list in range(0, len(map)):
        highest = -1
        for key in range(0, len(map[list])):
            if (map[key][list][0] > highest):
                highest = map[key][list][0]
                visible[map[key][list][1]] = map[key][list][0]

    #right
    for list in range(len(map)-1, -1, -1):
        highest = -1
        for key in range(len(map[list])-1, -1, -1):
            if (map[list][key][0] > highest):
                highest = map[list][key][0]
                visible[map[list][key][1]] = map[list][key][0]
 
    #bottom
    for list in range(len(map)-1, -1, -1):
        highest = -1
        for key in range(len(map[list])-1, -1, -1):
            if (map[key][list][0] > highest):
                highest = map[key][list][0]
                visible[map[key][list][1]] = map[key][list][0]

            
    print(len(visible))


def part2():
    max_score = 0

    for line in range(0, len(input)):
        for column in range(0, len(input[line])):

            if (line == 3 and column == 2):
                print("")

            score = 0
            considered = int(input[line][column])
            
            count = 0
            for number in range(line+1, len(input)):
                if (considered > int(input[number][column])):
                    count += 1
                else: 
                    count += 1
                    break
            score = count

            count = 0
            l = 0 if line-1 < 0 else line-1
            for number in range(l, -1, -1):
                if (considered > int(input[number][column])):
                    count += 1
                else: 
                    count += 1
                    break
            score = score * count 

            count = 0
            for number in range(column+1, len(input[line])):
                if (considered > int(input[line][number])):
                    count += 1
                else: 
                    count += 1
                    break
            score = score * count

            count = 0
            c = 0 if column-1 < 0 else column-1
            for number in range(c, -1, -1):
                if (considered > int(input[line][number])):
                    count += 1
                else: 
                    count += 1
                    break
            score = score * count

            if (score > max_score):
                max_score = score

    print(max_score)

part1()
part2()
