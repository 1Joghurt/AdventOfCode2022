input = open("01/inputs.txt", "r").read().split("\n")

sum = 0
sum_list = []

for x in input:
    if x == "":
        sum_list.append(sum)
        sum = 0
    else:
        sum += int(x)

sum_list.sort(reverse=True);

print(sum_list[0]) #Part 1
print(sum_list[0]+sum_list[1]+sum_list[2]) #Part 2