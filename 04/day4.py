input = open("04/inputs.txt", "r").read().split("\n")


def part1():
    sum = 0

    for x in input:
        assignments = x.split(",")
        assignment1 = assignments[0].split("-")
        assignment2 = assignments[1].split("-")
        assignment1_range = range(int(assignment1[0]), int(assignment1[1]))
        assignment2_range = range(int(assignment2[0]), int(assignment2[1]))

        if ispart(assignment1_range, assignment2_range):
            sum += 1

    print(sum)

def part2():
    sum = 0

    for x in input:
        assignments = x.split(",")
        assignment1 = assignments[0].split("-")
        assignment2 = assignments[1].split("-")
        assignment1_range = range(int(assignment1[0]), int(assignment1[1]))
        assignment2_range = range(int(assignment2[0]), int(assignment2[1]))

        if overlap(assignment1_range, assignment2_range):
            sum += 1

    print(sum)

def ispart(range1: range, range2: range):
    if (range1.start <= range2.start and range1.stop >= range2.stop):
        return True
    elif (range2.start <= range1.start and range2.stop >= range1.stop):
        return True
    return False


def overlap(range1: range, range2: range):
    return range1.stop >= range2.start and range2.stop >= range1.start


part1()
part2()
