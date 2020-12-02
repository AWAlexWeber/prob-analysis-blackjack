import random
from collections import defaultdict

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class Deck:

    def __init__(self, size: int):
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.size = size

        # Keeping track of the total number of drawn cards
        self.totalDrawn = 0
        self.drawnMap = defaultdict(lambda: 0)

        # Building the deck
        self.deck = list()
        for card in self.cards:
            for i in range(4 * size):
                self.deck.append(card)

    def draw(self):
        card_index = random.randint(0, len(self.deck))
        self.totalDrawn += 1
        card = self.deck[card_index]
        self.drawnMap[card] += 1
        return self.deck.pop(card_index)

    def count_prob(self, cardType):
        # Calculating the probability of drawing this card type
        totalCards = (self.size * 4)
        totalCards -= self.drawnMap[cardType]

        return totalCards / (len(self.deck))

    def expectedDrawValue(self):
        o = 0
        for i in range(len(self.cards)):
            o += (self.count_prob(self.cards[i]) * self.values[i])
        return o

d = Deck(1)
print(d.expectedDrawValue())
for c in cards:
    print(d.count_prob(c))
print(d.draw())
for c in cards:
    print(d.count_prob(c))
print(d.expectedDrawValue())