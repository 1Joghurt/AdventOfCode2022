from monkey import Monkey

class Monkeys:
    def __init__(self) -> None:
        self.monkeys = []

    def CreateMonkeyFromInput(self, stringList):
        monkey_list = []
        for s in stringList:
            if s == "":
                self.__AddMonkey(monkey_list)
                monkey_list = []
            else:
                monkey_list.append(s)
        self.__AddMonkey(monkey_list)

    def __AddMonkey(self, stringList):
        monkey = Monkey()
        monkey.ParseFromStringList(stringList)
        self.monkeys.append(monkey)
        

    def Inspect(self, count, divider):
        for _ in range(count):
            for monkey in self.monkeys:
                thrown_items = monkey.Inspect(divider)

                for thrown_item in thrown_items:
                    dest_monkey = next(m for m in self.monkeys if m.number == thrown_item[1])
                    dest_monkey.items.append(thrown_item[0])

    def __SortElement(self, monkey):
        return monkey.inspection_count

    def GetMonkeyBusiness(self):
        self.monkeys.sort(key=self.__SortElement, reverse=True)
        return self.monkeys[0].inspection_count * self.monkeys[1].inspection_count