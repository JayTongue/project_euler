import re
from collections import Counter

with open('data/54.txt', 'r') as data:
    data = data.read().split('\n')
data = [[row.split(' ')[:5], row.split(' ')[5:]] for row in data]

def find_value(hand):

    def make_int(numbers):
        rep_dict = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
        for i in rep_dict:
            numbers = [re.sub(i, rep_dict[i], number) for number in numbers]
        return numbers
    
    def find_flushes(letters):
        return len(set(letters)) == 1
    
    def find_straights(numbers):
        straight = False
        for number in numbers:
            if set(numbers) == set(number + i for i in range(0, 5)):
                straight = True
        counter_dict = Counter(numbers)
        counts_list = sorted([counter_dict[i] for i in counter_dict])
        four_of_a_kind = counts_list == [1, 4]
        full_house = counts_list == [2, 3]
        two_pair = counts_list == [1, 2, 2]
        three_of_a_kind = counts_list == [1, 1, 3]
        pair = counts_list == [1, 1, 1, 2]
        high_card = counts_list == [1, 1, 1, 1, 1]

        return straight, four_of_a_kind, full_house, two_pair, three_of_a_kind, pair, high_card
    
    def break_ties(numbers, hand):
        if hand in (0, 3, 4, 8):
            tiebreaker_ind = numbers.index(max(numbers))
            tiebreaker = numbers[tiebreaker_ind]
        else:
            tiebreaker_counter = Counter(numbers)
            if hand in (1, 2, 5, 7):
                tiebreaker = [key for key, val in tiebreaker_counter.items() if val == max(tiebreaker_counter.values())][0]
            if hand == 6:
                tiebreaker = max([key for key, val in tiebreaker_counter.items() if val == max(tiebreaker_counter.values())])
        return tiebreaker
    
    numbers, letters = [card[0] for card in list(hand)], [card[1] for card in list(hand)]
    numbers = [int(j) for j in make_int(numbers)]
    flush = find_flushes(letters)
    straight, four_of_a_kind, full_house, two_pair, three_of_a_kind, pair, high_card = find_straights(numbers)

    if flush and straight:
        straight_flush = True
    else:
        straight_flush = False

    hand = [count for count, match in enumerate([straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair, high_card]) if match][0]
    tiebreaker = break_ties(numbers, hand)

    return [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair, high_card], tiebreaker


def get_score(hand):
    zipped = zip(hand, [128, 64, 32, 16, 8, 4, 2, 1, 0])
    return max([score for hand, score in zipped if hand])

one_wins, tie, two_wins = 0, 0, 0
for pair in data:
    p_one, p_two = pair
    one_value, one_tb = find_value(p_one)
    two_value, two_tb = find_value(p_two)
    one_score, two_score = map(get_score, (one_value, two_value))

    if one_score > two_score:
        one_wins += 1
    elif one_score == two_score:
        if one_tb > two_tb:
            one_wins += 1
        elif two_tb > one_tb:
            two_wins += 1
        else:
            tie += 1
            print(p_one, p_two, 'unbroken', one_tb, two_tb)
    else: 
        two_wins += 1
print(one_wins, tie, two_wins)
    
    