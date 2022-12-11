with open("06/inputs.txt", "r") as f:
    input = f.read()


def FirstDistinctChars(count):
   for i in range(0, len(input)-count):
        list = []
        for inner in range(count):
            if input[i+inner] in list:
                break
            else: 
                list.append(input[i+inner])

        if len(list) == count:
            return i+count

print(FirstDistinctChars(4)) #part1
print(FirstDistinctChars(14)) #part2




