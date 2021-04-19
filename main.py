from Card import Card
from Minion import Minion

def main():
    
    deck = []

    cards = open("Cards.txt", 'r')

    for card in cards:
        cardInfo = card.split(',')
        nameOfCard = cardInfo[0]
        costOfCard = cardInfo[1]
        lengthOfList = len(cardInfo)
        #if card length is 2 create an instance of the Card object
        if lengthOfList == 2:
            cardData = Card(nameOfCard, costOfCard)
        #if card lenght is 4 create an instance of the Minion object
        if lengthOfList == 4:
            attackPoints = cardInfo[2]
            healthPoints = cardInfo[3]
            cardData = Minion(nameOfCard,costOfCard,attackPoints,healthPoints)
        deck.append(cardData)

    cards.close()

    for card in deck:
        card.printCard()
        print ('\n')

if __name__ == "__main__":
    main()