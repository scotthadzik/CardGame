#Child class of Card
from Card import Card

class Minion(Card):
    def __init__(self, name, cost, attackPoints, healthPoints):
        Card.__init__(self, name, cost)
        self.attackPoints = attackPoints
        self.healthPoints = healthPoints

    def printCard(self):
        # self.printCard()
        print('Attack Pnts:', self.attackPoints)
        print('Health Pnts:', self.healthPoints)