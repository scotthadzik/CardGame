class Card:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def printCard(self):
        print ('Name:', self.name)
        print ('Cost:', self.cost)