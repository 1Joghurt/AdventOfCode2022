input = open("03/inputs.txt", "r").read().split("\n")


def part1():
    sum = 0

    for x in input:
        comp_lenght = int(len(x)/2)
        first_comp = x[:comp_lenght]
        second_comp = x[-1*comp_lenght:]

        for letter in first_comp:
            if letter in second_comp:
                sum += getValueForLetter(letter)
                break
    print(sum)




def part2():
    sum = 0

    for x in range(0, len(input)-1, 3):
        rucksack1 = input[x]
        rucksack2 = input[x+1]
        rucksack3 = input[x+2]

        for letter in rucksack1:
            if letter in rucksack2 and letter in rucksack3:
                    sum += getValueForLetter(letter)
                    break

    print(sum)               

def getValueForLetter(letter):
    value = ord(letter)
    if(letter.isupper()):
        value = value - 38
    else:
        value = value - 96
    return value

part1()
part2()


