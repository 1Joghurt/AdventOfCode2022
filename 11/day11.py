from monkeys import Monkeys

with open("11/inputs.txt", "r") as f:
    inputs = f.read().split("\n")


def part1():
    monkeys = Monkeys()
    monkeys.CreateMonkeyFromInput(inputs)

    monkeys.Inspect(20, 3)

    print(monkeys.GetMonkeyBusiness())
        

def part2():
    monkeys = Monkeys()
    monkeys.CreateMonkeyFromInput(inputs)

    monkeys.Inspect(10000, 1)

    print(monkeys.GetMonkeyBusiness())
   

part1()
part2()