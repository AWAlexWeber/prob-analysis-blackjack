from collections import defaultdict
total_count = defaultdict(lambda: 0)

cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
cardsStr = ['2','3','4','5','6','7','8','9','10','J','Q','K','A','1']
scores = [2,3,4,5,6,7,8,9,10,10,10,10,1]
scoreMap = [2,3,4,5,6,7,8,9,10,10,10,10,1,1]

def calc_prob(score_list):
    # Calculating the estimated next-hand probability
    total_score = 0
    total_count = 4 * len(scores)
    for score in scores:
        total_score += (score * 4)

    for score in score_list:
        index = cardsStr.index(str(score))
        total_score -= scoreMap[index]
        total_count -= 1

    return total_score / total_count



def permutate_prob(current_score, score_list, cmap=None):
    if calc_prob(score_list) + current_score > 23:
        # Checking for bust, if we bust but we have an ace we reduce the ace to a 1 and continue
        if 'A' in score_list:
            a_index = score_list.index('A')
            score_list[a_index] = 1
            current_score -= 10

        if calc_prob(score_list) + current_score > 23:
            total_count[current_score] += 1
            return  

    else:
        # Performing permutate with all available cards
        for c in cards:
            # Do not permutate deeper if map is not none and this is already at its maximal value
            if cmap and cmap[c] >= 4:
                continue

            new_map = cmap.copy()
            new_map[c] += 1

            new_score_list = score_list.copy()
            new_score_list.append(c)
            if type(c) == int:
                permutate_prob(current_score + c, new_score_list, new_map)
            else:
                if c == 'J' or c == 'Q' or c == 'K':
                    permutate_prob(current_score + 10, new_score_list, new_map)

                elif c == 'A':
                    permutate_prob(current_score + 11, new_score_list, new_map)


total_count = defaultdict(lambda: 0)
cmap = defaultdict(lambda: 0)
print(cmap)
permutate_prob(0, list(), cmap)
print("")
for k in sorted(total_count.keys()):
    print(k,total_count[k])
print('')