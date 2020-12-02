import random

choice = [2,3,4,5,6,7,8,9,'J','Q','K','A']
deck = list()
for c in choice:
    for i in range(4):
        deck.append(c)

def draw_card():
    score = 0
    select_card = random.choice(choice)
    if type(select_card) == int:
        score = select_card
    else:
        if select_card == 'A':
            score = 11
        else:
            score = 10
    return score, select_card

hit_until_array = [10,11,12,13,14,15,16,17,18,19,20]
hit_runs = 1000000
for hit_until in hit_until_array:
    total_value = 0
    for run in range(hit_runs):
        cards = list()
        s1, c1 = draw_card()
        s2, c2 = draw_card()
        cards.append(c1)
        cards.append(c2)

        current_value = s1 + s2

        while current_value < hit_until:
            score, card = draw_card()
            cards.append(card)
            current_value += score
            if current_value > 21 and 'A' in cards:
                ace_index = cards.index('A')
                current_value -= 10
                cards[ace_index] = 1
            
        total_value += current_value

    print(total_value / hit_runs, hit_until)