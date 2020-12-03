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

        # Building the deck if our size is nonzero
        if self.size != 0:
            self.deck = list()
            for card in self.cards:
                for i in range(4 * size):
                    self.deck.append(card)

    def draw(self):
        if self.size == 0:
            return random.choice(self.cards)

        if len(self.deck) <= 0:
            return None

        card_index = random.randint(0, len(self.deck) - 1)
        self.totalDrawn += 1
        card = self.deck[card_index]
        self.drawnMap[card] += 1
        return self.deck.pop(card_index)

    def count_prob(self, cardType):
        if self.size == 0:
            return 1/13

        # Calculating the probability of drawing this card type
        totalCards = (self.size * 4)
        totalCards -= self.drawnMap[cardType]

        return totalCards / (len(self.deck))

    def expectedDrawValue(self):
        if self.size == 0:
            o = 0
            for v in self.values:
                o += v
            return o / len(self.values)

        o = 0
        for i in range(len(self.cards)):
            o += (self.count_prob(self.cards[i]) * self.values[i])
        return o

target_player_score_set = [15,16,17,18,19,20,21,22,23,24,25]

for player_target_score in target_player_score_set:

    final_scores = {'dealer': 0, 'player': 0, 'tie': 0}

    for iteration in range(0,50000):

        # Creating the deck
        d = Deck(1)

        # Dealer drawing initial card
        dealer_card = [d.draw()]

        card_index = d.cards.index(dealer_card[0])
        dealer_score = d.values[card_index]

        # Drawing two card's for the player
        player_cards = [d.draw(), d.draw()]

        #print(d.deck)
        #print(d.expectedDrawValue())

        # Calculating the score
        player_score = 0
        for card in player_cards:
            card_index = d.cards.index(card)
            player_score += d.values[card_index]

        # Checking if we busted
        if player_score > player_target_score:
            # Do we have an ace?
            if 'A' in player_cards:
                a_index = player_cards.index('A')
                player_cards[a_index] = '1'
                player_score -= 10

        # We will continue to draw while our expectedDrawValue + our current score is less than or equal to 21
        while d.expectedDrawValue() + player_score <= player_target_score:
            new_card = d.draw()
            player_cards.append(new_card)
            card_index = d.cards.index(new_card)
            player_score += d.values[card_index]

            # Checking if we busted
            if player_score > player_target_score:
                # Do we have an ace?
                if 'A' in player_cards:
                    a_index = player_cards.index('A')
                    player_cards[a_index] = '1'
                    player_score -= 10

        # Drawing for the dealer
        while dealer_score < 19:
            new_card = d.draw()
            dealer_card.append(new_card)
            card_index = d.cards.index(new_card)
            dealer_score += d.values[card_index]

            # Checking if we busted
            if dealer_score > 21:
                # Do we have an ace?
                if 'A' in dealer_card:
                    a_index = dealer_card.index('A')
                    dealer_card[a_index] = '1'
                    dealer_score -= 10

        #print(player_cards,player_score)
        #print(dealer_card,dealer_score)
        if player_score > 21:
            final_scores['dealer'] += 1
            
        elif dealer_score > 21:
            final_scores['player'] += 1

        elif dealer_score > player_score:
            final_scores['dealer'] += 1

        elif player_score > dealer_score:
            final_scores['player'] += 1

        elif player_score == dealer_score:
            final_scores['tie'] += 1

    print(final_scores['dealer'],final_scores['player'],final_scores['tie'],player_target_score)
