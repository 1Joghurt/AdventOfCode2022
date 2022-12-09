class Bridge:
    def __init__(self, knots) -> None:
        self.visitedByTail = []   
        self.headPosition = (0, 0)
        self.knots = knots-1
        self.tailPosition = {} 
        for k in range(0, self.knots):
            self.tailPosition[k] = (0, 0)
        self.visitedByTail = [str(self.tailPosition[self.knots-1])]

    def Move(self, direction, count):
        for _ in range(0, count):
            if (direction == "U"):
                self.headPosition = self.headPosition[0], self.headPosition[1] + 1
            elif (direction == "D"):
                self.headPosition = self.headPosition[0], self.headPosition[1] - 1
            elif (direction == "R"):
                self.headPosition = self.headPosition[0] + 1, self.headPosition[1],
            elif (direction == "L"):
                self.headPosition = self.headPosition[0] - 1, self.headPosition[1],

            predecessor = self.headPosition
            for k in range(0, self.knots):
                tailDirection = self.__GetDirectionToMove(predecessor, self.tailPosition[k])
                self.tailPosition[k] = (self.tailPosition[k][0] + tailDirection[0], self.tailPosition[k][1] + tailDirection[1])

                if k == self.knots - 1 and str(self.tailPosition[self.knots-1]) not in self.visitedByTail:
                    self.visitedByTail.append(str(self.tailPosition[self.knots-1]))

                predecessor = self.tailPosition[k]


        
    def __GetDirectionToMove(self, predecessor, current):       
        if predecessor == current:
            return (0,0)
        elif predecessor[0] == current[0] and abs(predecessor[1] - current[1]) > 1:          # X Achse gleich, Y ungleich
            return (0, 1 if predecessor[1] > current[1] else -1)
        elif predecessor[1] == current[1] and abs(predecessor[0] - current[0]) > 1:          # X Achse ungleich, Y gleich
            return (1 if predecessor[0] > current[0] else -1, 0)
        elif abs(predecessor[0] - current[0]) > 1 or abs(predecessor[1] - current[1]) > 1:   # Beide ungleich
            if predecessor[0] > current[0] and predecessor[1] > current[1]:
                return (1, 1)
            elif predecessor[0] < current[0] and predecessor[1] < current[1]:
                return (-1, -1)
            elif predecessor[0] > current[0] and predecessor[1] < current[1]:
                return (1, -1)
            elif predecessor[0] < current[0] and predecessor[1] > current[1]:
                return (-1, 1)
        return (0,0)








    #def Move(self, direction, count):
    #    for _ in range(0, count):
    #        old_head_position =  self.headPosition
    #        if (direction == "U"):
    #            self.headPosition = self.headPosition[0], self.headPosition[1] + 1
    #        elif (direction == "D"):
    #            self.headPosition = self.headPosition[0], self.headPosition[1] - 1
    #        elif (direction == "R"):
    #            self.headPosition = self.headPosition[0] + 1, self.headPosition[1],
    #        elif (direction == "L"):
    #            self.headPosition = self.headPosition[0] - 1, self.headPosition[1],
    #
    #        if abs(self.headPosition[0] - self.tailPosition[0]) > 1 or abs(self.headPosition[1] - self.tailPosition[1]) > 1:
    #            self.tailPosition = old_head_position
    #
    #            if str(self.tailPosition) not in self.visitedByTail:
    #                self.visitedByTail.append(str(self.tailPosition))