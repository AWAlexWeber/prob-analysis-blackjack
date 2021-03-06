''' Calculating total permutations. '''
cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

from collections import defaultdict
total_count = defaultdict(lambda: 0)

def permutate(current_score, score_list, cmap=None):
    if current_score >= target_score:
        # Checking for bust, if we bust but we have an ace we reduce the ace to a 1 and continue
        if 'A' in score_list:
            a_index = score_list.index('A')
            score_list[a_index] = 1
            current_score -= 10

        if current_score >= target_score:
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
                permutate(current_score + c, new_score_list, new_map)
            else:
                if c == 'J' or c == 'Q' or c == 'K':
                    permutate(current_score + 10, new_score_list, new_map)

                elif c == 'A':
                    permutate(current_score + 11, new_score_list, new_map)

target_scores = [14,15,16,17,18,19,20,21]
for t in target_scores:
    target_score = t
    total_count = defaultdict(lambda: 0)
    permutate(0, list())
    print("")
    for k in sorted(total_count.keys()):
        print(k,',',total_count[k])
    print('')

for t in target_scores:
    target_score = t
    total_count = defaultdict(lambda: 0)
    cmap = defaultdict(lambda: 0)
    print(cmap)
    permutate(0, list(), cmap)
    print("")
    for k in sorted(total_count.keys()):
        print(k,total_count[k])
    print('')