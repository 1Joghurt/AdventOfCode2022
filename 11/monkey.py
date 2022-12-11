class Monkey:
    def __init__(self) -> None:
        self.number = None
        self.items = []
        self.operation = None
        self.test = None
        self.inspection_count = 0



    def ParseFromStringList(self, stringlist):
        test_operation = {}

        for string in stringlist:
            if string.startswith("Monkey"):
                self.number = int(string.replace("Monkey ", "").replace(":",""))
            elif string.startswith("  Starting"):
                items = string.replace("  Starting items: ","").split(", ")
                for item in items:
                    self.items.append(int(item))
            elif string.startswith("  Operation"):
                operation = string.replace("  Operation: new = old ","").split(" ")
                def operation_function(input):
                    if operation[0] == "+":
                        return int(input) + int(input if operation[1] == "old" else operation[1])
                    elif operation[0] == "*":
                        return int(input) * int(input if operation[1] == "old" else operation[1])
                self.operation = operation_function
            elif string.startswith("  Test"):
                test_operation["Number"] = int(string.replace("  Test: divisible by ",""))
            elif string.startswith("    If true"):  
                test_operation["True"] = int(string.replace("    If true: throw to monkey ",""))
            elif string.startswith("    If false"):
                test_operation["False"] = int(string.replace("    If false: throw to monkey ",""))
        
        def test_function(input):
            if (input % test_operation["Number"] == 0):
                return test_operation["True"]
            return test_operation["False"]
        
        self.test = test_function


    def Inspect(self, divider):
        throw_list = []

        for item in self.items:
            self.inspection_count += 1
            worry_level = self.operation(item)
            worry_level = worry_level // divider
            test_result = self.test(worry_level)

            worry_level = worry_level % 9699690 if divider == 1 else worry_level
            
            throw_list.append((worry_level, test_result))

        self.items = []

        return throw_list   


