from Card import Card
from Minion import Minion

def main():
    acornBearer = Minion('Acorn Bearer', 1, 2, 1 )
    crystalPower = Card('Crystal Power', 1)

    acornBearer.printCard()
    crystalPower.printCard()


if __name__ == "__main__":
    main()