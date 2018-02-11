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
        dices_info[index] = 0

    for pair in list(itertools.combinations(dices_info, 2)):
        winner_dice = get_winner_dice(
            dices[pair[0]],
            dices[pair[1]]
        )
        if winner_dice >= 0:
            dices_info[pair[winner_dice]] += 1
            if dices_info[pair[winner_dice]] == len(dices) - 1:
                return pair[winner_dice]
    return -1


def map_dice_wins(dices):
    assert all(len(dice) == 6 for dice in dices)
    dices_info = dict()
    for index, item in enumerate(dices):
        dices_info[index] = {'wins': 0, 'vs': [], 'owned': {'dice': -1, 'by': 0}}

    for pair in list(itertools.combinations(dices_info, 2)):
        win_count = count_wins(
            dices[pair[0]],
            dices[pair[1]]
        )
        win_difference = abs(win_count[0] - win_count[1])
        if win_count[0] > win_count[1]:
            dices_info[pair[0]]['wins'] += 1
            dices_info[pair[0]]['vs'].append({'dice': pair[1], 'by': win_difference})
            if dices_info[pair[1]]['owned']['by'] < win_difference:
                dices_info[pair[1]]['owned'] = {'dice': pair[0], 'by': win_difference}
        if win_count[0] < win_count[1]:
            dices_info[pair[1]]['wins'] += 1
            dices_info[pair[1]]['vs'].append({'dice': pair[0], 'by': win_difference})
            if dices_info[pair[0]]['owned']['by'] < win_difference:
                dices_info[pair[0]]['owned'] = {'dice': pair[1], 'by': win_difference}
    return dices_info


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    dices_count = len(dices)
    strategy = dict()
    win_map = dict()
    dice_info = map_dice_wins(dices)
    for key, value in dice_info.items():
        win_map[key] = dice_info[key]['owned']['dice']
        if value['wins'] == dices_count - 1:
            strategy["choose_first"] = True
            strategy["first_dice"] = key
            return strategy
    strategy['choose_first'] = False
    strategy.update(win_map)

    return strategy
