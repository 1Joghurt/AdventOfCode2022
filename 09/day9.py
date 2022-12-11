from bridge import Bridge

with open("09/inputs.txt", "r") as f:
    inputs = f.read().split("\n")

bridge_2 = Bridge(2)
bridge_9 = Bridge(10)
for move in inputs:
    input = move.split(" ")
    direction = input[0]
    count  = int(input[1])
    bridge_2.Move(direction, count)
    bridge_9.Move(direction, count)
print(len(bridge_2.visitedByTail)) # part1
print(len(bridge_9.visitedByTail)) # part2


