import itertools


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for pair in list(itertools.product(dice1, dice2)):
        if pair[0] > pair[1]:
            dice1_wins += 1
        elif pair[0] < pair[1]:
            dice2_wins += 1

    return dice1_wins, dice2_wins


def get_winner_dice(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for pair in list(itertools.product(dice1, dice2)):
        if pair[0] > pair[1]:
            dice1_wins += 1
        elif pair[0] < pair[1]:
            dice2_wins += 1

    comparison = dice2_wins - dice1_wins
    output_map = {0: -1, -1: 0, 1: 1}
    return output_map[(comparison > 0) - (comparison < 0)]


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    dices_info = dict()
    for index, item in enumerate(dices):
        dices_info[index] = {'dice': item, 'wins': 0}

    for pair in list(itertools.combinations(dices_info, 2)):
        winner_dice = get_winner_dice(
            dices_info[pair[0]]['dice'],
            dices_info[pair[1]]['dice']
        )
        if winner_dice >= 0:
            dices_info[pair[winner_dice]]['wins'] += 1
            if dices_info[pair[winner_dice]]['wins'] == len(dices) - 1:
                return pair[winner_dice]
    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    best_dice = find_the_best_dice(dices)
    if best_dice != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = best_dice
    else:
        for i in range(len(dices)):
            strategy[i] = (i + 1) % len(dices)

    # write your code here

    return strategy
